#!/usr/bin/env Rscript
# Build the bounded DigiKat extracts from the author's local project checkout.
#
# DigiKat (Prikaz i analiza katolicke tematike u digitalnom medijskom prostoru,
# HKS, PI Luka Sikic) tracks ten aggregate tables under `data/processed/*.rds`
# and declares them in its own DATA_AVAILABILITY.md as CC BY 4.0, aggregate, no
# PII, redistributable. Those ten files are the source of record here. The
# roughly 710.000-row master corpus is NOT read, is not redistributable, and
# stays `external-only` in the catalogue under `determ_korpus`.
#
# This script never touches the network.
#
# Run:
#   Rscript scripts/build-digikat-extracts.R --checkout <path>
#   Rscript scripts/build-digikat-extracts.R --checkout <path> --write
#
# Without --write every extract is rebuilt in memory and compared byte for byte
# with the file on disk, so a drifted extract is caught rather than silently
# overwritten.
#
# Five shape rules, the same ones the DZS and CroAIcon extracts obey:
#
#   1. UTF-8 without BOM, LF line endings, comma as the field separator.
#   2. No value contains a comma, a quote or a line break.
#   3. Source labels are copied VERBATIM. The upstream platform codes (web,
#      youtube, facebook, ...) survive next to the Croatian column names.
#   4. A missing value carries a code and never an empty cell.
#   5. Full numeric precision is preserved. Rounding exists only in display.
#
# THE ONE SUBSTANTIVE DECISION IN THIS SCRIPT
#
# DigiKat's upstream aggregates store 0 for interactions and 0 for reach on
# reddit, forum and comment, in every one of the six years. That is not a
# measured zero: the media-monitoring provider does not supply engagement
# metrics for those source types at all. The book's storage convention requires
# zero and missing to stay distinct, and re-coding someone else's number is not
# this script's business, so the extract does BOTH: it copies the upstream value
# verbatim AND carries an explicit `metrika_dostupna` flag. A reader who
# averages across platforms without reading the flag gets the wrong answer, and
# that is exactly the mistake the chapter is meant to teach.

suppressPackageStartupMessages({
  library(dplyr)
})

ROOT <- normalizePath(file.path(dirname(sub("^--file=", "", grep("^--file=",
  commandArgs(FALSE), value = TRUE)[1])), ".."), mustWork = TRUE)

# Platforms for which the provider supplies interaction and reach metrics.
MJERENE_PLATFORME <- c("web", "youtube", "facebook", "twitter", "instagram", "tiktok")

# The corpus runs 2021-01 to 2026-06. 2026 is the only incomplete year and is
# kept, flagged, rather than dropped: an incomplete last year that is labelled
# is a better teaching object than a silent truncation.
ZADNJA_POTPUNA_GODINA <- 2025L

# An outlet name counts as an organisation, and so may be named, when it is a
# bare domain: no whitespace and an alphabetic top-level domain. Everything else
# in the upstream `FROM` column - Facebook pages, YouTube channels, personal
# accounts - is dropped. The book does not publish a named-individual table.
DOMENA <- "^[A-Za-z0-9][A-Za-z0-9.-]*\\.[A-Za-z]{2,}$"


ucitaj <- function(checkout, ime) {
  path <- file.path(checkout, "data", "processed", paste0(ime, ".rds"))
  if (!file.exists(path)) stop("Checkout aggregate is missing: ", path, call. = FALSE)
  as.data.frame(readRDS(path), stringsAsFactors = FALSE)
}


broj <- function(x) {
  # Full precision, no scientific notation, no invented format.
  ifelse(is.na(x), "..", format(x, scientific = FALSE, trim = TRUE, digits = 15))
}


# --- extract 1: platform by year --------------------------------------------

build_platforme_godisnje <- function(checkout) {
  d <- ucitaj(checkout, "platform_summary")
  d$SOURCE_TYPE <- as.character(d$SOURCE_TYPE)
  d <- d[order(d$year, -d$total_posts), ]
  # The upstream `proportions_summary` carries the three shares as doubles. They
  # are not copied. The convention is that a percentage keeps its numerator and
  # its denominator, and a share printed to more digits than a double holds is a
  # claim about precision that is not true. `objave_godina_ukupno` is the
  # denominator; the reader divides.
  godisnji_zbroj <- stats::ave(d$total_posts, d$year, FUN = sum)
  data.frame(
    godina = as.character(d$year),
    platforma = d$SOURCE_TYPE,
    objave = broj(d$total_posts),
    objave_godina_ukupno = broj(godisnji_zbroj),
    interakcije = broj(d$total_interactions),
    doseg = broj(d$total_reach),
    metrika_dostupna = ifelse(d$SOURCE_TYPE %in% MJERENE_PLATFORME, "da", "ne"),
    godina_potpuna = ifelse(d$year <= ZADNJA_POTPUNA_GODINA, "da", "ne"),
    stringsAsFactors = FALSE
  )
}


