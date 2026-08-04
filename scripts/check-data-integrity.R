#!/usr/bin/env Rscript

# Fail-closed integrity checks for data that exists before P3-CATALOG.
# The catalogue contract itself remains owned by P3-CATALOG. Until that packet
# adds its schema validator, an undeclared catalogue or snapshot fails rather
# than being silently admitted to the book or release path.

args <- commandArgs(trailingOnly = TRUE)
root <- normalizePath(".", winslash = "/", mustWork = TRUE)
fixture <- ""
i <- 1L
while (i <= length(args)) {
  if (identical(args[[i]], "--root") && i < length(args)) {
    root <- normalizePath(args[[i + 1L]], winslash = "/", mustWork = TRUE)
    i <- i + 2L
  } else if (identical(args[[i]], "--fixture") && i < length(args)) {
    fixture <- args[[i + 1L]]
    i <- i + 2L
  } else {
    stop("Usage: check-data-integrity.R [--root PATH] [--fixture duplicate-key]")
  }
}

put <- function(...) file.path(root, ...)
generator_path <- put("R", "podaci-nastavni.R")
notice_path <- put("data", "LICENCA-generirani-podaci.md")
fetch_path <- put("R", "fetch-podaci.R")
for (path in c(generator_path, notice_path, fetch_path)) {
  if (!file.exists(path)) stop("Missing data-integrity source: ", path)
}

source(generator_path, local = globalenv(), encoding = "UTF-8")
if (nzchar(fixture)) {
  if (!identical(fixture, "duplicate-key")) stop("Unknown fixture: ", fixture)
  anketa_mreze$ispitanik[[2]] <- anketa_mreze$ispitanik[[1]]
  message("Applied in-memory negative fixture: duplicate-key")
}

failures <- character()
check <- function(ok, message) {
  if (!isTRUE(ok)) failures <<- c(failures, message)
}

expected_anketa <- c(
  "ispitanik", "dob", "dobna_skupina", "minute_dnevno", "povjerenje"
)
expected_populacija <- c(
  "osoba", "dob", "spol", "obrazovanje", "izvor_vijesti",
  "povjerenje_medijima", "minute_medija", "spremnost_platiti"
)

check(identical(names(anketa_mreze), expected_anketa),
      "anketa_mreze schema differs from the declared columns")
check(identical(names(populacija_medija), expected_populacija),
      "populacija_medija schema differs from the declared columns")
check(nrow(anketa_mreze) == 300L, "anketa_mreze must contain 300 rows")
check(nrow(populacija_medija) == 50000L,
      "populacija_medija must contain 50000 rows")
check(!anyDuplicated(anketa_mreze$ispitanik),
      "anketa_mreze contains a duplicate respondent key")
check(!anyDuplicated(populacija_medija$osoba),
      "populacija_medija contains a duplicate population key")
check(!anyNA(anketa_mreze), "anketa_mreze contains an undeclared missing value")
check(!anyNA(populacija_medija),
      "populacija_medija contains an undeclared missing value")
check(all(anketa_mreze$dob >= 18 & anketa_mreze$dob <= 70),
      "anketa_mreze age domain is invalid")
check(all(anketa_mreze$minute_dnevno >= 1),
      "anketa_mreze daily minutes must be positive")
check(all(anketa_mreze$povjerenje >= 1 & anketa_mreze$povjerenje <= 10),
      "anketa_mreze trust domain is invalid")
check(all(populacija_medija$dob >= 18 & populacija_medija$dob <= 80),
      "populacija_medija age domain is invalid")
check(all(populacija_medija$povjerenje_medijima >= 1 &
            populacija_medija$povjerenje_medijima <= 10),
      "populacija_medija trust domain is invalid")
check(all(populacija_medija$minute_medija >= 0),
      "populacija_medija media minutes cannot be negative")
check(all(populacija_medija$spremnost_platiti >= 0),
      "populacija_medija willingness to pay cannot be negative")

check(identical(simuliraj_anketu(), anketa_mreze),
      "anketa_mreze no longer reproduces exactly from its declared seed")
check(identical(simuliraj_populaciju(), populacija_medija),
      "populacija_medija no longer reproduces exactly from its declared seed")

generator_text <- paste(readLines(generator_path, warn = FALSE, encoding = "UTF-8"),
                        collapse = "\n")
notice_text <- paste(readLines(notice_path, warn = FALSE, encoding = "UTF-8"),
                     collapse = "\n")
for (needle in c("anketa_mreze", "populacija_medija", "CC BY 4.0", "Luka Sikic")) {
  check(grepl(needle, generator_text, fixed = TRUE),
        paste("generator licence notice is missing", needle))
  check(grepl(needle, notice_text, fixed = TRUE),
        paste("download-adjacent licence notice is missing", needle))
}

catalogue <- put("data", "katalog.yml")
snapshots <- list.files(put("data"), pattern = "\\.(csv|tsv|parquet|rds)$",
                        full.names = TRUE, ignore.case = TRUE)
if (file.exists(catalogue)) {
  failures <- c(
    failures,
    paste(
      "data/katalog.yml exists but P3-CATALOG has not yet supplied its",
      "ratified schema/checksum validator; promotion fails closed"
    )
  )
}
if (length(snapshots)) {
  failures <- c(
    failures,
    paste(
      "materialised data snapshots exist before the canonical catalogue",
      paste(basename(snapshots), collapse = ", ")
    )
  )
}

fetch_text <- paste(readLines(fetch_path, warn = FALSE, encoding = "UTF-8"),
                    collapse = "\n")
for (needle in c('identical(unos$traka, "bundled")',
                 'identical(unos$redistribucija, "provjerena")')) {
  check(grepl(needle, fetch_text, fixed = TRUE),
        paste("fetch dispatcher lost its fail-closed lane guard:", needle))
}

if (length(failures)) {
  cat("DATA_INTEGRITY_FAILED\n")
  for (failure in failures) cat("- ", failure, "\n", sep = "")
  quit(status = 1L)
}

cat(
  "DATA_INTEGRITY_OK generated_sets=2 rows=50300 catalogue=pre-P3 ",
  "snapshots=0 licence=CC-BY-4.0\n",
  sep = ""
)
