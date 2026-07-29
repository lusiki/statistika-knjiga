#!/usr/bin/env Rscript

# style_lint.R - deterministic STYLE.md checks for Quarto chapter prose.
# Usage:
#   Rscript style_lint.R chapters/08-uzorkovanje.qmd
#   Rscript style_lint.R "chapters/*.qmd"
#
# Shell wildcards are expanded here, so the quoted sweep works in PowerShell as
# well as POSIX shells. The linter ignores YAML other than the chapter title,
# fenced code, inline code and math, URLs, Quarto attributes, and multiline HTML
# comments. It reports candidates; it never edits prose.

expand_inputs <- function(args) {
  if (length(args) == 0) {
    stop("Provide one or more .qmd paths, e.g. Rscript style_lint.R chapters/08-uzorkovanje.qmd")
  }
  out <- character()
  for (arg in args) {
    hits <- Sys.glob(arg)
    if (length(hits) == 0 && file.exists(arg)) hits <- arg
    if (length(hits) == 0) stop(paste("No files matched:", arg))
    out <- c(out, hits)
  }
  out <- unique(out[grepl("\\.qmd$", out, ignore.case = TRUE)])
  if (length(out) == 0) stop("No .qmd files to lint.")
  out
}

strip_html_comments <- function(lines) {
  clean <- character(length(lines))
  in_comment <- FALSE
  for (i in seq_along(lines)) {
    rest <- lines[[i]]
    kept <- ""
    repeat {
      if (in_comment) {
        end <- regexpr("-->", rest, fixed = TRUE)[1]
        if (end < 0) {
          rest <- ""
          break
        }
        rest <- substring(rest, end + 3L)
        in_comment <- FALSE
      } else {
        start <- regexpr("<!--", rest, fixed = TRUE)[1]
        if (start < 0) {
          kept <- paste0(kept, rest)
          break
        }
        if (start > 1) kept <- paste0(kept, substring(rest, 1L, start - 1L))
        rest <- substring(rest, start + 4L)
        in_comment <- TRUE
      }
      if (!nzchar(rest)) break
    }
    clean[[i]] <- kept
  }
  clean
}

fence_token <- function(s) {
  m <- regexec("^\\s*(`{3,}|~{3,})", s, perl = TRUE)
  hit <- regmatches(s, m)[[1]]
  if (length(hit) < 2) "" else hit[[2]]
}

is_fence_close <- function(s, token) {
  if (!nzchar(token)) return(FALSE)
  rx <- sprintf("^\\s*%s{%d,}\\s*$", substr(token, 1, 1), nchar(token))
  grepl(rx, s, perl = TRUE)
}

strip_inline_exemptions <- function(s) {
  # Syntax and content explicitly exempt from H1/H2.
  s <- gsub("`+[^`]*`+", "", s, perl = TRUE)
  s <- gsub("\\$\\$[^$]*\\$\\$", "", s, perl = TRUE)
  s <- gsub("(?<!\\$)\\$[^$\\n]+\\$(?!\\$)", "", s, perl = TRUE)
  s <- gsub("\\\\\\([^)]*\\\\\\)", "", s, perl = TRUE)
  s <- gsub("\\{[^{}]*\\}", "", s, perl = TRUE)
  s <- gsub("\\b[A-Za-z][A-Za-z0-9+.-]*://[^\\s)>]+", "", s, perl = TRUE)
  s <- gsub("\\b(?:mailto|doi):[^\\s)>]+", "", s, perl = TRUE, ignore.case = TRUE)
  s
}

heading_text <- function(s) {
  value <- sub("^\\s*#{1,6}\\s+", "", s, perl = TRUE)
  trimws(sub("\\s*\\{[^{}]*\\}\\s*$", "", value, perl = TRUE))
}

is_table_delimiter <- function(s) {
  grepl("^\\s*\\|?\\s*:?-{3,}:?\\s*(\\|\\s*:?-{3,}:?\\s*)+\\|?\\s*$", s, perl = TRUE)
}

