#!/usr/bin/env Rscript

# Independent numerical verifier for P5-CLOSURE-16.
#
# This script does not source the chapter and does not call lm(), anova(),
# t.test() or oneway.test(). It rebuilds every generated regression quantity
# used in Chapter 16 from the committed population snapshot with explicit
# least-squares and sampling formulas.

options(OutDec = ".", scipen = 999)

fail <- function(...) {
  stop(paste0(...), call. = FALSE)
}

check <- function(condition, ...) {
  if (!isTRUE(condition)) fail(...)
}

close_to <- function(actual, expected, tolerance = 1e-10) {
  is.finite(actual) && abs(actual - expected) <= tolerance
}

ols <- function(y, x) {
  beta <- solve(crossprod(x), crossprod(x, y))
  fitted <- drop(x %*% beta)
  residual <- y - fitted
  sse <- sum(residual^2)
  sst <- sum((y - mean(y))^2)
  n <- length(y)
  p <- ncol(x)
  list(
    beta = drop(beta),
    fitted = fitted,
    residual = residual,
    sse = sse,
    r2 = 1 - sse / sst,
    adj_r2 = 1 - (sse / (n - p)) / (sst / (n - 1))
  )
}

source_levels <- c("portal", "društvene mreže", "TV", "radio", "tisak")

source_design <- function(data, include_age = TRUE, extra = NULL) {
  columns <- list(intercept = rep(1, nrow(data)))
  if (include_age) columns$dob <- data$dob
  for (level in source_levels[-1]) {
    columns[[paste0("izvor:", level)]] <- as.numeric(data$izvor_vijesti == level)
  }
  if (!is.null(extra)) {
    for (name in names(extra)) columns[[name]] <- extra[[name]]
  }
  result <- do.call(cbind, columns)
  colnames(result) <- names(columns)
  result
}

simple_design <- function(x) cbind(intercept = 1, x = x)

population <- read.csv(
  "data/populacija-medija.csv",
  stringsAsFactors = FALSE,
  check.names = FALSE,
  encoding = "UTF-8"
)
check(nrow(population) == 50000L, "Population row count is not 50000.")
check(identical(population$osoba, seq_len(50000L)), "Population key is not canonical.")
check(setequal(unique(population$izvor_vijesti), source_levels), "Source levels drifted.")

y <- population$povjerenje_medijima
model_one <- ols(y, simple_design(population$dob))
model_two <- ols(y, source_design(population))

group_rows <- split(seq_len(nrow(population)), population$izvor_vijesti)
group_age_means <- vapply(group_rows, function(index) mean(population$dob[index]), numeric(1))
group_slopes <- vapply(
  group_rows,
  function(index) ols(y[index], simple_design(population$dob[index]))$beta[[2]],
  numeric(1)
)

set.seed(1414)
two_pool <- population[population$izvor_vijesti %in% c("TV", "društvene mreže"), ]
two <- two_pool[sample.int(nrow(two_pool), 120L), ]
two_groups <- split(two$povjerenje_medijima, factor(two$izvor_vijesti, levels = source_levels[2:3]))
two_n <- vapply(two_groups, length, integer(1))
two_mean <- vapply(two_groups, mean, numeric(1))
two_var <- vapply(two_groups, var, numeric(1))
two_difference <- unname(two_mean[[2]] - two_mean[[1]])
two_model <- ols(
  two$povjerenje_medijima,
  cbind(intercept = 1, tv = as.numeric(two$izvor_vijesti == "TV"))
)
pooled_variance <- sum((two_n - 1) * two_var) / (sum(two_n) - 2)
student_se <- sqrt(pooled_variance * sum(1 / two_n))
student_t <- abs(two_difference / student_se)
student_df <- sum(two_n) - 2
welch_se <- sqrt(sum(two_var / two_n))
welch_t <- abs(two_difference / welch_se)
welch_df <- sum(two_var / two_n)^2 /
  sum((two_var / two_n)^2 / (two_n - 1))

