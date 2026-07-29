# theme_book.R --------------------------------------------------------------
# ggplot2 tema i paleta knjige.
#
# JEDINI IZVOR ISTINE ZA BOJE JE design-tokens.yml. Ova datoteka ga ČITA, ne
# prepisuje — pa promjena dizajna u design-tokens.yml automatski mijenja i grafove.
# Ako yaml paket nije dostupan (npr. minimalan CI), koristi se ugrađeni
# rezervni skup identičan trenutnom design-tokens.yml.
#
# Učitava se automatski preko R/setup.R.
# ---------------------------------------------------------------------------

library(ggplot2)

# --- tokeni iz design-tokens.yml ---------------------------------------------------
.ucitaj_tokene <- function() {
  rezerva <- c(
    paper        = "#FFFFFF",
    `paper-soft` = "#F4F4F5",
    ink          = "#18181B",
    `ink-soft`   = "#3F3F46",
    `ink-mute`   = "#71717A",
    `ink-faint`  = "#A1A1AA",
    accent       = "#2563A8",
    `accent-deep`= "#1B4A7D",
    `accent-wash`= "#E8F0F8",
    emphasis     = "#9C2B2B",
    archival     = "#8A6D3B"
  )
  put <- file.path(getwd(), "design-tokens.yml")
  if (!requireNamespace("yaml", quietly = TRUE) || !file.exists(put)) return(rezerva)
  out <- tryCatch({
    p <- yaml::read_yaml(put)$color$palette
    unlist(p)
  }, error = function(e) rezerva)
  if (length(out) == 0) rezerva else out
}

tok <- .ucitaj_tokene()

# Kratki pristupnik: tok_boja("accent")
tok_boja <- function(ime) {
  v <- tok[[ime]]
  if (is.null(v)) stop("Nepoznat token boje: ", ime)
  unname(v)
}

# --- paleta za grafove ------------------------------------------------------
# Redoslijed je namjeran: prva boja nosi glavnu seriju, druga kontrast,
# treća arhivski akcent, dalje neutrali. Nikad ne upisujte hex u poglavlje —
# koristite boje_knjige ili scale_*_knjiga().
boje_knjige <- c(
  glavna    = tok_boja("accent"),
  kontrast  = tok_boja("emphasis"),
  treca     = tok_boja("archival"),
  duboka    = tok_boja("accent-deep"),
  neutral   = tok_boja("ink-mute"),
  tamna     = tok_boja("ink-soft")
)

# Sivi niz za tiskane blizance grafova (v. notes/pdf-charts-spec.md).
sivo <- c("#1A1A1A", "#4D4D4D", "#7A7A7A", "#A6A6A6", "#CCCCCC")

# --- tema -------------------------------------------------------------------
# Pozadina je prozirna: boju stranice određuje samo jedno mjesto po formatu
# (CSS za web, \pagecolor u tex/theme.tex za PDF), pa graf nikad ne iscrta
# bijeli pravokutnik na obojanoj stranici.
theme_knjiga <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      text             = element_text(color = tok_boja("ink")),
      plot.background  = element_rect(fill = NA, color = NA),
      panel.background = element_rect(fill = NA, color = NA),
      plot.title       = element_text(face = "bold", size = rel(1.15), hjust = 0),
      plot.subtitle    = element_text(color = tok_boja("ink-mute"), size = rel(0.9),
                                      margin = margin(b = 10)),
      plot.caption     = element_text(color = tok_boja("ink-mute"), size = rel(0.75),
                                      hjust = 1),
      panel.grid.minor   = element_blank(),
      panel.grid.major.x = element_blank(),
      panel.grid.major.y = element_line(color = tok_boja("ink-faint"), linewidth = 0.25),
      axis.title  = element_text(size = rel(0.85), color = tok_boja("ink-soft")),
      axis.text   = element_text(color = tok_boja("ink-mute")),
      legend.position = "top",
      legend.title    = element_text(face = "bold", size = rel(0.85)),
      plot.margin     = margin(10, 10, 10, 10)
    )
}

scale_fill_knjiga  <- function(...) scale_fill_manual(values = unname(boje_knjige), ...)
scale_color_knjiga <- function(...) scale_color_manual(values = unname(boje_knjige), ...)
scale_colour_knjiga <- scale_color_knjiga

scale_fill_sivo  <- function(...) scale_fill_manual(values = sivo, ...)
scale_color_sivo <- function(...) scale_color_manual(values = sivo, ...)
