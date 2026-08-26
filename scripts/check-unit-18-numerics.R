# Independent unit 18 verification ------------------------------------------
#
# This script does not source the chapter, its setup file, the teaching-data
# generator, or the assessment checker. It independently rebuilds the fixed
# capstone survey from its declared algorithm, computes the descriptive and
# regression quantities from matrix operations, reconstructs the ParlaSent
# selection and grouped split from pinned raw files, and checks the promoted
# evidence package.

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Package 'jsonlite' is required for the independent unit 18 check.")
}
if (!requireNamespace("digest", quietly = TRUE)) {
  stop("Package 'digest' is required for the independent unit 18 check.")
}

root <- normalizePath(".", winslash = "/", mustWork = TRUE)
at <- function(...) file.path(root, ...)

expect_equal <- function(actual, expected, tolerance = 0) {
  if (length(actual) != length(expected) ||
      any(is.na(actual) != is.na(expected)) ||
      any(abs(as.numeric(actual) - as.numeric(expected)) > tolerance, na.rm = TRUE)) {
    stop(
      "Numerical mismatch: observed ", paste(actual, collapse = ", "),
      "; expected ", paste(expected, collapse = ", ")
    )
  }
}

expect_identical <- function(actual, expected) {
  if (!identical(actual, expected)) {
    stop(
      "Identity mismatch: observed ", paste(actual, collapse = ", "),
      "; expected ", paste(expected, collapse = ", ")
    )
  }
}

cor_manual <- function(x, y) {
  x_centered <- x - mean(x)
  y_centered <- y - mean(y)
  sum(x_centered * y_centered) /
    sqrt(sum(x_centered^2) * sum(y_centered^2))
}

ols_manual <- function(y, x) {
  xtx_inverse <- solve(crossprod(x))
  beta <- as.vector(xtx_inverse %*% crossprod(x, y))
  fitted <- as.vector(x %*% beta)
  residuals <- y - fitted
  degrees_freedom <- length(y) - ncol(x)
  sigma_squared <- sum(residuals^2) / degrees_freedom
  standard_errors <- sqrt(diag(sigma_squared * xtx_inverse))
  critical <- stats::qt(0.975, degrees_freedom)
  intervals <- cbind(
    lower = beta - critical * standard_errors,
    upper = beta + critical * standard_errors
  )
  list(
    beta = beta,
    intervals = intervals,
    r_squared = 1 - sum(residuals^2) / sum((y - mean(y))^2),
    degrees_freedom = degrees_freedom
  )
}

# Rebuild the declared survey algorithm without sourcing R/podaci-nastavni.R.
set.seed(4001)
group_labels <- c("18 do 24", "25 do 34", "35 do 44", "45 i više")
group_shares <- c(0.30, 0.28, 0.22, 0.20)
age_min <- c(18, 25, 35, 45)
age_max <- c(24, 34, 44, 70)
typical_minutes <- c(75, 48, 28, 14)
minute_spread <- c(0.55, 0.55, 0.60, 0.65)
trust_means <- c(6.4, 5.6, 4.9, 4.3)
n <- 300L
group_counts <- diff(c(0, round(cumsum(group_shares) * n)))
group_index <- rep(seq_along(group_labels), times = group_counts)

age <- floor(stats::runif(
  n,
  min = age_min[group_index],
  max = age_max[group_index] + 1
))
minutes <- pmax(1, round(stats::rlnorm(
  n,
  meanlog = log(typical_minutes[group_index]),
  sdlog = minute_spread[group_index]
)))
trust <- pmin(10, pmax(1, round(stats::rnorm(
  n,
  mean = trust_means[group_index],
  sd = 1.7
))))

simple <- ols_manual(trust, cbind(1, minutes))
adjusted <- ols_manual(trust, cbind(1, minutes, age))

group_summary <- t(vapply(
  seq_along(group_labels),
  function(group) {
    in_group <- group_index == group
    c(
      n = sum(in_group),
      correlation = cor_manual(minutes[in_group], trust[in_group]),
      minutes = mean(minutes[in_group]),
      trust = mean(trust[in_group])
    )
  },
  numeric(4)
))
rownames(group_summary) <- group_labels

survey_values <- c(
  n = n,
  missing = sum(is.na(c(age, minutes, trust))),
  age_mean = mean(age),
  minute_mean = mean(minutes),
  minute_median = median(minutes),
  minute_min = min(minutes),
  minute_max = max(minutes),
  trust_mean = mean(trust),
  trust_sd = stats::sd(trust),
  correlation = cor_manual(minutes, trust),
  simple_slope = simple$beta[[2]],
  adjusted_slope = adjusted$beta[[2]],
  age_slope = adjusted$beta[[3]],
  simple_effect_30 = 30 * simple$beta[[2]],
  simple_lower_30 = 30 * simple$intervals[2, "lower"],
  simple_upper_30 = 30 * simple$intervals[2, "upper"],
  adjusted_effect_30 = 30 * adjusted$beta[[2]],
  adjusted_lower_30 = 30 * adjusted$intervals[2, "lower"],
  adjusted_upper_30 = 30 * adjusted$intervals[2, "upper"],
  simple_r_squared = simple$r_squared,
  adjusted_r_squared = adjusted$r_squared,
  group_correlation_min = min(group_summary[, "correlation"]),
  group_correlation_max = max(group_summary[, "correlation"])
)

