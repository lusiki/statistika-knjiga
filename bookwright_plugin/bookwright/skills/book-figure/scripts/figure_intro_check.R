#!/usr/bin/env Rscript

# figure_intro_check.R - flag conceptual figures without a prose introduction.
# Usage:
#   Rscript figure_intro_check.R chapters/08-uzorkovanje.qmd
#   Rscript figure_intro_check.R "chapters/*.qmd"
#   Rscript figure_intro_check.R                     # defaults to all chapters
#
# Wildcards are expanded by the script for PowerShell/POSIX parity. HTML
# comments are ignored. Quarto #| and OJS //| figure labels are recognised.
# HTML/PDF/DOCX variants whose labels differ only by a format suffix count as
# one conceptual figure and share the paragraph before their format wrapper.

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
  if (length(out) == 0) stop("No .qmd files to check.")
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
  # Require a label option, rather than accepting fig- in a caption or comment.
  m <- regexec("^(?:#|//)\\|\\s*label\\s*:\\s*(fig-[A-Za-z0-9_-]+)", trimws(s), perl = TRUE)
  hit <- regmatches(trimws(s), m)[[1]]
  if (length(hit) < 2) "" else hit[[2]]
}

canonical_id <- function(id) {
  id <- tolower(sub("^#", "", id))
  sub("-(?:print|static|interactive|html|pdf|docx)$", "", id, perl = TRUE)
}

is_transparent_wrapper <- function(attrs) {
  grepl("\\.(?:content-visible|content-hidden|widget-frame)\\b", attrs, perl = TRUE)
}

is_prose_line <- function(s) {
  t <- trimws(s)
  if (!nzchar(t)) return(FALSE)
  if (grepl("^#{1,6}\\s+", t)) return(FALSE)
  if (grepl("^:::", t)) return(FALSE)
  if (grepl("^(`{3,}|~{3,})", t)) return(FALSE)
  if (grepl("^[-*+]\\s+|^[0-9]+[.)]\\s+", t, perl = TRUE)) return(FALSE)
  if (grepl("^>", t)) return(FALSE)
  if (grepl("^\\|", t)) return(FALSE)
  if (grepl("^\\s*:\\s+.*\\{#tbl-", t)) return(FALSE)
  if (grepl("^!\\[", t)) return(FALSE)
  if (grepl("^\\$\\$|^\\\\\\[|^\\\\\\]", t)) return(FALSE)
  if (grepl("^</?[A-Za-z][^>]*>\\s*$", t)) return(FALSE)
  if (grepl("^\\{[^{}]*\\}\\s*$", t)) return(FALSE)
  TRUE
}

previous_block_kind <- function(lines, before_line) {
  j <- before_line - 1L
  while (j >= 1L && !nzchar(trimws(lines[[j]]))) j <- j - 1L
  if (j < 1L) return(list(ok = FALSE, reason = "nothing before the figure"))
  prev <- trimws(lines[[j]])
  if (is_prose_line(prev)) return(list(ok = TRUE, reason = ""))
  kind <- if (grepl("^#", prev)) {
    "a heading"
  } else if (grepl("^:::", prev)) {
    "a callout or div fence"
  } else if (grepl("^(`{3,}|~{3,})", prev)) {
    "a code fence"
  } else if (grepl("^[-*+]\\s+|^[0-9]+[.)]\\s+", prev, perl = TRUE)) {
    "a list"
  } else if (grepl("^!\\[", prev)) {
    "another figure"
  } else if (grepl("^\\||^\\s*:\\s+.*\\{#tbl-", prev)) {
    "a table"
  } else if (grepl("^\\$\\$|^\\\\\\[|^\\\\\\]", prev)) {
    "display math"
  } else {
    "not prose"
  }
  list(ok = FALSE, reason = paste("preceded by", kind))
}

