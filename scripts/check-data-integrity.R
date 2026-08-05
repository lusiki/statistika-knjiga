#!/usr/bin/env Rscript

# Fail-closed integrity checks for the book's data.
#
# P3-CATALOG created data/katalog.yml as the sole machine-readable record and
# scripts/check-katalog.py as its schema and promotion validator. This script
# keeps the generated teaching sets honest and enforces the boundary the
# catalogue draws: the catalogue must exist, and a materialised snapshot may
# exist only when a catalogue entry declares it. An undeclared snapshot still
# fails rather than being silently admitted to the book or the release path.
#
# P3-EXISTING added the data-level half. Every materialised snapshot is now
# validated against the codebook, storage disposition and reconciliation
# contract that its own catalogue entry declares: encoding and line endings,
# header against codebook, key uniqueness, row band, numeric and category
# domains, code/label pairing, absent-versus-zero, the sidecar licence notice,
# and an exact recomputation of every aggregate from its analysis file. The
# recomputation is what proves the file rounds nothing: a rounded mean cannot
# equal the sum divided by the count.
#
# Deliberate file-level defects are exercised by scripts/check-data-fixtures.py
# in a temporary root; this script keeps one in-memory fixture of its own:
#
#     --fixture duplicate-key

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

# --- data-level validation of every materialised snapshot ------------------
#
# The catalogue is the contract; this section only enforces it. Nothing here
# knows the name of a column or a level: every rule is read from the entry's
# own codebook, storage disposition and reconciliation block, so a later
# package is validated by declaring itself rather than by editing this file.

MISSING_TOKENS <- c("", "NA", "na", "N/A", "NULL", "null", ".", "-", "?")

read_snapshot <- function(path) {
  size <- file.info(path)$size
  bytes <- readBin(path, "raw", n = size)
  text <- rawToChar(bytes)
  Encoding(text) <- "UTF-8"
  list(bytes = bytes, text = text)
}

split_fields <- function(line) strsplit(line, ",", fixed = TRUE)[[1]]

field_at <- function(rows, index) {
  vapply(rows, function(row) row[[index]], character(1))
}

as_exact_numeric <- function(values) suppressWarnings(as.numeric(values))

validate_file_record <- function(record, entry_id, storage) {
  problems <- character()
  note <- function(...) problems <<- c(problems, paste0(entry_id, "/",
                                                        record$path, ": ", ...))
  path <- put(record$path)
  if (!file.exists(path)) {
    note("declared snapshot is missing from disk")
    return(list(problems = problems, columns = NULL))
  }

  raw <- read_snapshot(path)
  if (length(raw$bytes) >= 3L &&
      identical(as.integer(raw$bytes[1:3]), c(239L, 187L, 191L))) {
    note("snapshot starts with a UTF-8 BOM")
  }
  if (any(raw$bytes == as.raw(13L))) {
    note("snapshot uses CR line endings; the declared ending is LF")
  }
  if (!validUTF8(raw$text)) note("snapshot is not valid UTF-8")
  if (!length(raw$bytes) || raw$bytes[[length(raw$bytes)]] != as.raw(10L)) {
    note("snapshot does not end with a newline")
  }
  if (!grepl("^[a-z0-9][a-z0-9.-]*$", basename(record$path))) {
    note("file name is not a stable lowercase ASCII name")
  }

  lines <- strsplit(raw$text, "\n", fixed = TRUE)[[1]]
  if (length(lines) < 2L) {
    note("snapshot has no data rows")
    return(list(problems = problems, columns = NULL))
  }
  header <- split_fields(lines[[1]])
  declared <- vapply(record$columns, function(column) column$name, character(1))
  if (!identical(header, declared)) {
    note("header does not match the declared codebook: file has ",
         paste(header, collapse = ", "))
    return(list(problems = problems, columns = NULL))
  }

  rows <- lapply(lines[-1], split_fields)
  widths <- vapply(rows, length, integer(1))
  if (any(widths != length(header))) {
    note("a row has a different number of fields than the header")
    return(list(problems = problems, columns = NULL))
  }
  if (length(rows) != as.integer(record$rows)) {
    note("row count ", length(rows), " differs from the declared ",
         record$rows)
  }
  band <- as.integer(unlist(record$row_band))
  if (length(rows) < band[[1]] || length(rows) > band[[2]]) {
    note("row count ", length(rows), " is outside the declared band [",
         band[[1]], ", ", band[[2]], "]")
  }

  columns <- setNames(
    lapply(seq_along(header), function(i) field_at(rows, i)), header
  )

  key <- record$key
  if (!key %in% header) {
    note("declared key column is absent: ", key)
  } else if (anyDuplicated(columns[[key]])) {
    note("key column ", key, " is not unique")
  }

  for (column in record$columns) {
    values <- columns[[column$name]]
    label <- paste0("column ", column$name, ": ")
    if (is.null(column$missing_code)) {
      if (any(values %in% MISSING_TOKENS)) {
        note(label, "declares no missing code, yet a cell is empty or ",
             "carries a conventional missing token")
      }
    } else if (!any(values == column$missing_code)) {
      note(label, "declares missing code '", column$missing_code,
           "' that never occurs")
    }

    if (column$type %in% c("integer", "code")) {
      if (!all(grepl("^-?[0-9]+$", values))) {
        note(label, "is declared integral but carries a non-integer literal")
        next
      }
    }
    if (column$type %in% c("integer", "number", "code")) {
      numbers <- as_exact_numeric(values)
      if (anyNA(numbers)) {
        note(label, "carries a value that does not parse as a number")
        next
      }
      if (!is.null(column$min) && any(numbers < as.numeric(column$min))) {
        note(label, "falls below the declared minimum ", column$min)
      }
      if (!is.null(column$max) && any(numbers > as.numeric(column$max))) {
        note(label, "rises above the declared maximum ", column$max)
      }
      if (isTRUE(column$zero_is_meaningful) && !any(numbers == 0)) {
        note(label, "declares zero as a meaningful value that never occurs")
      }
    }
    if (identical(column$type, "text") && !is.null(column$pattern)) {
      if (!all(grepl(column$pattern, values))) {
        note(label, "has a value outside its declared pattern")
      }
    }
    if (identical(column$type, "code")) {
      levels_declared <- unlist(column$levels, use.names = FALSE)
      codes <- as.integer(values)
      if (any(codes < 1L) || any(codes > length(levels_declared))) {
        note(label, "carries a code outside the declared levels")
        next
      }
      partner <- column$pairs_with
      if (is.null(partner) || !partner %in% header) {
        note(label, "declares no label column beside the code")
      } else if (!identical(levels_declared[codes], columns[[partner]])) {
        note(label, "code and label disagree; the original code must stand ",
             "beside its Croatian label, never instead of it")
      }
    }
  }

  if (!identical(storage$encoding, "UTF-8") ||
      !identical(storage$line_ending, "LF") ||
      !isTRUE(storage$filenames_ascii)) {
    note("the storage disposition does not declare UTF-8, LF and ASCII names")
  }

  list(problems = problems, columns = columns)
}

