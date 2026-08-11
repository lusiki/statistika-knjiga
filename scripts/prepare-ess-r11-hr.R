#!/usr/bin/env Rscript

# Prepare a reader-owned ESS Round 11 Croatia subset without network access.
# Input and output must remain outside this repository. The source SAV is read
# with user-defined missing values preserved so that denominators are derived
# from edition-specific metadata rather than remembered numeric codes.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2L) {
  stop(
    paste(
      "Usage: prepare-ess-r11-hr.R <official-ESS11-edition-3.0.sav>",
      "<output-directory-outside-repository>"
    ),
    call. = FALSE
  )
}

required_packages <- c("haven", "jsonlite")
missing_packages <- required_packages[
  !vapply(required_packages, requireNamespace, logical(1), quietly = TRUE)
]
if (length(missing_packages)) {
  stop(
    "Missing required R packages: ", paste(missing_packages, collapse = ", "),
    call. = FALSE
  )
}

normalise_existing <- function(path) {
  normalizePath(path, winslash = "/", mustWork = TRUE)
}

normalise_future <- function(path) {
  parent <- dirname(path)
  parent_resolved <- normalizePath(parent, winslash = "/", mustWork = TRUE)
  paste0(parent_resolved, "/", basename(path))
}

inside <- function(path, root) {
  path_lower <- tolower(path)
  root_lower <- tolower(sub("/+$", "", root))
  identical(path_lower, root_lower) || startsWith(path_lower, paste0(root_lower, "/"))
}

full_args <- commandArgs(trailingOnly = FALSE)
script_arg <- grep("^--file=", full_args, value = TRUE)
if (!length(script_arg)) {
  stop("Cannot determine the repository boundary from the script path.", call. = FALSE)
}
script_path <- normalise_existing(sub("^--file=", "", script_arg[[1]]))
repo_root <- normalise_existing(file.path(dirname(script_path), ".."))
input_path <- normalise_existing(args[[1]])

if (tolower(tools::file_ext(input_path)) != "sav") {
  stop("The official input must be a SAV file so labels and missing metadata survive.", call. = FALSE)
}
if (inside(input_path, repo_root)) {
  stop("ESS input is inside the repository; move the reader-owned file outside it.", call. = FALSE)
}

output_arg <- args[[2]]
output_parent <- dirname(output_arg)
if (!dir.exists(output_parent)) {
  stop("The parent of the output directory must already exist.", call. = FALSE)
}
output_path <- normalise_future(output_arg)
if (inside(output_path, repo_root)) {
  stop("ESS output would be inside the repository; choose an external directory.", call. = FALSE)
}
dir.create(output_path, recursive = FALSE, showWarnings = FALSE)
output_path <- normalise_existing(output_path)

identity_variables <- c("essround", "edition", "proddate", "idno", "cntry")
design_variables <- c(
  "dweight", "pspwght", "pweight", "anweight", "prob", "stratum", "psu"
)
teaching_variables <- c("vote", "trstprl", "stflife", "gndr", "agea", "eisced")
required_variables <- c(identity_variables, design_variables, teaching_variables)

source_data <- haven::read_sav(input_path, user_na = TRUE)
absent <- setdiff(required_variables, names(source_data))
if (length(absent)) {
  stop("Official file is missing required variables: ", paste(absent, collapse = ", "), call. = FALSE)
}

plain_values <- function(x) {
  as.character(unclass(x))
}

round_values <- unique(plain_values(source_data$essround[!is.na(source_data$essround)]))
if (!length(round_values) || any(round_values != "11")) {
  stop("essround does not identify only ESS Round 11.", call. = FALSE)
}
edition_values <- unique(plain_values(source_data$edition[!is.na(source_data$edition)]))
edition_normalised <- sub("[.]0+$", "", edition_values)
if (!length(edition_values) || any(edition_normalised != "3")) {
  stop("edition does not identify edition 3.0.", call. = FALSE)
}

country <- as.character(source_data$cntry)
hr_rows <- !is.na(country) & country == "HR"
if (!any(hr_rows)) {
  stop("The official integrated file contains no cntry == HR rows.", call. = FALSE)
}
selected <- source_data[hr_rows, required_variables, drop = FALSE]

