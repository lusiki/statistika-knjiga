# theme_book.R --------------------------------------------------------------
# ggplot2 tema i paleta knjige.
#
# JEDINI IZVOR ISTINE ZA BOJE JE design-tokens.yml. Ova datoteka ga ČITA, ne
# prepisuje — pa promjena dizajna u design-tokens.yml automatski mijenja i grafove.
# Ako yaml paket nije dostupan (npr. minimalan CI), koristi se ugrađeni
# rezervni skup identičan trenutnom design-tokens.yml.
#
# DVA PRAVILA KOJA OVA DATOTEKA NOSI
#   1. Paleta podataka poredana je po SVJETLINI, ne po tonu. Tiskani blok je
#      crno-bijel; ovih pet boja u njemu postaju pet razlučivih sivih. Treba
#      li serija više od pet razina, mijenja se oblik točke ili uzorak ispune.
#   2. Oker NIJE boja podataka. On znači „ovo se može dodirnuti" i u grafu se
#      pojavljuje samo kad se jedna serija namjerno ističe — skala_naglasak().
#
# Učitava se automatski preko R/setup.R.
# ---------------------------------------------------------------------------

library(ggplot2)
suppressPackageStartupMessages(library(grid))

# --- tokeni iz design-tokens.yml -------------------------------------------
.ucitaj_tokene <- function() {
  rezerva <- c(
    paper         = "#FBFAF6",
    `paper-soft`  = "#F3EFE6",
    surface       = "#FFFFFF",
    ink           = "#16150F",
    `ink-soft`    = "#33322A",
    `ink-mute`    = "#6E6C61",
    `ink-faint`   = "#9B9789",
    rule          = "#E4DFD2",
    `rule-soft`   = "#EFEBE0",
    accent        = "#C08A16",
    `accent-deep` = "#8A6212",
    `accent-dark` = "#5C4109",
    `accent-wash` = "#FAF2DE",
    `data-1`      = "#16150F",
    `data-2`      = "#40566B",
    `data-3`      = "#8A6212",
    `data-4`      = "#9B9789",
    `data-5`      = "#C9C2B0",
    alert         = "#8A2A12"
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

# --- pisma ------------------------------------------------------------------
# Newsreader (naslovi) · Public Sans (osi i legende) · JetBrains Mono (brojke).
# Ako showtext/sysfonts nisu dostupni ili pismo ne uspije registrirati, tema
# tiho pada na sistemska pisma. Graf se uvijek nacrta.
.st_fontovi <- new.env(parent = emptyenv())
.st_fontovi$ok <- FALSE

ucitaj_fontove <- function(google = TRUE) {
  if (.st_fontovi$ok) return(invisible(TRUE))
  if (!requireNamespace("showtext", quietly = TRUE) ||
      !requireNamespace("sysfonts", quietly = TRUE)) return(invisible(FALSE))

  trazena <- c("Newsreader", "Public Sans", "JetBrains Mono")
  if (google) {
    for (f in trazena) {
      if (f %in% sysfonts::font_families()) next
      try(sysfonts::font_add_google(f, f), silent = TRUE)
    }
  }
  if (!all(trazena %in% sysfonts::font_families())) return(invisible(FALSE))

  showtext::showtext_auto()
  showtext::showtext_opts(dpi = 300)
  .st_fontovi$ok <- TRUE
  invisible(TRUE)
}

# Vrati ime pisma samo ako je stvarno registrirano; inače "" (zadano ggplotovo).
.pismo <- function(uloga = c("displej", "sucelje", "mono")) {
  uloga <- match.arg(uloga)
  if (!.st_fontovi$ok) return("")
  switch(uloga,
         displej = "Newsreader",
         sucelje = "Public Sans",
         mono    = "JetBrains Mono")
}

# --- paleta za grafove ------------------------------------------------------
# Poredana po svjetlini (8 % → 78 %) da preživi pretvorbu u sivo. Nikad ne
# upisujte hex u poglavlje — koristite boje_knjige ili scale_*_knjiga().
boje_knjige <- c(
  tinta      = tok_boja("data-1"),
  skriljevac = tok_boja("data-2"),
  oker       = tok_boja("data-3"),
  siva       = tok_boja("data-4"),
  blijeda    = tok_boja("data-5")
)

# Sekvencijalna i divergentna, obje sigurne u sivim tonovima.
paleta_seq <- c(tok_boja("accent-wash"), "#E4C97E", tok_boja("accent"),
                tok_boja("accent-deep"), tok_boja("accent-dark"))
paleta_div <- c(tok_boja("data-2"), "#8FA0AE", tok_boja("rule-soft"),
                "#D9AE55", tok_boja("accent-deep"))

# Sivi niz za tiskane blizance grafova (v. notes/pdf-charts-spec.md).
sivo <- c("#1A1A1A", "#4D4D4D", "#7A7A7A", "#A6A6A6", "#CCCCCC")

# --- tema -------------------------------------------------------------------
# Pozadina je prozirna: boju stranice određuje samo jedno mjesto po formatu
# (CSS za web, \pagecolor u tex/theme.tex za PDF), pa graf nikad ne iscrta
# bijeli pravokutnik na obojanoj stranici.
#
# @param base_size osnovna veličina teksta u točkama
# @param mreza     "y" (zadano), "x", "oboje" ili "bez"
theme_knjiga <- function(base_size = 11, mreza = "y") {
  tinta  <- tok_boja("ink")
  prigus <- tok_boja("ink-mute")
  slaba  <- tok_boja("ink-faint")
  linija <- tok_boja("rule")

  t <- theme_minimal(base_size = base_size, base_family = .pismo("sucelje")) +
    theme(
      # ploha — prozirna u oba formata
      text             = element_text(colour = tok_boja("ink-soft")),
      plot.background  = element_rect(fill = NA, colour = NA),
      panel.background = element_rect(fill = NA, colour = NA),
      panel.border     = element_blank(),

      # mreža: vlas linija, samo ondje gdje pomaže očitati vrijednost
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(colour = linija, linewidth = 0.3),

      # osi: jedna crta na dnu, bez okvira i bez crtica
      axis.line.x = element_line(colour = tinta, linewidth = 0.4),
      axis.line.y = element_blank(),
      axis.ticks  = element_blank(),
      # brojke su uvijek mono
      axis.text   = element_text(family = .pismo("mono"),
                                 size = rel(0.82), colour = prigus),
      axis.title  = element_text(size = rel(0.86), colour = prigus, hjust = 0),
      axis.title.x = element_text(margin = margin(t = 9)),
      axis.title.y = element_text(margin = margin(r = 9), angle = 90),

      # naslovi: displejni serif, svijetli rez, nikad bold
      plot.title    = element_text(family = .pismo("displej"), face = "plain",
                                   size = rel(1.45), colour = tinta,
                                   hjust = 0, margin = margin(b = 5)),
      plot.subtitle = element_text(size = rel(0.95), colour = prigus, hjust = 0,
                                   margin = margin(b = 14), lineheight = 1.35),
      plot.caption  = element_text(family = .pismo("mono"), size = rel(0.72),
                                   colour = slaba, hjust = 0,
                                   margin = margin(t = 14)),
      plot.title.position   = "plot",
      plot.caption.position = "plot",
      plot.margin           = margin(6, 6, 6, 6),

      # legenda: vodoravno pod naslovom, bez okvira i bez naslova
      legend.position      = "top",
      legend.justification = "left",
      legend.direction     = "horizontal",
      legend.title         = element_blank(),
      legend.text          = element_text(size = rel(0.82), colour = prigus),
      legend.key           = element_blank(),
      legend.margin        = margin(0, 0, 8, 0),
      legend.box.spacing   = unit(0, "pt"),

      # faceti: oznaka kao mono verzal, bez sive trake
      strip.background = element_blank(),
      strip.text       = element_text(family = .pismo("mono"), size = rel(0.74),
                                      colour = tinta, hjust = 0,
                                      margin = margin(b = 6)),
      panel.spacing    = unit(18, "pt")
    )

  if (mreza == "y")   t <- t + theme(panel.grid.major.x = element_blank())
  if (mreza == "x")   t <- t + theme(panel.grid.major.y = element_blank())
  if (mreza == "bez") t <- t + theme(panel.grid.major = element_blank())
  t
}

# --- skale ------------------------------------------------------------------
scale_fill_knjiga   <- function(...) scale_fill_manual(values = unname(boje_knjige), ...)
scale_color_knjiga  <- function(...) scale_color_manual(values = unname(boje_knjige), ...)
scale_colour_knjiga <- scale_color_knjiga

scale_fill_knjiga_c   <- function(...) scale_fill_gradientn(colours = paleta_seq, ...)
scale_color_knjiga_c  <- function(...) scale_color_gradientn(colours = paleta_seq, ...)
scale_colour_knjiga_c <- scale_color_knjiga_c

scale_fill_div  <- function(...) scale_fill_gradientn(colours = paleta_div, ...)
scale_color_div <- function(...) scale_color_gradientn(colours = paleta_div, ...)

scale_fill_sivo  <- function(...) scale_fill_manual(values = sivo, ...)
scale_color_sivo <- function(...) scale_color_manual(values = sivo, ...)
scale_colour_sivo <- scale_color_sivo

#' Naglasak: jedna serija u okeru, sve ostale prigušene.
#'
#' Jedini legitiman način da oker uđe u graf — i tada znači „gledajte ovo",
#' ne „ovo je kategorija A".
#'
#'   skala_naglasak("Hrvatska", razine = levels(d$zemlja))
skala_naglasak <- function(istaknuto, razine,
                           boja   = tok_boja("accent"),
                           ostalo = tok_boja("data-5"),
                           tip    = c("colour", "fill")) {
  tip <- match.arg(tip)
  v <- stats::setNames(rep(ostalo, length(razine)), razine)
  v[istaknuto] <- boja
  if (tip == "fill") scale_fill_manual(values = v) else scale_color_manual(values = v)
}

#' Hrvatski zapis broja na osima: decimalni zarez, razmak za tisućice.
#' scale_y_continuous(labels = hr_broj)
hr_broj <- function(x, decimala = 1) {
  format(round(x, decimala), big.mark = " ", decimal.mark = ",",
         trim = TRUE, nsmall = decimala)
}

# --- zadano za cijelu knjigu ------------------------------------------------
# Geom zadane vrijednosti: podaci su u tinti, ne u okeru. Ispune stupaca idu
# u najsvjetliji ton palete da tekst iznad njih ostane čitljiv.
postavi_temu <- function() {
  theme_set(theme_knjiga())
  try({
    update_geom_defaults("point",  list(colour = tok_boja("ink"), size = 1.7, alpha = 0.85))
    update_geom_defaults("line",   list(colour = tok_boja("ink"), linewidth = 0.6))
    update_geom_defaults("bar",    list(fill = tok_boja("data-4")))
    update_geom_defaults("col",    list(fill = tok_boja("data-4")))
    update_geom_defaults("smooth", list(colour = tok_boja("accent"), linewidth = 0.7))
    update_geom_defaults("text",   list(family = .pismo("mono"), size = 3,
                                        colour = tok_boja("ink-mute")))
  }, silent = TRUE)
  invisible(TRUE)
}

#' Spremi statičnog blizanca widgeta: SVG za web, PDF za tisak.
#' spremi_figuru(p, "08-clt", visina = 4)
spremi_figuru <- function(plot, naziv, sirina = 6.6, visina = 4.0,
                          mapa = "images") {
  dir.create(mapa, showWarnings = FALSE, recursive = TRUE)
  ggsave(file.path(mapa, paste0(naziv, ".svg")), plot,
         width = sirina, height = visina, device = "svg", bg = "transparent")
  ggsave(file.path(mapa, paste0(naziv, ".pdf")), plot,
         width = sirina, height = visina, device = grDevices::cairo_pdf, bg = "transparent")
  invisible(file.path(mapa, naziv))
}