set.seed(1515)
five <- population[sample.int(nrow(population), 300L), ]
five_groups <- split(five$povjerenje_medijima, factor(five$izvor_vijesti, levels = source_levels))
five_n <- vapply(five_groups, length, integer(1))
five_mean <- vapply(five_groups, mean, numeric(1))
five_var <- vapply(five_groups, var, numeric(1))
five_overall <- mean(five$povjerenje_medijima)
five_between <- sum(five_n * (five_mean - five_overall)^2)
five_within <- sum((five_n - 1) * five_var)
five_df1 <- length(five_groups) - 1
five_df2 <- nrow(five) - length(five_groups)
five_f <- (five_between / five_df1) / (five_within / five_df2)
five_r2 <- five_between / (five_between + five_within)
welch_weights <- five_n / five_var
welch_weighted_mean <- sum(welch_weights * five_mean) / sum(welch_weights)
welch_term <- sum((1 / (five_n - 1)) * (1 - welch_weights / sum(welch_weights))^2)
five_welch_f <- (
  sum(welch_weights * (five_mean - welch_weighted_mean)^2) / five_df1
) / (1 + (2 * (length(five_groups) - 2) / (length(five_groups)^2 - 1)) * welch_term)
five_welch_df2 <- (length(five_groups)^2 - 1) / (3 * welch_term)

narrow <- population[population$dob >= 30 & population$dob <= 50, ]
model_narrow <- ols(narrow$povjerenje_medijima, simple_design(narrow$dob))

model_consequence <- ols(
  y,
  source_design(population, extra = list(spremnost_platiti = population$spremnost_platiti))
)

set.seed(1616)
small <- population[sample.int(nrow(population), 200L), ]
small_noise <- replicate(5L, rnorm(200L))
colnames(small_noise) <- paste0("sum", seq_len(5L))
model_small_plain <- ols(small$povjerenje_medijima, source_design(small))
model_small_noise <- ols(
  small$povjerenje_medijima,
  source_design(small, extra = as.data.frame(small_noise))
)

set.seed(1618)
noise_count <- 25L
training_index <- sample.int(nrow(population), 150L)
training <- population[training_index, ]
remaining <- population[-training_index, ]
verification <- remaining[sample.int(nrow(remaining), 2000L), ]
training_noise <- matrix(rnorm(nrow(training) * noise_count), nrow(training), noise_count)
verification_noise <- matrix(rnorm(nrow(verification) * noise_count), nrow(verification), noise_count)
colnames(training_noise) <- colnames(verification_noise) <- paste0("z", seq_len(noise_count))
training_plain_x <- source_design(training)
verification_plain_x <- source_design(verification)
training_rich_x <- cbind(training_plain_x, training_noise)
verification_rich_x <- cbind(verification_plain_x, verification_noise)
model_training_plain <- ols(training$povjerenje_medijima, training_plain_x)
model_training_rich <- ols(training$povjerenje_medijima, training_rich_x)
rmse <- function(actual, predicted) sqrt(mean((actual - predicted)^2))
rmse_plain_training <- rmse(training$povjerenje_medijima, model_training_plain$fitted)
rmse_rich_training <- rmse(training$povjerenje_medijima, model_training_rich$fitted)
rmse_plain_verification <- rmse(
  verification$povjerenje_medijima,
  drop(verification_plain_x %*% model_training_plain$beta)
)
rmse_rich_verification <- rmse(
  verification$povjerenje_medijima,
  drop(verification_rich_x %*% model_training_rich$beta)
)
rmse_mean_verification <- rmse(
  verification$povjerenje_medijima,
  rep(mean(training$povjerenje_medijima), nrow(verification))
)

