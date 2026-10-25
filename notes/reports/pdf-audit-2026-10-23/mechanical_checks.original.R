## Mechanical round for the print PDF of Osnove statistike za društvene znanosti
## Usage.  Rscript mechanical_checks.R path/to/Statistika.pdf [output_dir]
## Needs pdftotext (poppler) on the PATH and curl for the URL check. Base R only.
## Rerun after every revision. If chapters move, update `ranges` (printed pages) and `offset`.
## Writes round4_mechanical.md into output_dir (default: the folder of the PDF).

args <- commandArgs(trailingOnly = TRUE)
pdf <- if (length(args) >= 1) args[1] else "Statistika.pdf"
wd  <- if (length(args) >= 2) args[2] else dirname(normalizePath(pdf))
dir.create(file.path(wd, "results"), showWarnings = FALSE, recursive = TRUE)
dir.create(file.path(wd, "chapters"), showWarnings = FALSE)
setwd(wd)
Sys.setlocale("LC_ALL", "C.UTF-8")

## 1. text extraction, one element per PDF page
txt <- system2("pdftotext", c("-layout", "-enc", "UTF-8", shQuote(pdf), "-"), stdout = TRUE)
txt <- paste(txt, collapse = "\n")
pages <- strsplit(strsplit(txt, "\f", fixed = TRUE)[[1]], "\n", fixed = TRUE)
offset <- 4  # PDF page = printed page + offset
ranges <- list(
  "00_predgovor" = c(1, 4), "01_zasto_statistika" = c(7, 28), "02_mjerenje" = c(29, 52),
  "03_kako_brojke_zavode" = c(53, 72), "04_sazimanje" = c(75, 96), "05_vizualizacija" = c(97, 120),
  "06_povezanost" = c(121, 146), "07_vjerojatnost" = c(149, 168), "08_uzorkovanje" = c(169, 192),
  "09_procjena" = c(193, 216), "10_logika_testiranja" = c(219, 238), "11_velicina_ucinka" = c(239, 256),
  "12_kriza_obnova" = c(257, 278), "13_kategoricki" = c(281, 304), "14_dvije_grupe" = c(305, 322),
  "15_vise_grupa" = c(323, 340), "16_regresija" = c(341, 368), "17_algoritmi" = c(369, 390),
  "18_prvo_istrazivanje" = c(393, 418), "19_provjere" = c(419, 426), "20_literatura" = c(427, 435))
for (nm in names(ranges)) {
  r <- ranges[[nm]]
  chunk <- unlist(lapply(r[1]:r[2], function(pp) c(sprintf("<<<<< STRANICA %d >>>>>", pp), pages[[pp + offset]])))
  writeLines(chunk, file.path("chapters", paste0(nm, ".txt")), useBytes = TRUE)
}

out <- character()
say <- function(...) out <<- c(out, paste0(...))

chfiles <- list.files("chapters", pattern = "^(0[1-9]|1[0-8])_.*\\.txt$", full.names = TRUE)
chtxt <- setNames(lapply(chfiles, function(f) readLines(f, encoding = "UTF-8", warn = FALSE)), basename(chfiles))
body_all <- unlist(chtxt)

## 1. Figure and table numbering per chapter ------------------------------------
say("## 1. Numbering of figures and tables per chapter")
say("")
say("| Chapter | Figure captions found | Sequential | Table captions found | Sequential | Unnumbered tables (no caption) |")
say("|---|---|---|---|---|---|")
for (nm in names(chtxt)) {
  tx <- chtxt[[nm]]
  figs <- as.integer(sub("^\\s*Slika (\\d+):.*", "\\1", grep("^\\s*Slika \\d+:", tx, value = TRUE)))
  tabs <- as.integer(sub("^\\s*Tablica (\\d+):.*", "\\1", grep("^\\s*Tablica \\d+:", tx, value = TRUE)))
  seqok <- function(v) if (length(v) == 0) "n/a" else if (identical(v, seq_along(v))) "yes" else paste("NO", paste(v, collapse = ","))
  ## tables rendered without caption: a header like 'Faza   Pitanje' followed by rows; approximate by counting lines of 2+ column layout preceded by blank line and not inside a captioned table. Rough proxy, reported only as a count of header like lines.
  say("| ", nm, " | ", length(figs), " | ", seqok(figs), " | ", length(tabs), " | ", seqok(tabs), " | see section 2 |")
}
say("")

