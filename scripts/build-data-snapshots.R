#!/usr/bin/env Rscript

# build-data-snapshots.R ----------------------------------------------------
# Materijalizira CSV snimke generiranih nastavnih skupova.
#
#   python bookwright_plugin/bookwright/scripts/run_rscript.py \
#     scripts/build-data-snapshots.R            # samo provjeri
#
#   python bookwright_plugin/bookwright/scripts/run_rscript.py \
#     scripts/build-data-snapshots.R --write    # zapisi
#
# Zadano ponasanje je PROVJERA, ne pisanje. Skripta usporedi bajtove snimke s
# onim sto generator proizvede iz deklariranoga sjemena i pada ako se
# razlikuju. Tek `--write` prepisuje datoteke, i to je jedini nacin na koji
# snimka smije nastati.
#
# Skripta se pokrece RUCNO. Nije u Quartovu lancu, pa render nikada ne pise u
# data/. Prije nego sto se snimka urezi, njezina putanja mora vec stajati u
# data/katalog.yml, inace scripts/check-data-integrity.R pada na neprijavljenoj
# snimci.
# ---------------------------------------------------------------------------

options(OutDec = ".")

args <- commandArgs(trailingOnly = TRUE)
root <- normalizePath(".", winslash = "/", mustWork = TRUE)
pisi <- FALSE
i <- 1L
while (i <= length(args)) {
  if (identical(args[[i]], "--write")) {
    pisi <- TRUE
    i <- i + 1L
  } else if (identical(args[[i]], "--root") && i < length(args)) {
    root <- normalizePath(args[[i + 1L]], winslash = "/", mustWork = TRUE)
    i <- i + 2L
  } else {
    stop("Usage: build-data-snapshots.R [--root PATH] [--write]")
  }
}

put <- function(...) file.path(root, ...)
source(put("R", "podaci-nastavni.R"), local = globalenv(), encoding = "UTF-8")
source(put("R", "snimke-nastavnih-podataka.R"), local = globalenv(),
       encoding = "UTF-8")

neuskladjene <- character()
for (snimka in snimke_nastavnih_podataka()) {
  ocekivano <- csv_redci(snimka$redci())
  cilj <- put(snimka$putanja)
  if (pisi) {
    zapisi_snimku(ocekivano, cilj)
    cat("zapisano: ", snimka$putanja, " (", length(ocekivano) - 1L,
        " redaka)\n", sep = "")
    next
  }
  if (!file.exists(cilj)) {
    neuskladjene <- c(neuskladjene,
                      paste0(snimka$putanja, ": snimka ne postoji"))
    next
  }
  zateceno <- readLines(cilj, warn = FALSE, encoding = "UTF-8")
  if (!identical(enc2utf8(zateceno), enc2utf8(ocekivano))) {
    neuskladjene <- c(
      neuskladjene,
      paste0(snimka$putanja, ": snimka se ne poklapa s generatorom i sjemenom")
    )
  }
}

if (length(neuskladjene)) {
  cat("DATA_SNAPSHOTS_FAILED\n")
  for (poruka in neuskladjene) cat("- ", poruka, "\n", sep = "")
  quit(status = 1L)
}

if (!pisi) {
  cat("DATA_SNAPSHOTS_OK snapshots=", length(snimke_nastavnih_podataka()),
      " mode=verify\n", sep = "")
} else {
  cat("DATA_SNAPSHOTS_OK snapshots=", length(snimke_nastavnih_podataka()),
      " mode=write\n", sep = "")
}
