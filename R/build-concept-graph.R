# build-concept-graph.R ------------------------------------------------------
# Ekstraktor mreže pojmova ("Karpathy" koncept-graf, vidi notes/concept-graph-spec.md).
#
# Što radi:
#   1. Iz _quarto.yml čita kanonski redoslijed poglavlja i pripadnost DIO-u.
#   2. U svakom poglavlju nalazi `::: {#def-SLUG}` divove i bilježi pojam,
#      matični chapter, DIO i prvu rečenicu definicije.
#   3. Bridove gradi iz SUPOJAVLJIVANJA pojmova u tekstu (u knjizi gotovo da
#      nema eksplicitnih @def- crossrefova), uz dodatne "definicijske" bridove
#      kada definicija jednog pojma spominje drugi pojam.
#   4. Piše data/concept-graph.json (čvorovi + bridovi) koji statički čita
#      pojmovnik.qmd preko OJS FileAttachment-a.
#
# Pokreni ručno kad se poglavlja promijene:
#   Rscript R/build-concept-graph.R
# ---------------------------------------------------------------------------

suppressMessages({
  library(yaml)
  library(jsonlite)
  library(stringr)
  library(stringi)
})

PROJECT_ROOT <- normalizePath(".", winslash = "/")
QUARTO_YML   <- file.path(PROJECT_ROOT, "_quarto.yml")
OUT_JSON     <- file.path(PROJECT_ROOT, "data", "concept-graph.json")

# --- 1. chapter -> DIO mapiranje iz _quarto.yml ----------------------------
book <- yaml::read_yaml(QUARTO_YML)$book$chapters

chapter_dio <- list()   # file -> list(dio = int|"uvod", dioLabel = chr)
dio_counter <- 0L
for (entry in book) {
  if (is.character(entry)) {
    # poglavlje izvan ijednog DIO-a (index.qmd, 00-uvod.qmd)
    chapter_dio[[entry]] <- list(dio = 0L, dioLabel = "Uvod")
  } else if (is.list(entry) && !is.null(entry$part)) {
    dio_counter <- dio_counter + 1L
    label <- entry$part
    for (ch in entry$chapters) {
      chapter_dio[[ch]] <- list(dio = dio_counter, dioLabel = label)
    }
  }
}

# Samo poglavlja iz chapters/ (preskoči index.qmd) — tamo žive #def- divovi.
chapter_files <- names(chapter_dio)
chapter_files <- chapter_files[str_detect(chapter_files, "^chapters/")]

# --- pomoćne funkcije -------------------------------------------------------

# Normalizacija: makni dijakritike, na mala slova, zbij razmake.
norm_txt <- function(x) {
  x <- stri_trans_general(x, "Latin-ASCII")
  x <- tolower(x)
  x <- str_replace_all(x, "[^a-z0-9 ]+", " ")
  str_squish(x)
}

CRO_STOP <- c("i","ili","te","pa","a","ali","na","u","za","od","do","sa","iz",
              "kao","koji","koja","koje","kojih","kojim","je","su","da","se",
              "ne","to","sto","sve","vise","te","ovaj","taj","jedan","jedna",
              "bez","pri","po","o","ka","s","li","ako","kad","kada")

# Ručni nadjev za prikazne oznake gdje je podebljani pojam u definiciji
# gramatički sklonjen (npr. "Pareto učinkovita" → "Pareto učinkovitost") ili
# gdje definicija uvodi par/trojku pojmova, a slug imenuje sve njih. Mijenja
# SAMO prikaznu oznaku (term); regex za podudaranje i dalje se gradi iz prvog
# podebljanog spomena u tekstu (koji je sklonjen kao i prose, pa bolje hvata).
# Primjer unosa (dodaj ih kad se pojave prvi sklonjeni pojmovi):
#   "interval-pouzdanosti" = "Interval pouzdanosti",
#   "velicina-ucinka"      = "Veličina učinka"
LABEL_OVERRIDES <- list(
)

# Pretvori pojam u "stemove" značajnih riječi (za hvatanje sklonidbe).
# Prag je >= 3 znaka: kratke RAZLIKOVNE riječi poput "dug" (javni dug), "lov"
# (lov na rentu) ili "šok" moraju preživjeti, inače se regex sruši na jedan
# sveprisutan stem (npr. samo "javn") i pojam se lažno broji u svakom poglavlju.
term_stems <- function(term) {
  toks <- str_split(norm_txt(term), " ")[[1]]
  toks <- toks[nchar(toks) >= 3 & !(toks %in% CRO_STOP)]
  vapply(toks, function(w) {
    n <- nchar(w)
    if (n >= 7) substr(w, 1, n - 2)
    else if (n >= 5) substr(w, 1, n - 1)
    else w
  }, character(1), USE.NAMES = FALSE)
}

