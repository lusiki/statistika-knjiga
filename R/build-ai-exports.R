# build-ai-exports.R --------------------------------------------------------
# AI-konzumabilni izvoz knjige (vidi notes/ai-export-spec.md).
#
# Što radi:
#   1. Iz _quarto.yml čita kanonski redoslijed poglavlja i pripadnost DIO-u.
#   2. Svako poglavlje pretvara iz .qmd u čisti tekstualni .md (skida YAML,
#      code-blokove {r}/{ojs}, OJS upravljačke ploče i PDF-blizance; zadržava
#      prozu, naslove, tablice, formule, definicije i sadržaj callout-kutija;
#      razrješuje [@citate], @crossref-ove i bilješke u čitljiv tekst).
#   3. Piše:
#        docs/ai/<poglavlje>.md      — radni konj, jedno poglavlje po datoteci
#        docs/ai/dio-1.md … dio-N.md — paketi po DIO-u
#        docs/llms-full.txt          — cijela knjiga u jednoj datoteci
#        docs/llms.txt               — karta (llmstxt.org) s poveznicama
#        data/ai-exports.json        — manifest koji čita stranica uci-s-ai.qmd
#
# Pokreni ručno kad se poglavlja promijene (kao i build-concept-graph.R):
#   Rscript R/build-ai-exports.R
# Blokirajući release način:
#   Rscript R/build-ai-exports.R --release
# U CI-ju se pokreće kao samostalna release naredba prije rendera, a konačni
# se artefakti ponovno validiraju nakon Quarto `pre-render` hooka (vidi
# _quarto.yml i .github/workflows/publish.yml).
# ---------------------------------------------------------------------------

# Lokalni pre-render zadržava dosadašnji best-effort način. Release način je
# namjerno fail-closed: svaka pogreška, metapodatkovni nesklad ili nalaz
# zaštićenoga sadržaja vraća nenulti status i zaustavlja objavu.
ARGS <- commandArgs(trailingOnly = TRUE)

arg_value <- function(name, default = NULL) {
  prefix <- paste0(name, "=")
  hits <- ARGS[startsWith(ARGS, prefix)]
  if (length(hits) > 1L) stop("argument je zadan više puta: ", name)
  if (length(hits) == 0L) return(default)
  substring(hits, nchar(prefix) + 1L)
}

known_args <- c("--release", "--validate-only")
unknown_args <- ARGS[
  !ARGS %in% known_args &
    !startsWith(ARGS, "--project-root=") &
    !startsWith(ARGS, "--output-root=")
]
if (length(unknown_args) > 0L) {
  stop("nepoznat argument: ", paste(unknown_args, collapse = ", "))
}

RELEASE_MODE <- "--release" %in% ARGS ||
  identical(tolower(trimws(Sys.getenv("AI_EXPORT_MODE", ""))), "release")
VALIDATE_ONLY <- "--validate-only" %in% ARGS
if (VALIDATE_ONLY) RELEASE_MODE <- TRUE

project_arg <- arg_value("--project-root", ".")
PROJECT_ROOT <- normalizePath(project_arg, winslash = "/", mustWork = TRUE)
output_arg <- arg_value("--output-root", PROJECT_ROOT)
dir.create(output_arg, recursive = TRUE, showWarnings = FALSE)
OUTPUT_ROOT <- normalizePath(output_arg, winslash = "/", mustWork = TRUE)

QUARTO_YML    <- file.path(PROJECT_ROOT, "_quarto.yml")
GOVERNANCE_YML <- file.path(PROJECT_ROOT, "release", "governance.yml")
BIB_FILE      <- file.path(PROJECT_ROOT, "references.bib")
AI_DIR        <- file.path(OUTPUT_ROOT, "docs", "ai")
DATE_STR      <- format(Sys.Date())

# Vrijednosti se pune isključivo iz release/governance.yml i njegova
# authorship_source zapisa. Nema drugoga autorskog izvora metapodataka.
SITE_URL <- BOOK_TITLE <- BOOK_DESC <- AUTHORS <- LICENSE_LINE <- NA_character_
AUTHOR_NAMES <- character(0)
GOVERNANCE_STATE <- TITLE_STATE <- AUTHORSHIP_STATE <- NA_character_

