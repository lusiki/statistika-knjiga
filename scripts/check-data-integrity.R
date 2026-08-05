#!/usr/bin/env Rscript

# Fail-closed integrity checks for the book's data.
#
# P3-CATALOG created data/katalog.yml as the sole machine-readable record and
# scripts/check-katalog.py as its schema and promotion validator. This script
# keeps the generated teaching sets honest and enforces the boundary the
# catalogue draws: the catalogue must exist, and a materialised snapshot may
# exist only when a catalogue entry declares it. An undeclared snapshot still
# fails rather than being silently admitted to the book or the release path.

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
catalogue_schema <- put("data", "katalog.schema.json")
catalogue_check <- put("scripts", "check-katalog.py")
snapshots <- list.files(put("data"), pattern = "\\.(csv|tsv|parquet|rds)$",
                        full.names = TRUE, ignore.case = TRUE)

declared_files <- character()
promoted_count <- 0L
if (!file.exists(catalogue)) {
  failures <- c(
    failures,
    "data/katalog.yml is missing; the canonical catalogue is the sole data record"
  )
} else {
  for (required in c(catalogue_schema, catalogue_check)) {
    if (!file.exists(required)) {
      failures <- c(
        failures,
        paste("the catalogue exists without its validator:", basename(required))
      )
    }
  }
  if (!requireNamespace("yaml", quietly = TRUE)) {
    failures <- c(failures, "missing R package 'yaml'; the catalogue cannot be read")
  } else {
    parsed <- yaml::read_yaml(catalogue)
    for (entry in parsed$packages) {
      if (isTRUE(entry$promoted)) promoted_count <- promoted_count + 1L
      if (length(entry$files)) {
        declared_files <- c(declared_files, unlist(entry$files, use.names = FALSE))
      }
    }
  }
}

relative_snapshots <- sub(paste0("^", root, "/"), "", snapshots)
undeclared <- setdiff(relative_snapshots, declared_files)
if (length(undeclared)) {
  failures <- c(
    failures,
    paste(
      "materialised data snapshots are not declared by any catalogue entry:",
      paste(undeclared, collapse = ", ")
    )
  )
}

fetch_text <- paste(readLines(fetch_path, warn = FALSE, encoding = "UTF-8"),
                    collapse = "\n")
for (needle in c('identical(unos$lane, "bundled")',
                 'identical(unos$redistribution, "provjerena")',
                 'KANDIDAT_DIR',
                 'promocija odbijena: katalog ne biljezi kontrolni zbroj')) {
  check(grepl(needle, fetch_text, fixed = TRUE),
        paste("fetch dispatcher lost its fail-closed candidate-first guard:", needle))
}
check(grepl("KATALOG <- \"data/katalog.yml\"", fetch_text, fixed = TRUE),
      "fetch dispatcher no longer reads the canonical catalogue as its only registry")

if (length(failures)) {
  cat("DATA_INTEGRITY_FAILED\n")
  for (failure in failures) cat("- ", failure, "\n", sep = "")
  quit(status = 1L)
}

cat(
  "DATA_INTEGRITY_OK generated_sets=2 rows=50300 catalogue=present ",
  "promoted=", promoted_count, " snapshots=", length(snapshots),
  " undeclared=0 licence=CC-BY-4.0\n",
  sep = ""
)