validate_reconciliation <- function(rule, entry_id, tables) {
  problems <- character()
  note <- function(...) problems <<- c(problems, paste0(entry_id, ": ", ...))

  analysis <- tables[[rule$analysis_file]]
  aggregate <- tables[[rule$aggregate_file]]
  if (is.null(analysis) || is.null(aggregate)) {
    note("reconciliation names a file that did not parse")
    return(problems)
  }

  codes <- as.integer(aggregate[[rule$group_code]])
  labels <- aggregate[[rule$group_label]]
  unit_codes <- as.integer(analysis[[rule$group_code]])
  unit_labels <- analysis[[rule$group_label]]

  counts <- vapply(codes, function(code) sum(unit_codes == code), numeric(1))
  declared_counts <- as_exact_numeric(aggregate[[rule$count_column]])
  if (!identical(counts, declared_counts)) {
    note("group counts in the aggregate do not equal the analysis file")
  }
  total <- nrow_of <- length(unit_codes)
  declared_total <- as_exact_numeric(aggregate[[rule$denominator_column]])
  if (!all(declared_total == total)) {
    note("the declared denominator does not equal the number of analysis rows")
  }
  if (sum(counts) != total) {
    note("group counts do not sum to the number of analysis rows")
  }
  for (i in seq_along(codes)) {
    expected_label <- unique(unit_labels[unit_codes == codes[[i]]])
    if (length(expected_label) != 1L || !identical(expected_label, labels[[i]])) {
      note("aggregate group label disagrees with the analysis file for code ",
           codes[[i]])
    }
  }

  for (share in rule$shares) {
    numerator <- as_exact_numeric(aggregate[[share$numerator]])
    denominator <- as_exact_numeric(aggregate[[share$denominator]])
    declared <- as_exact_numeric(aggregate[[share$share]])
    if (!identical(numerator / denominator, declared)) {
      note("share ", share$share, " does not equal ", share$numerator, " / ",
           share$denominator, " at full precision")
    }
  }

  for (sum_rule in rule$sums) {
    source_values <- as_exact_numeric(analysis[[sum_rule$source]])
    totals <- vapply(codes, function(code) {
      sum(source_values[unit_codes == code])
    }, numeric(1))
    declared_totals <- as_exact_numeric(aggregate[[sum_rule$total]])
    if (!identical(totals, declared_totals)) {
      note("total ", sum_rule$total, " does not equal the sum of ",
           sum_rule$source, " over its group")
    }
    declared_means <- as_exact_numeric(aggregate[[sum_rule$mean]])
    if (!identical(totals / counts, declared_means)) {
      note("mean ", sum_rule$mean, " does not equal ", sum_rule$total, " / ",
           rule$count_column, " at full precision; a rounded mean cannot pass")
    }
  }

  for (positive in rule$positive_counts) {
    source_values <- as_exact_numeric(analysis[[positive$source]])
    counted <- vapply(codes, function(code) {
      sum(source_values[unit_codes == code] > 0)
    }, numeric(1))
    declared <- as_exact_numeric(aggregate[[positive$count]])
    if (!identical(counted, declared)) {
      note("count ", positive$count, " does not equal the number of rows with ",
           positive$source, " above zero")
    }
  }

  problems
}