## 2. Cross references to figures and tables ----------------------------------
say("## 2. In text references to figures and tables")
say("")
say("Numbering restarts in every chapter, so a reference to „Slika 3“ is resolved against the figures of the same chapter.")
say("")
say("| Chapter | Reference | Count | Resolves |")
say("|---|---|---|---|")
for (nm in names(chtxt)) {
  tx <- paste(chtxt[[nm]], collapse = " ")
  figs <- as.integer(sub("^\\s*Slika (\\d+):.*", "\\1", grep("^\\s*Slika \\d+:", chtxt[[nm]], value = TRUE)))
  tabs <- as.integer(sub("^\\s*Tablica (\\d+):.*", "\\1", grep("^\\s*Tablica \\d+:", chtxt[[nm]], value = TRUE)))
  refs <- regmatches(tx, gregexpr("(?i)\\b(slik[aeiu]|slikom|tablic[aeiu]|tablicom)\\s+(\\d+)\\b", tx, perl = TRUE))[[1]]
  refs <- refs[!grepl("^(Slika|Tablica) \\d+$", refs)]  # drop captions themselves (captions have a colon, so already excluded)
  if (length(refs) == 0) { say("| ", nm, " | none (figures and tables are referred to without numbers) | 0 | n/a |"); next }
  tb <- table(refs)
  for (r in names(tb)) {
    n <- as.integer(sub(".*?(\\d+)$", "\\1", r))
    isfig <- grepl("^(?i)slik", r, perl = TRUE)
    ok <- if (isfig) n %in% figs else n %in% tabs
    say("| ", nm, " | ", r, " | ", tb[[r]], " | ", if (ok) "yes" else "NO", " |")
  }
}
say("")

## 3. Chapter cross references ---------------------------------------------------
say("## 3. Cross references to chapters by number")
say("")
chrefs <- regmatches(body_all, gregexpr("\\b[Pp]oglavlj[aeu]\\s+(\\d+)\\b", body_all))
chrefs <- unlist(chrefs)
if (length(chrefs)) {
  tb <- table(chrefs)
  say("| Reference | Count | Valid chapter number |"); say("|---|---|---|")
  for (r in names(tb)) { n <- as.integer(sub(".*?(\\d+)$", "\\1", r)); say("| ", r, " | ", tb[[r]], " | ", if (n >= 1 && n <= 18) "yes" else "NO", " |") }
} else say("No numbered chapter references in the body text; chapters are referred to by topic („u poglavlju o uzorkovanju“).")
say("")
topicrefs <- grep("poglavlj[aeu] o ", body_all, value = TRUE)
say("Topic style chapter references found in body text. ", length(topicrefs), " lines. Sample below for manual check that each names an existing chapter topic.")
say("")
for (l in head(unique(trimws(topicrefs)), 60)) say("* ", l)
say("")