main <- function() {

  suppressMessages({
    library(yaml)
    library(jsonlite)
    library(stringr)
    library(stringi)
  })

  metadata <- load_export_metadata()
  SITE_URL <<- metadata$site_url
  BOOK_TITLE <<- metadata$title
  BOOK_DESC <<- metadata$description
  AUTHOR_NAMES <<- metadata$authors
  AUTHORS <<- paste(AUTHOR_NAMES, collapse = ", ")
  GOVERNANCE_STATE <<- metadata$governance_state
  TITLE_STATE <<- metadata$title_state
  AUTHORSHIP_STATE <<- metadata$authorship_state
  LICENSE_LINE <<- paste0(
    "© 2026 ", AUTHORS,
    ". MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE"
  )

  # --- 1. redoslijed poglavlja + DIO mapiranje iz _quarto.yml --------------
  quarto <- yaml::read_yaml(QUARTO_YML)
  book <- quarto$book$chapters
  if (is.null(book) || length(book) == 0L) {
    stop("_quarto.yml nema deklariran redoslijed poglavlja")
  }

  chapters <- list()   # poredani popis: list(file, dio, dioLabel)
  dio_counter <- 0L
  for (entry in book) {
    if (is.character(entry)) {
      if (entry == "index.qmd") next            # naslovnica (marketing) — preskoči
      chapters[[length(chapters) + 1L]] <-
        list(file = entry, dio = 0L, dioLabel = "Uvod")
    } else if (is.list(entry) && !is.null(entry$part)) {
      dio_counter <- dio_counter + 1L
      for (ch in entry$chapters) {
        chapters[[length(chapters) + 1L]] <-
          list(file = ch, dio = dio_counter, dioLabel = entry$part)
      }
    }
  }
  missing_chapters <- vapply(chapters, function(c) {
    !file.exists(file.path(PROJECT_ROOT, c$file))
  }, logical(1))
  if (any(missing_chapters)) {
    missing <- vapply(chapters[missing_chapters], function(c) c$file, character(1))
    if (RELEASE_MODE) {
      stop("nedostaje deklarirano poglavlje: ", paste(missing, collapse = ", "))
    }
    message("build-ai-exports.R: preskočena nedostupna poglavlja: ",
            paste(missing, collapse = ", "))
  }
  chapters <- chapters[!missing_chapters]
  if (length(chapters) == 0L) stop("nema dostupnih poglavlja za izvoz")

  protected_files <- unique(c(
    vapply(chapters, function(c) c$file, character(1)),
    relative_qmd_files(file.path(PROJECT_ROOT, "dodaci"))
  ))
  protected_regions <- collect_protected_regions(protected_files)

  # --- 2. bibliografija: ključ -> "Prezime, godina" -----------------------
  bib_map <- parse_bib(BIB_FILE)

  # --- 3. registar pojmova (def/prp/thm) za razrješavanje @crossref-ova ----
  xref_map <- collect_xref_terms(vapply(chapters, function(c) c$file, character(1)))

  if (VALIDATE_ONLY) {
    for (i in seq_along(chapters)) {
      c <- chapters[[i]]
      lines <- readLines(
        file.path(PROJECT_ROOT, c$file), warn = FALSE, encoding = "UTF-8"
      )
      chapters[[i]]$title <- extract_title(lines, c$file)
      chapters[[i]]$base <- str_replace(basename(c$file), "\\.qmd$", "")
    }
    validate_public_exports(chapters, dio_counter, protected_regions)
    message(sprintf(
      "AI_EXPORT_RELEASE_VALIDATION_OK chapters=%d protected_regions=%d governance=%s",
      length(chapters), length(protected_regions), GOVERNANCE_STATE
    ))
    return(invisible(NULL))
  }

  # --- 4. obradi svako poglavlje ------------------------------------------
  dir.create(AI_DIR, showWarnings = FALSE, recursive = TRUE)
  for (i in seq_along(chapters)) {
    c <- chapters[[i]]
    path  <- file.path(PROJECT_ROOT, c$file)
    lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
    title <- extract_title(lines, c$file)
    base  <- str_replace(basename(c$file), "\\.qmd$", "")

    body  <- strip_chapter(lines, bib_map, xref_map)
    words <- str_count(paste(body, collapse = " "), "\\S+")

    header <- chapter_header(title, base)
    md <- paste(c(header, "", body), collapse = "\n")

    write_utf8(md, file.path(AI_DIR, paste0(base, ".md")))

    chapters[[i]]$title <- title
    chapters[[i]]$base  <- base
    chapters[[i]]$md    <- md
    chapters[[i]]$words <- words
  }

  # --- 5. paketi po DIO-u (dio-1.md … dio-5.md) ---------------------------
  for (d in seq_len(dio_counter)) {
    members <- Filter(function(c) c$dio == d, chapters)
    if (length(members) == 0) next
    label <- members[[1]]$dioLabel
    head_md <- paste0(
      "# ", label, "\n\n",
      "> Iz knjige: ", BOOK_TITLE, "\n",
      "> Autori: ", AUTHORS, "\n",
      "> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.\n",
      "> Generirano: ", DATE_STR, " · ", LICENSE_LINE, "\n"
    )
    parts <- vapply(members, function(c) c$md, character(1))
    write_utf8(paste(c(head_md, parts), collapse = "\n\n---\n\n"),
               file.path(AI_DIR, paste0("dio-", d, ".md")))
  }

  # Ukloni samo zastarjele izvoze koje je ova skripta ranije generirala.
  # Time promjena strukture knjige ne ostavlja prividna poglavlja u docs/ai,
  # ali se nijedna ručno dodana .md datoteka bez knjižnog zaglavlja ne dira.
  expected_ai <- c(
    paste0(vapply(chapters, function(c) c$base, character(1)), ".md"),
    paste0("dio-", seq_len(dio_counter), ".md")
  )
  existing_ai <- list.files(AI_DIR, pattern = "\\.md$", full.names = TRUE)
  stale_ai <- existing_ai[!basename(existing_ai) %in% expected_ai]
  generated_by_book <- vapply(stale_ai, function(path) {
    head_lines <- readLines(path, n = 8L, warn = FALSE, encoding = "UTF-8")
    any(grepl(paste0("> Iz knjige: ", BOOK_TITLE), head_lines, fixed = TRUE))
  }, logical(1))
  if (any(generated_by_book)) {
    unlink(stale_ai[generated_by_book])
  }

  # --- 6. cijela knjiga: docs/llms-full.txt -------------------------------
  full_head <- paste0(
    "# ", BOOK_TITLE, "\n\n",
    "> ", BOOK_DESC, "\n",
    "> Autori: ", AUTHORS, "\n",
    "> Izvor: ", SITE_URL, "\n",
    "> Cjelovita tekstualna verzija knjige za korištenje s AI-asistentima.\n",
    "> Generirano: ", DATE_STR, " · ", LICENSE_LINE, "\n"
  )
  all_parts <- vapply(chapters, function(c) c$md, character(1))
  write_utf8(paste(c(full_head, all_parts), collapse = "\n\n---\n\n"),
             file.path(OUTPUT_ROOT, "docs", "llms-full.txt"))

  # --- 7. karta: docs/llms.txt (llmstxt.org) ------------------------------
  write_utf8(build_llms_txt(chapters, dio_counter),
             file.path(OUTPUT_ROOT, "docs", "llms.txt"))

  # --- 8. manifest za stranicu: data/ai-exports.json ----------------------
  write_manifest(chapters, dio_counter)

  # --- 9. release audit metapodataka i zaštićenoga sadržaja ---------------
  if (RELEASE_MODE) {
    validate_public_exports(chapters, dio_counter, protected_regions)
  }

  # --- izvještaj (de-risk korak iz spec-a) --------------------------------
  fmt <- function(x) format(x, big.mark = ".", decimal.mark = ",")
  tw <- sum(vapply(chapters, function(c) c$words, integer(1)))
  message(sprintf("Poglavlja izvezena: %d", length(chapters)))
  message(sprintf("Ukupno riječi (bez koda): %s  (~%s tokena, gruba procjena)",
                  fmt(tw), fmt(round(tw * 1.6))))
  big <- chapters[[which.max(vapply(chapters, function(c) c$words, integer(1)))]]
  message(sprintf("Najveće poglavlje: %s — %s riječi (~%sk tokena)",
                  big$base, fmt(big$words), round(big$words * 1.6 / 1000)))
  message(sprintf("Zapisano u %s, docs/llms.txt, docs/llms-full.txt, data/ai-exports.json",
                  AI_DIR))
  if (RELEASE_MODE) {
    message(sprintf(
      "AI_EXPORT_RELEASE_OK chapters=%d protected_regions=%d governance=%s",
      length(chapters), length(protected_regions), GOVERNANCE_STATE
    ))
  }
}

