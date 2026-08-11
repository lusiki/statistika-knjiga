#!/usr/bin/env Rscript
# Build the bounded DigiKat extracts from the author's local project checkout.
#
# DigiKat (Prikaz i analiza katolicke tematike u digitalnom medijskom prostoru,
# HKS, PI Luka Sikic) tracks fourteen aggregate tables under
# `data/processed/*.rds` and declares them in its own DATA_AVAILABILITY.md as CC
# BY 4.0, aggregate, no PII, redistributable. Three files are the source of
# record here. The
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


potpune_godine <- function(checkout) {
  d <- ucitaj(checkout, "platform_monthly")
  d$godina <- as.integer(format(d$month, "%Y"))
  d$mjesec_redni <- as.integer(format(d$month, "%m"))
  mjeseci <- split(d$mjesec_redni, d$godina)
  as.integer(names(mjeseci)[vapply(mjeseci, function(x) {
    identical(sort(unique(x)), 1:12)
  }, logical(1))])
}


oznaka_loma_godisnje <- function(godina) {
  ifelse(
    godina <= 2022L, "prije_promjene_obuhvata",
    ifelse(
      godina == 2023L, "tiktok_od_2023-07",
      ifelse(
        godina == 2024L,
        "nepotpuno_lom_2024-06_instagram_od_2024-07",
        "nakon_loma_2024-06"
      )
    )
  )
}


oznaka_loma_mjesecno <- function(mjesec) {
  x <- format(mjesec, "%Y-%m")
  ifelse(
    x < "2023-07", "prije_promjene_obuhvata",
    ifelse(
      x < "2024-06", "tiktok_od_2023-07",
      ifelse(
        x == "2024-06", "lom_2024-06",
        "nakon_loma_2024-06_instagram_od_2024-07"
      )
    )
  )
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
    godina_potpuna = ifelse(d$year %in% potpune_godine(checkout), "da", "ne"),
    lom_metode = oznaka_loma_godisnje(d$year),
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
    lom_metode = oznaka_loma_mjesecno(d$month),
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


verify_contract <- function(built) {
  annual <- built[["data/digikat-platforme-godisnje.csv"]]
  monthly <- built[["data/digikat-platforme-mjesecno.csv"]]
  sources <- built[["data/digikat-izvori.csv"]]

  # D-1: a complete year has all twelve observed calendar months. This makes
  # 2024 explicitly incomplete: February-May are absent and January is only a
  # partial 1,911-post month. 2026 remains a labelled six-month year.
  full_by_year <- tapply(annual$godina_potpuna, annual$godina,
                         function(x) identical(unique(x), "da"))
  expected_full <- c("2021", "2022", "2023", "2025")
  if (!identical(names(full_by_year)[full_by_year], expected_full)) {
    stop("godina_potpuna does not identify exactly 2021, 2022, 2023 and 2025.",
         call. = FALSE)
  }
  months_2024 <- sort(unique(monthly$mjesec[monthly$godina == "2024"]))
  expected_2024 <- c("2024-01", sprintf("2024-%02d", 6:12))
  if (!identical(months_2024, expected_2024)) {
    stop("The recorded 2024 gap is not exactly February-May.", call. = FALSE)
  }
  jan_2024 <- sum(as.numeric(monthly$objave[monthly$mjesec == "2024-01"]))
  if (!identical(jan_2024, 1911)) {
    stop("The partial January 2024 total is no longer 1911.", call. = FALSE)
  }

  # D-2 and the denominator part of the non-official-source reconciliation.
  annual$objave_num <- as.numeric(annual$objave)
  annual$denominator_num <- as.numeric(annual$objave_godina_ukupno)
  denominator_ok <- vapply(split(annual, annual$godina), function(d) {
    length(unique(d$denominator_num)) == 1L &&
      sum(d$objave_num) == unique(d$denominator_num)
  }, logical(1))
  if (length(denominator_ok) != 6L || !all(denominator_ok)) {
    stop("The annual denominator identity fails for at least one year.",
         call. = FALSE)
  }

  monthly$objave_num <- as.numeric(monthly$objave)
  monthly_sum <- aggregate(objave_num ~ godina + platforma, monthly, sum)
  names(monthly_sum)[3] <- "mjesecno"
  compared <- merge(
    annual[, c("godina", "platforma", "objave_num")], monthly_sum,
    by = c("godina", "platforma"), all.x = TRUE
  )
  compared$mjesecno[is.na(compared$mjesecno)] <- 0
  compared$razlika <- compared$mjesecno - compared$objave_num
  different <- compared[compared$razlika != 0, ]
  largest_positive <- compared[which.max(compared$razlika), ]
  largest_negative <- compared[which.min(compared$razlika), ]
  if (nrow(different) != 17L || sum(compared$razlika) != 0 ||
      sum(compared$objave_num) != 710307 || sum(compared$mjesecno) != 710307 ||
      largest_positive$razlika != 446 || largest_positive$godina != "2022" ||
      largest_positive$platforma != "web" ||
      largest_negative$razlika != -389 || largest_negative$godina != "2024" ||
      largest_negative$platforma != "web") {
    stop("The annual/monthly divergence no longer matches its recorded exact contract.",
         call. = FALSE)
  }

  # D-3: both files carry a method-break flag. The flag records TikTok's entry,
  # the June 2024 break and Instagram's subsequent entry; a chapter may not
  # compare across its values as though collection were uniform.
  if (!identical(annual$lom_metode,
                 oznaka_loma_godisnje(as.integer(annual$godina)))) {
    stop("The annual method-break flag is inconsistent.", call. = FALSE)
  }
  if (!identical(monthly$lom_metode,
                 oznaka_loma_mjesecno(as.Date(paste0(monthly$mjesec, "-01"))))) {
    stop("The monthly method-break flag is inconsistent.", call. = FALSE)
  }

  source_posts <- sum(as.numeric(sources$objave))
  if (nrow(sources) != 3604L || source_posts != 551712) {
    stop("The named-source denominator is no longer 3604 sources / 551712 posts.",
         call. = FALSE)
  }

  cat(paste0(
    "DIGIKAT_RECONCILIATION_OK years=6 denominator_tolerance=0 ",
    "divergent_cells=17 direction=monthly_minus_annual max=446@2022:web ",
    "min=-389@2024:web net=0 corpus_posts=710307 ",
    "named_sources=3604 named_source_posts=551712 share_pct=77.67\n"
  ))
}


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
  built <- lapply(EXTRACTS, function(builder) builder(checkout))
  verify_contract(built)
  for (relative in names(EXTRACTS)) {
    payload <- serialise(built[[relative]])
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
