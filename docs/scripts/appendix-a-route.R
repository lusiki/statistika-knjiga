#!/usr/bin/env Rscript

# Samostalna provjerna ruta za Dodatak A.
#
# Skripta namjerno ne učitava R/setup.R niti izvršava kod iz poglavlja. Sve
# ulaze čita iz kanonskih datoteka, provjerava njihove sažetke i zatim ponavlja
# po jedan podržani postupak iz poglavlja 6--16.

args <- commandArgs(trailingOnly = TRUE)

arg_value <- function(flag, default = NULL) {
  hit <- match(flag, args)
  if (is.na(hit)) return(default)
  if (hit == length(args)) stop("Nedostaje vrijednost nakon ", flag, ".")
  args[[hit + 1L]]
}

route_root <- normalizePath(arg_value("--root", "."), mustWork = TRUE)
output_path <- arg_value("--output", "")
text_candidate <- arg_value("--text-candidate", "")
python_bin <- arg_value("--python", Sys.which("python"))

root_file <- function(...) file.path(route_root, ...)

assert_md5 <- function(path, expected) {
  if (!file.exists(path)) stop("Nedostaje kanonska datoteka: ", path)
  actual <- unname(tools::md5sum(path))
  if (!identical(actual, expected)) {
    stop("Neispravan MD5 za ", path, ": ", actual, "; očekivano ", expected, ".")
  }
}

read_book_csv <- function(path) {
  read.csv(
    path,
    stringsAsFactors = FALSE,
    check.names = FALSE,
    fileEncoding = "UTF-8"
  )
}

anketa_path <- root_file("data", "anketa-mreze.csv")
populacija_path <- root_file("data", "populacija-medija.csv")
evidence12_path <- root_file("notes", "reports", "p3-evidence12-rrr-lab-effects.csv")

assert_md5(anketa_path, "b988c25a8017e2d4dcd26be160890e89")
assert_md5(populacija_path, "07e158ca6385fe406dd6741e680fd756")

anketa_mreze <- read_book_csv(anketa_path)
populacija_medija <- read_book_csv(populacija_path)
evidence12 <- read_book_csv(evidence12_path)

stopifnot(
  nrow(anketa_mreze) == 300L,
  nrow(populacija_medija) == 50000L,
  all(c("dob", "dobna_skupina", "minute_dnevno", "povjerenje") %in% names(anketa_mreze)),
  all(c("dob", "obrazovanje", "izvor_vijesti", "povjerenje_medijima") %in% names(populacija_medija)),
  all(c("lab", "cohen_d", "d_se") %in% names(evidence12))
)

dob_razine <- c("18 do 24", "25 do 34", "35 do 44", "45 i više")
izvor_razine <- c("portal", "društvene mreže", "TV", "radio", "tisak")
obrazovanje_razine <- c("osnovna", "srednja", "viša", "diplomska")

anketa_mreze$dobna_skupina <- factor(anketa_mreze$dobna_skupina, levels = dob_razine)
populacija_medija$izvor_vijesti <- factor(
  populacija_medija$izvor_vijesti,
  levels = izvor_razine
)
populacija_medija$obrazovanje <- factor(
  populacija_medija$obrazovanje,
  levels = obrazovanje_razine
)

rows <- list()
add_result <- function(chapter, dataset, file, question, metric, value) {
  rows[[length(rows) + 1L]] <<- data.frame(
    chapter = chapter,
    dataset = dataset,
    file = file,
    question = question,
    metric = metric,
    value = as.numeric(value),
    stringsAsFactors = FALSE,
    check.names = FALSE
  )
}

q_anketa <- "Koliko vremena ljudi provode na mrežama i kako to ide uz povjerenje?"
q_populacija <- "Kako se povjerenje u medije mijenja s dobi i izvorom vijesti?"
q_evidence12 <- "Koliki je zajednički učinak laboratorijskih replikacija RRR-a?"

# Poglavlje 6: povezanost dviju numeričkih varijabli.
r6 <- cor(
  anketa_mreze$minute_dnevno,
  anketa_mreze$povjerenje,
  use = "complete.obs"
)
add_result(6, "anketa_mreze", "data/anketa-mreze.csv", q_anketa, "pearson_r", r6)

