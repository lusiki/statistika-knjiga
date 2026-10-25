# Verify the recurring-media lineage against the live chapter calculations.
# Run with bookwright_plugin/bookwright/scripts/run_rscript.py.
suppressPackageStartupMessages({library(dplyr); library(tidyr)})
source("R/podaci-nastavni.R", encoding = "UTF-8")
source("R/theme_book.R", encoding = "UTF-8")

chapter_values <- function(path, label) {
  lines <- readLines(path, encoding = "UTF-8", warn = FALSE)
  start <- which(lines == paste0("#| label: ", label))
  stopifnot(length(start) == 1L)
  finish <- which(seq_along(lines) > start & lines == "```")[[1]]
  eval(parse(text = lines[(start + 1L):(finish - 1L)]), envir = .GlobalEnv)
}
chapter_values("chapters/13-kategoricki-podaci.qmd", "s13-vrijednosti")
chapter_values("chapters/14-dvije-grupe.qmd", "s14-vrijednosti")
chapter_values("chapters/15-vise-grupa.qmd", "s15-vrijednosti")
chapter_values("chapters/16-regresija.qmd", "s16-vrijednosti")

catalogue <- yaml::read_yaml("data/katalog.yml")
variants <- unlist(lapply(catalogue$packages, function(p) p$teaching_variants), recursive = FALSE)
ids <- vapply(variants, function(v) v$id, character(1))
stopifnot(!anyDuplicated(ids))
observed <- list(
  "anketa-300" = nrow(anketa_mreze), "c18-anketa-300" = nrow(anketa_mreze),
  "mediji-50000" = nrow(populacija_medija), "c13-800" = nrow(s13_uzorak),
  "c13-digitalni" = sum(s13_spojena), "c14-120" = nrow(dvije_skupine),
  "c14-parovi-60" = length(s14_prije), "c15-300" = nrow(pet_izvora),
  "c16-populacija" = nrow(populacija_medija), "c16-dvije" = nrow(s16_dvije),
  "c16-pet" = nrow(s16_pet), "c16-ucenje" = nrow(s16_ucenje),
  "c16-provjera" = nrow(s16_provjera)
)
stopifnot(setequal(ids, names(observed)))
for (variant in variants) {
  stopifnot(file.exists(variant$source), observed[[variant$id]] == variant$rows)
  if (!is.null(variant$parent)) stopifnot(variant$parent %in% ids)
}
stopifnot(identical(s16_dvije, dvije_skupine), identical(s16_pet, pet_izvora))
stopifnot(sum(s13_tablica) == sum(s13_spojena),
          identical(unname(rowSums(s13_tablica)), unname(rowSums(s13_spojena))),
          all(s13_spojena[, "digitalni"] ==
              s13_tablica[, "portal"] + s13_tablica[, "društvene mreže"]))
stopifnot(length(s14_prije) == length(s14_poslije),
          identical(s14_razlike, s14_poslije - s14_prije))
stopifnot("osoba" %in% names(s16_ucenje), "osoba" %in% names(s16_provjera),
          length(s16_ucenje$osoba) == 150L, length(s16_provjera$osoba) == 2000L,
          !any(s16_ucenje$osoba %in% s16_provjera$osoba))
stopifnot(s13_test_spojena$p.value < .001)
stopifnot(abs(s13$razlika_digitalni - 56.37526) < .00001,
          all(abs(s13$ci_digitalni - c(47.42072, 65.32979)) < .00001))
cat(sprintf("TEACHING_VARIANTS_OK variants=%d same_people=2 recoding=1 paired=1\n", length(variants)))
