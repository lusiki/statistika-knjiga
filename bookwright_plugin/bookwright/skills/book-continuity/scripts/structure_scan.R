#!/usr/bin/env Rscript

# structure_scan.R - count the structural elements of each chapter.
# Usage: Rscript structure_scan.R chapters/*.qmd
# Prints, per chapter: vignette present, count of definitions, figures, the
# callout-divljina box, the two AI boxes (callout-model + callout-greska), and
# how many of the four exercise tiers are present. It only counts;
# book-continuity reads conventions.json and compares the counts to the bands.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) stop("Provide one or more .qmd paths, e.g. Rscript structure_scan.R chapters/*.qmd")

# This book opens each chapter with a .callout-vinjeta box, not a heading.
div_re <- function(cls) paste0("^:::+\\s*\\{[^}]*\\.", cls)

count_file <- function(path) {
  if (!file.exists(path)) { cat(sprintf("skip, not found  %s\n", path)); return(invisible()) }
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  n <- length(lines)

  vinjeta  <- any(grepl(div_re("callout-vinjeta"), lines))
  # Definitions use the {#def-} div convention (::: {#def-standardna-pogreska}).
  defs     <- sum(grepl("^:::+\\s*\\{[^}]*#def-", lines))
  divljina <- sum(grepl(div_re("callout-divljina"), lines))
  ai       <- sum(grepl(div_re("callout-model"), lines)) +
              sum(grepl(div_re("callout-greska"), lines))
  # Four exercise tiers, matched on their headings.
  zadaci   <- sum(grepl(paste0("^#+\\s*(Konceptualni|Računski|Kritički|",
                               "Revizija modela)"), lines))

  figs <- 0L
  in_code <- FALSE; code_is_fig <- FALSE; in_yaml <- FALSE
  for (i in seq_len(n)) {
    t <- trimws(lines[[i]])
    if (i == 1 && grepl("^---$", t)) { in_yaml <- TRUE; next }
    if (in_yaml) { if (grepl("^---$", t)) in_yaml <- FALSE; next }
    if (grepl("^(```|~~~)", t)) {
      if (!in_code) { in_code <- TRUE; code_is_fig <- FALSE }
      else { if (code_is_fig) figs <- figs + 1L; in_code <- FALSE }
      next
    }
    # Detect OJS chart blocks via //| label: fig-* as well as R chunk fig labels
    if (in_code) {
      if (grepl("^(#|//)\\|\\s*label:\\s*fig-", t) ||
          (grepl("^(#|//)\\|", t) && grepl("fig-[A-Za-z0-9_-]+", t))) code_is_fig <- TRUE
      next
    }
    if (grepl("^:::+\\s*\\{[^}]*#fig-", t)) { figs <- figs + 1L; next }
    if (grepl("^!\\[", t)) { figs <- figs + 1L; next }
  }

  cat(sprintf("%-34s vinjeta %-3s  def %d  fig %d  divljina %d  ai %d  zadaci %d/4\n",
              basename(path), if (vinjeta) "yes" else "NO",
              defs, figs, divljina, ai, zadaci))
}

for (p in args) count_file(p)
