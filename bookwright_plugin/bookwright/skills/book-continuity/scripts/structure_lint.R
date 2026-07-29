#!/usr/bin/env Rscript

# structure_lint.R - flag STYLE.md S7 section-rhythm candidates in a Quarto
# chapter, or across the whole book.
# Usage:
#   Rscript structure_lint.R chapters/19-reforme.qmd     # one chapter
#   Rscript structure_lint.R chapters/*.qmd              # the whole book
#   Rscript structure_lint.R                             # defaults to chapters/*.qmd
#
# It measures, per ## section, the paragraph count, word count, and ### nesting,
# then judges each section against the S7 bands for the chapter's declared
# template (essay or catalogue). Every hit is a candidate restructuring for you
# to apply by hand, never an automatic edit. The bands and the catalogue-chapter
# roster live in shared/conventions.json under "structure"; this script reads
# them so the numbers have one source of truth.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) == 0) {
  args <- Sys.glob(file.path("chapters", "*.qmd"))
}
args <- args[grepl("\\.qmd$", args)]
if (length(args) == 0) stop("No .qmd files to lint.")

# --- locate and read conventions.json (walk up from this script) -------------
find_conventions <- function() {
  candidates <- c(
    file.path("bookwright_plugin", "bookwright", "shared", "conventions.json"),
    file.path("..", "..", "shared", "conventions.json"),
    file.path("..", "shared", "conventions.json")
  )
  for (p in candidates) if (file.exists(p)) return(p)
  NA_character_
}

# defaults, used if conventions.json lacks a "structure" block
S <- list(
  essay = list(
    sections = c(6, 9), pars = c(3, 10), words = c(200, 700),
    ratio_max = 3, vodic_pars = c(2, 4), par_words = c(40, 130), allow_h3 = FALSE
  ),
  catalogue = list(
    entry_pars = c(2, 4), entry_words = c(120, 400),
    frame_pars = c(4, 12), allow_h3 = FALSE
  ),
  catalogue_chapters = character(0),
  deep_dive_chapters = c("16-regresija"),
  vodic_label = "Vinjeta",
  summary_label = "Sažetak",
  word_chapter_max = 5500,
  evenness_cv_max = 0.55,
  coda_min_ratio_to_median = 0.6,
  scaffold_min_prose_words = 60,
  element_words = list(callout = 70, figure = 60, ojs = 60, table = 50)
)

# Apply a parsed structure list `st` over the defaults in S.
apply_structure <- function(st) {
  pick <- function(a, b) if (is.null(a) || length(a) == 0) b else a
  S$essay$sections   <<- pick(st$essay$sections,    S$essay$sections)
  S$essay$pars       <<- pick(st$essay$pars,        S$essay$pars)
  S$essay$words      <<- pick(st$essay$words,       S$essay$words)
  S$essay$ratio_max  <<- pick(st$essay$ratio_max,   S$essay$ratio_max)
  S$essay$vodic_pars <<- pick(st$essay$vodic_pars,  S$essay$vodic_pars)
  S$essay$par_words  <<- pick(st$essay$par_words,   S$essay$par_words)
  S$catalogue$entry_pars  <<- pick(st$catalogue$entry_pars,  S$catalogue$entry_pars)
  S$catalogue$entry_words <<- pick(st$catalogue$entry_words, S$catalogue$entry_words)
  S$catalogue$frame_pars  <<- pick(st$catalogue$frame_pars,  S$catalogue$frame_pars)
  S$catalogue_chapters <<- pick(st$catalogue_chapters, S$catalogue_chapters)
  S$deep_dive_chapters <<- pick(st$deep_dive_chapters, S$deep_dive_chapters)
  S$word_chapter_max   <<- pick(st$word_chapter_max,   S$word_chapter_max)
  S$evenness_cv_max          <<- pick(st$evenness_cv_max,          S$evenness_cv_max)
  S$coda_min_ratio_to_median <<- pick(st$coda_min_ratio_to_median, S$coda_min_ratio_to_median)
  S$scaffold_min_prose_words <<- pick(st$scaffold_min_prose_words, S$scaffold_min_prose_words)
  if (!is.null(st$element_words)) {
    ew <- st$element_words
    for (k in c("callout", "figure", "ojs", "table"))
      if (!is.null(ew[[k]])) S$element_words[[k]] <<- ew[[k]]
  }
  if (!is.null(st$vodic_label))   S$vodic_label   <<- st$vodic_label
  if (!is.null(st$summary_label)) S$summary_label <<- st$summary_label
}