minute_model <- ols(population$minute_medija, simple_design(population$dob))
minute_order <- order(minute_model$fitted, seq_along(minute_model$fitted))
bucket_sizes <- rep(floor(nrow(population) / 6), 6)
bucket_sizes[seq_len(nrow(population) %% 6)] <- bucket_sizes[seq_len(nrow(population) %% 6)] + 1
bucket <- integer(nrow(population))
bucket[minute_order] <- rep(seq_len(6), bucket_sizes)
minute_spread <- vapply(
  seq_len(6),
  function(index) sd(minute_model$residual[bucket == index]),
  numeric(1)
)

heterogeneity <- expand.grid(
  group = factor(c("Skupina A", "Skupina B"), levels = c("Skupina A", "Skupina B")),
  x = 0:10
)
heterogeneity$predicted <- ifelse(
  heterogeneity$group == "Skupina A",
  2 + 0.6 * heterogeneity$x,
  8 - 0.2 * heterogeneity$x
)
heterogeneity_a <- ols(
  heterogeneity$predicted[heterogeneity$group == "Skupina A"],
  simple_design(heterogeneity$x[heterogeneity$group == "Skupina A"])
)$beta[[2]]
heterogeneity_b <- ols(
  heterogeneity$predicted[heterogeneity$group == "Skupina B"],
  simple_design(heterogeneity$x[heterogeneity$group == "Skupina B"])
)$beta[[2]]
heterogeneity_pooled <- ols(heterogeneity$predicted, simple_design(heterogeneity$x))$beta[[2]]

set.seed(1616)
widget_interest <- rnorm(52)
widget_time <- pmax(0, 5 + 1.8 * widget_interest + rnorm(52, 0, 1.5))
widget_engagement <- 20 + 2.3 * widget_time + 7 * widget_interest + rnorm(52, 0, 4.5)
widget_plain <- ols(widget_engagement, simple_design(widget_time))
widget_adjusted <- ols(widget_engagement, cbind(1, widget_time, widget_interest))
widget_candidate_sse <- sum((widget_engagement - (10 + 4.5 * widget_time))^2)

values <- c(
  latent_age = 0.028,
  latent_networks = -0.55,
  latent_tv = 0.35,
  latent_radio = 0.60,
  latent_print = 0.50,
  slope_one = model_one$beta[[2]],
  intercept_one = model_one$beta[[1]],
  r2_one = model_one$r2,
  slope_two = model_two$beta[[2]],
  r2_two = model_two$r2,
  source_networks = model_two$beta[[3]],
  source_tv = model_two$beta[[4]],
  source_radio = model_two$beta[[5]],
  source_print = model_two$beta[[6]],
  age_networks = group_age_means[["društvene mreže"]],
  age_radio = group_age_means[["radio"]],
  within_slope_portal = group_slopes[["portal"]],
  within_slope_networks = group_slopes[["društvene mreže"]],
  within_slope_tv = group_slopes[["TV"]],
  within_slope_radio = group_slopes[["radio"]],
  within_slope_print = group_slopes[["tisak"]],
  within_slope_min = min(group_slopes),
  within_slope_max = max(group_slopes),
  ten_year_one = 10 * model_one$beta[[2]],
  ten_year_two = 10 * model_two$beta[[2]],
  thirty_year_one = 30 * model_one$beta[[2]],
  thirty_year_two = 30 * model_two$beta[[2]],
  two_difference = two_difference,
  two_coefficient = two_model$beta[[2]],
  two_student_t = student_t,
  two_student_df = student_df,
  two_welch_t = welch_t,
  two_welch_df = welch_df,
  five_f = five_f,
  five_df1 = five_df1,
  five_df2 = five_df2,
  five_welch_f = five_welch_f,
  five_welch_df1 = five_df1,
  five_welch_df2 = five_welch_df2,
  five_r2 = five_r2,
  small_r2_plain = model_small_plain$r2,
  small_r2_noise = model_small_noise$r2,
  small_adj_plain = model_small_plain$adj_r2,
  small_adj_noise = model_small_noise$adj_r2,
  narrow_n = nrow(narrow),
  narrow_slope = model_narrow$beta[[2]],
  narrow_r2 = model_narrow$r2,
  consequence_r2 = model_consequence$r2,
  consequence_residual_sd = sd(model_consequence$residual),
  outcome_sd = sd(y),
  residual_sd = sd(model_two$residual),
  minute_slope = minute_model$beta[[2]],
  minute_spread_low = minute_spread[[1]],
  minute_spread_high = minute_spread[[6]],
  heterogeneity_a = heterogeneity_a,
  heterogeneity_b = heterogeneity_b,
  heterogeneity_pooled = heterogeneity_pooled,
  training_n = nrow(training),
  verification_n = nrow(verification),
  noise_count = noise_count,
  training_plain_r2 = model_training_plain$r2,
  training_rich_r2 = model_training_rich$r2,
  rmse_plain_training = rmse_plain_training,
  rmse_rich_training = rmse_rich_training,
  rmse_plain_verification = rmse_plain_verification,
  rmse_rich_verification = rmse_rich_verification,
  rmse_mean_verification = rmse_mean_verification,
  widget_plain_intercept = widget_plain$beta[[1]],
  widget_plain_slope = widget_plain$beta[[2]],
  widget_adjusted_intercept = widget_adjusted$beta[[1]],
  widget_adjusted_time_slope = widget_adjusted$beta[[2]],
  widget_adjusted_interest_slope = widget_adjusted$beta[[3]],
  widget_candidate_sse = widget_candidate_sse,
  widget_minimum_sse = widget_plain$sse
)

