# fetch-podaci.R ------------------------------------------------------------
# Dispecer za osvjezavanje podataka: dohvat -> kandidat -> provjera -> razlika
# -> odobrenje -> promocija.
#
#   Rscript R/fetch-podaci.R                  # svi promotivno dopusteni paketi
#   Rscript R/fetch-podaci.R dzs_turizam      # samo jedan, po kljucu
#   Rscript R/fetch-podaci.R --promote KLJUC  # promovira odobrenoga kandidata
#
# Pokrece se RUCNO, nikada pri renderu. Render koji ovisi o mrezi je render koji
# jednom pukne u najgorem trenutku, pa ova skripta nema ni jednu tocku ulaska iz
# Quartova lanca.
#
# Cetiri pravila koja ova skripta provodi i koja se ne smiju ukloniti:
#
#   1. Katalog je jedini izvor. Registar se cita iz data/katalog.yml; ova
#      skripta nema vlastiti popis paketa.
#   2. Dohvaca se samo paket u traci `bundled` s provjerenom redistribucijom.
#      Portalni i vanjski paketi ne mogu se tehnicki preuzeti ovom skriptom.
#   3. Dohvat nikada ne pise u nastavne podatke. Pise samo u privremenu mapu
#      data/_kandidat/, koja je gitignorirana.
#   4. Promocija je zaseban, izricit poziv koji trazi da kandidat postoji, da
#      katalog za taj paket biljezi kontrolni zbroj i da se zbroj poklapa.
# ---------------------------------------------------------------------------

suppressMessages({
  library(yaml)
})

KATALOG <- "data/katalog.yml"
KANDIDAT_DIR <- file.path("data", "_kandidat")

ucitaj_katalog <- function() {
  if (!file.exists(KATALOG)) {
    stop("Katalog ne postoji: ", KATALOG,
         ". Bez kanonskoga kataloga nijedan dohvat nije dopusten.")
  }
  katalog <- yaml::read_yaml(KATALOG)
  paketi <- katalog$packages
  names(paketi) <- vapply(paketi, function(p) p$id, character(1))
  paketi
}

provjeri_traku <- function(unos, kljuc) {
  if (!identical(unos$lane, "bundled") ||
      !identical(unos$redistribution, "provjerena")) {
    stop(
      "[", kljuc, "] dohvat odbijen: samo paket s provjerenom ",
      "redistribucijom i trakom bundled smije u data/. Trenutacna traka je '",
      unos$lane, "', redistribucija '", unos$redistribution, "'."
    )
  }
  invisible(TRUE)
}

dohvati <- function(unos, kljuc) {
  provjeri_traku(unos, kljuc)

  if (is.null(unos$source_url) || !nzchar(unos$source_url)) {
    message("[", kljuc, "] nema automatskoga preuzimanja. ",
            "Katalog biljezi pristup: ", unos$access)
    return(invisible(FALSE))
  }

  dir.create(KANDIDAT_DIR, showWarnings = FALSE, recursive = TRUE)
  cilj <- file.path(KANDIDAT_DIR, paste0(kljuc, ".kandidat"))

  message("[", kljuc, "] preuzimam u kandidata: ", cilj)
  ok <- tryCatch({
    utils::download.file(unos$source_url, cilj, mode = "wb", quiet = TRUE)
    TRUE
  }, error = function(e) {
    message("[", kljuc, "] NEUSPJEH: ", conditionMessage(e))
    FALSE
  })
  if (ok) {
    message("[", kljuc, "] kandidat spremljen. Nastavni podaci NISU dirnuti. ",
            "Provjeri razliku, pa promoviraj s --promote ", kljuc, ".")
  }
  invisible(ok)
}

promoviraj <- function(unos, kljuc) {
  provjeri_traku(unos, kljuc)

  kandidat <- file.path(KANDIDAT_DIR, paste0(kljuc, ".kandidat"))
  if (!file.exists(kandidat)) {
    stop("[", kljuc, "] promocija odbijena: kandidat ne postoji. ",
         "Najprije dohvati, pa pregledaj razliku.")
  }
  zbroj <- unos$integrity$checksum
  if (is.null(zbroj) || !nzchar(zbroj)) {
    stop("[", kljuc, "] promocija odbijena: katalog ne biljezi kontrolni zbroj. ",
         "Zbroj upisuje paketni gate, ne ova skripta.")
  }
  if (is.null(unos$files) || !length(unos$files)) {
    stop("[", kljuc, "] promocija odbijena: katalog ne biljezi nijedan ",
         "datotecni put za ovaj paket.")
  }
  stvarni <- tools::md5sum(kandidat)[[1]]
  if (!identical(unname(stvarni), zbroj)) {
    stop("[", kljuc, "] promocija odbijena: kontrolni zbroj kandidata (",
         stvarni, ") ne odgovara zabiljezenom (", zbroj, ").")
  }
  cilj <- unos$files[[1]]
  dir.create(dirname(cilj), showWarnings = FALSE, recursive = TRUE)
  file.copy(kandidat, cilj, overwrite = TRUE)
  message("[", kljuc, "] promovirano u ", cilj)
  invisible(TRUE)
}

args <- commandArgs(trailingOnly = TRUE)
promocija <- FALSE
if (length(args) && identical(args[[1]], "--promote")) {
  promocija <- TRUE
  args <- args[-1]
}

paketi <- ucitaj_katalog()
dopusteni <- Filter(
  function(p) identical(p$lane, "bundled") &&
    identical(p$redistribution, "provjerena"),
  paketi
)

kljucevi <- if (length(args)) args else names(dopusteni)

if (!length(kljucevi)) {
  message("Nijedan paket u katalogu nema traku bundled s provjerenom ",
          "redistribucijom, pa nema sto dohvatiti. Traku i redistribuciju ",
          "mijenja pripadni G-A3 gate, ne ova skripta.")
} else {
  for (k in kljucevi) {
    unos <- paketi[[k]]
    if (is.null(unos)) {
      message("Nepoznat kljuc: ", k, ". Katalog poznaje: ",
              paste(names(paketi), collapse = ", "))
      next
    }
    if (promocija) promoviraj(unos, k) else dohvati(unos, k)
  }
}