# Minimal regex reader for the "structure" block, used when jsonlite is absent.
# Reads only the flat numeric-array and string fields S7 needs; nested objects
# (essay, catalogue) are scoped by brace matching on a flattened string.
read_structure_regex <- function(path) {
  txt <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  block <- sub('.*"structure"\\s*:\\s*\\{', "", txt)  # drop everything before the block body
  nums <- function(scope, key) {
    m <- regmatches(scope, regexpr(sprintf('"%s"\\s*:\\s*\\[[^]]*\\]', key), scope))
    if (length(m) == 0) return(NULL)
    as.numeric(regmatches(m, gregexpr("-?[0-9.]+", m))[[1]])
  }
  scalar <- function(scope, key) {
    m <- regmatches(scope, regexpr(sprintf('"%s"\\s*:\\s*-?[0-9.]+', key), scope))
    if (length(m) == 0) return(NULL)
    as.numeric(regmatches(m, regexpr("-?[0-9.]+", m)))
  }
  strarr <- function(scope, key) {
    m <- regmatches(scope, regexpr(sprintf('"%s"\\s*:\\s*\\[[^]]*\\]', key), scope))
    if (length(m) == 0) return(NULL)
    regmatches(m, gregexpr('"([^"]+)"', m))[[1]] |> (\(v) gsub('"', "", v))()
  }
  subobj <- function(scope, key) {
    m <- regmatches(scope, regexpr(sprintf('"%s"\\s*:\\s*\\{[^}]*\\}', key), scope))
    if (length(m) == 0) "" else m
  }
  essay <- subobj(block, "essay")
  catal <- subobj(block, "catalogue")
  ewobj <- subobj(block, "element_words")
  ew_field <- function(key) {
    m <- regmatches(ewobj, regexpr(sprintf('"%s"\\s*:\\s*-?[0-9.]+', key), ewobj))
    if (length(m) == 0) return(NULL)
    as.numeric(regmatches(m, regexpr("-?[0-9.]+", m)))
  }
  list(
    essay = list(
      sections = nums(essay, "sections"), pars = nums(essay, "pars"),
      words = nums(essay, "words"), ratio_max = scalar(essay, "ratio_max"),
      vodic_pars = nums(essay, "vodic_pars"), par_words = nums(essay, "par_words")
    ),
    catalogue = list(
      entry_pars = nums(catal, "entry_pars"), entry_words = nums(catal, "entry_words"),
      frame_pars = nums(catal, "frame_pars")
    ),
    catalogue_chapters = strarr(block, "catalogue_chapters"),
    deep_dive_chapters = strarr(block, "deep_dive_chapters"),
    word_chapter_max = scalar(block, "word_chapter_max"),
    evenness_cv_max = scalar(block, "evenness_cv_max"),
    coda_min_ratio_to_median = scalar(block, "coda_min_ratio_to_median"),
    scaffold_min_prose_words = scalar(block, "scaffold_min_prose_words"),
    element_words = list(
      callout = ew_field("callout"), figure = ew_field("figure"),
      ojs = ew_field("ojs"), table = ew_field("table")
    ),
    vodic_label = strarr(block, "vodic_label")[1],
    summary_label = strarr(block, "summary_label")[1]
  )
}