# --- extract 2: platform by month -------------------------------------------

build_platforme_mjesecno <- function(checkout) {
  d <- ucitaj(checkout, "platform_monthly")
  d$SOURCE_TYPE <- as.character(d$SOURCE_TYPE)
  d <- d[order(d$month, -d$total_posts), ]
  out <- data.frame(
    mjesec = format(d$month, "%Y-%m"),
    godina = format(d$month, "%Y"),
    mjesec_redni = as.character(as.integer(format(d$month, "%m"))),
    platforma = d$SOURCE_TYPE,
    objave = broj(d$total_posts),
    interakcije = broj(d$total_interactions),
    doseg = broj(d$total_reach),
    metrika_dostupna = ifelse(d$SOURCE_TYPE %in% MJERENE_PLATFORME, "da", "ne"),
    stringsAsFactors = FALSE
  )
  out
}


# --- extract 3: outlet totals over the whole span ---------------------------

build_izvori <- function(checkout) {
  d <- ucitaj(checkout, "source_summary")
  d <- d[!is.na(d$FROM) & grepl(DOMENA, d$FROM), ]
  # `avg_engagement_rate` is a mean of per-post ratios and cannot be summed
  # across years, so it is not carried. A reader who wants a rate builds it from
  # the two totals, which is the ratio of sums and the correct quantity.
  agg <- d %>%
    group_by(izvor = tolower(FROM)) %>%
    summarise(
      objave = sum(productivity),
      interakcije = sum(total_interactions),
      doseg = sum(total_reach),
      godine_prisutnosti = n_distinct(year),
      .groups = "drop"
    ) %>%
    arrange(desc(objave), izvor)
  data.frame(
    izvor = agg$izvor,
    objave = broj(agg$objave),
    interakcije = broj(agg$interakcije),
    doseg = broj(agg$doseg),
    godine_prisutnosti = broj(agg$godine_prisutnosti),
    stringsAsFactors = FALSE
  )
}


EXTRACTS <- list(
  "data/digikat-platforme-godisnje.csv" = build_platforme_godisnje,
  "data/digikat-platforme-mjesecno.csv" = build_platforme_mjesecno,
  "data/digikat-izvori.csv" = build_izvori
)


serialise <- function(df) {
  for (nm in names(df)) {
    v <- df[[nm]]
    if (any(is.na(v)) || any(v == "")) {
      stop("Empty cell in column ", nm, ": a missing value carries its own code.",
           call. = FALSE)
    }
    if (any(grepl('[,"\r\n]', v))) {
      stop("Value in column ", nm, " contains a separator, quote or break.",
           call. = FALSE)
    }
  }
  linije <- c(paste(names(df), collapse = ","),
              do.call(paste, c(unname(as.list(df)), sep = ",")))
  charToRaw(paste0(paste(linije, collapse = "\n"), "\n"))
}


main <- function() {
  args <- commandArgs(TRUE)
  if (!("--checkout" %in% args)) {
    stop("Usage: build-digikat-extracts.R --checkout <path> [--write]", call. = FALSE)
  }
  checkout <- args[which(args == "--checkout") + 1L]
  write <- "--write" %in% args
  if (!dir.exists(checkout)) {
    stop("Checkout directory does not exist: ", checkout, call. = FALSE)
  }

  drift <- character(0)
  for (relative in names(EXTRACTS)) {
    payload <- serialise(EXTRACTS[[relative]](checkout))
    target <- file.path(ROOT, relative)
    if (write) {
      dir.create(dirname(target), showWarnings = FALSE, recursive = TRUE)
      writeBin(payload, target)
    } else if (!file.exists(target)) {
      drift <- c(drift, paste0(relative, ": extract does not exist"))
    } else if (!identical(readBin(target, "raw", file.size(target)), payload)) {
      drift <- c(drift, paste0(relative, ": extract no longer reproduces from the checkout"))
    }
  }

  if (length(drift)) {
    cat("DIGIKAT_EXTRACTS_FAILED\n")
    for (m in drift) cat("- ", m, "\n", sep = "")
    quit(status = 1L)
  }

  cat(sprintf("DIGIKAT_EXTRACTS_OK extracts=%d mode=%s\n",
              length(EXTRACTS), if (write) "write" else "verify"))
  invisible(NULL)
}

main()