## 4. Citations against Literatura -------------------------------------------------
say("## 4. Citations against the bibliography")
say("")
lit <- readLines("chapters/20_literatura.txt", encoding = "UTF-8", warn = FALSE)
lit <- lit[!grepl("^<<<<<|^\\s*Literatura\\s*$|^\\s*\\d+\\s*$", lit)]
## join wrapped entries. An entry starts with a non indented line after a blank line.
entries <- character(); cur <- ""
for (l in lit) {
  if (grepl("^\\S", l) && nchar(cur) > 0 && !grepl("^\\s", l)) { entries <- c(entries, cur); cur <- l }
  else if (trimws(l) == "") { if (nchar(cur)) { entries <- c(entries, cur); cur <- "" } }
  else cur <- paste(cur, trimws(l))
}
if (nchar(cur)) entries <- c(entries, cur)
entries <- trimws(entries); entries <- entries[nchar(entries) > 0]
## key = first surname + year(+letter)
bibkey <- function(e) {
  yr <- regmatches(e, regexpr("\\b(19|20)\\d{2}\\.[a-z]?", e))
  sur <- sub("^([^,]+),.*", "\\1", e)
  sur <- sub("^(\\S+).*", "\\1", sur)
  if (length(yr) == 0) yr <- "NOYEAR"
  paste(sur, sub("\\.$", "", yr))
}
keys <- sapply(entries, bibkey, USE.NAMES = FALSE)
say("Bibliography entries parsed. ", length(entries), ". Keys. ", paste(keys, collapse = "; "))
say("")
## in text citations. Patterns. (Name YYYY.) (Name i sur. YYYY.) Name (YYYY.) (Name i Name YYYY.) with optional letter and page
txt1 <- paste(body_all, collapse = " ")
txt1 <- gsub("\\s+", " ", txt1)
cit <- regmatches(txt1, gregexpr("\\(([A-ZŠĐČĆŽ][^()]{0,80}?)\\s((19|20)\\d{2}\\.[a-z]?)(, [^()]*)?\\)", txt1, perl = TRUE))[[1]]
cit2 <- regmatches(txt1, gregexpr("\\b([A-ZŠĐČĆŽ][a-zšđčćžA-Z'’]+)( i sur\\.| i [A-ZŠĐČĆŽ][a-zšđčćž]+)? \\(((19|20)\\d{2}\\.[a-z]?)(;[^()]*)?\\)", txt1, perl = TRUE))[[1]]
allcit <- c(cit, cit2)
## split multi citations on ;
parts <- unlist(strsplit(allcit, ";"))
parts <- gsub("[()]", "", parts); parts <- trimws(parts)
citkey <- function(p) {
  yr <- regmatches(p, regexpr("(19|20)\\d{2}\\.[a-z]?", p))
  if (!length(yr)) return(NA)
  nm <- trimws(sub("(19|20)\\d{2}\\..*$", "", p))
  nm <- sub(",.*$", "", nm)
  first <- sub("^(\\S+).*", "\\1", nm)
  first <- sub("[’'].*$", "", first)
  paste(first, sub("\\.$", "", yr))
}
ck <- na.omit(sapply(parts, citkey, USE.NAMES = FALSE))
cktab <- table(ck)
say("| In text citation key | Count | In bibliography |"); say("|---|---|---|")
for (k in names(cktab)) {
  surname <- sub(" .*$", "", k); yr <- sub("^.* ", "", k)
  found <- any(grepl(paste0("^", surname), keys) & grepl(yr, keys, fixed = TRUE))
  say("| ", k, " | ", cktab[[k]], " | ", if (found) "yes" else "NO", " |")
}
say("")
say("Bibliography entries never cited in the body text (by surname and year).")
say("")
for (i in seq_along(keys)) {
  surname <- sub(" .*$", "", keys[i]); yr <- sub("^.* ", "", keys[i])
  hit <- any(grepl(paste0("^", surname), names(cktab)) & grepl(yr, names(cktab), fixed = TRUE))
  if (!hit) say("* ", substr(entries[i], 1, 110))
}
say("")

## 5. URLs ---------------------------------------------------------------------------
say("## 5. URLs in the book")
say("")
alltxt <- paste(unlist(pages), collapse = "\n")
## join URLs broken across lines inside footnotes and bibliography is unreliable; collect candidate URLs from single lines and from the bibliography entries joined above
urls <- unique(c(regmatches(alltxt, gregexpr("https?://[^\\s„“\"<>]+", alltxt))[[1]],
                 unlist(regmatches(entries, gregexpr("https?://[^\\s„“\"<>]+", entries)))))