# Poglavlje 7: uvjetna vjerojatnost izvora vijesti u mlađoj dobnoj skupini.
mladi <- populacija_medija$dob <= 29
p7 <- mean(populacija_medija$izvor_vijesti[mladi] == "društvene mreže")
add_result(7, "populacija_medija", "data/populacija-medija.csv", q_populacija, "p_mreze_dob_le_29", p7)

# Poglavlje 8: stvarna standardna pogreška sredine za uzorke veličine 100.
se8 <- sqrt(mean((populacija_medija$povjerenje_medijima - mean(populacija_medija$povjerenje_medijima))^2)) / sqrt(100)
add_result(8, "populacija_medija", "data/populacija-medija.csv", q_populacija, "se_povjerenje_n_100", se8)

# Poglavlje 9: jedan ponovljiv interval pouzdanosti iz uzorka.
set.seed(909)
uzorak9 <- populacija_medija[sample.int(nrow(populacija_medija), 200L), , drop = FALSE]
mean9 <- mean(uzorak9$povjerenje_medijima)
se9 <- stats::sd(uzorak9$povjerenje_medijima) / sqrt(nrow(uzorak9))
add_result(9, "populacija_medija", "data/populacija-medija.csv", q_populacija, "mean_povjerenje", mean9)
add_result(9, "populacija_medija", "data/populacija-medija.csv", q_populacija, "ci95_lower", mean9 - 1.96 * se9)
add_result(9, "populacija_medija", "data/populacija-medija.csv", q_populacija, "ci95_upper", mean9 + 1.96 * se9)

# Poglavlje 10: permutacijska provjera razlike portala i tiska.
dvije10 <- populacija_medija[populacija_medija$izvor_vijesti %in% c("portal", "tisak"), , drop = FALSE]
set.seed(1011)
dvije10 <- dvije10[sample.int(nrow(dvije10), 300L), , drop = FALSE]
diff10 <- with(
  dvije10,
  mean(povjerenje_medijima[izvor_vijesti == "portal"]) - mean(povjerenje_medijima[izvor_vijesti == "tisak"])
)
set.seed(1012)
permuted10 <- replicate(4000L, {
  shuffled <- sample(dvije10$izvor_vijesti)
  mean(dvije10$povjerenje_medijima[shuffled == "portal"]) -
    mean(dvije10$povjerenje_medijima[shuffled == "tisak"])
})
p10 <- (sum(abs(permuted10) >= abs(diff10)) + 1) / (length(permuted10) + 1)
add_result(10, "populacija_medija", "data/populacija-medija.csv", q_populacija, "mean_difference_portal_minus_tisak", diff10)
add_result(10, "populacija_medija", "data/populacija-medija.csv", q_populacija, "permutation_p_two_sided", p10)

# Poglavlje 11: standardizirana razlika istih dviju skupina u cijeloj populaciji.
portal11 <- populacija_medija$povjerenje_medijima[populacija_medija$izvor_vijesti == "portal"]
tisak11 <- populacija_medija$povjerenje_medijima[populacija_medija$izvor_vijesti == "tisak"]
pooled11 <- sqrt(
  ((length(portal11) - 1) * stats::var(portal11) +
     (length(tisak11) - 1) * stats::var(tisak11)) /
    (length(portal11) + length(tisak11) - 2)
)
d11 <- (mean(portal11) - mean(tisak11)) / pooled11
add_result(11, "populacija_medija", "data/populacija-medija.csv", q_populacija, "cohen_d_portal_minus_tisak", d11)

# Poglavlje 12: obje ponderirane grane provjerenoga dokaznog paketa.
z95 <- stats::qnorm(0.975)
w12_raw <- 1 / evidence12$raw_se^2
pooled12_raw <- sum(w12_raw * evidence12$raw_mean_difference) / sum(w12_raw)
se12_raw <- sqrt(1 / sum(w12_raw))
add_result(12, "rrr_lab_effects", "notes/reports/p3-evidence12-rrr-lab-effects.csv", q_evidence12, "raw_fixed_effect_estimate", pooled12_raw)
add_result(12, "rrr_lab_effects", "notes/reports/p3-evidence12-rrr-lab-effects.csv", q_evidence12, "raw_ci95_lower", pooled12_raw - z95 * se12_raw)
add_result(12, "rrr_lab_effects", "notes/reports/p3-evidence12-rrr-lab-effects.csv", q_evidence12, "raw_ci95_upper", pooled12_raw + z95 * se12_raw)

