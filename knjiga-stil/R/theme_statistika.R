# ─────────────────────────────────────────────────────────────────────────────
#  theme_statistika.R — ggplot2 theme + palette for the book's figures
#
#  Every figure in the book uses this. It guarantees the two things the style
#  depends on: the book's typefaces, and a palette ordered by lightness so the
#  black & white print interior loses nothing.
#
#  Usage in a chapter:
#      source("knjiga-stil/R/theme_statistika.R")
#      ggplot(d, aes(x, y, colour = grupa)) + geom_point() +
#        skala_boja() + theme_statistika()
#
#  Fonts: install Newsreader, Literata, Public Sans, JetBrains Mono locally,
#  or let showtext fetch them from Google (see ucitaj_fontove()).
# ─────────────────────────────────────────────────────────────────────────────

suppressPackageStartupMessages({
  library(ggplot2)
  library(grid)
})

# ── Boje ─────────────────────────────────────────────────────────────────────
st_boje <- list(
  papir      = "#FBFAF6",
  papir_alt  = "#F3EFE6",
  ploha      = "#FFFFFF",
  tinta      = "#16150F",
  tekst      = "#33322A",
  prigusena  = "#6E6C61",
  slaba      = "#9B9789",
  linija     = "#E4DFD2",
  linija_m   = "#EFEBE0",
  oker       = "#C08A16",
  oker_tekst = "#8A6212",
  oker_ispun = "#FAF2DE"
)

# Poredano po svjetlini — preživljava pretvorbu u sivo
st_paleta <- c("#16150F", "#40566B", "#8A6212", "#9B9789", "#C9C2B0")

# Sekvencijalna i divergentna, obje sigurne u sivim tonovima
st_paleta_seq <- c("#FAF2DE", "#E4C97E", "#C08A16", "#8A6212", "#4A3408")
st_paleta_div <- c("#40566B", "#8FA0AE", "#EDE9DF", "#D9AE55", "#8A6212")

#' Fontovi. Pozovite jednom po sesiji prije crtanja.
ucitaj_fontove <- function(google = TRUE) {
  if (!requireNamespace("showtext", quietly = TRUE)) {
    warning("Paket showtext nije instaliran; koriste se sistemski fontovi.")
    return(invisible(FALSE))
  }
  if (google && requireNamespace("sysfonts", quietly = TRUE)) {
    try(sysfonts::font_add_google("Newsreader", "Newsreader"), silent = TRUE)
    try(sysfonts::font_add_google("Literata", "Literata"), silent = TRUE)
    try(sysfonts::font_add_google("Public Sans", "Public Sans"), silent = TRUE)
    try(sysfonts::font_add_google("JetBrains Mono", "JetBrains Mono"), silent = TRUE)
  }
  showtext::showtext_auto()
  showtext::showtext_opts(dpi = 300)
  invisible(TRUE)
}