# Regex koji traži pojam kao FRAZU: stemovi značajnih riječi moraju biti
# susjedni (dopušta sklonidbene nastavke preko \w*). Time se izbjegava lažno
# brojanje kad "javno" i "dobro" samo zasebno postoje u istom poglavlju.
term_regex <- function(stems) {
  if (length(stems) == 0) return(NA_character_)
  esc <- str_replace_all(stems, "([\\^$.|?*+()\\[\\]{}\\\\])", "\\\\\\1")
  # Stemovi moraju biti gotovo susjedni: dopuštena je najviše JEDNA umetnuta
  # riječ (npr. prijedlog "za" u "vrijednost za novac"), ne razbacani po cijelom
  # poglavlju. \w* hvata sklonidbene nastavke.
  paste0("(?<![a-z0-9])", paste(paste0(esc, "[a-z]*"), collapse = " (?:[a-z0-9]+ )?"))
}

# Je li pojam (kao fraza) spomenut u danom normaliziranom tekstu?
mentioned_in <- function(rgx, norm_text) {
  if (is.na(rgx)) return(FALSE)
  str_detect(norm_text, rgx)
}

# --- 2. ekstrakcija #def- divova -------------------------------------------
concepts <- list()
chapter_raw   <- list()  # file -> puni normalizirani tekst poglavlja
chapter_title <- list()

# Slug klasa [^}]+ (ne samo ASCII) — neki slugovi imaju dijakritike,
# npr. {#def-mrežno-upravljanje}; slug se koristi doslovno kao id i #def- sidro.
def_open_re  <- "^:::+\\s*\\{#def-([^}]+)\\}"
fence_open_re<- "^:::+\\s*\\{"        # bilo koji div-otvarač (ugniježđeni callout itd.)
fence_close_re<- "^:::+\\s*$"         # goli zatvarač

for (f in chapter_files) {
  path <- file.path(PROJECT_ROOT, f)
  if (!file.exists(path)) next
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")

  ttl <- str_match(paste(head(lines, 20), collapse = "\n"),
                   "title:\\s*\"([^\"]+)\"")[, 2]
  chapter_title[[f]] <- if (is.na(ttl)) f else ttl

  # puni tekst poglavlja za detekciju spominjanja (bez code-fence sadržaja)
  in_code <- FALSE
  prose <- character(0)
  for (ln in lines) {
    if (str_detect(ln, "^```")) { in_code <- !in_code; next }
    if (!in_code) prose <- c(prose, ln)
  }
  chapter_raw[[f]] <- norm_txt(paste(prose, collapse = " "))

  # def blokovi
  i <- 1L; n <- length(lines)
  while (i <= n) {
    m <- str_match(lines[i], def_open_re)
    if (!is.na(m[1, 1])) {
      slug <- m[1, 2]
      # Hvatanje tijela uz praćenje dubine: ugniježđeni ::: {.callout} ... :::
      # ne smije prerano zatvoriti definiciju.
      depth <- 1L; j <- i + 1L
      body <- character(0)
      while (j <= n && depth > 0L) {
        ln <- lines[j]
        if (str_detect(ln, fence_open_re)) { depth <- depth + 1L; body <- c(body, ln) }
        else if (str_detect(ln, fence_close_re)) { depth <- depth - 1L; if (depth > 0L) body <- c(body, ln) }
        else body <- c(body, ln)
        j <- j + 1L
      }
      block <- paste(body, collapse = " ")
      matchTerm <- str_match(block, "\\*\\*([^*]+)\\*\\*")[, 2]   # prvi podebljani spomen
      if (is.na(matchTerm)) matchTerm <- slug
      # prikazna oznaka: ručni nadjev ako postoji, inače prvi podebljani spomen
      label <- if (!is.null(LABEL_OVERRIDES[[slug]])) LABEL_OVERRIDES[[slug]] else matchTerm
      # prva rečenica (do prvog ". " ili kraj), bez markdown bolda i citata [@kljuc]
      clean <- str_replace_all(block, "\\[[^]]*@[^]]*\\]", "")     # [@kljuc] / [tekst @kljuc]
      clean <- str_replace_all(clean, "@[A-Za-z0-9_:.-]+", "")     # goli @kljuc
      clean <- str_replace_all(clean, "\\*\\*|\\*|\\[|\\]|\\(#?[a-z0-9-]+\\)", "")
      clean <- str_squish(clean)
      sent  <- str_match(clean, "^(.*?[\\.!?])\\s")[, 2]
      if (is.na(sent)) sent <- clean
      if (nchar(sent) > 280) sent <- paste0(substr(sent, 1, 277), "…")

      concepts[[slug]] <- list(
        id           = slug,
        term         = str_trim(label),
        chapter      = f,
        chapterTitle = chapter_title[[f]],
        dio          = chapter_dio[[f]]$dio,
        dioLabel     = chapter_dio[[f]]$dioLabel,
        firstSentence= sent,
        defBlockNorm = norm_txt(block),
        regex        = term_regex(term_stems(matchTerm))
      )
      i <- j
    } else {
      i <- i + 1L
    }
  }
}

