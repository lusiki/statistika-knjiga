#!/usr/bin/env Rscript

# style_lint.R - flag STYLE.md hard-rule candidates in a Quarto .qmd chapter.
# Usage:
#   Rscript style_lint.R chapters/01-uloga-drzave.qmd
# It ignores YAML frontmatter, fenced code blocks, inline code, and callout
# fences, then reports prose that likely breaks a STYLE.md rule. Every hit is a
# candidate for you to restructure by hand, never an automatic edit.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) {
  stop("Provide a path to a .qmd file, e.g. Rscript style_lint.R chapters/00-uvod.qmd")
}
path <- args[[1]]
if (!file.exists(path)) stop(paste("File not found:", path))

lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
n <- length(lines)

in_yaml <- FALSE
in_code <- FALSE
is_prose <- logical(n)
yaml_lines <- integer(0)
fence <- "^\\s*(```|~~~)"

for (i in seq_len(n)) {
  ln <- lines[[i]]
  if (i == 1 && grepl("^---\\s*$", ln)) { in_yaml <- TRUE; next }
  if (in_yaml) {
    yaml_lines <- c(yaml_lines, i)
    if (grepl("^---\\s*$", ln)) in_yaml <- FALSE
    next
  }
  if (grepl(fence, ln)) { in_code <- !in_code; next }
  if (in_code) next
  if (grepl("^\\s*:::", ln)) next   # callout or div fence, structural not prose
  is_prose[[i]] <- TRUE
}

strip_inline <- function(s) gsub("`[^`]*`", "", s)

report <- list()
add <- function(line_no, rule, text) {
  report[[length(report) + 1]] <<- data.frame(
    line = line_no, rule = rule, text = trimws(text), stringsAsFactors = FALSE
  )
}

colon_rx  <- "(?<!:):(?!//)"
emdash_rx <- "\\S\\s*\u2014\\s*\\S"
openers <- c(
  "Glavna poruka", "U ovom poglavlju", "U ovom dijelu",
  "Kako je knjiga organizirana", "Kako je organizirano",
  "Drugim rije\u010dima", "Naime,", "To\u010dnije,", "Ukratko,",
  "Jednostavnije re\u010deno"
)
openers_rx <- paste0("(", paste(openers, collapse = "|"), ")")

for (i in seq_len(n)) {
  if (!is_prose[[i]]) next
  raw <- lines[[i]]
  s <- strip_inline(raw)
  if (grepl(colon_rx,  s, perl = TRUE)) add(i, "colon in prose", raw)
  if (grepl(emdash_rx, s, perl = TRUE)) add(i, "mid-sentence em dash", raw)
  if (grepl(openers_rx, s, perl = TRUE)) add(i, "mechanical opener / restatement", raw)
}

for (i in yaml_lines) {
  ln <- lines[[i]]
  if (grepl("^\\s*title\\s*:", ln)) {
    val <- regmatches(ln, regexpr('"[^"]*"', ln))
    if (length(val) == 1 && grepl(":", val)) add(i, "colon in chapter title (use em dash)", ln)
  }
}

cat(sprintf("STYLE.md lint for %s\n", path))
cat(strrep("=", 64), "\n", sep = "")
if (length(report) == 0) {
  cat("No candidate violations found. Still read the chapter top to bottom.\n")
} else {
  df <- do.call(rbind, report)
  df <- df[order(df$line), ]
  for (k in seq_len(nrow(df))) {
    cat(sprintf("L%-5d  %-32s  %s\n", df$line[k], df$rule[k], df$text[k]))
  }
  cat("\n", nrow(df), " candidate(s). Each is for you to restructure, not an auto-fix.\n", sep = "")
}
