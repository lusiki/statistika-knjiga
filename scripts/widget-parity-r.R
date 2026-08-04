#!/usr/bin/env Rscript
# Numeric adapters for the claims made by the seventeen R print twins.
# The adapters intentionally omit styling, labels, jitter, and point coordinates.

args <- commandArgs(trailingOnly = TRUE)
root <- normalizePath(if (length(args)) args[[1]] else ".", winslash = "/", mustWork = TRUE)
registry <- jsonlite::fromJSON(
  file.path(root, "data", "widgets.json"),
  simplifyVector = FALSE
)

sample_sd <- function(x) stats::sd(x)
skewness <- function(x) {
  centered <- x - mean(x)
  mean(centered^3) / mean(centered^2)^1.5
}

fit_line <- function(x, y) {
  slope <- sum((x - mean(x)) * (y - mean(y))) / sum((x - mean(x))^2)
  list(intercept = mean(y) - slope * mean(x), slope = slope)
}

scenario_list <- function(parameters) parameters$scenarios

adapter_w01 <- function(parameters) {
  p <- scenario_list(parameters)[[1]]
  list(
    "default.aggregate_a" = p$share_a_easy * 0.8 + (1 - p$share_a_easy) * 0.2,
    "default.aggregate_b" = p$share_b_easy * 0.9 + (1 - p$share_b_easy) * 0.3,
    "default.easy_a" = 0.8,
    "default.easy_b" = 0.9,
    "default.hard_a" = 0.2,
    "default.hard_b" = 0.3
  )
}

adapter_w02 <- function(parameters) {
  p <- scenario_list(parameters)[[1]]
  group <- rep(c("low", "high"), each = 16)
  row <- rep(seq_len(16), 2)
  u <- (row - 8.5) / 7.5
  exposure <- ifelse(group == "high", 6.6, 2.8) + 1.6 * u
  noise <- 0.28 * sin(row * 2.3) + 0.10 * cos(row * 1.1)
  outcome <- 7.2 - 0.55 * exposure + ifelse(group == "high", p$shift, 0) + noise
  list(
    "default.pooled_slope" = fit_line(exposure, outcome)$slope,
    "default.low_slope" = fit_line(exposure[group == "low"], outcome[group == "low"])$slope,
    "default.high_slope" = fit_line(exposure[group == "high"], outcome[group == "high"])$slope
  )
}

adapter_w03 <- function(parameters) {
  result <- list()
  for (p in scenario_list(parameters)) {
    estimate <- p$share
    margin <- 1.96 * sqrt(estimate * (1 - estimate) / p$n)
    result[[paste0(p$id, ".estimate")]] <- estimate
    result[[paste0(p$id, ".truth")]] <- estimate - p$bias
    result[[paste0(p$id, ".margin")]] <- margin
    result[[paste0(p$id, ".lower")]] <- max(0, estimate - margin)
    result[[paste0(p$id, ".upper")]] <- min(1, estimate + margin)
  }
  result
}

adapter_w04 <- function(parameters) {
  deviations <- c(-3, -2, -1, -1, 0, 1, 1, 2, 3)
  result <- list()
  for (p in scenario_list(parameters)) {
    values <- sort(c(11 + deviations * p$spread, p$extreme))
    result[[paste0(p$id, ".mean")]] <- mean(values)
    result[[paste0(p$id, ".median")]] <- median(values)
    result[[paste0(p$id, ".sd")]] <- sample_sd(values)
    result[[paste0(p$id, ".iqr")]] <- unname(diff(stats::quantile(values, c(0.25, 0.75), type = 7)))
  }
  result
}

adapter_w05 <- function(parameters) {
  p <- scenario_list(parameters)[[1]]
  set.seed(p$seed)
  group <- rep(c("a", "b"), each = p$n / 2)
  x <- rep(seq(1, 10, length.out = p$n / 2), 2)
  y <- 1.5 + 0.55 * x + ifelse(group == "b", p$group_shift, 0) +
    rnorm(p$n, 0, p$noise_sd)
  list(
    "default.overall_mean" = mean(y),
    "default.overall_sd" = sample_sd(y),
    "default.group_a_mean" = mean(y[group == "a"]),
    "default.group_b_mean" = mean(y[group == "b"]),
    "default.group_difference" = mean(y[group == "b"]) - mean(y[group == "a"]),
    "default.slope" = fit_line(x, y)$slope
  )
}

adapter_w06 <- function(parameters) {
  set.seed(scenario_list(parameters)[[1]]$r_seed)
  result <- list()
  for (index in seq_along(scenario_list(parameters))) {
    p <- scenario_list(parameters)[[index]]
    x <- rnorm(p$n)
    z <- rnorm(p$n)
    y <- p$rho * x + sqrt(1 - p$rho^2) * z
    result[[paste0("cloud_", index, ".correlation")]] <- cor(x, y)
  }
  result
}

