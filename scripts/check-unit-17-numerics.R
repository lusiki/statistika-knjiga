# Independent unit 17 verification ------------------------------------------
#
# This script does not source the chapter, its setup file, or the assessment
# checker. It reconstructs the ParlaSent selection and grouped split from the
# pinned raw JSONL files, recomputes every confusion-table and exercise value,
# and implements both default widget generators independently.

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Package 'jsonlite' is required for the independent unit 17 check.")
}
if (!requireNamespace("digest", quietly = TRUE)) {
  stop("Package 'digest' is required for the independent unit 17 check.")
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

read_jsonl <- function(path) {
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  jsonlite::fromJSON(paste0("[", paste(lines, collapse = ","), "]"),
                     simplifyDataFrame = TRUE)
}

train_raw <- read_jsonl(at("data", "_kandidat", "p3-text", "ParlaSent_BCS.jsonl"))
test_raw <- read_jsonl(at("data", "_kandidat", "p3-text", "ParlaSent_BCS_test.jsonl"))
train_hr <- train_raw[train_raw$country == "HR", , drop = FALSE]
test_hr <- test_raw[test_raw$country == "HR", , drop = FALSE]

expect_identical(nrow(train_hr), 1387L)
expect_identical(nrow(test_hr), 1336L)

train_documents <- unique(as.character(train_hr$document_id))
test_documents <- unique(as.character(test_hr$document_id))
overlap_documents <- intersect(train_documents, test_documents)
retained_train <- train_hr[
  !as.character(train_hr$document_id) %in% overlap_documents,
  ,
  drop = FALSE
]
removed_rows <- nrow(train_hr) - nrow(retained_train)
expect_identical(length(overlap_documents), 20L)
expect_identical(removed_rows, 25L)
expect_identical(nrow(retained_train), 1362L)

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
raw_split_documents <- c(
  ucenje = length(unique(as.character(retained_train$document_id[derived_train_split == "ucenje"]))),
  provjera = length(unique(as.character(retained_train$document_id[derived_train_split == "provjera"]))),
  ispitivanje = length(unique(as.character(test_hr$document_id)))
)
expect_equal(raw_split_counts, c(1090, 272, 1336))
expect_equal(raw_split_documents, c(944, 234, 1321))

promoted_path <- at("data", "parlament_oznake.csv")
promoted <- read.csv(
  promoted_path,
  check.names = FALSE,
  stringsAsFactors = FALSE,
  fileEncoding = "UTF-8"
)
expect_identical(nrow(promoted), 2698L)
expect_identical(
  digest::digest(file = promoted_path, algo = "sha256"),
  "0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef"
)

split_levels <- c("ucenje", "provjera", "ispitivanje")
observed_split_counts <- table(factor(promoted$derived_split, levels = split_levels))
observed_split_documents <- vapply(
  split_levels,
  function(split) length(unique(promoted$source_document_id[promoted$derived_split == split])),
  integer(1)
)
expect_equal(observed_split_counts, raw_split_counts)
expect_equal(observed_split_documents, raw_split_documents)

label_levels <- c("Negative", "Neutral", "Positive")
expected_labels <- rbind(
  ucenje = c(530, 343, 217),
  provjera = c(122, 90, 60),
  ispitivanje = c(560, 546, 230)
)
observed_labels <- t(vapply(
  split_levels,
  function(split) as.numeric(table(factor(
    promoted$recorded_label[promoted$derived_split == split],
    levels = label_levels
  ))),
  numeric(3)
))
expect_equal(observed_labels, expected_labels)

expect_identical(promoted$record_id[[1]], "train-0001")
expect_identical(promoted$annotator1_raw[[1]], "N_Neutral")
expect_identical(promoted$annotator2_raw[[1]], "Negative")
expect_identical(promoted$reconciliation_raw[[1]], "M_Negative")
expect_identical(promoted$recorded_label[[1]], "Negative")

validation <- promoted[promoted$derived_split == "provjera", , drop = FALSE]
negative_vote <- function(value) endsWith(value, "Negative")
validation$negative_votes <- (
  as.integer(negative_vote(validation$annotator1_raw)) +
  as.integer(negative_vote(validation$annotator2_raw))
) / 2
validation$reference_negative <- validation$recorded_label == "Negative"

confusion <- function(threshold) {
  decision <- validation$negative_votes >= threshold
  reference <- validation$reference_negative
  tp <- sum(decision & reference)
  fp <- sum(decision & !reference)
  fn <- sum(!decision & reference)
  tn <- sum(!decision & !reference)
  c(
    TP = tp,
    FP = fp,
    FN = fn,
    TN = tn,
    FPR = fp / (fp + tn),
    FNR = fn / (fn + tp),
    PPV = tp / (tp + fp),
    accuracy = (tp + tn) / (tp + fp + fn + tn)
  )
}

at_least_one <- confusion(0.5)
both_votes <- confusion(1)
expect_equal(
  at_least_one,
  c(122, 16, 0, 134, 16 / 150, 0 / 122, 122 / 138, 256 / 272),
  1e-15
)
expect_equal(
  both_votes,
  c(100, 1, 22, 149, 1 / 150, 22 / 122, 100 / 101, 249 / 272),
  1e-15
)

task <- c(TP = 90, FP = 30, FN = 10, TN = 170)
task_metrics <- c(
  FPR = task[["FP"]] / (task[["FP"]] + task[["TN"]]),
  FNR = task[["FN"]] / (task[["FN"]] + task[["TP"]]),
  PPV = task[["TP"]] / (task[["TP"]] + task[["FP"]]),
  accuracy = (task[["TP"]] + task[["TN"]]) / sum(task)
)
expect_equal(task_metrics, c(0.15, 0.10, 0.75, 260 / 300), 1e-15)

metric_values <- function(fpr, fnr, base_rate) {
  tpr <- 1 - fnr
  tnr <- 1 - fpr
  c(
    ppv = base_rate * tpr /
      (base_rate * tpr + (1 - base_rate) * fpr),
    accuracy = base_rate * tpr + (1 - base_rate) * tnr
  )
}

# Reimplement d3.randomLcg(1717) and the uncached Marsaglia-polar generator
# from the live OJS block. The modular arithmetic remains exact below 2^53.
make_lcg <- function(seed) {
  state <- as.numeric(abs(seed)) %% 2^32
  function() {
    state <<- (1664525 * state + 1013904223) %% 2^32
    state / 2^32
  }
}
make_polar <- function(rng) {
  function() {
    repeat {
      x <- 2 * rng() - 1
      y <- 2 * rng() - 1
      radius <- x * x + y * y
      if (radius > 0 && radius <= 1) {
        return(x * sqrt(-2 * log(radius) / radius))
      }
    }
  }
}
clamp01 <- function(value) pmax(0, pmin(1, value))

ojs_rng <- make_lcg(1717)
ojs_normal <- make_polar(ojs_rng)
ojs_nonnegative <- clamp01(vapply(seq_len(6000), function(index) 0.30 + 0.18 * ojs_normal(), numeric(1)))
ojs_negative <- clamp01(vapply(seq_len(6000), function(index) 0.70 + 0.18 * ojs_normal(), numeric(1)))
ojs_fpr <- mean(ojs_nonnegative >= 0.60)
ojs_fnr <- mean(ojs_negative < 0.60)
ojs_a <- metric_values(ojs_fpr, ojs_fnr, 0.20)
ojs_b <- metric_values(ojs_fpr, ojs_fnr, 0.45)
expect_equal(
  c(ojs_fpr, ojs_fnr, ojs_a, ojs_b),
  c(
    0.051333333333333335,
    0.2966666666666667,
    0.7740278796771827,
    0.8996000000000001,
    0.918100947592342,
    0.8382666666666667
  ),
  1e-15
)

set.seed(1717)
r_nonnegative <- clamp01(rnorm(6000, 0.30, 0.18))
r_negative <- clamp01(rnorm(6000, 0.70, 0.18))
r_fpr <- mean(r_nonnegative >= 0.60)
r_fnr <- mean(r_negative < 0.60)
r_a <- metric_values(r_fpr, r_fnr, 0.20)
r_b <- metric_values(r_fpr, r_fnr, 0.45)
expect_equal(
  c(r_fpr, r_fnr, r_a, r_b),
  c(
    0.0495,
    0.28883333333333333,
    0.782218148487626,
    0.9026333333333334,
    0.921598272138229,
    0.8428000000000002
  ),
  1e-15
)

if (!(ojs_a[["ppv"]] < ojs_b[["ppv"]] && r_a[["ppv"]] < r_b[["ppv"]])) {
  stop("Widget base-rate PPV ordering no longer holds.")
}
if (!(abs(ojs_fpr - r_fpr) <= 0.03 && abs(ojs_fnr - r_fnr) <= 0.03)) {
  stop("OJS/R distributional parity exceeded the ratified tolerance.")
}

cat("UNIT_17_NUMERICS_OK\n")
cat(
  sprintf(
    paste0(
      "package=%d/%d/%d removed=%d/%d ",
      "validation-low=%d/%d/%d/%d-%.12f/%.12f/%.12f/%.12f ",
      "validation-high=%d/%d/%d/%d-%.12f/%.12f/%.12f/%.12f\n"
    ),
    raw_split_counts[["ucenje"]], raw_split_counts[["provjera"]],
    raw_split_counts[["ispitivanje"]], length(overlap_documents), removed_rows,
    at_least_one[["TP"]], at_least_one[["FP"]], at_least_one[["FN"]], at_least_one[["TN"]],
    at_least_one[["FPR"]], at_least_one[["FNR"]], at_least_one[["PPV"]], at_least_one[["accuracy"]],
    both_votes[["TP"]], both_votes[["FP"]], both_votes[["FN"]], both_votes[["TN"]],
    both_votes[["FPR"]], both_votes[["FNR"]], both_votes[["PPV"]], both_votes[["accuracy"]]
  )
)
cat(
  sprintf(
    "task=%.12f/%.12f/%.12f/%.12f widget-ojs=%.12f/%.12f/%.12f/%.12f/%.12f/%.12f widget-r=%.12f/%.12f/%.12f/%.12f/%.12f/%.12f\n",
    task_metrics[["FPR"]], task_metrics[["FNR"]], task_metrics[["PPV"]], task_metrics[["accuracy"]],
    ojs_fpr, ojs_fnr, ojs_a[["ppv"]], ojs_a[["accuracy"]], ojs_b[["ppv"]], ojs_b[["accuracy"]],
    r_fpr, r_fnr, r_a[["ppv"]], r_a[["accuracy"]], r_b[["ppv"]], r_b[["accuracy"]]
  )
)