lint_file <- function(path) {
  if (!file.exists(path)) stop(paste("File not found:", path))
  raw_lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  lines <- strip_html_comments(raw_lines)
  n <- length(lines)

  report <- list()
  add <- function(line_no, rule, text) {
    report[[length(report) + 1L]] <<- data.frame(
      line = line_no,
      rule = rule,
      text = trimws(text),
      stringsAsFactors = FALSE
    )
  }

  colon_rx <- "(?<!:):(?!//)"
  emdash_rx <- "\\S\\s*\u2014\\s*\\S"
  mechanical_rx <- paste0(
    "(",
    paste(
      c(
        "Glavna poruka",
        "U ovom poglavlju",
        "U ovom dijelu",
        "Kako je knjiga organizirana",
        "Kako je organizirano"
      ),
      collapse = "|"
    ),
    ")"
  )
  restatement_rx <- paste0(
    "(",
    paste(
      c(
        "Drugim riječima,",
        "Naime,",
        "Točnije,",
        "Ukratko,",
        "Jednostavnije rečeno,",
        "Štoviše,"
      ),
      collapse = "|"
    ),
    ")"
  )

  in_yaml <- FALSE
  yaml_finished <- FALSE
  in_code <- FALSE
  code_token <- ""
  in_display_math <- FALSE
  div_stack <- character()
  in_exercises <- FALSE
  in_try_block <- FALSE
  restatement_count <- 0L
  capstone <- grepl("^18-", basename(path))

  for (i in seq_len(n)) {
    raw <- raw_lines[[i]]
    s <- lines[[i]]
    t <- trimws(s)

    if (i == 1L && grepl("^---\\s*$", t)) {
      in_yaml <- TRUE
      next
    }
    if (in_yaml) {
      if (grepl("^(---|\\.\\.\\.)\\s*$", t)) {
        in_yaml <- FALSE
        yaml_finished <- TRUE
        next
      }
      if (grepl("^title\\s*:", t, ignore.case = TRUE)) {
        title <- trimws(sub("^title\\s*:\\s*", "", t, ignore.case = TRUE))
        title <- sub("^(['\"])(.*)\\1$", "\\2", title, perl = TRUE)
        if (grepl(":", title, fixed = TRUE)) {
          add(i, "H1/H6 colon in chapter title", raw)
        }
      }
      next
    }
    if (!yaml_finished && i == 1L) yaml_finished <- TRUE

    token <- fence_token(t)
    if (!in_code && nzchar(token)) {
      in_code <- TRUE
      code_token <- token
      next
    }
    if (in_code) {
      if (is_fence_close(t, code_token)) {
        in_code <- FALSE
        code_token <- ""
      }
      next
    }

    if (grepl("^\\s*\\$\\$\\s*$", s)) {
      in_display_math <- !in_display_math
      next
    }
    if (in_display_math) next

    if (!nzchar(t)) next

    if (grepl("^:::+\\s*\\{", t)) {
      div_stack <- c(div_stack, t)
      next
    }
    if (grepl("^:::+\\s*$", t)) {
      if (length(div_stack)) div_stack <- head(div_stack, -1L)
      next
    }

    if (grepl("^#{1,6}\\s+", t)) {
      h <- heading_text(t)
      level <- nchar(sub("^(#+).*$", "\\1", t))
      if (level == 2L) {
        in_exercises <- grepl("^Zadaci\\b", h)
        in_try_block <- FALSE
      }
      check <- strip_inline_exemptions(h)
      if (grepl(colon_rx, check, perl = TRUE)) add(i, "H1/H6 colon in heading", raw)
      if (grepl("^\\s*(?:[0-9]+|[IVXLC]+)[.)]\\s+", check, perl = TRUE)) {
        add(i, "H6 hard-coded heading number", raw)
      }
      next # an em dash is explicitly allowed in title position
    }

    if (grepl("^\\s*(---+|\\*\\*\\*+|___+)\\s*$", s)) next
    if (is_table_delimiter(s)) next
    if (grepl("^\\s*</?[A-Za-z][^>]*>\\s*$", s)) next

    check <- strip_inline_exemptions(s)
    # Quarto's leading table-caption colon is syntax, not rendered punctuation.
    if (grepl("^\\s*:\\s+", check)) check <- sub("^\\s*:\\s+", "", check)
    if (!nzchar(trimws(check))) next

    if (grepl("\\*\\*Što isprobati\\.\\*\\*", s)) in_try_block <- TRUE
    is_list <- grepl("^\\s*(?:[-*+]\\s+|[0-9]+[.)]\\s+)", check, perl = TRUE)
    in_error_callout <- any(grepl("\\.callout-greska\\b", div_stack))
    if (is_list && !(in_exercises || in_error_callout || in_try_block || capstone)) {
      add(i, "H4 list in running prose", raw)
    }

    if (grepl(colon_rx, check, perl = TRUE)) add(i, "H1 colon in prose", raw)
    if (grepl(emdash_rx, check, perl = TRUE)) add(i, "H2 mid-sentence em dash", raw)
    if (grepl(mechanical_rx, check, perl = TRUE)) add(i, "H3 mechanical transition", raw)

    matches <- gregexpr(restatement_rx, check, perl = TRUE)[[1]]
    occurrences <- if (matches[[1]] < 0) 0L else length(matches)
    if (occurrences > 0L) {
      for (k in seq_len(occurrences)) {
        restatement_count <- restatement_count + 1L
        if (restatement_count > 1L) {
          add(i, "H5 restatement budget exceeded", raw)
          break
        }
      }
    }
  }

  cat(sprintf("STYLE.md lint for %s\n", path))
  cat(strrep("=", 64), "\n", sep = "")
  if (length(report) == 0) {
    cat("No deterministic candidate violations found. Still read the chapter top to bottom.\n")
    return(0L)
  }

  df <- do.call(rbind, report)
  df <- unique(df[order(df$line, df$rule), , drop = FALSE])
  for (k in seq_len(nrow(df))) {
    cat(sprintf("L%-5d  %-34s  %s\n", df$line[k], df$rule[k], df$text[k]))
  }
  cat("\n", nrow(df), " candidate(s). Each is for you to restructure, not an auto-fix.\n", sep = "")
  nrow(df)
}

paths <- expand_inputs(commandArgs(trailingOnly = TRUE))
total <- 0L
for (p in paths) {
  if (length(paths) > 1L) cat("\n")
  total <- total + lint_file(p)
}
if (length(paths) > 1L) {
  cat(sprintf("\n%d candidate(s) across %d file(s).\n", total, length(paths)))
}