w12_d <- 1 / evidence12$d_se^2
pooled12_d <- sum(w12_d * evidence12$cohen_d) / sum(w12_d)
se12_d <- sqrt(1 / sum(w12_d))
add_result(12, "rrr_lab_effects", "notes/reports/p3-evidence12-rrr-lab-effects.csv", q_evidence12, "standardized_fixed_effect_estimate", pooled12_d)
add_result(12, "rrr_lab_effects", "notes/reports/p3-evidence12-rrr-lab-effects.csv", q_evidence12, "standardized_ci95_lower", pooled12_d - z95 * se12_d)
add_result(12, "rrr_lab_effects", "notes/reports/p3-evidence12-rrr-lab-effects.csv", q_evidence12, "standardized_ci95_upper", pooled12_d + z95 * se12_d)

# Poglavlje 13: hi-kvadrat test tablice obrazovanja i izvora vijesti.
set.seed(1313)
uzorak13 <- populacija_medija[sample.int(nrow(populacija_medija), 800L), , drop = FALSE]
tab13 <- table(uzorak13$obrazovanje, uzorak13$izvor_vijesti)
chi13 <- suppressWarnings(stats::chisq.test(tab13, correct = FALSE))
v13 <- sqrt(unname(chi13$statistic) / (sum(tab13) * min(nrow(tab13) - 1L, ncol(tab13) - 1L)))
add_result(13, "populacija_medija", "data/populacija-medija.csv", q_populacija, "chi_squared", unname(chi13$statistic))
add_result(13, "populacija_medija", "data/populacija-medija.csv", q_populacija, "cramers_v", v13)

# Poglavlje 14: Welchov interval razlike TV-a i društvenih mreža.
dvije14 <- populacija_medija[populacija_medija$izvor_vijesti %in% c("TV", "društvene mreže"), , drop = FALSE]
set.seed(1414)
dvije14 <- dvije14[sample.int(nrow(dvije14), 120L), , drop = FALSE]
tv14 <- dvije14$povjerenje_medijima[dvije14$izvor_vijesti == "TV"]
mreze14 <- dvije14$povjerenje_medijima[dvije14$izvor_vijesti == "društvene mreže"]
test14 <- stats::t.test(tv14, mreze14)
add_result(14, "populacija_medija", "data/populacija-medija.csv", q_populacija, "mean_difference_tv_minus_mreze", mean(tv14) - mean(mreze14))
add_result(14, "populacija_medija", "data/populacija-medija.csv", q_populacija, "welch_ci95_lower", unname(test14$conf.int[[1L]]))
add_result(14, "populacija_medija", "data/populacija-medija.csv", q_populacija, "welch_ci95_upper", unname(test14$conf.int[[2L]]))

# Poglavlje 15: jednofaktorska ANOVA i eta-kvadrat.
set.seed(1515)
uzorak15 <- populacija_medija[sample.int(nrow(populacija_medija), 300L), , drop = FALSE]
fit15 <- stats::aov(povjerenje_medijima ~ izvor_vijesti, data = uzorak15)
anova15 <- summary(fit15)[[1L]]
eta15 <- anova15["izvor_vijesti", "Sum Sq"] / sum(anova15[, "Sum Sq"])
add_result(15, "populacija_medija", "data/populacija-medija.csv", q_populacija, "anova_f", anova15["izvor_vijesti", "F value"])
add_result(15, "populacija_medija", "data/populacija-medija.csv", q_populacija, "eta_squared", eta15)

# Poglavlje 16: višestruka regresija na cijeloj sintetičkoj populaciji.
fit16 <- stats::lm(povjerenje_medijima ~ dob + izvor_vijesti, data = populacija_medija)
coef16 <- stats::coef(fit16)
add_result(16, "populacija_medija", "data/populacija-medija.csv", q_populacija, "slope_dob", unname(coef16[["dob"]]))
add_result(16, "populacija_medija", "data/populacija-medija.csv", q_populacija, "coefficient_drustvene_mreze", unname(coef16[["izvor_vijestidruštvene mreže"]]))
add_result(16, "populacija_medija", "data/populacija-medija.csv", q_populacija, "adjusted_r_squared", summary(fit16)$adj.r.squared)