task_values <- c(
  minute_difference = group_summary[1, "minutes"] - group_summary[4, "minutes"],
  observed_trust_difference = group_summary[1, "trust"] - group_summary[4, "trust"]
)
task_values <- c(
  task_values,
  simple_model_attributed_difference = simple$beta[[2]] * task_values[["minute_difference"]]
)

expect_equal(
  survey_values,
  c(
    n = 300,
    missing = 0,
    age_mean = 34.516666666666667,
    minute_mean = 50.063333333333333,
    minute_median = 39,
    minute_min = 3,
    minute_max = 248,
    trust_mean = 5.446666666666666,
    trust_sd = 1.786372294756555,
    correlation = 0.1798494626817405,
    simple_slope = 0.008204853313673210,
    adjusted_slope = -0.0002774402232627593,
    age_slope = -0.04437094375860995,
    simple_effect_30 = 0.2461455994101963,
    simple_lower_30 = 0.09266609735471668,
    simple_upper_30 = 0.3996251014656760,
    adjusted_effect_30 = -0.008323206697882779,
    adjusted_lower_30 = -0.1863548331880542,
    adjusted_upper_30 = 0.1697084197922886,
    simple_r_squared = 0.03234582922691076,
    adjusted_r_squared = 0.1082928038751434,
    group_correlation_min = -0.2072868866927125,
    group_correlation_max = 0.1480402766234398
  ),
  1e-12
)
expect_equal(
  as.numeric(group_summary),
  c(
    90, 84, 66, 60,
    -0.1011000566463691, -0.2072868866927125,
    -0.05143805799285237, 0.1480402766234398,
    81.54444444444445, 54.36904761904762,
    32.40909090909091, 16.23333333333333,
    6.377777777777778, 5.559523809523809,
    4.893939393939394, 4.5
  ),
  1e-12
)
expect_equal(
  task_values,
  c(
    minute_difference = 65.31111111111112,
    observed_trust_difference = 1.877777777777778,
    simple_model_attributed_difference = 0.5358680864196793
  ),
  1e-12
)

# Reconstruct the empirical evidence package from its pinned raw inputs.
read_jsonl <- function(path) {
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  jsonlite::fromJSON(
    paste0("[", paste(lines, collapse = ","), "]"),
    simplifyDataFrame = TRUE
  )
}

train_raw <- read_jsonl(at("data", "_kandidat", "p3-text", "ParlaSent_BCS.jsonl"))
test_raw <- read_jsonl(at("data", "_kandidat", "p3-text", "ParlaSent_BCS_test.jsonl"))
train_hr <- train_raw[train_raw$country == "HR", , drop = FALSE]
test_hr <- test_raw[test_raw$country == "HR", , drop = FALSE]
overlap_documents <- intersect(
  unique(as.character(train_hr$document_id)),
  unique(as.character(test_hr$document_id))
)
retained_train <- train_hr[
  !as.character(train_hr$document_id) %in% overlap_documents,
  ,
  drop = FALSE
]
removed_rows <- nrow(train_hr) - nrow(retained_train)

split_salt <- "statistika-p3-text-parlasent-only-v1"
threshold_hex <- "3333333333333400"
document_hash <- vapply(
  as.character(retained_train$document_id),
  function(document_id) digest::digest(
    paste0(split_salt, "|", document_id),
    algo = "sha256",
    serialize = FALSE
  ),
  character(1)
)
derived_train_split <- ifelse(
  substr(document_hash, 1, 16) < threshold_hex,
  "provjera",
  "ucenje"
)
raw_split_counts <- c(
  ucenje = sum(derived_train_split == "ucenje"),
  provjera = sum(derived_train_split == "provjera"),
  ispitivanje = nrow(test_hr)
)

promoted_path <- at("data", "parlament_oznake.csv")
promoted <- read.csv(
  promoted_path,
  check.names = FALSE,
  stringsAsFactors = FALSE,
  fileEncoding = "UTF-8"
)
split_levels <- c("ucenje", "provjera", "ispitivanje")
label_levels <- c("Negative", "Neutral", "Positive")
path_levels <- c("dva_kodera_i_uskladjenje", "jedan_uvjezbani_koder")