adapter_w07 <- function(parameters) {
  scenarios <- scenario_list(parameters)
  set.seed(scenarios[[1]]$r_seed)
  result <- list()
  standard_deviations <- numeric()
  for (p in scenarios) {
    rates <- rbinom(p$repetitions, size = p$n, prob = p$probability) / p$n
    result[[paste0(p$id, ".mean")]] <- mean(rates)
    result[[paste0(p$id, ".sd")]] <- sample_sd(rates)
    result[[paste0(p$id, ".q05")]] <- unname(quantile(rates, 0.05, type = 7))
    result[[paste0(p$id, ".q95")]] <- unname(quantile(rates, 0.95, type = 7))
    standard_deviations <- c(standard_deviations, sample_sd(rates))
  }
  result$width_ratio <- standard_deviations[[1]] / standard_deviations[[2]]
  result
}

adapter_w08 <- function(parameters) {
  scenarios <- scenario_list(parameters)
  set.seed(scenarios[[1]]$r_seed)
  population <- rbeta(scenarios[[1]]$r_population_n, shape1 = 1, shape2 = 5)
  result <- list()
  for (p in scenarios) {
    sample_means <- replicate(
      p$repetitions,
      mean(sample(population, p$n, replace = TRUE))
    )
    result[[paste0(p$id, ".se_ratio")]] <- sample_sd(sample_means) / sample_sd(population)
    result[[paste0(p$id, ".mean_skewness")]] <- skewness(sample_means)
    result[[paste0(p$id, ".center_offset_sd")]] <-
      (mean(sample_means) - mean(population)) / sample_sd(population)
  }
  result$skew_reduction <-
    abs(result[[paste0(scenarios[[1]]$id, ".mean_skewness")]]) -
    abs(result[[paste0(scenarios[[2]]$id, ".mean_skewness")]])
  result
}

adapter_w09 <- function(parameters) {
  p <- scenario_list(parameters)[[1]]
  set.seed(p$r_seed)
  estimates <- replicate(p$intervals, mean(rnorm(p$n)))
  margin <- p$critical / sqrt(p$n)
  covered <- estimates - margin <= 0 & estimates + margin >= 0
  list(
    "default.coverage_rate" = mean(covered),
    "default.mean_width" = 2 * margin,
    "default.mean_estimate" = mean(estimates)
  )
}

adapter_w10 <- function(parameters) {
  p <- scenario_list(parameters)[[1]]
  set.seed(p$seed)
  z_null <- rnorm(p$repetitions)
  z_effect <- rnorm(p$repetitions, p$effect * sqrt(p$n / 2))
  p_null <- 2 * pnorm(-abs(z_null))
  p_effect <- 2 * pnorm(-abs(z_effect))
  list(
    "default.null_rejection_rate" = mean(p_null <= p$threshold),
    "default.effect_rejection_rate" = mean(p_effect <= p$threshold),
    "default.null_p_mean" = mean(p_null),
    "default.effect_p_mean" = mean(p_effect)
  )
}

adapter_w11 <- function(parameters) {
  set.seed(parameters$r_seed)
  result <- list()
  for (effect in unlist(parameters$effects)) {
    powers <- list()
    for (n in seq(20, 300, by = 10)) {
      power <- mean(abs(rnorm(
        parameters$repetitions,
        mean = effect * sqrt(n / 2), sd = 1
      )) >= qnorm(1 - parameters$threshold / 2))
      powers[[as.character(n)]] <- power
    }
    for (n in unlist(parameters$report_n)) {
      result[[paste0("d", effect, ".n", n, ".power")]] <- powers[[as.character(n)]]
    }
    eligible <- as.numeric(names(powers))[unlist(powers) >= 0.8]
    result[[paste0("d", effect, ".first_n_80")]] <- if (length(eligible)) min(eligible) else NA_real_
  }
  result
}

adapter_w12 <- function(parameters) {
  set.seed(parameters$r_seed)
  result <- list()
  for (paths in unlist(parameters$paths)) {
    minima <- replicate(parameters$repetitions, min(runif(paths)))
    result[[paste0("paths", paths, ".nominal_rate")]] <- mean(minima <= 0.05)
    result[[paste0("paths", paths, ".corrected_rate")]] <- mean(minima <= 0.05 / paths)
    result[[paste0("paths", paths, ".cdf_001")]] <- mean(minima <= 0.01)
  }
  result
}

adapter_w13 <- function(parameters) {
  result <- list()
  for (p in scenario_list(parameters)) {
    expected <- p$n / 2
    shift <- round(expected * p$shift_percent / 100)
    contribution <- shift^2 / expected
    chi_square <- 4 * contribution
    result[[paste0(p$id, ".expected")]] <- expected
    result[[paste0(p$id, ".shift")]] <- shift
    result[[paste0(p$id, ".cell_contribution")]] <- contribution
    result[[paste0(p$id, ".chi_square")]] <- chi_square
    result[[paste0(p$id, ".cramers_v")]] <- sqrt(chi_square / (2 * p$n))
  }
  result
}