results <- do.call(rbind, rows)

expected <- c(
  "6:pearson_r" = 0.179849462681741,
  "7:p_mreze_dob_le_29" = 0.458576051779935,
  "8:se_povjerenje_n_100" = 0.198409986684138,
  "9:mean_povjerenje" = 4.815,
  "9:ci95_lower" = 4.52485748398763,
  "9:ci95_upper" = 5.10514251601237,
  "10:mean_difference_portal_minus_tisak" = -0.640938989801461,
  "10:permutation_p_two_sided" = 0.0117470632341915,
  "11:cohen_d_portal_minus_tisak" = -0.388897632206793,
  "12:raw_fixed_effect_estimate" = 0.026765925060349,
  "12:raw_ci95_lower" = -0.107693099301188,
  "12:raw_ci95_upper" = 0.161224949421886,
  "12:standardized_fixed_effect_estimate" = 0.0141509286792652,
  "12:standardized_ci95_lower" = -0.0761906831634761,
  "12:standardized_ci95_upper" = 0.104492540522006,
  "13:chi_squared" = 6.03709187333708,
  "13:cramers_v" = 0.0501543113523033,
  "14:mean_difference_tv_minus_mreze" = 1.18571428571429,
  "14:welch_ci95_lower" = 0.446686471420565,
  "14:welch_ci95_upper" = 1.92474210000801,
  "15:anova_f" = 8.38181295740898,
  "15:eta_squared" = 0.102053183237968,
  "16:slope_dob" = 0.0268851731781231,
  "16:coefficient_drustvene_mreze" = -0.533533786572297,
  "16:adjusted_r_squared" = 0.122189733503462
)
result_keys <- paste(results$chapter, results$metric, sep = ":")
if (!identical(result_keys, names(expected))) stop("Promijenio se popis provjernih rezultata.")
if (any(abs(results$value - unname(expected)) > 1e-12)) {
  stop("Najmanje se jedan provjerni rezultat razišao s očekivanom vrijednošću.")
}

if (nzchar(text_candidate)) {
  if (!nzchar(python_bin)) stop("Python nije pronađen; zadajte --python.")
  candidate_path <- normalizePath(text_candidate, mustWork = TRUE)
  text_output <- tempfile(fileext = ".csv")
  on.exit(unlink(text_output), add = TRUE)
  builder <- root_file("scripts", "build-text-package.py")
  builder_output <- system2(
    python_bin,
    c(
      shQuote(builder),
      "--candidate", shQuote(candidate_path),
      "--output", shQuote(text_output),
      "--write"
    ),
    stdout = TRUE,
    stderr = TRUE
  )
  builder_status <- attr(builder_output, "status")
  if (!is.null(builder_status) && builder_status != 0L) {
    stop("Tekstna transformacija nije uspjela:\n", paste(builder_output, collapse = "\n"))
  }
  expected_sha <- "0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef"
  if (!any(grepl(expected_sha, builder_output, fixed = TRUE))) {
    stop("Graditelj nije prijavio očekivani SHA-256 izlaza.")
  }
  assert_md5(text_output, "55b1c4263009ab783911f094907312d9")
  add_result(
    "A-tekst",
    "parlasent_hr",
    "data/parlament_oznake.csv",
    "Kako se ton parlamentarnih iskaza razlikuje s obzirom na stranačku pripadnost?",
    "prepared_rows",
    nrow(read_book_csv(text_output))
  )
  results <- do.call(rbind, rows)
}

if (nzchar(output_path)) {
  dir.create(dirname(output_path), recursive = TRUE, showWarnings = FALSE)
  write.csv(results, output_path, row.names = FALSE, fileEncoding = "UTF-8")
} else {
  print(results, row.names = FALSE, digits = 10)
}

cat(
  "APPENDIX_A_ROUTE_OK",
  "chapters=6-16",
  paste0("checks=", nrow(results)),
  if (nzchar(text_candidate)) "text_transform=verified" else "text_transform=not_requested",
  "\n"
)
