#!/usr/bin/env Rscript

# figure_intro_check.R - flag figures that lack a prose paragraph immediately before them.
# Usage:
#   Rscript figure_intro_check.R chapters/03-distribucijska-funkcija.qmd
#   Rscript figure_intro_check.R chapters/*.qmd        # sweep the whole book
# A figure passes only when the nearest non blank source block above it is a prose
# paragraph. The caption (fig-cap) and the rendered Slika X.Y prefix are not the
# intro paragraph; this looks for explanatory prose preceding the figure.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) {
  stop("Provide one or more .qmd paths, e.g. Rscript figure_intro_check.R chapters/03-distribucijska-funkcija.qmd")
}

is_prose_line <- function(s) {
  t <- trimws(s)
  if (t == "") return(FALSE)
  if (grepl("^#", t)) return(FALSE)            # heading
  if (grepl("^:::", t)) return(FALSE)          # div or callout fence
  if (grepl("^(```|~~~)", t)) return(FALSE)    # code fence boundary
  if (grepl("^[-*+] ", t)) return(FALSE)       # bullet list
  if (grepl("^[0-9]+[.)] ", t)) return(FALSE)  # ordered list
  if (grepl("^>", t)) return(FALSE)            # blockquote
  if (grepl("^\\|", t)) return(FALSE)          # table row
  if (grepl("^!\\[", t)) return(FALSE)         # another image
  if (grepl("^#\\|", t)) return(FALSE)         # chunk option
  TRUE
}

check_file <- function(path) {
  if (!file.exists(path)) { cat(sprintf("skip, not found  %s\n", path)); return(invisible()) }
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  n <- length(lines)

  in_yaml <- FALSE
  in_code <- FALSE
  code_start <- 0L
  code_is_fig <- FALSE
  anchors <- list()

  for (i in seq_len(n)) {
    ln <- lines[[i]]
    t <- trimws(ln)
    if (i == 1 && grepl("^---$", t)) { in_yaml <- TRUE; next }
    if (in_yaml) { if (grepl("^---$", t)) in_yaml <- FALSE; next }

    if (grepl("^(```|~~~)", t)) {
      if (!in_code) { in_code <- TRUE; code_start <- i; code_is_fig <- FALSE }
      else {
        if (code_is_fig) anchors[[length(anchors) + 1]] <- list(line = code_start, id = "fig chunk")
        in_code <- FALSE
      }
      next
    }
    if (in_code) {
      m <- regmatches(t, regexpr("fig-[A-Za-z0-9_-]+", t))
      if (grepl("^#\\|", t) && length(m) == 1) code_is_fig <- TRUE
      next
    }

    if (grepl("^:::+\\s*\\{[^}]*#fig-", t)) {
      m <- regmatches(t, regexpr("#fig-[A-Za-z0-9_-]+", t))
      anchors[[length(anchors) + 1]] <- list(line = i, id = if (length(m)) m else "fig div")
      next
    }
    if (grepl("^!\\[", t)) {
      m <- regmatches(t, regexpr("#fig-[A-Za-z0-9_-]+", t))
      anchors[[length(anchors) + 1]] <- list(line = i, id = if (length(m)) m else "image")
      next
    }
  }

  if (length(anchors) == 0) { cat(sprintf("%-45s no figures found\n", path)); return(invisible()) }

  cat(sprintf("== %s  (%d figure(s)) ==\n", path, length(anchors)))
  flagged <- 0L
  for (a in anchors) {
    j <- a$line - 1L
    while (j >= 1 && trimws(lines[[j]]) == "") j <- j - 1L
    reason <- NA_character_
    if (j < 1) reason <- "nothing before the figure"
    else if (!is_prose_line(lines[[j]])) {
      prev <- trimws(lines[[j]])
      kind <- if (grepl("^#", prev)) "a heading"
        else if (grepl("^:::", prev)) "a callout or div fence"
        else if (grepl("^(```|~~~)", prev)) "a code fence"
        else if (grepl("^[-*+] |^[0-9]+[.)] ", prev)) "a list"
        else if (grepl("^!\\[", prev)) "another figure"
        else "not prose"
      reason <- paste("preceded by", kind)
    }
    if (!is.na(reason)) {
      flagged <- flagged + 1L
      cat(sprintf("  L%-5d %-16s %s\n", a$line, a$id, reason))
    }
  }
  if (flagged == 0L) cat("  all figures have a prose paragraph before them\n")
  else cat(sprintf("  %d figure(s) need an intro paragraph\n", flagged))
}

for (p in args) check_file(p)