validate_notice <- function(entry) {
  problems <- character()
  path <- put(entry$snapshot_notice)
  if (!file.exists(path)) {
    return(paste0(entry$id, ": the declared snapshot licence notice is ",
                  "missing: ", entry$snapshot_notice))
  }
  text <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"),
                collapse = "\n")
  for (needle in c("creativecommons.org/licenses/by/4.0", "CC BY 4.0",
                   entry$id, "LICENCA-generirani-podaci.md")) {
    if (!grepl(needle, text, fixed = TRUE)) {
      problems <- c(problems, paste0(entry$id, ": the snapshot licence notice ",
                                     "is missing ", needle))
    }
  }
  problems
}

snapshot_failures <- character()
validated_files <- 0L
if (exists("parsed") && is.list(parsed)) {
  for (entry in parsed$packages) {
    if (!length(entry$file_records)) next

    if (is.null(entry$storage)) {
      snapshot_failures <- c(snapshot_failures, paste0(
        entry$id, ": a package with materialised files must declare a storage ",
        "disposition"
      ))
      next
    }
    if (is.null(entry$snapshot_notice)) {
      snapshot_failures <- c(snapshot_failures, paste0(
        entry$id, ": a package with materialised files must declare a ",
        "snapshot licence notice"
      ))
    } else {
      snapshot_failures <- c(snapshot_failures, validate_notice(entry))
    }

    # A sampling weight is either present as a real column or explicitly absent
    # with a reason. Silence is the failure mode this clause exists to prevent.
    analysis_record <- NULL
    for (record in entry$file_records) {
      if (identical(record$role, "analysis")) analysis_record <- record
    }
    if (is.null(entry$storage$weights)) {
      if (!nzchar(paste0(entry$storage$weights_note, ""))) {
        snapshot_failures <- c(snapshot_failures, paste0(
          entry$id, ": a package without sampling weights must record why"
        ))
      }
    } else if (!is.null(analysis_record)) {
      analysis_columns <- vapply(analysis_record$columns,
                                 function(column) column$name, character(1))
      if (!entry$storage$weights %in% analysis_columns) {
        snapshot_failures <- c(snapshot_failures, paste0(
          entry$id, ": the declared weights column is absent from the analysis ",
          "file: ", entry$storage$weights
        ))
      }
    }

    tables <- list()
    for (record in entry$file_records) {
      outcome <- validate_file_record(record, entry$id, entry$storage)
      snapshot_failures <- c(snapshot_failures, outcome$problems)
      if (!is.null(outcome$columns)) {
        tables[[record$path]] <- outcome$columns
        validated_files <- validated_files + 1L
      }
    }

    if (!is.null(entry$aggregate_reconciliation)) {
      snapshot_failures <- c(snapshot_failures, validate_reconciliation(
        entry$aggregate_reconciliation, entry$id, tables
      ))
    } else if (!is.null(entry$aggregate_view)) {
      snapshot_failures <- c(snapshot_failures, paste0(
        entry$id, ": an aggregate view exists without a reconciliation contract"
      ))
    }
  }
}
failures <- c(failures, snapshot_failures)

# --- every snapshot must still reproduce from its generator and seed --------
serialiser <- put("R", "snimke-nastavnih-podataka.R")
if (!file.exists(serialiser)) {
  failures <- c(failures, "missing serialiser: R/snimke-nastavnih-podataka.R")
} else {
  source(serialiser, local = globalenv(), encoding = "UTF-8")
  for (snapshot in snimke_nastavnih_podataka()) {
    target <- put(snapshot$putanja)
    if (!file.exists(target)) {
      failures <- c(failures, paste0(snapshot$putanja,
                                     ": declared snapshot does not exist"))
      next
    }
    expected <- csv_redci(snapshot$redci())
    found <- readLines(target, warn = FALSE, encoding = "UTF-8")
    if (!identical(enc2utf8(found), enc2utf8(expected))) {
      failures <- c(failures, paste0(
        snapshot$putanja,
        ": snapshot no longer reproduces from its declared generator and seed"
      ))
    }
  }
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
  " validated=", validated_files, " undeclared=0 licence=CC-BY-4.0\n",
  sep = ""
)