# ── Tema ─────────────────────────────────────────────────────────────────────
#' @param base_size osnovna veličina teksta u točkama
#' @param tisak     TRUE za crno-bijeli blok (bijela podloga, sve u tinti)
#' @param mreza     "y" (zadano), "x", "oboje" ili "bez"
theme_statistika <- function(base_size = 10, tisak = FALSE, mreza = "y") {
  pozadina <- if (tisak) "#FFFFFF" else st_boje$papir
  tinta    <- st_boje$tinta
  prigus   <- if (tisak) "#5A584F" else st_boje$prigusena
  slaba    <- if (tisak) "#8A887F" else st_boje$slaba
  linija   <- if (tisak) "#D8D8D8" else st_boje$linija

  t <- theme_minimal(base_size = base_size, base_family = "Public Sans") +
    theme(
      # ploha
      plot.background   = element_rect(fill = pozadina, colour = NA),
      panel.background  = element_rect(fill = pozadina, colour = NA),
      panel.border      = element_blank(),

      # mreža: vlas, samo gdje pomaže čitanju vrijednosti
      panel.grid.minor  = element_blank(),
      panel.grid.major  = element_line(colour = linija, linewidth = 0.3),

      # osi: jedna crna linija na dnu, bez okvira
      axis.line.x       = element_line(colour = tinta, linewidth = 0.4),
      axis.line.y       = element_blank(),
      axis.ticks        = element_blank(),
      axis.text         = element_text(family = "JetBrains Mono",
                                       size = rel(0.82), colour = prigus),
      axis.title        = element_text(family = "Public Sans", size = rel(0.86),
                                       colour = prigus, hjust = 0),
      axis.title.x      = element_text(margin = margin(t = 9)),
      axis.title.y      = element_text(margin = margin(r = 9), angle = 90),

      # naslovi: displej serif, svijetli rez
      plot.title        = element_text(family = "Newsreader", face = "plain",
                                       size = rel(1.5), colour = tinta,
                                       hjust = 0, margin = margin(b = 5)),
      plot.subtitle     = element_text(family = "Public Sans", size = rel(0.95),
                                       colour = prigus, hjust = 0,
                                       margin = margin(b = 14), lineheight = 1.35),
      plot.caption      = element_text(family = "JetBrains Mono", size = rel(0.72),
                                       colour = slaba, hjust = 0,
                                       margin = margin(t = 14)),
      plot.caption.position = "plot",
      plot.title.position   = "plot",
      plot.margin       = margin(6, 6, 6, 6),

      # legenda: vodoravno pod naslovom, bez okvira i naslova
      legend.position   = "top",
      legend.justification = "left",
      legend.direction  = "horizontal",
      legend.title      = element_blank(),
      legend.text       = element_text(family = "Public Sans", size = rel(0.82),
                                       colour = prigus),
      legend.key        = element_blank(),
      legend.margin     = margin(0, 0, 8, 0),
      legend.box.spacing = unit(0, "pt"),

      # faceti: oznaka kao verzalni mono, bez sive trake
      strip.background  = element_blank(),
      strip.text        = element_text(family = "JetBrains Mono", size = rel(0.74),
                                       colour = tinta, hjust = 0,
                                       margin = margin(b = 6)),
      panel.spacing     = unit(18, "pt")
    )

  if (mreza == "y")     t <- t + theme(panel.grid.major.x = element_blank())
  if (mreza == "x")     t <- t + theme(panel.grid.major.y = element_blank())
  if (mreza == "bez")   t <- t + theme(panel.grid.major = element_blank())
  t
}

# ── Skale ────────────────────────────────────────────────────────────────────
skala_boja <- function(...) scale_colour_manual(values = st_paleta, ...)
skala_ispune <- function(...) scale_fill_manual(values = st_paleta, ...)
skala_boja_c <- function(...) scale_colour_gradientn(colours = st_paleta_seq, ...)
skala_ispune_c <- function(...) scale_fill_gradientn(colours = st_paleta_seq, ...)

#' Naglasak: jedna serija u okeru, sve ostale prigušene.
#' skala_naglasak("Hrvatska", razine = levels(d$zemlja))
skala_naglasak <- function(istaknuto, razine, boja = st_boje$oker,
                           ostalo = "#C9C2B0", aes_type = "colour") {
  v <- setNames(rep(ostalo, length(razine)), razine)
  v[istaknuto] <- boja
  if (aes_type == "fill") scale_fill_manual(values = v) else scale_colour_manual(values = v)
}

#' Hrvatski format brojeva na osima: decimalni zarez, razmak za tisućice.
hr_broj <- function(x, decimala = 1) {
  format(round(x, decimala), big.mark = " ", decimal.mark = ",",
         trim = TRUE, nsmall = decimala)
}

# ── Zadano za cijelu knjigu ──────────────────────────────────────────────────
postavi_temu <- function(tisak = FALSE) {
  theme_set(theme_statistika(tisak = tisak))
  update_geom_defaults("point",  list(colour = st_boje$tinta, size = 1.7, alpha = 0.85))
  update_geom_defaults("line",   list(colour = st_boje$tinta, linewidth = 0.6))
  update_geom_defaults("bar",    list(fill = st_boje$oker))
  update_geom_defaults("col",    list(fill = st_boje$oker))
  update_geom_defaults("smooth", list(colour = st_boje$oker, linewidth = 0.7))
  update_geom_defaults("text",   list(family = "JetBrains Mono", size = 3,
                                      colour = st_boje$prigusena))
  invisible(TRUE)
}

#' Spremi statičnog blizanca widgeta: SVG za web, PDF za tisak.
#' spremi_figuru(p, "08-clt", visina = 4)
spremi_figuru <- function(plot, naziv, sirina = 6.6, visina = 4.0,
                          mapa = "slike") {
  dir.create(mapa, showWarnings = FALSE, recursive = TRUE)
  ggsave(file.path(mapa, paste0(naziv, ".svg")), plot,
         width = sirina, height = visina, device = "svg")
  ggsave(file.path(mapa, paste0(naziv, ".pdf")),
         plot + theme_statistika(tisak = TRUE),
         width = sirina, height = visina, device = cairo_pdf)
  invisible(file.path(mapa, naziv))
}