generator_text <- paste(readLines("R/podaci-nastavni.R", encoding = "UTF-8"), collapse = "\n")
for (token in c(
  "4.81 + 0.028 * (dob - 42.7)",
  "`društvene mreže` = -0.55",
  "TV = 0.35",
  "radio = 0.60",
  "tisak = 0.50"
)) {
  check(grepl(token, generator_text, fixed = TRUE),
        "Generator no longer exposes the latent Chapter 16 contract: ", token)
}

check(close_to(values[["two_difference"]], values[["two_coefficient"]], 1e-12),
      "Binary coefficient no longer equals the two-group mean difference.")
check(close_to(values[["two_student_t"]], student_t, 1e-12),
      "Student t reconstruction is inconsistent.")
check(values[["small_r2_noise"]] > values[["small_r2_plain"]],
      "Adding noise no longer increases training R-squared.")
check(values[["small_adj_noise"]] < values[["small_adj_plain"]],
      "Adjusted R-squared no longer penalizes the five noise predictors.")
check(values[["rmse_rich_training"]] < values[["rmse_plain_training"]],
      "Rich model no longer looks better on its training data.")
check(values[["rmse_rich_verification"]] > values[["rmse_plain_verification"]],
      "Rich model no longer performs worse on held-out data.")
check(values[["rmse_rich_verification"]] > values[["rmse_mean_verification"]],
      "Rich model no longer performs worse than the held-out mean baseline.")
check(values[["consequence_r2"]] > values[["r2_two"]],
      "Post-outcome variable no longer raises in-sample R-squared.")
check(values[["minute_spread_high"]] > values[["minute_spread_low"]],
      "Media-minute residual spread no longer increases across fitted sextiles.")
check(close_to(values[["heterogeneity_a"]], 0.6, 1e-12) &&
        close_to(values[["heterogeneity_b"]], -0.2, 1e-12) &&
        close_to(values[["heterogeneity_pooled"]], 0.2, 1e-12),
      "Heterogeneity slopes no longer equal 0.6, -0.2 and 0.2.")
check(values[["widget_candidate_sse"]] > values[["widget_minimum_sse"]],
      "Static widget candidate no longer has a larger SSE than the minimum.")

