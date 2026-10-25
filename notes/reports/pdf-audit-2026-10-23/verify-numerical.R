# Independent arithmetic checks on freshly evaluated manuscript examples.
# Run from the checkout root through the Bookwright R launcher.
chunks <- function(path) {
  x <- readLines(path, encoding = "UTF-8", warn = FALSE)
  out <- list(); inside <- FALSE; current <- character()
  for (line in x) {
    if (!inside && grepl("^```\\{r", line)) {
      inside <- TRUE; current <- character()
    } else if (inside && identical(trimws(line), "```")) {
      out[[length(out) + 1L]] <- current; inside <- FALSE
    } else if (inside) current <- c(current, line)
  }
  out
}
run_hidden <- function(path) {
  for (code in chunks(path)) {
    if (any(grepl("^#\\| include: false", code)))
      eval(parse(text = code, encoding = "UTF-8"), envir = .GlobalEnv)
  }
}
run_hidden("chapters/09-procjena.qmd")
stopifnot(identical(as.integer(s9_preseti$promasaji), c(3L, 0L, 1L)))
stopifnot(length(s9_asimetricni_obuhvat) == 10000L,
  sum(s9_asimetricni_obuhvat) == 8622L,
  abs(1 - 0.98^20 - 0.3323920282) < 1e-9,
  round(4.815 - 1.96 * 2.093/sqrt(200), 3) == 4.525,
  round(4.815 + 1.96 * 2.093/sqrt(200), 3) == 5.105,
  median(c(83,82,134,139,164)) == 134,
  median(c(83,83,82,139,164)) == 83,
  ceiling((1.96*2/.5)^2) == 62)
cat("ADDITIONAL_PRINT_EXERCISES_AND_SKEWED_COVERAGE_OK\n")
widths <- c(2*qnorm(.975)/sqrt(40), 2*qnorm(.995)/sqrt(40),
  2*qnorm(.975)/sqrt(160))
cat("INTERVAL_MISSES\n"); print(s9_preseti)
cat("INDEPENDENT_WIDTHS\n"); print(widths, digits = 12)
stopifnot(sum(abs(rowMeans(s9_crte[, 1:40])) > qnorm(.975)/sqrt(40)) == 3L)

run_hidden("chapters/11-velicina-ucinka-i-snaga.qmd")
stopifnot(all(s11_krivulja$odbacivanja <= s11_krivulja$valjani),
  all(s11_krivulja$valjani + s11_krivulja$izostavljeni == s11_krivulja$pokusaji),
  all(abs(s11_krivulja$snaga - 100*s11_krivulja$odbacivanja/s11_krivulja$valjani) < 1e-10),
  all(s11_krivulja$odbacivanja == c(68, 107, 170, 239, 281, 299)))
cat("POWER_COUNTS_AND_DENOMINATORS\n"); print(s11_krivulja)

run_hidden("chapters/17-doba-algoritama.qmd")
u <- usporedba_pragova_c17
stopifnot(all(u$TP + u$FP + u$FN + u$TN == 272),
  all(abs(u[["Stopa lažno pozitivnih"]] - u$FP/(u$FP+u$TN)) < 1e-12),
  all(abs(u[["Stopa lažno negativnih"]] - u$FN/(u$FN+u$TP)) < 1e-12),
  all(abs(u[["Pozitivna prediktivna vrijednost"]] - u$TP/(u$TP+u$FP)) < 1e-12))
cat("CLASSIFICATION_COUNTS_AND_RATES\n"); print(u)

raw <- read.csv("data/populacija-medija.csv", check.names = FALSE)
ag <- read.csv("data/populacija-medija-agregat.csv", check.names = FALSE)
stopifnot(sum(ag$broj[ag$izvor_vijesti %in% c("TV", "radio")]) == 16666,
  sum(ag$broj_platio[ag$izvor_vijesti %in% c("TV", "radio")]) == 4301,
  4301/16666 < 1289/4855)
cat("REVISED_FIRST_ERROR_EXERCISE\n"); print(c(combined = 4301/16666, print = 1289/4855), digits = 12)
cat("NUMERICAL_AUDIT_OK\n")
