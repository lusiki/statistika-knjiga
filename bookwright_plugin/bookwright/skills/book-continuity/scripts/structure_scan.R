#!/usr/bin/env Rscript

# structure_scan.R - count structural elements and expose empty placeholders.
# Usage:
#   Rscript structure_scan.R                       # all chapters
#   Rscript structure_scan.R chapters/08-uzorkovanje.qmd
#   Rscript structure_scan.R "chapters/*.qmd"     # portable quoted sweep
#
# Counts conceptual figures rather than format twins, checks the four distinct
# exercise tiers, and distinguishes an element that merely has an opener from
# one with authored (non-comment) content.

expand_inputs <- function(args) {
  if (length(args) == 0) args <- file.path("chapters", "*.qmd")
  out <- character()
  for (arg in args) {
    hits <- Sys.glob(arg)
    if (length(hits) == 0 && file.exists(arg)) hits <- arg
    if (length(hits) == 0) stop(paste("No files matched:", arg))
    out <- c(out, hits)
  }
  out <- unique(out[grepl("\\.qmd$", out, ignore.case = TRUE)])
  if (length(out) == 0) stop("No .qmd files to scan.")
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

extract_fig_label <- function(s) {
  m <- regexec("^(?:#|//)\\|\\s*label\\s*:\\s*(fig-[A-Za-z0-9_-]+)", trimws(s), perl = TRUE)
  hit <- regmatches(trimws(s), m)[[1]]
  if (length(hit) < 2) "" else hit[[2]]
}

canonical_id <- function(id) {
  id <- tolower(sub("^#", "", id))
  sub("-(?:print|static|interactive|html|pdf|docx)$", "", id, perl = TRUE)
}

heading_text <- function(s) {
  value <- sub("^\\s*#{1,6}\\s+", "", s, perl = TRUE)
  trimws(sub("\\s*\\{[^{}]*\\}\\s*$", "", value, perl = TRUE))
}

parse_file <- function(path) {
  raw <- readLines(path, warn = FALSE, encoding = "UTF-8")
  lines <- strip_html_comments(raw)
  n <- length(lines)

  records <- list()
  div_stack <- integer()
  figures <- list()
  exercise_heads <- character()
  in_yaml <- FALSE
  in_code <- FALSE
  code_token <- ""
  code_start <- 0L
  code_label <- ""
  code_placeholder <- FALSE

  mark_div_content <- function() {
    if (length(div_stack) == 0) return()
    for (idx in div_stack) records[[idx]]$content <<- TRUE
  }
  add_figure <- function(id, line, placeholder = FALSE, kind = "source") {
    figures[[length(figures) + 1L]] <<- list(
      id = id,
      canonical = canonical_id(id),
      line = line,
      placeholder = placeholder,
      kind = kind
    )
  }

  for (i in seq_len(n)) {
    t <- trimws(lines[[i]])
    if (i == 1L && grepl("^---$", t)) {
      in_yaml <- TRUE
      next
    }
    if (in_yaml) {
      if (grepl("^(---|\\.\\.\\.)$", t)) in_yaml <- FALSE
      next
    }

    token <- fence_token(t)
    if (!in_code && nzchar(token)) {
      in_code <- TRUE
      code_token <- token
      code_start <- i
      code_label <- ""
      code_placeholder <- FALSE
      m <- regexec("\\{[^}]*\\b(fig-[A-Za-z0-9_-]+)\\b", t, perl = TRUE)
      hit <- regmatches(t, m)[[1]]
      if (length(hit) >= 2) code_label <- hit[[2]]
      next
    }
    if (in_code) {
      if (is_fence_close(t, code_token)) {
        if (nzchar(code_label)) add_figure(code_label, code_start, code_placeholder, "chunk")
        in_code <- FALSE
        code_token <- ""
        next
      }
      label <- extract_fig_label(t)
      if (nzchar(label)) code_label <- label
      if (grepl("\\bTODO\\b|još nije izrađen|placeholder", t, ignore.case = TRUE, perl = TRUE)) {
        code_placeholder <- TRUE
      }
      if (nzchar(t) && !grepl("^(?:#|//)\\|", t, perl = TRUE)) mark_div_content()
      next
    }

    if (grepl("^:::+\\s*\\{", t)) {
      attrs <- t
      records[[length(records) + 1L]] <- list(
        line = i,
        attrs = attrs,
        content = FALSE
      )
      idx <- length(records)
      if (grepl("#fig-[A-Za-z0-9_-]+", attrs)) {
        id <- sub("^#", "", regmatches(attrs, regexpr("#fig-[A-Za-z0-9_-]+", attrs)))
        add_figure(id, i, FALSE, "div")
      }
      div_stack <- c(div_stack, idx)
      next
    }
    if (grepl("^:::+\\s*$", t)) {
      if (length(div_stack)) div_stack <- head(div_stack, -1L)
      next
    }

    if (grepl("^!\\[", t)) {
      m <- regmatches(t, regexpr("#fig-[A-Za-z0-9_-]+", t))
      id <- if (length(m)) sub("^#", "", m) else sprintf("image-line-%d", i)
      add_figure(id, i, grepl("\\bTODO\\b|placeholder", t, ignore.case = TRUE), "image")
    }
    if (grepl("^###\\s+", t)) exercise_heads <- c(exercise_heads, heading_text(t))
    if (nzchar(t)) mark_div_content()
  }

  list(lines = lines, records = records, figures = figures, exercises = exercise_heads)
}

format_element <- function(n, empty) {
  if (n == 0L) return("0")
  if (empty == 0L) return(as.character(n))
  sprintf("%d(empty %d)", n, empty)
}

count_file <- function(path) {
  if (!file.exists(path)) stop(paste("File not found:", path))
  parsed <- parse_file(path)
  records <- parsed$records

  matching <- function(pattern) {
    which(vapply(records, function(x) grepl(pattern, x$attrs, perl = TRUE), logical(1)))
  }
  empty_count <- function(ix) {
    if (length(ix) == 0) return(0L)
    sum(!vapply(records[ix], `[[`, logical(1), "content"))
  }

  vin_idx <- matching("\\.callout-vinjeta\\b")
  def_idx <- matching("#def-[A-Za-z0-9_-]+")
  wild_idx <- matching("\\.callout-divljina\\b")
  model_idx <- matching("\\.callout-model\\b")
  error_idx <- matching("\\.callout-greska\\b")
  ai_idx <- c(model_idx, error_idx)

  figures <- parsed$figures
  if (length(figures)) {
    groups <- split(seq_along(figures), vapply(figures, `[[`, character(1), "canonical"))
    fig_n <- length(groups)
    placeholder_n <- sum(vapply(groups, function(ix) {
      any(vapply(figures[ix], `[[`, logical(1), "placeholder"))
    }, logical(1)))
    twin_n <- sum(lengths(groups) >= 2L)
  } else {
    fig_n <- placeholder_n <- twin_n <- 0L
  }

  tiers <- c("Konceptualni", "Računski", "Kritički", "Revizija modela")
  tier_present <- vapply(tiers, function(x) any(parsed$exercises == x), logical(1))

  vinjeta <- if (length(vin_idx)) {
    if (empty_count(vin_idx)) "yes(empty)" else "yes"
  } else {
    "NO"
  }
  fig_text <- sprintf("%d[placeholder %d; twins %d/%d]",
                      fig_n, placeholder_n, twin_n, fig_n)

  cat(sprintf(
    "%-34s vinjeta %-10s def %-10s fig %-29s divljina %-10s ai %-10s zadaci %d/4\n",
    basename(path),
    vinjeta,
    format_element(length(def_idx), empty_count(def_idx)),
    fig_text,
    format_element(length(wild_idx), empty_count(wild_idx)),
    format_element(length(ai_idx), empty_count(ai_idx)),
    sum(tier_present)
  ))
  invisible(list(
    figures = fig_n,
    placeholder_figures = placeholder_n,
    complete_twins = twin_n,
    exercise_tiers = sum(tier_present)
  ))
}

paths <- expand_inputs(commandArgs(trailingOnly = TRUE))
for (p in paths) count_file(p)