slugs <- names(concepts)
message(sprintf("Pronađeno %d pojmova u %d poglavlja.", length(slugs), length(chapter_files)))

# --- 3. spominjanja po poglavlju -> veličina čvora --------------------------
# Za svako poglavlje: koji su pojmovi spomenuti (po stemovima).
mentions_by_chapter <- lapply(chapter_files, function(f) {
  txt <- chapter_raw[[f]]
  slugs[vapply(slugs, function(s) mentioned_in(concepts[[s]]$regex, txt), logical(1))]
})
names(mentions_by_chapter) <- chapter_files

# veličina = broj RAZLIČITIH poglavlja koja spominju pojam (uvijek >= 1)
mention_count <- setNames(integer(length(slugs)), slugs)
for (f in chapter_files) for (s in mentions_by_chapter[[f]]) mention_count[s] <- mention_count[s] + 1L
mention_count[mention_count < 1L] <- 1L

# --- 4. bridovi -------------------------------------------------------------
# (a) supojavljivanje: par pojmova koji se zajedno spominju u poglavlju.
edge_w <- new.env(parent = emptyenv())
add_w <- function(a, b, by = 1L) {
  key <- paste(sort(c(a, b)), collapse = "\t")
  edge_w[[key]] <- (if (is.null(edge_w[[key]])) 0L else edge_w[[key]]) + by
}
for (f in chapter_files) {
  ms <- mentions_by_chapter[[f]]
  if (length(ms) >= 2) {
    cb <- combn(ms, 2)
    for (k in seq_len(ncol(cb))) add_w(cb[1, k], cb[2, k], 1L)
  }
}

# (b) definicijski bridovi: definicija pojma A spominje pojam B.
def_pairs <- new.env(parent = emptyenv())
for (a in slugs) {
  dtxt <- concepts[[a]]$defBlockNorm
  for (b in slugs) {
    if (a == b) next
    if (mentioned_in(concepts[[b]]$regex, dtxt)) {
      key <- paste(sort(c(a, b)), collapse = "\t")
      def_pairs[[key]] <- TRUE
    }
  }
}

edge_keys <- ls(edge_w)
edges <- lapply(edge_keys, function(key) {
  parts <- strsplit(key, "\t")[[1]]
  is_def <- isTRUE(def_pairs[[key]])
  list(source = parts[1], target = parts[2],
       weight = edge_w[[key]] + if (is_def) 3L else 0L,
       cooc   = edge_w[[key]],
       type   = if (is_def) "def" else "cooc")
})
# definicijski parovi koji se NE supojavljuju nigdje (rijetko) — dodaj i njih
for (key in ls(def_pairs)) {
  if (is.null(edge_w[[key]])) {
    parts <- strsplit(key, "\t")[[1]]
    edges[[length(edges) + 1]] <- list(source = parts[1], target = parts[2],
                                       weight = 3L, cooc = 0L, type = "def")
  }
}

# --- 5. izlazni JSON --------------------------------------------------------
nodes <- lapply(slugs, function(s) {
  c <- concepts[[s]]
  list(id = c$id, term = c$term, chapter = c$chapter,
       chapterTitle = c$chapterTitle, dio = c$dio, dioLabel = c$dioLabel,
       firstSentence = c$firstSentence, mentions = unname(mention_count[s]))
})

out <- list(
  generated = format(Sys.Date()),
  nodes = nodes,
  edges = edges
)

dir.create(dirname(OUT_JSON), showWarnings = FALSE, recursive = TRUE)
write_json(out, OUT_JSON, auto_unbox = TRUE, pretty = TRUE)

# --- kratki izvještaj o gustoći (de-risk korak iz spec-a) -------------------
ws <- vapply(edges, function(e) e$weight, integer(1))
message(sprintf("Bridova ukupno: %d", length(edges)))
message(sprintf("  cooc >= 2 (zadani prikaz): %d", sum(vapply(edges, function(e) e$cooc >= 2L, logical(1)))))
message(sprintf("  definicijskih: %d", sum(vapply(edges, function(e) e$type == "def", logical(1)))))
message(sprintf("Veličina čvora (spominjanja): min %d / median %d / max %d",
                min(mention_count), as.integer(median(mention_count)), max(mention_count)))
message(sprintf("JSON zapisan u %s", OUT_JSON))