evidence_values <- c(
  raw_train_hr = nrow(train_hr),
  raw_test_hr = nrow(test_hr),
  overlapping_documents = length(overlap_documents),
  removed_training_rows = removed_rows,
  retained_training_rows = nrow(retained_train),
  promoted_rows = nrow(promoted),
  promoted_documents = length(unique(promoted$source_document_id)),
  training_rows = sum(promoted$derived_split == "ucenje"),
  validation_rows = sum(promoted$derived_split == "provjera"),
  test_rows = sum(promoted$derived_split == "ispitivanje"),
  negative = sum(promoted$recorded_label == "Negative"),
  neutral = sum(promoted$recorded_label == "Neutral"),
  positive = sum(promoted$recorded_label == "Positive"),
  two_coders = sum(promoted$label_path == path_levels[[1]]),
  one_coder = sum(promoted$label_path == path_levels[[2]]),
  two_coders_negative = sum(
    promoted$label_path == path_levels[[1]] & promoted$recorded_label == "Negative"
  ),
  one_coder_negative = sum(
    promoted$label_path == path_levels[[2]] & promoted$recorded_label == "Negative"
  )
)
evidence_values <- c(
  evidence_values,
  two_coders_negative_share =
    evidence_values[["two_coders_negative"]] / evidence_values[["two_coders"]],
  one_coder_negative_share =
    evidence_values[["one_coder_negative"]] / evidence_values[["one_coder"]]
)

expect_identical(raw_split_counts, c(ucenje = 1090L, provjera = 272L, ispitivanje = 1336L))
expect_identical(
  digest::digest(file = promoted_path, algo = "sha256"),
  "0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef"
)
expect_equal(
  evidence_values[c(
    "raw_train_hr", "raw_test_hr", "overlapping_documents",
    "removed_training_rows", "retained_training_rows", "promoted_rows",
    "promoted_documents", "training_rows", "validation_rows", "test_rows",
    "negative", "neutral", "positive", "two_coders", "one_coder",
    "two_coders_negative", "one_coder_negative"
  )],
  c(1387, 1336, 20, 25, 1362, 2698, 2499, 1090, 272, 1336,
    1212, 979, 507, 1362, 1336, 652, 560)
)
expect_equal(
  evidence_values[c("two_coders_negative_share", "one_coder_negative_share")],
  c(652 / 1362, 560 / 1336),
  1e-15
)

cat("UNIT_18_NUMERICS_OK\n")
cat(
  sprintf(
    paste0(
      "survey=%d/%d age=%.12f minutes=%.12f/%.12f/%d/%d ",
      "trust=%.12f/%.12f correlations=%.12f/%.12f/%.12f ",
      "models=%.12f/%.12f/%.12f adjusted30=%.12f/%.12f/%.12f ",
      "simple30=%.12f/%.12f/%.12f r2=%.12f/%.12f\n"
    ),
    survey_values[["n"]], survey_values[["missing"]], survey_values[["age_mean"]],
    survey_values[["minute_mean"]], survey_values[["minute_median"]],
    survey_values[["minute_min"]], survey_values[["minute_max"]],
    survey_values[["trust_mean"]], survey_values[["trust_sd"]],
    survey_values[["correlation"]], survey_values[["group_correlation_min"]],
    survey_values[["group_correlation_max"]], survey_values[["simple_slope"]],
    survey_values[["adjusted_slope"]], survey_values[["age_slope"]],
    survey_values[["adjusted_effect_30"]], survey_values[["adjusted_lower_30"]],
    survey_values[["adjusted_upper_30"]], survey_values[["simple_effect_30"]],
    survey_values[["simple_lower_30"]], survey_values[["simple_upper_30"]],
    survey_values[["simple_r_squared"]], survey_values[["adjusted_r_squared"]]
  )
)
cat(
  sprintf(
    paste0(
      "groups=%d/%d/%d/%d task=%.12f/%.12f/%.12f ",
      "evidence=%d/%d removed=%d/%d promoted=%d/%d ",
      "splits=%d/%d/%d labels=%d/%d/%d paths=%d/%d shares=%.12f/%.12f\n"
    ),
    group_summary[1, "n"], group_summary[2, "n"],
    group_summary[3, "n"], group_summary[4, "n"],
    task_values[["minute_difference"]],
    task_values[["observed_trust_difference"]],
    task_values[["simple_model_attributed_difference"]],
    evidence_values[["raw_train_hr"]], evidence_values[["raw_test_hr"]],
    evidence_values[["overlapping_documents"]], evidence_values[["removed_training_rows"]],
    evidence_values[["promoted_rows"]], evidence_values[["promoted_documents"]],
    evidence_values[["training_rows"]], evidence_values[["validation_rows"]],
    evidence_values[["test_rows"]], evidence_values[["negative"]],
    evidence_values[["neutral"]], evidence_values[["positive"]],
    evidence_values[["two_coders"]], evidence_values[["one_coder"]],
    evidence_values[["two_coders_negative_share"]],
    evidence_values[["one_coder_negative_share"]]
  )
)
