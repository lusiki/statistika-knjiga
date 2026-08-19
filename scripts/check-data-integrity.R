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

field_at <- function(rows, index) {
  vapply(rows, function(row) row[[index]], character(1))
}

as_exact_numeric <- function(values) suppressWarnings(as.numeric(values))

validate_file_record <- function(record, entry_id, storage, source_codes = character()) {
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
  if (!grepl("^[a-z0-9][a-z0-9._-]*$", basename(record$path))) {
    note("file name is not a stable lowercase ASCII name")
  }

  parsed <- tryCatch(
    read.csv(
      text = raw$text,
      header = TRUE,
      check.names = FALSE,
      stringsAsFactors = FALSE,
      colClasses = "character",
      na.strings = character(),
      quote = "\"",
      comment.char = "",
      strip.white = FALSE
    ),
    error = function(error) error
  )
  if (inherits(parsed, "error")) {
    note("CSV parser failed: ", conditionMessage(parsed))
    return(list(problems = problems, columns = NULL))
  }
  if (!nrow(parsed)) {
    note("snapshot has no data rows")
    return(list(problems = problems, columns = NULL))
  }
  header <- names(parsed)
  declared <- vapply(record$columns, function(column) column$name, character(1))
  if (!identical(header, declared)) {
    note("header does not match the declared codebook: file has ",
         paste(header, collapse = ", "))
    return(list(problems = problems, columns = NULL))
  }

  rows <- lapply(seq_len(nrow(parsed)), function(index) {
    unname(as.character(parsed[index, , drop = TRUE]))
  })
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

  # A published cross-tabulation is identified by its dimensions together, so
  # the key may name several columns joined by '+'. Inventing one surrogate
  # column instead would add data the source does not have.
  key_columns <- strsplit(record$key, "+", fixed = TRUE)[[1]]
  missing_key <- setdiff(key_columns, header)
  if (length(missing_key)) {
    note("declared key column is absent: ", paste(missing_key, collapse = ", "))
  } else {
    tuples <- do.call(paste, c(columns[key_columns], sep = "\r"))
    if (anyDuplicated(tuples)) {
      note("key ", record$key, " is not unique")
    }
  }

  for (column in record$columns) {
    values <- columns[[column$name]]
    label <- paste0("column ", column$name, ": ")

    # A declared missing code is a value, not a hole. It is checked for its own
    # presence and then set aside, because a code can never satisfy the type,
    # domain or level rules of the quantity it stands in for.
    # A stray is any conventional missing token, or any absence code the SOURCE
    # publishes, turning up in a column that does not declare it. Without the
    # source's own codes the test would miss exactly the codes that matter:
    # '..' and '....' are absence codes in official statistics and in no
    # general-purpose list of missing tokens.
    absence_tokens <- union(MISSING_TOKENS, source_codes)
    if (is.null(column$missing_code)) {
      if (any(values %in% absence_tokens)) {
        note(label, "declares no missing code, yet a cell is empty or ",
             "carries a conventional missing token")
      }
      present <- values
      keep <- rep(TRUE, length(values))
    } else {
      if (!any(values == column$missing_code)) {
        note(label, "declares missing code '", column$missing_code,
             "' that never occurs")
      }
      stray <- setdiff(intersect(values, absence_tokens), column$missing_code)
      if (length(stray)) {
        note(label, "carries a missing token it does not declare: ",
             paste(stray, collapse = ", "),
             ". Every published absence code keeps its own meaning.")
      }
      keep <- values != column$missing_code
      present <- values[keep]
    }

    if (column$type %in% c("integer", "code")) {
      if (!all(grepl("^-?[0-9]+$", present))) {
        note(label, "is declared integral but carries a non-integer literal")
        next
      }
    }
    if (column$type %in% c("integer", "number", "code")) {
      numbers <- as_exact_numeric(present)
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
      if (!all(grepl(column$pattern, present))) {
        note(label, "has a value outside its declared pattern")
      }
    }
    # A label column may declare its level set. Checking membership beats a
    # regular expression over Croatian text and catches a stray or renamed
    # level, which is exactly how a published category quietly changes.
    if (column$type %in% c("text", "label") && !is.null(column$levels)) {
      levels_declared <- unlist(column$levels, use.names = FALSE)
      outside <- setdiff(present, levels_declared)
      if (length(outside)) {
        note(label, "carries a value outside its declared levels: ",
             paste(outside, collapse = ", "))
      }
      unused <- setdiff(levels_declared, present)
      if (length(unused)) {
        note(label, "declares a level that never occurs: ",
             paste(unused, collapse = ", "))
      }
    }
    if (identical(column$type, "code")) {
      levels_declared <- unlist(column$levels, use.names = FALSE)
      codes <- as.integer(present)
      if (any(codes < 1L) || any(codes > length(levels_declared))) {
        note(label, "carries a code outside the declared levels")
        next
      }
      partner <- column$pairs_with
      if (is.null(partner) || !partner %in% header) {
        note(label, "declares no label column beside the code")
      } else if (!identical(levels_declared[codes], columns[[partner]][keep])) {
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

# The notice must carry the terms of THIS package, not the terms the first two
# packages happened to share. Before P3-DZS this function demanded a CC BY 4.0
# link of every package; the first package under the Croatian Open Licence would
# have had to print a false one to pass.
validate_notice <- function(entry) {
  problems <- character()
  path <- put(entry$snapshot_notice)
  if (!file.exists(path)) {
    return(paste0(entry$id, ": the declared snapshot licence notice is ",
                  "missing: ", entry$snapshot_notice))
  }
  text <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"),
                collapse = "\n")
  needles <- c(entry$id, entry$licence, entry$licence_uri)
  if (!is.null(entry$generated_data_notice)) {
    needles <- c(needles, basename(entry$generated_data_notice))
  }
  if (is.null(entry$licence_uri) || !nzchar(entry$licence_uri)) {
    problems <- c(problems, paste0(
      entry$id, ": a package that ships a snapshot notice must declare the ",
      "direct link to its own licence"
    ))
  }
  for (needle in needles) {
    if (!grepl(needle, text, fixed = TRUE)) {
      problems <- c(problems, paste0(entry$id, ": the snapshot licence notice ",
                                     "is missing ", needle))
    }
  }
  problems
}

# --- a published total against its published parts -------------------------
#
# Declarative on purpose: nothing here knows a column name. The rule states
# which rows are the total, which are the parts, what must agree between them,
# and how large a residual is admissible. A count reconciles at zero. A survey
# estimate rounds every published cell independently, so its parts need not sum
# to its total; that residual is recorded exactly and compared for equality, so
# it can neither grow unnoticed nor be quietly rounded away.
or_list <- function(x) if (is.null(x)) list() else x

select_rows <- function(table, filters) {
  keep <- rep(TRUE, length(table[[1]]))
  for (filter in or_list(filters)) {
    if (!filter$column %in% names(table)) {
      return(list(rows = NULL, missing = filter$column))
    }
    values <- unlist(filter$values, use.names = FALSE)
    keep <- keep & table[[filter$column]] %in% values
  }
  list(rows = which(keep), missing = NULL)
}

validate_source_reconciliation <- function(rule, entry_id, tables) {
  messages <- character()
  note <- function(...) {
    messages <<- c(messages, paste0(entry_id, "/", rule$id, ": ", ...))
  }

  total_table <- tables[[rule$total$file]]
  parts_table <- tables[[rule$parts$file]]
  if (is.null(total_table) || is.null(parts_table)) {
    note("names a file that did not parse")
    return(messages)
  }

  total_side <- select_rows(total_table, rule$total$filters)
  parts_side <- select_rows(parts_table, rule$parts$filters)
  for (side in list(list("total", total_side), list("parts", parts_side))) {
    if (!is.null(side[[2]]$missing)) {
      note("the ", side[[1]], " side filters on a column the file does not ",
           "have: ", side[[2]]$missing)
    }
  }
  if (length(messages)) return(messages)
  total_rows <- total_side$rows
  parts_rows <- parts_side$rows
  if (!length(total_rows)) {
    note("selects no total row at all")
    return(messages)
  }
  if (!length(parts_rows)) {
    note("selects no part row at all")
    return(messages)
  }

  match_on <- unlist(or_list(rule$match_on), use.names = FALSE)
  values <- unlist(rule$values, use.names = FALSE)
  tolerance <- as.numeric(rule$tolerance)

  total_key <- if (length(match_on)) {
    do.call(paste, c(lapply(match_on, function(c) total_table[[c]][total_rows]),
                     sep = "\r"))
  } else {
    rep("", length(total_rows))
  }
  parts_key <- if (length(match_on)) {
    do.call(paste, c(lapply(match_on, function(c) parts_table[[c]][parts_rows]),
                     sep = "\r"))
  } else {
    rep("", length(parts_rows))
  }

  comparisons <- 0L
  observed <- 0
  for (i in seq_along(total_rows)) {
    selected <- parts_rows[parts_key == total_key[[i]]]
    if (!length(selected)) {
      note("a total row has no matching part row")
      next
    }
    for (value in values) {
      total <- as_exact_numeric(total_table[[value]][total_rows[[i]]])
      part_sum <- sum(as_exact_numeric(parts_table[[value]][selected]))
      if (is.na(total) || is.na(part_sum)) {
        note("column ", value, " does not parse as a number on both sides")
        next
      }
      residual <- total - part_sum
      comparisons <- comparisons + 1L
      observed <- max(observed, abs(residual))
      if (abs(residual) > tolerance) {
        note("column ", value, " leaves a residual of ", format(residual,
             scientific = FALSE), ", above the declared tolerance ", tolerance)
      }
    }
  }

  if (comparisons != as.integer(rule$comparisons)) {
    note("made ", comparisons, " comparisons, not the declared ",
         rule$comparisons)
  }
  if (observed != as.numeric(rule$max_abs_residual)) {
    note("the largest residual is ", format(observed, scientific = FALSE),
         ", not the recorded ", rule$max_abs_residual,
         "; a residual is recorded exactly, never rounded away")
  }
  messages
}

validate_non_official_substitute <- function(rule, entry_id, tables) {
  messages <- character()
  note <- function(...) {
    messages <<- c(messages, paste0(entry_id, "/non_official_substitute: ", ...))
  }

  tests <- rule$tests
  required <- c("byte_for_byte_reproduction", "denominator_identity",
                "recorded_divergence")
  if (!identical(rule$status, "satisfied") ||
      !all(required %in% names(tests)) ||
      !all(vapply(required, function(x) identical(tests[[x]]$status, "passed"),
                  logical(1)))) {
    note("a satisfied substitute must carry all three passed tests")
    return(messages)
  }

  byte_test <- tests$byte_for_byte_reproduction
  if (!file.exists(file.path(root, byte_test$builder))) {
    note("the byte-reproduction test names a builder that does not exist")
  }

  denominator <- tests$denominator_identity
  table <- tables[[denominator$file]]
  if (is.null(table)) {
    note("the denominator test names a file that did not parse")
  } else {
    groups <- split(seq_along(table[[denominator$group_by]]),
                    table[[denominator$group_by]])
    residuals <- vapply(groups, function(rows) {
      values <- as_exact_numeric(table[[denominator$value]][rows])
      declared <- unique(as_exact_numeric(table[[denominator$denominator]][rows]))
      if (length(declared) != 1L || anyNA(c(values, declared))) return(Inf)
      sum(values) - declared
    }, numeric(1))
    if (length(groups) != as.integer(denominator$comparisons)) {
      note("the denominator identity made ", length(groups),
           " comparisons, not the recorded ", denominator$comparisons)
    }
    if (any(abs(residuals) > as.numeric(denominator$tolerance))) {
      note("the denominator identity exceeds its recorded tolerance")
    }
  }

  divergence <- tests$recorded_divergence
  annual <- tables[[divergence$annual_file]]
  monthly <- tables[[divergence$monthly_file]]
  if (is.null(annual) || is.null(monthly)) {
    note("the divergence test names a file that did not parse")
    return(messages)
  }
  match_on <- unlist(divergence$match_on, use.names = FALSE)
  key <- function(table) do.call(paste, c(table[match_on], sep = "\r"))
  annual_key <- key(annual)
  monthly_key <- key(monthly)
  annual_values <- as_exact_numeric(annual[[divergence$value]])
  monthly_values <- as_exact_numeric(monthly[[divergence$value]])
  monthly_sum <- tapply(monthly_values, monthly_key, sum)
  if (anyDuplicated(annual_key) || !setequal(annual_key, names(monthly_sum))) {
    note("the annual and monthly files do not expose the same comparison keys")
    return(messages)
  }
  differences <- as.numeric(monthly_sum[annual_key]) - annual_values
  if (sum(differences != 0) != as.integer(divergence$differing_cells)) {
    note("the number of divergent cells is not the recorded ",
         divergence$differing_cells)
  }
  if (sum(differences) != as.numeric(divergence$net_difference)) {
    note("the corpus-wide divergence does not equal the recorded net difference")
  }
  compared_total <- as.numeric(divergence$compared_total)
  if (sum(annual_values) != compared_total || sum(monthly_values) != compared_total) {
    note("the two files do not both equal the recorded compared total")
  }

  check_extreme <- function(which_fun, recorded, label) {
    i <- which_fun(differences)
    if (differences[[i]] != as.numeric(recorded$difference)) {
      note("the ", label, " divergence is not the recorded value")
    }
    for (field in names(recorded$match)) {
      if (!identical(as.character(annual[[field]][[i]]),
                     as.character(recorded$match[[field]]))) {
        note("the ", label, " divergence is not in the recorded cell")
      }
    }
  }
  check_extreme(which.max, divergence$largest_positive, "largest positive")
  check_extreme(which.min, divergence$largest_negative, "largest negative")
  messages
}

validate_digikat_repairs <- function(entry, tables) {
  messages <- character()
  note <- function(...) messages <<- c(messages, paste0(entry$id, ": ", ...))
  annual <- tables[["data/digikat-platforme-godisnje.csv"]]
  monthly <- tables[["data/digikat-platforme-mjesecno.csv"]]
  sources <- tables[["data/digikat-izvori.csv"]]
  if (is.null(annual) || is.null(monthly) || is.null(sources)) return(messages)

  full <- unique(data.frame(godina = annual$godina,
                            potpuna = annual$godina_potpuna,
                            stringsAsFactors = FALSE))
  expected_full <- c("2021", "2022", "2023", "2025")
  if (!identical(full$godina[full$potpuna == "da"], expected_full) ||
      any(full$potpuna[full$godina %in% c("2024", "2026")] != "ne")) {
    note("godina_potpuna must mark exactly 2021, 2022, 2023 and 2025 complete")
  }
  months_2024 <- sort(unique(monthly$mjesec[monthly$godina == "2024"]))
  if (!identical(months_2024, c("2024-01", sprintf("2024-%02d", 6:12)))) {
    note("the 2024 gap must leave February-May visibly absent")
  }
  january_posts <- sum(as_exact_numeric(monthly$objave[monthly$mjesec == "2024-01"]))
  if (january_posts != 1911) note("January 2024 must retain its partial 1911 posts")

  annual_expected <- ifelse(
    as.integer(annual$godina) <= 2022L, "prije_promjene_obuhvata",
    ifelse(as.integer(annual$godina) == 2023L, "tiktok_od_2023-07",
           ifelse(as.integer(annual$godina) == 2024L,
                  "nepotpuno_lom_2024-06_instagram_od_2024-07",
                  "nakon_loma_2024-06")))
  monthly_expected <- ifelse(
    monthly$mjesec < "2023-07", "prije_promjene_obuhvata",
    ifelse(monthly$mjesec < "2024-06", "tiktok_od_2023-07",
           ifelse(monthly$mjesec == "2024-06", "lom_2024-06",
                  "nakon_loma_2024-06_instagram_od_2024-07")))
  if (!identical(annual$lom_metode, annual_expected) ||
      !identical(monthly$lom_metode, monthly_expected)) {
    note("the method-break flags do not match the recorded coverage changes")
  }
  if (length(sources$izvor) != 3604L ||
      sum(as_exact_numeric(sources$objave)) != 551712) {
    note("the source file must retain 3604 domains carrying 551712 posts")
  }
  messages
}

validate_eurostat_snapshot <- function(entry, tables) {
  messages <- character()
  note <- function(...) messages <<- c(messages, paste0(entry$id, ": ", ...))
  path <- "data/eurostat-drustvo-2025.csv"
  table <- tables[[path]]
  if (is.null(table)) return(messages)

  expected_geo <- c(
    "AT", "BE", "BG", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "EL",
    "HR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT",
    "RO", "SK", "SI", "ES", "SE"
  )
  expected_indicators <- c(
    "stopa_zaposlenosti_20_64",
    "rizik_siromastva_ili_iskljucenosti",
    "tercijarno_obrazovanje_25_34",
    "rano_napustanje_obrazovanja_18_24",
    "uporaba_interneta_16_74",
    "udio_stanovnistva_65_plus"
  )
  keys <- paste(table$geo, table$godina, table$pokazatelj, sep = "\r")
  if (length(keys) != 162L || anyDuplicated(keys) ||
      !setequal(unique(table$geo), expected_geo) ||
      !setequal(unique(table$pokazatelj), expected_indicators) ||
      any(table$godina != "2025")) {
    note("the ratified 27-country x 6-indicator x 2025 key grid is not exact")
  }

  unavailable <- table$vrijednost_dostupna == "ne"
  expected_missing <- table$geo == "LU" &
    table$pokazatelj == "rano_napustanje_obrazovanja_18_24" &
    table$godina == "2025"
  if (!identical(unavailable, expected_missing) ||
      !identical(table$vrijednost == ":", expected_missing)) {
    note("the one official missing value must remain LU early-leaving 2025 and ':'")
  }
  if (sum(expected_missing) != 1L ||
      table$status_api[expected_missing] != "u" ||
      table$obs_status[expected_missing] != "u" ||
      table$conf_status[expected_missing] != "bez_objavljene_oznake") {
    note("the official LU missing value must retain API/OBS status u and explicit absent CONF status")
  }
  if (any(table$status_api != table$obs_status) ||
      any(table$conf_status != "bez_objavljene_oznake")) {
    note("selected status tokens must remain observational and confidentiality-unmarked")
  }

  builder <- put("scripts", "build-eurostat-extracts.py")
  python <- Sys.which("python")
  if (!file.exists(builder)) {
    note("offline Eurostat builder is absent")
  } else if (!nzchar(python)) {
    note("Python is unavailable for the offline Eurostat builder check")
  } else {
    output <- suppressWarnings(system2(
      python, shQuote(builder), stdout = TRUE, stderr = TRUE
    ))
    status <- attr(output, "status")
    if (is.null(status)) status <- 0L
    if (status != 0L) {
      note("offline builder verification failed: ", paste(output, collapse = " | "))
    }
  }
  messages
}

snapshot_failures <- character()
validated_files <- 0L
reconciliations <- 0L
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

    source_codes <- vapply(or_list(entry$missing_value_codes),
                           function(code) as.character(code$code), character(1))
    tables <- list()
    for (record in entry$file_records) {
      outcome <- validate_file_record(record, entry$id, entry$storage, source_codes)
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

    # A package built from a published source must reconcile against that
    # source's own totals, not only against itself.
    for (rule in or_list(entry$source_reconciliation)) {
      snapshot_failures <- c(snapshot_failures,
                             validate_source_reconciliation(rule, entry$id, tables))
      reconciliations <- reconciliations + 1L
    }
    if (!is.null(entry$integrity$non_official_reconciliation_substitute)) {
      snapshot_failures <- c(
        snapshot_failures,
        validate_non_official_substitute(
          entry$integrity$non_official_reconciliation_substitute,
          entry$id,
          tables
        )
      )
      reconciliations <- reconciliations + 1L
    }
    if (identical(entry$id, "digikat_mediji")) {
      snapshot_failures <- c(snapshot_failures,
                             validate_digikat_repairs(entry, tables))
    }
    if (identical(entry$id, "eurostat_drustvo")) {
      snapshot_failures <- c(snapshot_failures,
                             validate_eurostat_snapshot(entry, tables))
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
  " validated=", validated_files, " reconciliations=", reconciliations,
  " undeclared=0\n",
  sep = ""
)