conv_path <- find_conventions()
bands_source <- "built-in defaults"
if (!is.na(conv_path)) {
  if (requireNamespace("jsonlite", quietly = TRUE)) {
    cj <- tryCatch(jsonlite::read_json(conv_path, simplifyVector = TRUE), error = function(e) NULL)
    if (!is.null(cj$structure)) { apply_structure(cj$structure); bands_source <- conv_path }
  } else {
    st <- tryCatch(read_structure_regex(conv_path), error = function(e) NULL)
    if (!is.null(st)) { apply_structure(st); bands_source <- paste0(conv_path, " (regex reader; install jsonlite for the canonical parse)") }
  }
}

# --- profile one chapter into a per-section data frame -----------------------
# Counts prose paragraphs/words AND structural elements (callouts, fig divs, OJS
# blocks, tables) per ## section. A section's "weight" is prose words plus a
# per-element word equivalent, so a page that renders full no longer reads as a
# stub and a page that is all boxes is exposed as a scaffold.
profile_chapter <- function(f) {
  x <- readLines(f, warn = FALSE, encoding = "UTF-8")
  if (length(x) > 0 && grepl("^---\\s*$", x[1])) {
    end <- which(grepl("^---\\s*$", x))[2]
    if (!is.na(end)) x <- x[-(1:end)]
  }

  # fenced code blocks: mark opener lines and interior. Count {ojs} openers as
  # OJS elements; everything inside any fence is excluded from prose.
  fence <- grepl("^\\s*(```|~~~)", x)
  fence_open <- fence & ((cumsum(fence) %% 2) == 1)   # odd fence = an opener
  ojs_open <- fence_open & grepl("\\{\\s*ojs", x, ignore.case = TRUE)
  inside <- (cumsum(fence) %% 2) == 1 & !fence        # interior lines (not the fence line itself)

  h2 <- grepl("^## ", x) & !inside
  h3 <- grepl("^### ", x) & !inside
  sec_idx <- cumsum(h2)

  # div elements: opener line carries the class. callout-* -> callout, fig- id or
  # .figure / #fig- -> figure. Track div depth to know prose-vs-div membership.
  div_open  <- grepl("^:::+\\s*\\{", x) & !inside
  div_close <- grepl("^:::+\\s*$", x) & !inside
  is_callout <- div_open & grepl("\\.callout", x)
  is_figdiv  <- div_open & grepl("#fig-|\\.cell|fig-", x)
  depth <- cumsum(div_open) - cumsum(div_close)
  in_div <- depth > 0 | div_open

  # table lines: a markdown pipe-table row or a Quarto caption line ": ... {#tbl-"
  tbl_caption <- grepl("^\\s*:\\s.*\\{#tbl-", x) & !inside
  tbl_row <- grepl("^\\s*\\|", x) & !inside

  # display math ($$...$$): exclude from prose so an equation does not register as
  # its own paragraph. Handles both a whole single-line equation ($$...$$ on one
  # line) and a multi-line block delimited by lone $$ lines.
  math_single <- grepl("^\\s*\\$\\$.*\\$\\$\\s*$", x) & !inside
  math_delim  <- grepl("^\\s*\\$\\$\\s*$", x) & !inside
  math_block  <- (cumsum(math_delim) %% 2) == 1          # opener + interior of a block
  is_math <- (math_single | math_delim | math_block) & !inside

  prose <- nzchar(trimws(x)) & !h2 & !h3 & !grepl("^#", x) &
    !in_div & !div_close & !inside & !fence & !tbl_row & !tbl_caption & !is_math
  para_start <- prose & !c(FALSE, head(prose, -1))

  sec_lines <- which(h2)
  out <- data.frame()
  if (length(sec_lines) == 0) return(out)
  for (i in seq_along(sec_lines)) {
    sel <- sec_idx == i
    title <- sub("^## ", "", x[sec_lines[i]])
    title <- trimws(sub("\\s*\\{.*\\}\\s*$", "", title))
    words <- sum(lengths(strsplit(trimws(x[prose & sel]), "\\s+")))
    n_callout <- sum(is_callout & sel)
    n_figure  <- sum(is_figdiv & sel)
    n_ojs     <- sum(ojs_open & sel)
    n_table   <- sum(tbl_caption & sel)
    elem_weight <- n_callout * S$element_words$callout +
      n_figure * S$element_words$figure +
      n_ojs * S$element_words$ojs +
      n_table * S$element_words$table
    out <- rbind(out, data.frame(
      sec = i, title = title,
      subs = sum(h3 & sel), pars = sum(para_start & sel),
      words = words, callouts = n_callout, figures = n_figure,
      ojs = n_ojs, tables = n_table,
      weight = words + elem_weight,
      stringsAsFactors = FALSE
    ))
  }
  out
}