adapter_w14 <- function(parameters) {
  scenarios <- scenario_list(parameters)
  set.seed(parameters$r_seed)
  result <- list()
  standard_errors <- list()
  for (p in scenarios) {
    paired <- identical(p$design, "paired")
    standard_error <- if (paired) {
      p$sd * sqrt(2 * (1 - parameters$correlation) / p$n)
    } else {
      p$sd * sqrt(2 / p$n)
    }
    estimates <- rnorm(parameters$r_repetitions, p$difference, standard_error)
    result[[paste0(p$id, ".theoretical_se")]] <- standard_error
    result[[paste0(p$id, ".estimate_mean")]] <- mean(estimates)
    result[[paste0(p$id, ".estimate_sd")]] <- sample_sd(estimates)
    standard_errors[[p$id]] <- standard_error
  }
  result$se_ratio <- standard_errors$paired / standard_errors$independent
  result
}

adapter_w15 <- function(parameters) {
  result <- list()
  n <- parameters$n_per_group
  for (p in scenario_list(parameters)) {
    means <- unlist(p$means)
    grand <- mean(means)
    ss_between <- n * sum((means - grand)^2)
    ms_between <- ss_between / (length(means) - 1)
    ms_within <- p$sd^2
    result[[paste0(p$id, ".grand_mean")]] <- grand
    result[[paste0(p$id, ".ms_between")]] <- ms_between
    result[[paste0(p$id, ".ms_within")]] <- ms_within
    result[[paste0(p$id, ".f_ratio")]] <- ms_between / ms_within
  }
  result
}

adapter_w16 <- function(parameters) {
  p <- scenario_list(parameters)[[1]]
  set.seed(p$seed)
  interest <- rnorm(p$n)
  time <- pmax(0, 5 + 1.8 * interest + rnorm(p$n, 0, 1.5))
  engagement <- 20 + 2.3 * time + 7 * interest + rnorm(p$n, 0, 4.5)
  aggregate <- lm(engagement ~ time)
  adjusted <- lm(engagement ~ time + interest)
  aggregate_coefficients <- coef(aggregate)
  sse_minimum <- sum(residuals(aggregate)^2)
  user_sse <- sum((engagement - p$user_intercept - p$user_slope * time)^2)
  list(
    "default.aggregate_intercept" = unname(aggregate_coefficients[["(Intercept)"]]),
    "default.aggregate_slope" = unname(aggregate_coefficients[["time"]]),
    "default.adjusted_slope" = unname(coef(adjusted)[["time"]]),
    "default.sse_minimum" = sse_minimum,
    "default.user_sse" = user_sse,
    "default.user_to_minimum_ratio" = user_sse / sse_minimum
  )
}

adapter_w17 <- function(parameters) {
  p <- scenario_list(parameters)[[1]]
  set.seed(p$seed)
  negative <- pmin(pmax(rnorm(p$n_per_class, 0.30, 0.18), 0), 1)
  positive <- pmin(pmax(rnorm(p$n_per_class, 0.70, 0.18), 0), 1)
  fpr <- mean(negative >= p$threshold)
  fnr <- mean(positive < p$threshold)
  tpr <- 1 - fnr
  tnr <- 1 - fpr
  group <- function(base_rate) {
    list(
      ppv = base_rate * tpr / (base_rate * tpr + (1 - base_rate) * fpr),
      accuracy = base_rate * tpr + (1 - base_rate) * tnr
    )
  }
  a <- group(p$base_rate_a)
  b <- group(p$base_rate_b)
  list(
    "default.fpr" = fpr,
    "default.fnr" = fnr,
    "default.group_a.ppv" = a$ppv,
    "default.group_a.accuracy" = a$accuracy,
    "default.group_b.ppv" = b$ppv,
    "default.group_b.accuracy" = b$accuracy
  )
}

adapters <- list(
  w01 = adapter_w01, w02 = adapter_w02, w03 = adapter_w03,
  w04 = adapter_w04, w05 = adapter_w05, w06 = adapter_w06,
  w07 = adapter_w07, w08 = adapter_w08, w09 = adapter_w09,
  w10 = adapter_w10, w11 = adapter_w11, w12 = adapter_w12,
  w13 = adapter_w13, w14 = adapter_w14, w15 = adapter_w15,
  w16 = adapter_w16, w17 = adapter_w17
)

results <- list()
for (widget in registry$widgets) {
  if (is.null(widget$parity)) stop(widget$id, ": missing parity record")
  results[[widget$id]] <- adapters[[widget$id]](widget$parity$parameters)
}

cat(jsonlite::toJSON(
  list(schema_version = 1, adapter = "r", results = results),
  auto_unbox = TRUE,
  digits = 17,
  pretty = TRUE,
  na = "null"
), "\n", sep = "")