expected <- c(
  latent_age = 0.028000000000000,
  latent_networks = -0.550000000000000,
  latent_tv = 0.350000000000000,
  latent_radio = 0.600000000000000,
  latent_print = 0.500000000000000,
  slope_one = 0.036723816393759,
  intercept_one = 3.329375993217577,
  r2_one = 0.088000437806151,
  slope_two = 0.026885173178122,
  r2_two = 0.122277516285767,
  source_networks = -0.533533786572308,
  source_tv = 0.311646662154156,
  source_radio = 0.595079781147251,
  source_print = 0.486393753673952,
  age_networks = 33.429660636866494,
  age_radio = 47.867443055317693,
  within_slope_portal = 0.026907585027004,
  within_slope_networks = 0.025751887679822,
  within_slope_tv = 0.028054221774352,
  within_slope_radio = 0.026825402801560,
  within_slope_print = 0.025479869074142,
  within_slope_min = 0.025479869074142,
  within_slope_max = 0.028054221774352,
  ten_year_one = 0.367238163937590,
  ten_year_two = 0.268851731781220,
  thirty_year_one = 1.101714491812770,
  thirty_year_two = 0.806555195343660,
  two_difference = 1.185714285714286,
  two_coefficient = 1.185714285714286,
  two_student_t = 3.208648372705720,
  two_student_df = 118.000000000000000,
  two_welch_t = 3.182192655868045,
  two_welch_df = 102.471131550668645,
  five_f = 8.381812957409025,
  five_df1 = 4.000000000000000,
  five_df2 = 295.000000000000000,
  five_welch_f = 7.320807631165560,
  five_welch_df1 = 4.000000000000000,
  five_welch_df2 = 112.425284937608652,
  five_r2 = 0.102053183237969,
  small_r2_plain = 0.081378816922688,
  small_r2_noise = 0.091274637858667,
  small_adj_plain = 0.057703013235128,
  small_adj_noise = 0.043193930867062,
  narrow_n = 24282.000000000000000,
  narrow_slope = 0.038507423166654,
  narrow_r2 = 0.013875319001514,
  consequence_r2 = 0.131956275921432,
  consequence_residual_sd = 1.848581794786343,
  outcome_sd = 1.984119708137673,
  residual_sd = 1.858859146162441,
  minute_slope = 1.050468521424146,
  minute_spread_low = 58.060035646893873,
  minute_spread_high = 76.938912263518915,
  heterogeneity_a = 0.600000000000000,
  heterogeneity_b = -0.200000000000000,
  heterogeneity_pooled = 0.199999999999999,
  training_n = 150.000000000000000,
  verification_n = 2000.000000000000000,
  noise_count = 25.000000000000000,
  training_plain_r2 = 0.130991933684841,
  training_rich_r2 = 0.253764009686708,
  rmse_plain_training = 1.777449606406513,
  rmse_rich_training = 1.647113353822071,
  rmse_plain_verification = 1.880142878709777,
  rmse_rich_verification = 2.061987662423383,
  rmse_mean_verification = 1.991200084817640,
  widget_plain_intercept = 9.098363421034410,
  widget_plain_slope = 4.587964445158933,
  widget_adjusted_intercept = 21.278259136481005,
  widget_adjusted_time_slope = 2.020079145031726,
  widget_adjusted_interest_slope = 7.436775135608025,
  widget_candidate_sse = 2575.906468462459543,
  widget_minimum_sse = 2561.139633487692663
)

check(identical(names(values), names(expected)),
      "Independent value inventory no longer matches the fixed Chapter 16 contract.")
for (name in names(expected)) {
  tolerance <- max(1e-10, abs(expected[[name]]) * 1e-11)
  check(close_to(values[[name]], expected[[name]], tolerance),
        "Independent value drifted for ", name, ": ",
        format(values[[name]], digits = 16), " versus ",
        format(expected[[name]], digits = 16))
}

cat("UNIT_16_NUMERICS_OK\n")
for (name in names(values)) cat(sprintf("%s=%.15f\n", name, values[[name]]))