# coefficient of variation of a numeric vector (sd / mean), 0 if <2 positive.
cv <- function(v) {
  v <- v[v > 0]
  if (length(v) < 2) return(0)
  stats::sd(v) / mean(v)
}

slug_of <- function(f) sub("\\.qmd$", "", basename(f))

# section role: vodic (first), summary (last, label match), body
classify_roles <- function(secs, slug) {
  n <- nrow(secs)
  role <- rep("body", n)
  if (n >= 1 && grepl(S$vodic_label, secs$title[1], fixed = TRUE)) role[1] <- "vodic"
  is_sum <- grepl(S$summary_label, secs$title, fixed = TRUE)
  role[is_sum] <- "summary"
  role
}

# --- lint one chapter --------------------------------------------------------
lint_chapter <- function(f) {
  slug <- slug_of(f)
  secs <- profile_chapter(f)
  if (nrow(secs) == 0) {
    cat(sprintf("\n%s — no ## sections found.\n", slug))
    return(invisible(NULL))
  }
  is_cat <- slug %in% S$catalogue_chapters
  is_deep <- slug %in% S$deep_dive_chapters
  template <- if (is_cat) "catalogue" else "essay"
  role <- classify_roles(secs, slug)
  body <- secs[role == "body", , drop = FALSE]
  total_words <- sum(secs$words)
  body_wt <- body$weight[body$weight > 0]
  med_wt <- if (length(body_wt)) stats::median(body_wt) else 0
  evenness <- cv(body$weight)

  hits <- character(0)
  flag <- function(s) hits[[length(hits) + 1]] <<- s

  # chapter-level
  if (template == "essay") {
    ns <- nrow(secs)
    if (ns < S$essay$sections[1])
      flag(sprintf("  CHAPTER  only %d sections (essay band %d-%d) — chapter may be too thin or under-segmented",
                   ns, S$essay$sections[1], S$essay$sections[2]))
    if (ns > S$essay$sections[2])
      flag(sprintf("  CHAPTER  %d sections (essay band %d-%d) — consider whether two sections merge",
                   ns, S$essay$sections[1], S$essay$sections[2]))
    if (!is_deep && evenness > S$evenness_cv_max)
      flag(sprintf("  CHAPTER  evenness %.2f (cap %.2f) — section weights too uneven; level the worst sections",
                   evenness, S$evenness_cv_max))
    if (!is_deep && length(body_wt) >= 2) {
      ratio <- max(body_wt) / min(body_wt)
      if (ratio > S$essay$ratio_max)
        flag(sprintf("  CHAPTER  size ratio %.1fx (max %gx) — '%s' (%dw) dwarfs '%s' (%dw)",
                     ratio, S$essay$ratio_max,
                     substr(body$title[which.max(body$weight)], 1, 30), round(max(body_wt)),
                     substr(body$title[which.min(ifelse(body$weight>0, body$weight, Inf))], 1, 30), round(min(body_wt))))
    }
    # coda rule: the last body section must carry >= a fraction of median weight.
    bidx <- which(role == "body")
    if (length(bidx) >= 2) {
      last <- secs[bidx[length(bidx)], ]
      if (med_wt > 0 && last$weight > 0 && last$weight < S$coda_min_ratio_to_median * med_wt)
        flag(sprintf("  S%02d      CODA %dw vs median %dw — chapter fizzles out; synthesise at full weight or merge into Sažetak: '%s'",
                     last$sec, round(last$weight), round(med_wt), substr(last$title, 1, 34)))
    }
  }
  if (!is_deep && total_words > S$word_chapter_max)
    flag(sprintf("  CHAPTER  %d words total (soft cap %d) — candidate for splitting or a deep-dive exemption",
                 total_words, S$word_chapter_max))

  # section-level
  for (k in seq_len(nrow(secs))) {
    r <- role[k]; sc <- secs[k, ]
    title30 <- substr(sc$title, 1, 38)
    if (r == "vodic") {
      lo <- S$essay$vodic_pars[1]; hi <- S$essay$vodic_pars[2]
      if (sc$pars > 0 && (sc$pars < lo || sc$pars > hi))
        flag(sprintf("  S%02d      Vodič has %d paragraphs (band %d-%d): '%s'",
                     sc$sec, sc$pars, lo, hi, title30))
      next
    }
    if (r == "summary") next  # Sažetak format is the panel rule, not S7
    # body
    if (sc$subs > 0)
      flag(sprintf("  S%02d      MONSTER (nested) %d ### subsections — promote to ## or split: '%s'",
                   sc$sec, sc$subs, title30))
    # scaffold: section is mostly elements, little prose connecting them.
    n_elem <- sc$callouts + sc$figures + sc$ojs + sc$tables
    if (n_elem >= 2 && sc$words < S$scaffold_min_prose_words)
      flag(sprintf("  S%02d      SCAFFOLD %d elements / only %dw prose — add connecting argument: '%s'",
                   sc$sec, n_elem, sc$words, title30))
    if (template == "essay") {
      # a thin paragraph count is a stub UNLESS elements carry it to median weight.
      if (sc$pars > 0 && sc$pars < S$essay$pars[1] && sc$weight < S$coda_min_ratio_to_median * med_wt)
        flag(sprintf("  S%02d      STUB %d par / %dw (wt %d, band %d-%d par) — merge up or thicken: '%s'",
                     sc$sec, sc$pars, sc$words, round(sc$weight), S$essay$pars[1], S$essay$pars[2], title30))
      if (sc$pars > S$essay$pars[2])
        flag(sprintf("  S%02d      MONSTER %d par / %dw — split: '%s'",
                     sc$sec, sc$pars, sc$words, title30))
    } else {
      # catalogue: body entries must be uniform; opening/synthesis are frames.
      bidx <- which(role == "body")
      is_frame <- k == bidx[1] || k == bidx[length(bidx)]
      if (is_frame) {
        if (sc$pars > 0 && sc$pars < S$catalogue$frame_pars[1])
          flag(sprintf("  S%02d      FRAME thin %d par (band %d-%d) — opening/synthesis carries weight: '%s'",
                       sc$sec, sc$pars, S$catalogue$frame_pars[1], S$catalogue$frame_pars[2], title30))
      } else {
        lo <- S$catalogue$entry_pars[1]; hi <- S$catalogue$entry_pars[2]
        if (sc$pars > 0 && (sc$pars < lo || sc$pars > hi))
          flag(sprintf("  S%02d      ENTRY %d par / %dw (uniform band %d-%d) — even the catalogue: '%s'",
                       sc$sec, sc$pars, sc$words, lo, hi, title30))
      }
    }
  }

  tag <- if (is_deep) paste0(template, ", deep-dive") else template
  cat(sprintf("\n%s  [%s, %d sections, %d words, evenness %.2f]\n",
              slug, tag, nrow(secs), total_words, evenness))
  if (is_deep)
    cat("  (deep-dive: chapter-size and evenness flags suppressed by exemption)\n")
  if (length(hits) == 0) {
    cat("  OK — section rhythm within S7 bands.\n")
  } else {
    for (h in hits) cat(h, "\n", sep = "")
  }
  length(hits)
}

cat("STYLE.md S7 structure lint\n")
cat(sprintf("bands: %s\n", bands_source))
cat(strrep("=", 64), "\n", sep = "")
total <- 0
for (f in args) {
  h <- lint_chapter(f)
  if (!is.null(h)) total <- total + h
}
cat(sprintf("\n%d candidate(s) across %d chapter(s). Each is for you to restructure, not an auto-fix.\n",
            total, length(args)))