urls <- sub("[.,;)]+$", "", urls)
say("Distinct URL strings found. ", length(urls), ". Those with a line break inside them are shown as fragments; the rendered book must be checked by eye for those.")
say("")
chk <- function(u) {
  r <- tryCatch(system2("curl", c("-sS", "-o", "/dev/null", "-L", "--max-time", "20", "-w", "%{http_code}", shQuote(u)), stdout = TRUE, stderr = TRUE), error = function(e) "ERR")
  paste(r, collapse = " ")
}
say("| URL | HTTP status (from this container; 000 or 403 may be the container proxy, not the site) |"); say("|---|---|")
for (u in urls) say("| ", u, " | ", chk(u), " |")
say("")

## 6. Footnote numbering per page ------------------------------------------------------
say("## 6. Footnotes")
say("")
fn_pages <- which(sapply(pages, function(p) any(grepl("^\\s{1,3}\\d{1,2}\\s*$", p) | grepl("^\\s{0,4}\\d{1,2}\\s+https?://", p))))
say("Pages with footnote blocks detected. ", paste(fn_pages, collapse = ", "), " (PDF page numbers). Check by eye that footnote marks in the text match.")
say("")

## 7. Running headers vs chapter boundaries -------------------------------------------
say("## 7. Running headers")
say("")
hdr <- sapply(pages, function(p) { p2 <- p[nzchar(trimws(p))]; if (length(p2)) trimws(p2[1]) else "" })
say("Even page running headers should equal the chapter title. Pages where the first line is not a known chapter title and not a section name are listed for manual check.")
titles <- c("Zašto statistika","Mjerenje i istraživački dizajn","Kako brojke zavode","Sažimanje podataka","Vizualizacija kao argument","Povezanost","Vjerojatnost koliko treba","Uzorkovanje","Procjena","Logika testiranja","Veličina učinka i snaga","Kriza i obnova","Kategorički podaci","Uspoređivanje dviju grupa","Uspoređivanje više grupa","Regresija — opći okvir","Statistika u doba algoritama","Vaše prvo istraživanje","Provjere za samostalan rad","Literatura","Predgovor","Sadržaj")
odd <- which(seq_along(hdr) %% 2 == 0 & !(hdr %in% titles) & nzchar(hdr))
say("")
for (i in odd) say("* PDF page ", i, " (printed ", i - 4, ") first line is „", hdr[i], "“")
say("")

## 8. Numeric spot checks ----------------------------------------------------------------
say("## 8. Numeric spot checks recomputed in R")
say("")
chk_num <- function(label, expr, shown) { v <- eval(expr); say("| ", label, " | ", format(v, digits = 6), " | ", shown, " | ", if (isTRUE(all.equal(round(v, 2), round(shown, 2)))) "match" else "CHECK", " |") }
say("| Quantity | Recomputed | Shown in book | Verdict |"); say("|---|---|---|---|")
chk_num("Ch1 share willing to pay, tisak 1289/4855 (percent)", quote(100*1289/4855), 26.55)
chk_num("Ch1 share willing to pay, portal 3514/15101 (percent)", quote(100*3514/15101), 23.27)
chk_num("Ch1 weighted mean (10*220+100*60)/110", quote((10*220+100*60)/110), 74.55)
chk_num("Ch4 ln(69)", quote(log(69)), 4.23)
chk_num("Ch8 SE ratio 6.19/1.79", quote(6.19/1.79), 3.46)
chk_num("Ch8 sqrt(12)", quote(sqrt(12)), 3.46)
chk_num("Ch13 83/197", quote(83/197), 0.42)
chk_num("Ch17 22/122 (percent)", quote(100*22/122), 18.0)
chk_num("Ch17 1/150 (percent)", quote(100*1/150), 0.7)
say("")
say("Lines in the book containing these quantities, for the reviewer to confirm what is actually printed.")
say("")
for (pat in c("1\\.289", "3\\.514", "220 \\+ 100", "ln\\(69\\)", "6,19", "83 podijeljeno", "22 od 122", "0,7 %")) {
  hits <- grep(pat, body_all, value = TRUE)
  for (h in head(hits, 3)) say("* `", pat, "` → ", trimws(h))
}
say("")