# ===========================================================================
# pomoćne funkcije
# ===========================================================================

as_scalar_character <- function(value, field) {
  if (is.null(value) || length(value) != 1L || is.na(value) ||
      !nzchar(trimws(as.character(value)))) {
    stop("nedostaje obvezni metapodatak: ", field)
  }
  trimws(as.character(value))
}

author_names_from_quarto <- function(author) {
  if (is.null(author) || length(author) == 0L) {
    stop("authorship_source nema autora")
  }
  if (is.character(author)) {
    names <- author
  } else {
    names <- vapply(author, function(entry) {
      if (is.character(entry) && length(entry) == 1L) return(entry)
      if (is.list(entry) && !is.null(entry$name)) return(as.character(entry$name))
      NA_character_
    }, character(1))
  }
  names <- trimws(names)
  if (any(is.na(names)) || any(!nzchar(names))) {
    stop("authorship_source sadrži autora bez imena")
  }
  unname(names)
}

author_narrative <- function(names) {
  if (length(names) == 1L) return(names)
  if (length(names) == 2L) return(paste(names, collapse = " i "))
  paste0(paste(head(names, -1L), collapse = ", "), " i ", tail(names, 1L))
}

load_export_metadata <- function() {
  if (!file.exists(GOVERNANCE_YML)) {
    stop("nedostaje kanonski izvor release metapodataka: release/governance.yml")
  }
  governance <- yaml::read_yaml(GOVERNANCE_YML)
  if (!identical(as.integer(governance$schema_version), 1L) ||
      !identical(governance$mechanism, "pre-release-governance")) {
    stop("release/governance.yml nema očekivani predobjavni ugovor")
  }

  governance_title <- as_scalar_character(
    governance$book$working_title, "book.working_title"
  )
  authorship_source <- as_scalar_character(
    governance$book$authorship_source, "book.authorship_source"
  )
  metadata_path <- file.path(PROJECT_ROOT, authorship_source)
  if (!file.exists(metadata_path)) {
    stop("ne postoji authorship_source iz release/governance.yml: ",
         authorship_source)
  }
  canonical <- yaml::read_yaml(metadata_path)
  source_title <- as_scalar_character(canonical$book$title, "book.title")
  if (!identical(governance_title, source_title)) {
    stop(
      "metadata drift: release/governance.yml book.working_title ne odgovara ",
      authorship_source, " book.title"
    )
  }

  site_url <- sub("/+$", "", as_scalar_character(
    canonical$book[["site-url"]], "book.site-url"
  ))
  description <- as_scalar_character(
    canonical$book$description, "book.description"
  )
  authors <- author_names_from_quarto(canonical$book$author)

  list(
    title = governance_title,
    description = description,
    site_url = site_url,
    authors = authors,
    governance_state = as_scalar_character(
      governance$current_state, "current_state"
    ),
    title_state = as_scalar_character(
      governance$book$title_state, "book.title_state"
    ),
    authorship_state = as_scalar_character(
      governance$book$authorship_state, "book.authorship_state"
    )
  )
}

relative_qmd_files <- function(directory) {
  if (!dir.exists(directory)) return(character(0))
  paths <- list.files(
    directory, pattern = "\\.qmd$", recursive = TRUE, full.names = TRUE
  )
  prefix <- paste0(PROJECT_ROOT, "/")
  paths <- normalizePath(paths, winslash = "/", mustWork = TRUE)
  if (any(!startsWith(paths, prefix))) {
    stop("QMD putanja izlazi iz projektnoga korijena")
  }
  substring(paths, nchar(prefix) + 1L)
}

normalize_for_audit <- function(text) {
  text <- paste(text, collapse = " ")
  text <- stringr::str_replace_all(text, "<!--.*?-->", " ")
  text <- stringr::str_replace_all(text, "[`*_>#]", " ")
  text <- stringr::str_replace_all(text, "\\s+", " ")
  stringr::str_trim(text)
}