check_file <- function(path) {
  if (!file.exists(path)) stop(paste("File not found:", path))
  raw <- readLines(path, warn = FALSE, encoding = "UTF-8")
  lines <- strip_html_comments(raw)
  n <- length(lines)

  in_yaml <- FALSE
  in_code <- FALSE
  code_token <- ""
  code_start <- 0L
  code_label <- ""
  code_wrapper <- 0L
  div_stack <- list()
  div_ranges <- list()
  anchors <- list()

  add_anchor <- function(line, id, effective_line, kind) {
    anchors[[length(anchors) + 1L]] <<- list(
      line = line,
      id = id,
      canonical = canonical_id(id),
      effective_line = effective_line,
      kind = kind
    )
  }

  wrapper_line <- function() {
    if (length(div_stack) == 0) return(0L)
    candidates <- vapply(
      div_stack,
      function(x) if (is_transparent_wrapper(x$attrs)) x$line else 0L,
      integer(1)
    )
    candidates <- candidates[candidates > 0L]
    if (length(candidates)) min(candidates) else 0L
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
      code_wrapper <- wrapper_line()
      # Support the older knitr ```{r fig-name, ...} form as well.
      m <- regexec("\\{[^}]*\\b(fig-[A-Za-z0-9_-]+)\\b", t, perl = TRUE)
      hit <- regmatches(t, m)[[1]]
      if (length(hit) >= 2) code_label <- hit[[2]]
      next
    }
    if (in_code) {
      if (is_fence_close(t, code_token)) {
        if (nzchar(code_label)) {
          effective <- if (code_wrapper > 0L) code_wrapper else code_start
          add_anchor(code_start, code_label, effective, "fig chunk")
        }
        in_code <- FALSE
        code_token <- ""
        next
      }
      label <- extract_fig_label(t)
      if (nzchar(label)) code_label <- label
      next
    }

    if (grepl("^:::+\\s*\\{", t)) {
      if (grepl("#fig-[A-Za-z0-9_-]+", t)) {
        m <- regmatches(t, regexpr("#fig-[A-Za-z0-9_-]+", t))
        effective <- wrapper_line()
        if (effective == 0L) effective <- i
        add_anchor(i, sub("^#", "", m), effective, "fig div")
      }
      div_stack[[length(div_stack) + 1L]] <- list(line = i, attrs = t)
      next
    }
    if (grepl("^:::+\\s*$", t)) {
      if (length(div_stack)) {
        closed <- div_stack[[length(div_stack)]]
        closed$end <- i
        div_ranges[[length(div_ranges) + 1L]] <- closed
        div_stack <- head(div_stack, -1L)
      }
      next
    }
    if (grepl("^!\\[", t)) {
      m <- regmatches(t, regexpr("#fig-[A-Za-z0-9_-]+", t))
      id <- if (length(m)) sub("^#", "", m) else sprintf("image-line-%d", i)
      effective <- wrapper_line()
      if (effective == 0L) effective <- i
      add_anchor(i, id, effective, "image")
    }
  }

  if (length(anchors) == 0) {
    cat(sprintf("%-45s no figures found\n", path))
    return(0L)
  }

  # A static PDF wrapper commonly follows an HTML wrapper containing the
  # interactive twin. Treat adjacent format wrappers as one source group, so
  # the shared introduction is sought before the first wrapper, not between
  # the two variants.
  cluster_start <- function(start) {
    effective <- start
    repeat {
      j <- effective - 1L
      while (j >= 1L && !nzchar(trimws(lines[[j]]))) j <- j - 1L
      if (j < 1L || length(div_ranges) == 0L) break
      prior <- which(vapply(
        div_ranges,
        function(x) is_transparent_wrapper(x$attrs) && identical(x$end, j),
        logical(1)
      ))
      if (length(prior) == 0L) break
      effective <- min(vapply(div_ranges[prior], `[[`, integer(1), "line"))
    }
    effective
  }
  for (i in seq_along(anchors)) {
    anchors[[i]]$effective_line <- cluster_start(anchors[[i]]$effective_line)
  }

  # One conceptual figure may have HTML/PDF/DOCX source variants. A figure div
  # and the labelled chunk it wraps also collapse under the same canonical id.
  groups <- split(seq_along(anchors), vapply(anchors, `[[`, character(1), "canonical"))
  conceptual <- lapply(groups, function(ix) {
    first <- ix[which.min(vapply(anchors[ix], `[[`, integer(1), "effective_line"))]
    list(
      anchor = anchors[[first]],
      variants = length(ix),
      line = min(vapply(anchors[ix], `[[`, integer(1), "effective_line"))
    )
  })

  cat(sprintf("== %s  (%d conceptual figure(s), %d source variant(s)) ==\n",
              path, length(conceptual), length(anchors)))
  flagged <- 0L
  for (item in conceptual) {
    check <- previous_block_kind(lines, item$line)
    if (!check$ok) {
      flagged <- flagged + 1L
      suffix <- if (item$variants > 1L) sprintf(" [%d format variants]", item$variants) else ""
      cat(sprintf("  L%-5d %-20s %s%s\n",
                  item$anchor$line, item$anchor$id, check$reason, suffix))
    }
  }
  if (flagged == 0L) cat("  all conceptual figures have a prose paragraph before them\n")
  else cat(sprintf("  %d conceptual figure(s) need an intro paragraph\n", flagged))
  flagged
}

paths <- expand_inputs(commandArgs(trailingOnly = TRUE))
total_figures_needing_intro <- 0L
for (p in paths) total_figures_needing_intro <- total_figures_needing_intro + check_file(p)
if (length(paths) > 1L) {
  cat(sprintf("\n%d conceptual figure(s) need an intro across %d file(s).\n",
              total_figures_needing_intro, length(paths)))
}
