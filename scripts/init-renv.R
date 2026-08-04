# init-renv.R ---------------------------------------------------------------
# Deterministic R dependency entry point for the book.
#
# Public restoration is intentionally routed through
# `python scripts/restore-dependencies.py`, which restores both this R lock and
# the pinned browser toolchain.  This file also keeps the direct R dependency
# set used when an authorised dependency update deliberately rewrites the
# lockfile:
#
#   python bookwright_plugin/bookwright/scripts/run_rscript.py \
#     scripts/init-renv.R --snapshot
# ---------------------------------------------------------------------------

direct_packages <- c(
  "renv",
  "ggplot2", "dplyr", "tidyr", "tibble",
  "yaml", "jsonlite", "stringr", "stringi", "forcats",
  "knitr", "rmarkdown", "downlit", "xml2",
  "svglite", "showtext", "sysfonts", "digest", "rsvg"
)

args <- commandArgs(trailingOnly = TRUE)
mode <- if (length(args)) args[[1]] else "--restore"
if (!mode %in% c("--restore", "--snapshot")) {
  stop("Usage: init-renv.R [--restore|--snapshot]")
}

root <- normalizePath(".", winslash = "/", mustWork = TRUE)
lockfile <- file.path(root, "renv.lock")

if (identical(mode, "--snapshot")) {
  if (!requireNamespace("renv", quietly = TRUE)) {
    stop("The maintainer snapshot mode requires renv to be installed explicitly.")
  }
  renv::init(bare = TRUE, restart = FALSE)
  # The appendix shows tidyverse as a student convenience in eval:false
  # examples; the release build deliberately locks its executed component
  # packages instead of the unused meta-package.
  renv::settings$ignored.packages("tidyverse")
  renv::install(direct_packages)
  renv::snapshot(packages = direct_packages, prompt = FALSE)
  message("renv.lock refreshed from the declared direct package set.")
  quit(save = "no", status = 0L)
}

if (!file.exists(lockfile)) {
  stop("Missing renv.lock; restoration has no unlocked fallback.")
}
if (!requireNamespace("renv", quietly = TRUE)) {
  stop("renv bootstrap failed; renv/activate.R must restore the locked renv version.")
}

locked <- renv::lockfile_read(lockfile)
locked_r <- locked$R$Version
running_r <- paste(R.version$major, R.version$minor, sep = ".")
if (!identical(running_r, locked_r)) {
  stop(
    "R version mismatch: renv.lock requires ", locked_r,
    ", but the running interpreter is ", running_r, "."
  )
}

missing_records <- direct_packages[
  !vapply(direct_packages, function(package) {
    !is.null(locked$Packages[[package]]$Version)
  }, logical(1))
]
if (length(missing_records)) {
  stop("renv.lock omits direct packages: ", paste(missing_records, collapse = ", "))
}

renv::restore(lockfile = lockfile, prompt = FALSE)

detected <- renv::dependencies(root, progress = FALSE, errors = "fatal")
detected_packages <- sort(unique(detected$Package))
installed <- utils::installed.packages()
base_or_recommended <- rownames(installed)[!is.na(installed[, "Priority"])]
unlocked_dependencies <- setdiff(
  detected_packages,
  c(names(locked$Packages), base_or_recommended, "tidyverse")
)
if (length(unlocked_dependencies)) {
  stop(
    "Source dependencies are absent from renv.lock: ",
    paste(unlocked_dependencies, collapse = ", ")
  )
}

wrong_versions <- direct_packages[
  !vapply(direct_packages, function(package) {
    actual <- utils::packageDescription(package, fields = "Version")
    expected <- locked$Packages[[package]]$Version
    identical(actual, expected)
  }, logical(1))
]
if (length(wrong_versions)) {
  stop(
    "Restored R library does not match renv.lock for: ",
    paste(wrong_versions, collapse = ", ")
  )
}

message(
  "R_RESTORE_OK version=", locked_r,
  " direct_packages=", length(direct_packages),
  " detected_packages=", length(detected_packages)
)