collect_protected_regions <- function(files) {
  regions <- list()
  for (file in files) {
    path <- file.path(PROJECT_ROOT, file)
    if (!file.exists(path)) next
    lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
    stack <- list()
    for (i in seq_along(lines)) {
      line <- lines[[i]]
      opened <- stringr::str_match(line, "^:::+\\s*\\{(.*)\\}\\s*$")
      if (!is.na(opened[1, 1])) {
        attrs <- opened[1, 2]
        has_profile <- stringr::str_detect(attrs, "when-profile\\s*=")
        visible_profile <- has_profile &&
          stringr::str_detect(attrs, "(^|\\s)\\.?content-visible(\\s|$)")
        hidden_profile <- has_profile &&
          stringr::str_detect(attrs, "(^|\\s)\\.?content-hidden(\\s|$)")
        if (has_profile && !visible_profile && !hidden_profile && RELEASE_MODE) {
          stop("nepoznata when-profile ruta u ", file, ":", i)
        }
        region_id <- NA_integer_
        if (visible_profile) {
          region_id <- length(regions) + 1L
          regions[[region_id]] <- list(
            file = file, line = i, content = character(0)
          )
        }
        stack[[length(stack) + 1L]] <- list(
          protected = visible_profile, region_id = region_id
        )
        next
      }

      if (stringr::str_detect(line, "^:::+\\s*$")) {
        if (length(stack) == 0L) {
          if (RELEASE_MODE) stop("suvišan div zatvarač u ", file, ":", i)
        } else {
          stack <- stack[-length(stack)]
        }
        next
      }

      if (length(stack) > 0L) {
        active <- vapply(stack, function(entry) {
          isTRUE(entry$protected)
        }, logical(1))
        ids <- unique(vapply(stack[active], function(entry) {
          entry$region_id
        }, integer(1)))
        for (id in ids) regions[[id]]$content <- c(regions[[id]]$content, line)
      }
    }
    if (length(stack) > 0L && RELEASE_MODE) {
      stop("nezatvoren div u ", file)
    }
  }
  regions
}

write_utf8 <- function(text, path) {
  dir.create(dirname(path), recursive = TRUE, showWarnings = FALSE)
  con <- file(path, open = "wb")
  on.exit(close(con))
  writeLines(enc2utf8(text), con, useBytes = TRUE)
}

extract_title <- function(lines, file) {
  ttl <- str_match(paste(head(lines, 25), collapse = "\n"),
                   "(?m)^title:\\s*\"([^\"]+)\"")[, 2]
  if (is.na(ttl)) ttl <- str_match(paste(head(lines, 25), collapse = "\n"),
                                   "(?m)^title:\\s*(.+?)\\s*$")[, 2]
  if (is.na(ttl)) file else str_trim(ttl)
}

chapter_header <- function(title, base) {
  paste0(
    "# ", title, "\n\n",
    "> Iz knjige: ", BOOK_TITLE, "\n",
    "> Autori: ", AUTHORS, "\n",
    "> Izvor: ", SITE_URL, "/chapters/", base, ".html\n",
    "> Tekstualna verzija poglavlja za korištenje s AI-asistentima.\n",
    "> Generirano: ", DATE_STR, " · ", LICENSE_LINE, "\n\n",
    "---"
  )
}