## 9. Provjere coverage -------------------------------------------------------------------
say("## 9. Coverage of Provjere za samostalan rad")
say("")
prov <- readLines("chapters/19_provjere.txt", encoding = "UTF-8", warn = FALSE)
heads <- grep("^\\s*Poglavlje \\d+", prov, value = TRUE)
say("Headings found. ", paste(trimws(heads), collapse = "; "))
covered <- sort(unique(as.integer(sub("^\\s*Poglavlje (\\d+).*", "\\1", heads))))
say("")
say("Chapters with at least one check. ", paste(covered, collapse = ", "), ". Chapters without any. ", paste(setdiff(1:18, covered), collapse = ", "))
say("")

## 10. Terminology consistency counts ------------------------------------------------------
say("## 10. Terminology variants (counts across the body text)")
say("")
terms <- list(c("standardna pogreška", "standardna greška"), c("interval pouzdanosti", "interval povjerenja"), c("uzoračka", "uzorkovna"), c("raspodjela", "distribucija"), c("aritmetička sredina", "prosjek"), c("p-vrijednost", "P-vrijednost", "p vrijednost"), c("nulta hipoteza", "nulti model"), c("95 %", "95%"), c("z-vrijednost", "standardizirana vrijednost"), c("randomizacija", "nasumična dodjela"), c("regresijski koeficijent", "nagib"))
say("| Variant | Count |"); say("|---|---|")
for (grp in terms) { for (t in grp) say("| ", t, " | ", sum(grepl(t, body_all, fixed = TRUE)), " |"); say("| | |") }
say("")

## 11. Captions without source statement ---------------------------------------------------
say("## 11. Figure and table captions without a source statement")
say("")
say("Captions are expected to end with „Izrada autora“, „Izvor“ or a citation. Captions spanning lines are joined with the following two lines.")
say("")
for (nm in names(chtxt)) {
  tx <- chtxt[[nm]]
  idx <- grep("^\\s*(Slika|Tablica) \\d+:", tx)
  for (i in idx) {
    cap <- paste(trimws(tx[i:min(i+3, length(tx))]), collapse = " ")
    if (!grepl("Izrada autor|Izvor|\\(.*(19|20)\\d{2}\\.|autora|prema", cap)) say("* ", nm, " ", substr(cap, 1, 140))
  }
}
say("")

## 12. Typography and print edition residue, the patterns this audit found -----------
say("## 12. Typography and print edition residue")
say("")
pat <- list(
  "decimal comma rendered with a space (math mode, use icomma)" = "[0-9], [0-9]",
  "hyphen used as minus before a number"                       = "(^|[ (])-[0-9]",
  "true minus sign before a number"                            = "−[0-9]",
  "thousands with a point (prose style)"                       = "[0-9]\\.[0-9]{3}\\b",
  "thousands with a space (table style)"                       = "[0-9] [0-9]{3}\\b",
  "raw triple hyphen (header or smart dash failure)"           = "---",
  "interactive residue (prikaz, kontrol, interakcij, digitaln, program)" =
    "(?i)(u početnom prikazu|promjenom prikaza|kontrole mijenjaju|za ovu interakciju|digitalnom prikazu|\\bprogram iz\\b|klizač)",
  "missing glyph or slashed zero in extracted figure text"     = "[☐□Ø][0-9]{3}")
say("| Pattern | Lines | First hits (chapter file, text) |"); say("|---|---|---|")
for (nm in names(pat)) {
  hits <- unlist(lapply(names(chtxt), function(f) {
    l <- grep(pat[[nm]], chtxt[[f]], perl = TRUE, value = TRUE)
    l <- l[!grepl("^<<<<<", l)]
    if (length(l)) paste0(sub("\\.txt$", "", f), " „", trimws(substr(l, 1, 60)), "“") else character()
  }))
  say("| ", nm, " | ", length(hits), " | ", paste(head(hits, 3), collapse = "; "), " |")
}
say("")
say("Run headers on even pages should equal the chapter title; see section 7. Captions repeated on a following page are listed in section 1 as duplicated numbers.")

writeLines(out, "results/round4_mechanical.md")
cat("written results/round4_mechanical.md with", length(out), "lines\n")
