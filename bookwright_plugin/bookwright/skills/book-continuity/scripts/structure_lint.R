#!/usr/bin/env Rscript

# structure_lint.R - flag STYLE.md S7 section-rhythm candidates.
# Usage:
#   Rscript structure_lint.R
#   Rscript structure_lint.R chapters/08-uzorkovanje.qmd
#   Rscript structure_lint.R "chapters/*.qmd"
#
# The fixed book skeleton is not one-heading-per-part: Vinjeta and three recurring
# callouts are unheaded, while Sažetak, Pojmovi and Zadaci are separate ## blocks.
# This linter therefore assigns explicit roles instead of treating every ## as
# argumentative body prose. HTML TODO comments never contribute words or
# paragraphs, and the sanctioned exercise-tier ### headings are not "monsters".

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
  if (length(out) == 0) stop("No .qmd files to lint.")
  out
}

script_path <- function() {
  arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
  if (length(arg) == 0) return(NA_character_)
  normalizePath(sub("^--file=", "", arg[[1]]), winslash = "/", mustWork = TRUE)
}

find_conventions <- function() {
  script <- script_path()
  candidates <- character()
  if (!is.na(script)) {
    plugin_root <- normalizePath(
      file.path(dirname(script), "..", "..", ".."),
      winslash = "/",
      mustWork = TRUE
    )
    candidates <- c(candidates, file.path(plugin_root, "shared", "conventions.json"))
  }
  # Development fallback when the file is sourced rather than executed.
  candidates <- c(
    candidates,
    file.path("bookwright_plugin", "bookwright", "shared", "conventions.json"),
    file.path("shared", "conventions.json")
  )
  candidates <- unique(candidates)
  hit <- candidates[file.exists(candidates)]
  if (length(hit) == 0) {
    stop("Cannot locate shared/conventions.json from the script path or working directory.")
  }
  normalizePath(hit[[1]], winslash = "/", mustWork = TRUE)
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

strip_yaml <- function(lines) {
  if (length(lines) == 0 || !grepl("^---\\s*$", lines[[1]])) return(lines)
  ends <- which(seq_along(lines) > 1L & grepl("^(---|\\.\\.\\.)\\s*$", lines))
  if (length(ends)) lines[seq_len(ends[[1]])] <- ""
  lines
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

profile_code <- function(x) {
  n <- length(x)
  mask <- logical(n)
  ojs_nonfigure <- logical(n)
  figures <- list()
  in_code <- FALSE
  token <- ""
  start <- 0L
  lang <- ""
  label <- ""

  for (i in seq_len(n)) {
    t <- trimws(x[[i]])
    candidate <- fence_token(t)
    if (!in_code && nzchar(candidate)) {
      in_code <- TRUE
      token <- candidate
      start <- i
      mask[[i]] <- TRUE
      lang_hit <- regmatches(t, regexpr("\\{\\s*[A-Za-z0-9_+-]+", t))
      lang <- if (length(lang_hit)) tolower(trimws(sub("^\\{", "", lang_hit))) else ""
      label <- ""
      m <- regexec("\\{[^}]*\\b(fig-[A-Za-z0-9_-]+)\\b", t, perl = TRUE)
      hit <- regmatches(t, m)[[1]]
      if (length(hit) >= 2) label <- hit[[2]]
      next
    }
    if (in_code) {
      mask[[i]] <- TRUE
      if (is_fence_close(t, token)) {
        if (nzchar(label)) {
          figures[[length(figures) + 1L]] <- list(
            line = start,
            id = label,
            canonical = canonical_id(label)
          )
        } else if (identical(lang, "ojs")) {
          ojs_nonfigure[[start]] <- TRUE
        }
        in_code <- FALSE
        token <- ""
        next
      }
      candidate_label <- extract_fig_label(t)
      if (nzchar(candidate_label)) label <- candidate_label
    }
  }
  list(mask = mask, ojs = ojs_nonfigure, figures = figures)
}

# Canonical S7 values. conventions.json overrides these and is required.
S <- list(
  essay = list(
    sections = c(6, 9),
    pars = c(3, 10),
    words = c(200, 700),
    ratio_max = 3
  ),
  catalogue = list(
    entry_pars = c(2, 4),
    entry_words = c(120, 400),
    frame_pars = c(4, 12)
  ),
  catalogue_chapters = character(),
  deep_dive_chapters = c("16-regresija"),
  summary_label = "Sažetak",
  terms_label = "Pojmovi",
  exercises_label = "Zadaci",
  word_chapter_max = 5500,
  evenness_cv_max = 0.55,
  coda_min_ratio_to_median = 0.6,
  scaffold_min_prose_words = 60,
  element_words = list(callout = 70, figure = 60, ojs = 60, table = 50)
)

pick <- function(value, default) {
  if (is.null(value) || length(value) == 0) default else value
}

apply_structure <- function(st) {
  S$essay$sections <<- pick(st$essay$sections, S$essay$sections)
  S$essay$pars <<- pick(st$essay$pars, S$essay$pars)
  S$essay$words <<- pick(st$essay$words, S$essay$words)
  S$essay$ratio_max <<- pick(st$essay$ratio_max, S$essay$ratio_max)
  S$catalogue$entry_pars <<- pick(st$catalogue$entry_pars, S$catalogue$entry_pars)
  S$catalogue$entry_words <<- pick(st$catalogue$entry_words, S$catalogue$entry_words)
  S$catalogue$frame_pars <<- pick(st$catalogue$frame_pars, S$catalogue$frame_pars)
  S$catalogue_chapters <<- pick(st$catalogue_chapters, S$catalogue_chapters)
  S$deep_dive_chapters <<- pick(st$deep_dive_chapters, S$deep_dive_chapters)
  S$word_chapter_max <<- pick(st$word_chapter_max, S$word_chapter_max)
  S$evenness_cv_max <<- pick(st$evenness_cv_max, S$evenness_cv_max)
  S$coda_min_ratio_to_median <<- pick(
    st$coda_min_ratio_to_median,
    S$coda_min_ratio_to_median
  )
  S$scaffold_min_prose_words <<- pick(
    st$scaffold_min_prose_words,
    S$scaffold_min_prose_words
  )
  if (!is.null(st$element_words)) {
    for (key in names(S$element_words)) {
      S$element_words[[key]] <<- pick(st$element_words[[key]], S$element_words[[key]])
    }
  }
  S$summary_label <<- pick(st$summary_label, S$summary_label)
}

conv_path <- find_conventions()
if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("The canonical conventions parser requires jsonlite (installed with Quarto/rmarkdown).")
}
conventions <- jsonlite::read_json(conv_path, simplifyVector = TRUE)
if (is.null(conventions$structure)) stop("conventions.json has no structure block.")
apply_structure(conventions$structure)

profile_chapter <- function(path) {
  raw <- readLines(path, warn = FALSE, encoding = "UTF-8")
  scaffold <- any(grepl("STATUS\\s*:\\s*kostur", raw, ignore.case = TRUE))
  x <- strip_yaml(strip_html_comments(raw))
  n <- length(x)
  code <- profile_code(x)

  # Track source div membership. Prose inside a div is represented by the
  # element's calibrated weight, rather than counted again as paragraph prose.
  div_open <- grepl("^\\s*:::+\\s*\\{", x) & !code$mask
  div_close <- grepl("^\\s*:::+\\s*$", x) & !code$mask
  in_div <- logical(n)
  depth <- 0L
  for (i in seq_len(n)) {
    if (div_open[[i]]) {
      depth <- depth + 1L
      in_div[[i]] <- TRUE
    } else if (div_close[[i]]) {
      in_div[[i]] <- TRUE
      depth <- max(0L, depth - 1L)
    } else {
      in_div[[i]] <- depth > 0L
    }
  }

  h2 <- grepl("^##\\s+", x) & !code$mask & !in_div
  h3 <- grepl("^###\\s+", x) & !code$mask & !in_div
  sec_idx <- cumsum(h2)
  sec_lines <- which(h2)
  if (length(sec_lines) == 0) {
    return(list(sections = data.frame(), scaffold = scaffold))
  }

  is_callout <- div_open & grepl("\\.callout", x)
  is_fixed_callout <- div_open & grepl(
    "\\.callout-(?:vinjeta|divljina|model|greska)\\b",
    x,
    perl = TRUE
  )
  is_figdiv <- div_open & grepl("#fig-[A-Za-z0-9_-]+", x)
  markdown_image <- grepl("^\\s*!\\[", x) & !code$mask

  figure_records <- code$figures
  for (i in which(is_figdiv)) {
    id <- sub("^#", "", regmatches(x[[i]], regexpr("#fig-[A-Za-z0-9_-]+", x[[i]])))
    figure_records[[length(figure_records) + 1L]] <- list(
      line = i,
      id = id,
      canonical = canonical_id(id)
    )
  }
  for (i in which(markdown_image)) {
    m <- regmatches(x[[i]], regexpr("#fig-[A-Za-z0-9_-]+", x[[i]]))
    id <- if (length(m)) sub("^#", "", m) else sprintf("image-line-%d", i)
    figure_records[[length(figure_records) + 1L]] <- list(
      line = i,
      id = id,
      canonical = canonical_id(id)
    )
  }

  figure_lines <- integer()
  if (length(figure_records)) {
    groups <- split(
      seq_along(figure_records),
      vapply(figure_records, `[[`, character(1), "canonical")
    )
    figure_lines <- vapply(groups, function(ix) {
      min(vapply(figure_records[ix], `[[`, integer(1), "line"))
    }, integer(1))
  }

  tbl_caption <- grepl("^\\s*:\\s.*\\{#tbl-", x) & !code$mask
  tbl_row <- grepl("^\\s*\\|", x) & !code$mask

  math_single <- grepl("^\\s*\\$\\$.*\\$\\$\\s*$", x) & !code$mask
  math_delim <- grepl("^\\s*\\$\\$\\s*$", x) & !code$mask
  math_block <- logical(n)
  in_math <- FALSE
  for (i in seq_len(n)) {
    if (math_delim[[i]]) {
      math_block[[i]] <- TRUE
      in_math <- !in_math
    } else if (in_math) {
      math_block[[i]] <- TRUE
    }
  }
  is_math <- math_single | math_block
  raw_html <- grepl("^\\s*</?[A-Za-z][^>]*>\\s*$", x)
  horizontal <- grepl("^\\s*(?:---+|\\*\\*\\*+|___+)\\s*$", x, perl = TRUE)

  prose <- nzchar(trimws(x)) &
    !grepl("^#{1,6}\\s+", x) &
    !in_div &
    !code$mask &
    !tbl_row &
    !tbl_caption &
    !is_math &
    !markdown_image &
    !raw_html &
    !horizontal
  para_start <- prose & !c(FALSE, head(prose, -1L))

  out <- data.frame()
  for (i in seq_along(sec_lines)) {
    sel <- sec_idx == i
    title <- heading_text(x[[sec_lines[[i]]]])
    prose_lines <- trimws(x[prose & sel])
    words <- if (length(prose_lines)) {
      sum(lengths(strsplit(prose_lines, "\\s+")))
    } else {
      0L
    }
    n_callout <- sum(is_callout & !is_fixed_callout & sel)
    n_figure <- if (length(figure_lines)) sum(sec_idx[figure_lines] == i) else 0L
    n_ojs <- sum(code$ojs & sel)
    n_table <- sum(tbl_caption & sel)
    elem_weight <- n_callout * S$element_words$callout +
      n_figure * S$element_words$figure +
      n_ojs * S$element_words$ojs +
      n_table * S$element_words$table
    out <- rbind(
      out,
      data.frame(
        sec = i,
        title = title,
        subs = sum(h3 & sel),
        pars = sum(para_start & sel),
        words = words,
        callouts = n_callout,
        figures = n_figure,
        ojs = n_ojs,
        tables = n_table,
        weight = words + elem_weight,
        stringsAsFactors = FALSE
      )
    )
  }
  list(sections = out, scaffold = scaffold)
}

cv <- function(values) {
  values <- values[values > 0]
  if (length(values) < 2) return(0)
  stats::sd(values) / mean(values)
}

classify_roles <- function(sections) {
  role <- rep("body", nrow(sections))
  role[grepl(paste0("^", S$summary_label, "\\b"), sections$title)] <- "summary"
  role[grepl(paste0("^", S$terms_label, "\\b"), sections$title)] <- "terms"
  role[grepl(paste0("^", S$exercises_label, "\\b"), sections$title)] <- "exercises"
  role
}

lint_chapter <- function(path) {
  slug <- sub("\\.qmd$", "", basename(path))
  profile <- profile_chapter(path)
  secs <- profile$sections
  if (nrow(secs) == 0) {
    cat(sprintf("\n%s — no top-level ## sections found.\n", slug))
    return(1L)
  }

  role <- classify_roles(secs)
  body <- secs[role == "body", , drop = FALSE]
  is_catalogue <- slug %in% S$catalogue_chapters
  is_deep <- slug %in% S$deep_dive_chapters
  template <- if (is_catalogue) "catalogue" else "essay"
  total_words <- sum(secs$words)
  body_weights <- body$weight[body$weight > 0]
  median_weight <- if (length(body_weights)) stats::median(body_weights) else 0
  evenness <- cv(body$weight)

  hits <- character()
  flag <- function(text) hits[[length(hits) + 1L]] <<- text

  # Skeleton files deliberately contain empty slots. Report useful slot-level
  # gaps, but suppress calibrated chapter-rhythm claims until prose exists.
  if (!profile$scaffold && template == "essay") {
    ns <- nrow(secs)
    if (ns < S$essay$sections[[1]]) {
      flag(sprintf(
        "  CHAPTER  only %d top-level sections (essay band %d-%d)",
        ns,
        S$essay$sections[[1]],
        S$essay$sections[[2]]
      ))
    }
    if (ns > S$essay$sections[[2]]) {
      flag(sprintf(
        "  CHAPTER  %d top-level sections (essay band %d-%d) — consider a merge",
        ns,
        S$essay$sections[[1]],
        S$essay$sections[[2]]
      ))
    }
    if (!is_deep && evenness > S$evenness_cv_max) {
      flag(sprintf(
        "  CHAPTER  evenness %.2f (cap %.2f) — argumentative sections are too uneven",
        evenness,
        S$evenness_cv_max
      ))
    }
    if (!is_deep && length(body_weights) >= 2L) {
      ratio <- max(body_weights) / min(body_weights)
      if (ratio > S$essay$ratio_max) {
        nonzero <- body[body$weight > 0, , drop = FALSE]
        flag(sprintf(
          "  CHAPTER  size ratio %.1fx (max %gx) — '%s' outweighs '%s'",
          ratio,
          S$essay$ratio_max,
          substr(nonzero$title[which.max(nonzero$weight)], 1, 34),
          substr(nonzero$title[which.min(nonzero$weight)], 1, 34)
        ))
      }
    }
    if (!is_deep && total_words > S$word_chapter_max) {
      flag(sprintf(
        "  CHAPTER  %d prose words (soft cap %d) — review for a split",
        total_words,
        S$word_chapter_max
      ))
    }
    if (nrow(body) >= 2L && median_weight > 0) {
      last <- body[nrow(body), , drop = FALSE]
      if (last$weight > 0 && last$weight < S$coda_min_ratio_to_median * median_weight) {
        flag(sprintf(
          "  S%02d      CODA %dw vs median %dw — strengthen or merge: '%s'",
          last$sec,
          round(last$weight),
          round(median_weight),
          substr(last$title, 1, 38)
        ))
      }
    }
  }

  for (k in seq_len(nrow(secs))) {
    if (role[[k]] != "body") next
    section <- secs[k, , drop = FALSE]
    title <- substr(section$title, 1, 38)
    n_elements <- section$callouts + section$figures + section$ojs + section$tables

    if (section$subs > 0L) {
      flag(sprintf(
        "  S%02d      MONSTER (nested) %d top-level ### subsections — promote or split: '%s'",
        section$sec,
        section$subs,
        title
      ))
    }
    if (section$words == 0L && n_elements == 0L) {
      flag(sprintf("  S%02d      EMPTY argumentative section: '%s'", section$sec, title))
      next
    }
    if (n_elements >= 1L && section$words < S$scaffold_min_prose_words) {
      flag(sprintf(
        "  S%02d      SCAFFOLD %d element(s) / only %dw connecting prose: '%s'",
        section$sec,
        n_elements,
        section$words,
        title
      ))
    }
    if (profile$scaffold) next

    if (template == "essay") {
      if (
        section$pars < S$essay$pars[[1]] &&
        section$weight < S$coda_min_ratio_to_median * median_weight
      ) {
        flag(sprintf(
          "  S%02d      STUB %d par / %dw (band %d-%d par): '%s'",
          section$sec,
          section$pars,
          section$words,
          S$essay$pars[[1]],
          S$essay$pars[[2]],
          title
        ))
      }
      if (section$pars > S$essay$pars[[2]]) {
        flag(sprintf(
          "  S%02d      MONSTER %d par / %dw — split: '%s'",
          section$sec,
          section$pars,
          section$words,
          title
        ))
      }
    } else {
      lo <- S$catalogue$entry_pars[[1]]
      hi <- S$catalogue$entry_pars[[2]]
      if (section$pars < lo || section$pars > hi) {
        flag(sprintf(
          "  S%02d      ENTRY %d par / %dw (band %d-%d): '%s'",
          section$sec,
          section$pars,
          section$words,
          lo,
          hi,
          title
        ))
      }
    }
  }

  tag <- c(template, if (is_deep) "deep-dive", if (profile$scaffold) "skeleton")
  tag <- tag[nzchar(tag)]
  cat(sprintf(
    "\n%s  [%s, %d top-level sections, %d prose words, body evenness %.2f]\n",
    slug,
    paste(tag, collapse = ", "),
    nrow(secs),
    total_words,
    evenness
  ))
  if (profile$scaffold) {
    cat("  (skeleton: chapter-level rhythm bands suppressed; authored slot gaps still reported)\n")
  }
  if (length(hits) == 0) {
    cat("  OK — deterministic section-rhythm checks passed.\n")
  } else {
    for (hit in hits) cat(hit, "\n", sep = "")
  }
  length(hits)
}

paths <- expand_inputs(commandArgs(trailingOnly = TRUE))
cat("STYLE.md S7 structure lint\n")
cat(sprintf("bands: %s\n", conv_path))
cat(strrep("=", 64), "\n", sep = "")
total <- 0L
for (path in paths) total <- total + lint_chapter(path)
cat(sprintf(
  "\n%d candidate(s) across %d chapter(s). Each is for you to restructure, not an auto-fix.\n",
  total,
  length(paths)
))