# --- bibliografija ---------------------------------------------------------
# Vrlo tolerantan parser: ključ -> "Prezime, godina". Ako nešto ne uspije,
# fallback je goli ključ (nikad ne ruši izvoz).
parse_bib <- function(bib_file) {
  out <- list()
  if (!file.exists(bib_file)) return(out)
  raw <- paste(readLines(bib_file, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  entries <- str_split(raw, "(?m)^@")[[1]]
  for (e in entries) {
    key <- str_match(e, "^[A-Za-z]+\\s*\\{\\s*([^,\\s]+)\\s*,")[, 2]
    if (is.na(key)) next
    author <- str_match(e, "(?is)author\\s*=\\s*[{\"](.*?)[}\"]\\s*,?\\s*\\n")[, 2]
    year   <- str_match(e, "(?i)(?:year|date)\\s*=\\s*[{\"]?\\s*(\\d{4})")[, 2]
    surname <- NA_character_
    if (!is.na(author)) {
      first <- str_trim(str_split(author, "\\s+and\\s+")[[1]][1])
      surname <- if (str_detect(first, ",")) str_trim(str_split(first, ",")[[1]][1])
                 else str_extract(first, "\\S+$")
    }
    label <- if (!is.na(surname) && !is.na(year)) paste0(surname, ", ", year)
             else if (!is.na(surname)) surname
             else if (!is.na(year)) year
             else key
    out[[key]] <- label
  }
  out
}

# --- registar pojmova za @def-/@prp-/@thm- crossref-ove --------------------
collect_xref_terms <- function(files) {
  m <- list()
  open_re <- "^:::+\\s*\\{#(def|prp|thm|lem|cor|exm|exr)-([^}]+)\\}"
  for (f in files) {
    path <- file.path(PROJECT_ROOT, f)
    if (!file.exists(path)) next
    lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
    i <- 1L; n <- length(lines)
    while (i <= n) {
      mm <- str_match(lines[i], open_re)
      if (!is.na(mm[1, 1])) {
        kind <- mm[1, 2]; slug <- mm[1, 3]
        # prvi podebljani spomen u sljedećih nekoliko redaka = prikazni pojam
        look <- paste(lines[i:min(n, i + 6L)], collapse = " ")
        term <- str_match(look, "\\*\\*([^*]+)\\*\\*")[, 2]
        if (is.na(term)) term <- slug
        m[[paste0(kind, "-", slug)]] <- str_trim(term)
      }
      i <- i + 1L
    }
  }
  m
}

# --- razrješavanje @ključeva (citati + crossref) u tekstu ------------------
XREF_WORD <- c(fig = "slika", tbl = "tablica", sec = "odjeljak",
               eq = "jednadžba", lst = "isječak")

resolve_one_key <- function(key, bib_map, xref_map) {
  kind <- str_match(key, "^(fig|tbl|sec|eq|lst|def|prp|thm|lem|cor|exm|exr)-")[, 2]
  if (!is.na(kind)) {
    if (kind %in% names(XREF_WORD)) return(XREF_WORD[[kind]])
    term <- xref_map[[key]]
    if (!is.null(term)) return(term)
    return(c(def = "definicija", prp = "propozicija", thm = "teorem",
             lem = "lema", cor = "korolar", exm = "primjer",
             exr = "vježba")[[kind]])
  }
  lbl <- bib_map[[key]]
  if (!is.null(lbl)) lbl else key
}

resolve_refs <- function(line, bib_map, xref_map) {
  # (a) zagrade s ključevima: [@a; @b], [-@a], [vidi @a, str. 5]
  # (str_replace_all funkciji predaje SVE pogotke odjednom -> vektoriziraj)
  line <- str_replace_all(line, "\\[([^\\]]*@[^\\]]+)\\]", function(br) {
    vapply(br, function(one) {
      inner <- str_sub(one, 2, -2)
      keys <- str_match_all(inner, "-?@([A-Za-z0-9_:.\\-]+)")[[1]][, 2]
      if (length(keys) == 0) return(one)
      labs <- vapply(keys, resolve_one_key, character(1), bib_map, xref_map)
      paste0("(", paste(labs, collapse = "; "), ")")
    }, character(1), USE.NAMES = FALSE)
  })
  # (b) goli @ključ (narativno spominjanje izvan zagrada)
  line <- str_replace_all(line, "(?<![\\w@])-?@([A-Za-z0-9_:.\\-]+)", function(tok) {
    vapply(tok, function(one) {
      key <- str_replace(one, "^-?@", "")
      resolve_one_key(key, bib_map, xref_map)
    }, character(1), USE.NAMES = FALSE)
  })
  line
}

# --- čišćenje proznog retka ------------------------------------------------
clean_inline <- function(line, bib_map, xref_map) {
  line <- resolve_refs(line, bib_map, xref_map)
  # slike: ![alt](path) -> "alt" (zadrži opis, izbaci putanju)
  line <- str_replace_all(line, "!\\[([^\\]]*)\\]\\([^)]*\\)", "\\1")
  # poveznice: [tekst](http…) -> "tekst (url)"; [tekst](#…/relativno) -> "tekst"
  line <- str_replace_all(line, "\\[([^\\]]+)\\]\\((https?://[^)]+)\\)", "\\1 (\\2)")
  line <- str_replace_all(line, "\\[([^\\]]+)\\]\\([^)]*\\)", "\\1")
  # pandoc span: [tekst]{.klasa …} -> "tekst"
  line <- str_replace_all(line, "\\[([^\\]]+)\\]\\{[^}]*\\}", "\\1")
  # atributi na naslovima/elementima: "## Naslov {#sec-x}" -> "## Naslov"
  line <- str_replace(line, "\\s*\\{[#.][^}]*\\}\\s*$", "")
  str_trim(line, side = "right")
}

# --- glavni stripper: .qmd -> čisti markdown -------------------------------
strip_chapter <- function(lines, bib_map, xref_map) {
  out <- character(0)
  fnotes <- list()        # id -> tekst bilješke
  fnote_order <- character(0)
  in_yaml <- FALSE; seen_yaml <- FALSE
  in_code <- FALSE; cap_pending <- NA_character_
  in_comment <- FALSE         # HTML komentar (uredničke bilješke, TODO-ovi)
  div_stack <- character(0)   # "drop" (PDF-blizanac) ili "keep"

  drop_now <- function() any(div_stack == "drop")

  div_open_re  <- "^:::+\\s*\\{(.*)\\}\\s*$"
  div_close_re <- "^:::+\\s*$"
  code_fence_re<- "^```"
  cap_re       <- "^\\s*(?:#|//)\\|\\s*(?:fig|tbl)-cap:\\s*\"(.*)\"\\s*$"
  fnote_def_re <- "^\\[\\^([^\\]]+)\\]:\\s*(.*)$"

  label_for <- function(attrs) {
    if (str_detect(attrs, "callout-vinjeta"))  return("**Vinjeta.**")
    if (str_detect(attrs, "callout-divljina")) return("**Statistika u divljini.**")
    if (str_detect(attrs, "callout-model"))    return("**Pitajte model.**")
    if (str_detect(attrs, "callout-greska"))   return("**Nađite grešku.**")
    NA_character_
  }

  for (raw in lines) {
    ln <- raw

    # --- YAML front matter ---
    if (!seen_yaml && str_detect(ln, "^---\\s*$")) {
      in_yaml <- !in_yaml
      if (!in_yaml) seen_yaml <- TRUE
      next
    }
    if (in_yaml) next

    # --- HTML komentari (uredničke bilješke i TODO-ovi) ---
    # Ne smiju procuriti u izvoz: asistent bi ih čitao kao tekst knjige.
    # Jednorednim se briše samo komentar, višeredni guta cijele retke.
    if (in_comment) {
      if (str_detect(ln, "-->")) {
        in_comment <- FALSE
        ln <- str_replace(ln, "^.*?-->", "")
        if (str_trim(ln) == "") next
      } else next
    }
    ln <- str_replace_all(ln, "<!--.*?-->", "")
    if (str_detect(ln, "<!--")) {
      in_comment <- TRUE
      ln <- str_replace(ln, "<!--.*$", "")
      if (str_trim(ln) == "") next
    }

    # --- div otvarač / zatvarač (uvijek ažuriraj stog, nikad ne ispisuj fence) ---
    mo <- str_match(ln, div_open_re)
    if (!is.na(mo[1, 1])) {
      attrs <- mo[1, 2]
      has_profile <- str_detect(attrs, "when-profile\\s*=")
      visible_profile <- has_profile &&
        str_detect(attrs, "(^|\\s)\\.?content-visible(\\s|$)")
      hidden_profile <- has_profile &&
        str_detect(attrs, "(^|\\s)\\.?content-hidden(\\s|$)")
      if (has_profile && !visible_profile && !hidden_profile && RELEASE_MODE) {
        stop("nepoznata when-profile ruta u izvoru izvoza")
      }
      if (visible_profile || str_detect(attrs, "when-format=\"pdf\"")) {
        div_stack <- c(div_stack, "drop")
      } else {
        div_stack <- c(div_stack, "keep")
        if (!drop_now()) {
          lab <- label_for(attrs)
          if (!is.na(lab)) out <- c(out, "", lab)
        }
      }
      next
    }
    if (str_detect(ln, div_close_re)) {
      if (length(div_stack) > 0) {
        div_stack <- div_stack[-length(div_stack)]
      } else if (RELEASE_MODE) {
        stop("suvišan div zatvarač u poglavlju")
      }
      next
    }

    # --- unutar PDF-blizanca: preskoči sve ---
    if (drop_now()) next

    # --- code fence (drži se izvan koda; hvataj caption, odbaci kod) ---
    if (str_detect(ln, code_fence_re)) {
      if (!in_code) {
        in_code <- TRUE; cap_pending <- NA_character_
      } else {
        in_code <- FALSE
        if (!is.na(cap_pending)) out <- c(out, "", paste0("*Slika. ", cap_pending, "*"))
      }
      next
    }
    if (in_code) {
      cm <- str_match(ln, cap_re)
      if (!is.na(cm[1, 1])) cap_pending <- cm[1, 2]
      next
    }

    # --- bilješka (definicija) -> sakupi, ne ispisuj na mjestu ---
    fm <- str_match(ln, fnote_def_re)
    if (!is.na(fm[1, 1])) {
      id <- fm[1, 2]
      fnotes[[id]] <- clean_inline(fm[1, 3], bib_map, xref_map)
      next
    }

    # --- obična prozna linija ---
    out <- c(out, clean_inline(ln, bib_map, xref_map))
  }

  if (RELEASE_MODE) {
    if (in_yaml) stop("nezatvoren YAML front matter u poglavlju")
    if (in_comment) stop("nezatvoren HTML komentar u poglavlju")
    if (in_code) stop("nezatvoren code fence u poglavlju")
    if (length(div_stack) > 0L) stop("nezatvoren div u poglavlju")
  }

  # --- bilješke: inline [^id] -> [n], popis na kraju pod "## Bilješke" ---
  txt <- paste(out, collapse = "\n")
  markers <- str_match_all(txt, "\\[\\^([^\\]]+)\\]")[[1]][, 2]
  markers <- unique(markers)
  if (length(markers) > 0) {
    num <- setNames(seq_along(markers), markers)
    for (id in markers) {
      txt <- str_replace_all(txt, stringr::fixed(paste0("[^", id, "]")),
                             paste0("[", num[[id]], "]"))
    }
    notes <- vapply(markers, function(id) {
      body <- if (!is.null(fnotes[[id]])) fnotes[[id]] else ""
      paste0(num[[id]], ". ", body)
    }, character(1))
    txt <- paste0(txt, "\n\n## Bilješke\n\n", paste(notes, collapse = "\n"))
  }

  # počisti višak praznih redaka (najviše jedan prazan red zaredom)
  txt <- str_replace_all(txt, "\n{3,}", "\n\n")
  str_split(str_trim(txt), "\n")[[1]]
}

# --- llms.txt (karta) ------------------------------------------------------
build_llms_txt <- function(chapters, dio_counter) {
  L <- c(paste0("# ", BOOK_TITLE), "",
         paste0("> ", BOOK_DESC), "",
         paste0("Tekstualne (AI-čitljive) verzije poglavlja knjige dostupne na ",
                SITE_URL, ". Učitajte pojedino poglavlje radi najtočnijih odgovora ",
                "ili cijelu knjigu za širi pregled."), "")
  link <- function(c) paste0("- [", c$title, "](", SITE_URL, "/ai/", c$base, ".md)")
  intro <- Filter(function(c) c$dio == 0L, chapters)
  if (length(intro) > 0) {
    L <- c(L, "## Uvod", vapply(intro, link, character(1)), "")
  }
  for (d in seq_len(dio_counter)) {
    members <- Filter(function(c) c$dio == d, chapters)
    if (length(members) == 0) next
    L <- c(L, paste0("## ", members[[1]]$dioLabel),
           vapply(members, link, character(1)), "")
  }
  L <- c(L, "## Paketi i cijela knjiga",
         paste0("- [Cijela knjiga (jedna datoteka)](", SITE_URL, "/llms-full.txt)"))
  for (d in seq_len(dio_counter)) {
    members <- Filter(function(c) c$dio == d, chapters)
    if (length(members) == 0) next
    L <- c(L, paste0("- [", members[[1]]$dioLabel, " (paket)](",
                     SITE_URL, "/ai/dio-", d, ".md)"))
  }
  paste(L, collapse = "\n")
}

expected_export_paths <- function(chapters, dio_counter) {
  chapter_paths <- file.path(
    AI_DIR,
    paste0(vapply(chapters, function(c) c$base, character(1)), ".md")
  )
  part_paths <- file.path(AI_DIR, paste0("dio-", seq_len(dio_counter), ".md"))
  c(
    chapter_paths,
    part_paths,
    file.path(OUTPUT_ROOT, "docs", "llms-full.txt"),
    file.path(OUTPUT_ROOT, "docs", "llms.txt"),
    file.path(OUTPUT_ROOT, "data", "ai-exports.json")
  )
}

validate_public_exports <- function(chapters, dio_counter, protected_regions) {
  paths <- expected_export_paths(chapters, dio_counter)
  missing <- paths[!file.exists(paths)]
  if (length(missing) > 0L) {
    stop(
      "release izvoz nije potpun; nedostaje: ",
      paste(basename(missing), collapse = ", ")
    )
  }

  expected_ai <- normalizePath(
    paths[grepl("[/\\\\]ai[/\\\\].*\\.md$", paths)],
    winslash = "/", mustWork = TRUE
  )
  actual_ai <- normalizePath(
    list.files(AI_DIR, pattern = "\\.md$", full.names = TRUE),
    winslash = "/", mustWork = TRUE
  )
  unexpected_ai <- setdiff(actual_ai, expected_ai)
  if (length(unexpected_ai) > 0L) {
    stop(
      "release izvoz sadrži neočekivani javni artefakt: ",
      paste(basename(unexpected_ai), collapse = ", ")
    )
  }

  manifest_path <- file.path(OUTPUT_ROOT, "data", "ai-exports.json")
  manifest <- jsonlite::read_json(manifest_path, simplifyVector = TRUE)
  if (!identical(as.character(manifest$book$title), BOOK_TITLE)) {
    stop("metadata drift: manifest book.title nije kanonski naslov")
  }
  manifest_authors <- unname(as.character(manifest$book$authors))
  if (!identical(manifest_authors, AUTHOR_NAMES)) {
    stop("metadata drift: manifest book.authors nije kanonsko autorstvo")
  }
  if (!identical(as.character(manifest$book$url), SITE_URL)) {
    stop("metadata drift: manifest book.url nije kanonska adresa")
  }
  if (!identical(
    as.character(manifest$book$governance$source), "release/governance.yml"
  ) || !identical(
    as.character(manifest$book$governance$state), GOVERNANCE_STATE
  )) {
    stop("metadata drift: manifest ne bilježi kanonsko governance stanje")
  }
  if (length(manifest$chapters$slug) != length(chapters)) {
    stop("manifest nema točan broj poglavlja")
  }

  header_paths <- expected_ai
  expected_book_line <- paste0("> Iz knjige: ", BOOK_TITLE)
  expected_author_line <- paste0("> Autori: ", AUTHORS)
  for (path in header_paths) {
    header <- readLines(path, n = 12L, warn = FALSE, encoding = "UTF-8")
    if (!expected_book_line %in% header || !expected_author_line %in% header) {
      stop("metadata drift u zaglavlju izvoza: ", basename(path))
    }
  }

  full_path <- file.path(OUTPUT_ROOT, "docs", "llms-full.txt")
  full_header <- readLines(full_path, n = 10L, warn = FALSE, encoding = "UTF-8")
  if (!paste0("# ", BOOK_TITLE) %in% full_header ||
      !expected_author_line %in% full_header) {
    stop("metadata drift u docs/llms-full.txt")
  }
  llms_path <- file.path(OUTPUT_ROOT, "docs", "llms.txt")
  llms_header <- readLines(llms_path, n = 8L, warn = FALSE, encoding = "UTF-8")
  if (!paste0("# ", BOOK_TITLE) %in% llms_header) {
    stop("metadata drift u docs/llms.txt")
  }

  public_text <- paste(vapply(paths, function(path) {
    paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  }, character(1)), collapse = "\n")
  if (grepl("when-profile\\s*=|content-visible[^\n]*kolegij", public_text,
            perl = TRUE, ignore.case = TRUE)) {
    stop("protected-content leak: profilna oznaka pronađena je u javnom izvozu")
  }
  public_normalized <- normalize_for_audit(public_text)
  for (region in protected_regions) {
    protected_normalized <- normalize_for_audit(region$content)
    if (nchar(protected_normalized) >= 40L &&
        grepl(protected_normalized, public_normalized, fixed = TRUE)) {
      stop(
        "protected-content leak iz ", region$file, ":", region$line,
        " pronađen je u javnom izvozu"
      )
    }
  }

  invisible(list(paths = paths, protected_regions = length(protected_regions)))
}

# --- manifest za uci-s-ai.qmd ----------------------------------------------
write_manifest <- function(chapters, dio_counter) {
  ch <- lapply(chapters, function(c) list(
    slug = c$base, title = c$title, dio = c$dio, dioLabel = c$dioLabel,
    url = paste0(SITE_URL, "/chapters/", c$base, ".html"),
    mdUrl = paste0(SITE_URL, "/ai/", c$base, ".md"),
    words = c$words, tokensApprox = round(c$words * 1.6)
  ))
  dios <- lapply(seq_len(dio_counter), function(d) {
    members <- Filter(function(x) x$dio == d, chapters)
    if (length(members) == 0) return(NULL)
    list(n = d, label = members[[1]]$dioLabel,
         mdUrl = paste0(SITE_URL, "/ai/dio-", d, ".md"))
  })
  dios <- Filter(Negate(is.null), dios)
  # Puna mentorska uputa (za polje za kopiranje na stranici „Uči uz AI”).
  authors_in_prose <- author_narrative(AUTHOR_NAMES)
  prompt <- paste0(
    "Ti si moj osobni mentor i suputnik u učenju za sveučilišni udžbenik „", BOOK_TITLE,
    "” (autori ", authors_in_prose, "; mrežno izdanje na ", SITE_URL, "). Udžbenik uči statistiku za ",
    "društvene znanosti, od statističkog mišljenja i opisivanja podataka preko uzorkovanja, ",
    "procjene i testiranja do linearnih modela i statistike u doba algoritama. Uz ovu uputu ",
    "prilažem ti čisti tekst jednog poglavlja, jednog dijela knjige (DIO) ili cijele knjige. ",
    "Taj priloženi tekst tvoj je jedini izvor istine. Ja sam student koji uči iz njega, a ti si ",
    "moj strpljiv, topao i ohrabrujući vodič, kao dobar asistent na konzultacijama.\n\n",

    "KAKO RADIŠ\n",
    "Odgovaraš isključivo na hrvatskom jeziku (hr-HR), jasno i prirodno, ali stručno, koristeći ",
    "nazivlje točno onako kako ga knjiga uvodi (uz izvorni engleski naziv u zagradi i kurzivu, ",
    "onako kako to čini i sama knjiga). Gradiš intuiciju prije formalizma, jednako kao i knjiga: ",
    "ideju najprije objasniš kroz simulaciju, primjer ili analogiju, a tek onda imenuješ i ",
    "zapišeš formulu. Prilagođavaš dubinu mojoj razini; ako pogriješim ili nešto ne razumijem, ",
    "vraćaš se korak unatrag i objašnjavaš drukčije. Smiješ me voditi sokratski, kratkim ",
    "pitanjima koja me navode na odgovor, i povremeno provjeriš jesam li dobro razumio prije ",
    "nego što nastaviš.\n\n",

    "KAKO RAČUNAŠ\n",
    "Kad računaš, uvijek pokažeš postupak, a ne samo rezultat, i imenuješ svaku pretpostavku ",
    "koju si usput napravio. Rezultat interpretiraš rečenicom koju bi student mogao napisati u ",
    "izvještaju, a uz procjenu uvijek navedeš i mjeru nesigurnosti. Nikada ne izmišljaš podatke: ",
    "ako za izračun nemaš brojke, tražiš ih od mene ili jasno kažeš da simuliraš i pod kojim ",
    "pretpostavkama. Nikada ne izvodiš zaključak o uzročnosti iz podataka koji ga ne podnose. ",
    "Ako te zamolim za kod, pišeš čitljiv R (tidyverse) ili jamovi postupak, komentiraš svaki ",
    "korak i upozoriš me što moram provjeriti prije nego što rezultatu povjerujem.\n\n",

    "UTEMELJENOST I POŠTENJE (najvažnije pravilo)\n",
    "Sve tvrdnje, brojke, definicije i zaključke crpiš iz priloženog teksta. Na gradivo, ",
    "poglavlje ili odjeljak upućuješ riječima („u poglavlju o uzorkovanju”, „u odjeljku o ",
    "intervalima pouzdanosti”), nikada brojem. Kad nečega nema u priloženom tekstu, otvoreno ",
    "kažeš „Toga nema u priloženom tekstu” i tek onda, ako misliš da pomaže, ponudiš opće znanje ",
    "uz jasnu oznaku „Izvan knjige (opće znanje)” i napomenu da to treba samostalno provjeriti. ",
    "Nikada ne izmišljaš brojke, postotke, godine, imena autora, studije ni citate; ako nisi ",
    "siguran, to priznaš umjesto da nagađaš.\n\n",

    "PRIVATNOST\n",
    "Ako radim s podacima o ljudima, podsjetiš me da osobni i osjetljivi podaci ispitanika ne ",
    "idu u razgovor s modelom te predložiš rad na anonimiziranom ili simuliranom uzorku.\n\n",

    "ŠTO SVE MOŽEŠ NA ZAHTJEV\n",
    "Sažeti poglavlje ili dio na ključne teze, definicije i postupke; izraditi pitanja za ",
    "provjeru i kvizove s rješenjima i obrazloženjima; napraviti kartice za učenje; sastaviti ",
    "plan učenja do ispita; usporediti srodne postupke i reći kada se koji koristi; provesti me ",
    "kroz razrađeni primjer korak po korak; te mi dati zadatak u kojemu ti napraviš analizu s ",
    "jednom namjernom greškom koju ja moram naći.\n\n",

    "FORMAT ODGOVORA\n",
    "Odgovaraš strukturirano, jezgrovito, ali potpuno. Kreni od izravnog odgovora ili jednostavne ",
    "srži, zatim razradi s uporištem u tekstu, ondje gdje pomaže kratkim popisom ili tablicom. ",
    "Ključne pojmove podebljaš pri prvom spominjanju. Na kraju ponudi jedan korak dalje.\n\n",

    "GRANICE\n",
    "Ostaješ na temama ovog udžbenika i unutar njegova okvira. Podsjećaš me, kad je prikladno, ",
    "da si pomagalo u učenju, da možeš pogriješiti i da važne tvrdnje, brojke i postupke ",
    "provjerim u samom tekstu knjige.\n\n",

    "Za početak me pozdravi, u jednoj rečenici potvrdi što je u priloženom tekstu i pitaj me ",
    "odakle želim krenuti, koliko mi je tema već poznata i koji mi je cilj (razumijevanje, ",
    "ponavljanje ili priprema za ispit)."
  )

  # Kratka uputa (za „jedan klik” duboke poveznice; mora ostati kratka jer ide u URL).
  # DRŽI U SKLADU s konstantom UPUTA u styles/book-include.html.
  promptShort <- paste0(
    "Ti si moj mentor za udžbenik „", BOOK_TITLE, "”. Oslanjaj se isključivo na priloženi tekst, ",
    "poglavlja imenuj riječima, a ne brojem, i jasno reci „Toga nema u priloženom tekstu” kad ",
    "odgovora nema; ne izmišljaj brojke, izvore ni citate. Objašnjavaj korak po korak na ",
    "hrvatskom, gradi intuiciju prije formule, kad računaš pokaži postupak i pretpostavke, ",
    "prilagodi se mojoj razini i na zahtjev sažmi gradivo, izradi kviz, kartice ili plan učenja. ",
    "Na početku me pitaj što učim i koji mi je cilj."
  )

  out <- list(
    generated = DATE_STR,
    book = list(
      title = BOOK_TITLE,
      authors = AUTHOR_NAMES,
      description = BOOK_DESC,
      url = SITE_URL,
      governance = list(
        source = "release/governance.yml",
        state = GOVERNANCE_STATE,
        titleState = TITLE_STATE,
        authorshipState = AUTHORSHIP_STATE
      )
    ),
    prompt = prompt,
    promptShort = promptShort,
    full = list(mdUrl = paste0(SITE_URL, "/llms-full.txt"),
                mapUrl = paste0(SITE_URL, "/llms.txt")),
    dios = dios,
    chapters = ch
  )
  path <- file.path(OUTPUT_ROOT, "data", "ai-exports.json")
  dir.create(dirname(path), showWarnings = FALSE, recursive = TRUE)
  write_json(out, path, auto_unbox = TRUE, pretty = TRUE)
}

# ===========================================================================
tryCatch(
  main(),
  error = function(e) {
    if (RELEASE_MODE) {
      message("build-ai-exports.R: RELEASE GREŠKA — ", conditionMessage(e))
      quit(save = "no", status = 1L, runLast = FALSE)
    }
    message("build-ai-exports.R: GREŠKA — izvoz preskočen: ", conditionMessage(e))
    # Lokalni best-effort pre-render zadržava status 0 i postojeće artefakte.
  }
)
