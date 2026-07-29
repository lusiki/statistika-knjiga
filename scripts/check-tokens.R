# check-tokens.R ------------------------------------------------------------
# Provjerava da su svi slojevi dizajna usklađeni s design-tokens.yml.
#
#   Rscript scripts/check-tokens.R
#
# Dizajn knjige živi na točno četiri mjesta:
#   design-tokens.yml            IZVOR ISTINE (paleta + pisma)
#   styles/_tokens.scss   HTML sloj
#   tex/theme.tex         tiskarski (LaTeX) sloj
#   R/theme_book.R        grafovi — ČITA design-tokens.yml, pa se ne provjerava
#
# Slojevi se povezuju oznakama u komentaru:
#   _tokens.scss:  $tok-accent: #2563A8;            // token:accent
#   theme.tex:     \definecolor{accent}{HTML}{2563A8}  % token:accent
#
# Skripta usporedi hex vrijednosti po imenu tokena i ispiše svaku razliku
# s brojem retka. Izlazni kod 1 ako nešto ne odgovara, pa se može staviti
# u CI ili pre-commit hook.
# ---------------------------------------------------------------------------

if (!requireNamespace("yaml", quietly = TRUE)) {
  stop("Nedostaje paket 'yaml'. Instaliraj s install.packages('yaml').")
}

root <- normalizePath(".", winslash = "/")
put <- function(...) file.path(root, ...)

BRAND  <- put("design-tokens.yml")
TOKENS <- put("styles", "_tokens.scss")
THEME  <- put("tex", "theme.tex")

for (f in c(BRAND, TOKENS, THEME)) {
  if (!file.exists(f)) stop("Ne postoji: ", f)
}

norm_hex <- function(x) toupper(sub("^#", "", trimws(x)))

# --- 1. izvor istine --------------------------------------------------------
paleta <- yaml::read_yaml(BRAND)$color$palette
if (is.null(paleta)) stop("design-tokens.yml nema color.palette blok.")
izvor <- vapply(paleta, norm_hex, character(1))

# --- 2. pokupi oznake `token:<ime>` iz sloja --------------------------------
pokupi <- function(datoteka) {
  redci <- readLines(datoteka, warn = FALSE, encoding = "UTF-8")
  idx <- grep("token:[a-z-]+", redci)
  if (length(idx) == 0) return(list(hex = character(0), red = integer(0)))
  ime <- sub(".*token:([a-z-]+).*", "\\1", redci[idx])
  hex <- sub(".*?#?([0-9A-Fa-f]{6}).*", "\\1", redci[idx])
  ok  <- grepl("[0-9A-Fa-f]{6}", redci[idx])
  list(hex = setNames(norm_hex(hex[ok]), ime[ok]), red = setNames(idx[ok], ime[ok]))
}

slojevi <- list(
  "styles/_tokens.scss" = pokupi(TOKENS),
  "tex/theme.tex"       = pokupi(THEME)
)

# --- 3. usporedba -----------------------------------------------------------
greske <- 0L
poruka <- function(...) cat(..., "\n", sep = "")

poruka("Izvor istine: design-tokens.yml  (", length(izvor), " tokena)")
poruka("")

for (naziv in names(slojevi)) {
  s <- slojevi[[naziv]]
  lokalno   <- 0L
  nedostaje <- setdiff(names(izvor), names(s$hex))
  visak     <- setdiff(names(s$hex), names(izvor))

  poruka("── ", naziv)
  if (length(nedostaje)) {
    lokalno <- lokalno + length(nedostaje)
    poruka("   NEDOSTAJE token: ", paste(nedostaje, collapse = ", "))
  }
  if (length(visak)) {
    poruka("   (upozorenje) token koji design-tokens.yml ne poznaje: ",
           paste(visak, collapse = ", "))
  }
  for (ime in intersect(names(izvor), names(s$hex))) {
    if (izvor[[ime]] != s$hex[[ime]]) {
      lokalno <- lokalno + 1L
      poruka("   RAZLIKA  ", ime, ": design-tokens.yml #", izvor[[ime]],
             "  vs  #", s$hex[[ime]], "  (redak ", s$red[[ime]], ")")
    }
  }
  if (lokalno == 0) poruka("   u redu")
  greske <- greske + lokalno
  poruka("")
}

# --- 4. sirovi hex izvan sloja tokena ---------------------------------------
# Dizajn se mijenja na jednom mjestu samo ako nigdje drugdje nema hexova.
# _dark.scss je drugi legitiman sloj tokena (invertirane vrijednosti za tamni
# način) pa je izuzet iz ove provjere, kao i sam _tokens.scss.
kandidati <- c(
  list.files(put("styles"), pattern = "\\.(scss|css)$", full.names = TRUE),
  list.files(put("styles"), pattern = "\\.html$", full.names = TRUE)
)
kandidati <- setdiff(kandidati, c(TOKENS, put("styles", "_dark.scss")))
# Negativni pogled unaprijed izbjegava lažne pogotke na CSS selektorima i
# Quarto sidrima koja slučajno počinju heksadekadskim slovima (#def-, #fed…).
HEX_RE <- "#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?![0-9A-Za-z_-])"
prljavi <- list()
for (f in kandidati) {
  redci <- readLines(f, warn = FALSE, encoding = "UTF-8")
  idx <- grep(HEX_RE, redci, perl = TRUE)
  if (length(idx)) prljavi[[basename(f)]] <- idx
}
if (length(prljavi)) {
  poruka("── sirovi hex izvan _tokens.scss (popravi na izvoru, ne ovdje)")
  for (f in names(prljavi)) {
    poruka("   ", f, ": redci ", paste(prljavi[[f]], collapse = ", "))
  }
  poruka("")
  greske <- greske + length(prljavi)
}

if (greske > 0) {
  poruka("NIJE USKLAĐENO — ", greske, " problem(a). Vidi DESIGN.md.")
  quit(status = 1)
}
poruka("Svi slojevi dizajna usklađeni s design-tokens.yml.")