key <- paste(
  plain_values(selected$essround),
  as.character(selected$cntry),
  plain_values(selected$idno),
  sep = "|"
)
if (any(is.na(selected$idno)) || anyDuplicated(key)) {
  stop("essround + cntry + idno is not a complete unique key in the HR subset.", call. = FALSE)
}

metadata_record <- function(name, x) {
  variable_label <- attr(x, "label", exact = TRUE)
  value_labels <- attr(x, "labels", exact = TRUE)
  missing_values <- attr(x, "na_values", exact = TRUE)
  missing_range <- attr(x, "na_range", exact = TRUE)

  if (name %in% teaching_variables) {
    if (is.null(variable_label) || !nzchar(as.character(variable_label))) {
      stop("Missing official variable label for ", name, ".", call. = FALSE)
    }
    if (is.null(value_labels) || !length(value_labels)) {
      stop("Missing official value labels for ", name, ".", call. = FALSE)
    }
    if ((is.null(missing_values) || !length(missing_values)) &&
        (is.null(missing_range) || !length(missing_range))) {
      stop("Missing official user-defined missing metadata for ", name, ".", call. = FALSE)
    }
  }

  labelled_values <- if (is.null(value_labels)) {
    list()
  } else {
    lapply(seq_along(value_labels), function(i) {
      list(value = unname(value_labels[[i]]), label = names(value_labels)[[i]])
    })
  }

  list(
    name = name,
    variable_label = if (is.null(variable_label)) NULL else as.character(variable_label),
    storage_class = class(x),
    value_labels = labelled_values,
    na_values = if (is.null(missing_values)) list() else as.list(unname(missing_values)),
    na_range = if (is.null(missing_range)) list() else as.list(unname(missing_range))
  )
}

is_source_missing <- function(x) {
  raw <- unclass(x)
  result <- is.na(raw)
  missing_values <- attr(x, "na_values", exact = TRUE)
  missing_range <- attr(x, "na_range", exact = TRUE)
  if (!is.null(missing_values) && length(missing_values)) {
    result <- result | raw %in% missing_values
  }
  if (!is.null(missing_range) && length(missing_range) == 2L) {
    result <- result | (!is.na(raw) & raw >= missing_range[[1]] & raw <= missing_range[[2]])
  }
  result
}

schema <- list(
  source_identity = list(
    round = "ESS11",
    edition = "3.0",
    subset = "cntry == HR",
    input_file = basename(input_path),
    checksum_note = "Record SHA-256 separately beside the reader-owned input."
  ),
  key = c("essround", "cntry", "idno"),
  default_analysis_weight = "anweight",
  variables = lapply(required_variables, function(name) metadata_record(name, selected[[name]]))
)

denominators <- data.frame(
  variable = teaching_variables,
  hr_rows = rep(nrow(selected), length(teaching_variables)),
  valid_responses = vapply(
    teaching_variables,
    function(name) sum(!is_source_missing(selected[[name]])),
    integer(1)
  ),
  stringsAsFactors = FALSE
)

attr(selected, "ess_selection_contract") <- list(
  round = "ESS11",
  edition = "3.0",
  subset = "cntry == HR",
  variables = required_variables,
  default_analysis_weight = "anweight",
  denominator_rule = "analysis-specific official user-missing metadata"
)

rds_path <- file.path(output_path, "ess_r11_hr-reader-owned.rds")
schema_path <- file.path(output_path, "ess_r11_hr-schema.json")
denominator_path <- file.path(output_path, "ess_r11_hr-valid-denominators.csv")

saveRDS(selected, rds_path, version = 3)
jsonlite::write_json(schema, schema_path, auto_unbox = TRUE, pretty = TRUE, null = "null")
utils::write.csv(denominators, denominator_path, row.names = FALSE, fileEncoding = "UTF-8")

message(
  "ESS_PREP_OK rows_hr=", nrow(selected),
  " variables=", length(required_variables),
  " output=", output_path
)
