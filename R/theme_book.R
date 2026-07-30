# theme_book.R --------------------------------------------------------------
# ggplot2 tema i paleta knjige.
#
# JEDINI IZVOR ISTINE ZA BOJE JE design-tokens.yml. Ova datoteka ga ČITA, ne
# prepisuje — pa promjena dizajna u design-tokens.yml automatski mijenja i grafove.
# Ako yaml paket nije dostupan (npr. minimalan CI), koristi se ugrađeni
# rezervni skup identičan trenutnom design-tokens.yml. Tamna inačica čita
# uloge iz styles/_dark.scss kako se vrijednosti ne bi prepisivale u R-u.
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

# Tamni tokeni legitimno žive u styles/_dark.scss (DESIGN.md §2). Čitamo samo
# jednostavne $tok-ime: #RRGGBB deklaracije; izvedene rgba vrijednosti temi
# grafova nisu potrebne.
.ucitaj_tamne_tokene <- function(svijetli = tok) {
  put <- file.path(getwd(), "styles", "_dark.scss")
  if (!file.exists(put)) return(svijetli)

  redci <- readLines(put, warn = FALSE, encoding = "UTF-8")
  uzorak <- "^\\s*\\$tok-([[:alnum:]-]+):\\s*(#[[:xdigit:]]{6})\\s*;"
  pogodak <- regexec(uzorak, redci)
  dijelovi <- regmatches(redci, pogodak)
  dijelovi <- dijelovi[lengths(dijelovi) == 3L]
  if (length(dijelovi) == 0L) return(svijetli)

  tamni <- stats::setNames(
    vapply(dijelovi, `[[`, character(1), 3L),
    vapply(dijelovi, `[[`, character(1), 2L)
  )
  potrebni <- names(svijetli)
  nedostaju <- setdiff(potrebni, names(tamni))
  if (length(nedostaju) > 0L) {
    tamni[nedostaju] <- svijetli[nedostaju]
  }
  tamni[potrebni]
}

tok_tamno <- .ucitaj_tamne_tokene()

# Kratki pristupnik: tok_boja("accent") ili tok_boja("ink", "tamna").
tok_boja <- function(ime, varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  skup <- if (varijanta == "tamna") tok_tamno else tok
  v <- skup[[ime]]
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
# Poredana po svjetlini da preživi pretvorbu u sivo. Automatska paleta je
# namjerno neutralna: data-3 je oker i zato ostaje izvan običnog kodiranja
# kategorija. Oker ulazi samo kroz skala_naglasak().
.paleta_diskretna <- function(varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  c(
    tinta      = tok_boja("data-1", varijanta),
    skriljevac = tok_boja("data-2", varijanta),
    prigusena  = tok_boja("ink-mute", varijanta),
    siva       = tok_boja("data-4", varijanta),
    blijeda    = tok_boja("data-5", varijanta)
  )
}

boje_knjige <- .paleta_diskretna("svijetla")
boje_knjige_tamne <- .paleta_diskretna("tamna")

# Sekvencijalna i divergentna skala također su neutralne. Naglasak nije
# završna točka ljestvice, nego zasebna semantička odluka.
.paleta_sekvencijalna <- function(varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  c(
    tok_boja("rule-soft", varijanta),
    tok_boja("data-5", varijanta),
    tok_boja("data-4", varijanta),
    tok_boja("data-2", varijanta),
    tok_boja("data-1", varijanta)
  )
}

.paleta_divergentna <- function(varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  c(
    tok_boja("data-2", varijanta),
    tok_boja("data-4", varijanta),
    tok_boja("rule-soft", varijanta),
    tok_boja("ink-mute", varijanta),
    tok_boja("data-1", varijanta)
  )
}

paleta_seq <- .paleta_sekvencijalna("svijetla")
paleta_div <- .paleta_divergentna("svijetla")

# Sivi niz za tiskane blizance grafova (v. notes/pdf-charts-spec.md).
sivo <- c("#1A1A1A", "#4D4D4D", "#7A7A7A", "#A6A6A6", "#CCCCCC")

# --- tema -------------------------------------------------------------------
# Pozadina je prozirna: boju stranice određuje samo jedno mjesto po formatu
# (CSS za web, \pagecolor u tex/theme.tex za PDF), pa graf nikad ne iscrta
# bijeli pravokutnik na obojanoj stranici.
#
# @param base_size osnovna veličina teksta u točkama
# @param mreza     "y" (zadano), "x", "oboje" ili "bez"
# @param varijanta paleta za svijetlu ili tamnu HTML inačicu
theme_knjiga <- function(base_size = 12.5, mreza = "y",
                         varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  tinta  <- tok_boja("ink", varijanta)
  tekst  <- tok_boja("ink-soft", varijanta)
  prigus <- tok_boja("ink-mute", varijanta)
  slaba  <- tok_boja("ink-faint", varijanta)
  linija <- tok_boja("rule", varijanta)

  t <- theme_minimal(base_size = base_size, base_family = .pismo("sucelje")) +
    theme(
      # ploha — prozirna u oba formata
      text             = element_text(colour = tekst),
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
                                 size = rel(0.92), colour = prigus),
      axis.title  = element_text(size = rel(0.92), colour = prigus, hjust = 0),
      axis.title.x = element_text(margin = margin(t = 9)),
      axis.title.y = element_text(margin = margin(r = 9), angle = 90),

      # naslovi: displejni serif, svijetli rez, nikad bold
      plot.title    = element_text(family = .pismo("displej"), face = "plain",
                                   size = rel(1.35), colour = tinta,
                                   hjust = 0, margin = margin(b = 5)),
      plot.subtitle = element_text(size = rel(0.92), colour = prigus, hjust = 0,
                                   margin = margin(b = 14), lineheight = 1.35),
      plot.caption  = element_text(family = .pismo("mono"), size = rel(0.78),
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
      legend.text          = element_text(size = rel(0.9), colour = prigus),
      legend.key           = element_blank(),
      legend.margin        = margin(0, 0, 8, 0),
      legend.box.spacing   = unit(0, "pt"),

      # faceti: oznaka kao mono verzal, bez sive trake
      strip.background = element_blank(),
      strip.text       = element_text(family = .pismo("mono"), size = rel(0.82),
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
scale_fill_knjiga <- function(..., varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  scale_fill_manual(values = unname(.paleta_diskretna(varijanta)), ...)
}
scale_color_knjiga <- function(..., varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  scale_color_manual(values = unname(.paleta_diskretna(varijanta)), ...)
}
scale_colour_knjiga <- scale_color_knjiga

scale_fill_knjiga_c <- function(..., varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  scale_fill_gradientn(colours = .paleta_sekvencijalna(varijanta), ...)
}
scale_color_knjiga_c <- function(..., varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  scale_color_gradientn(colours = .paleta_sekvencijalna(varijanta), ...)
}
scale_colour_knjiga_c <- scale_color_knjiga_c

scale_fill_div <- function(..., varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  scale_fill_gradientn(colours = .paleta_divergentna(varijanta), ...)
}
scale_color_div <- function(..., varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  scale_color_gradientn(colours = .paleta_divergentna(varijanta), ...)
}

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
                           boja = NULL, ostalo = NULL,
                           tip = c("colour", "fill"),
                           varijanta = c("svijetla", "tamna")) {
  tip <- match.arg(tip)
  varijanta <- match.arg(varijanta)
  if (is.null(boja)) boja <- tok_boja("accent", varijanta)
  if (is.null(ostalo)) ostalo <- tok_boja("data-5", varijanta)
  v <- stats::setNames(rep(ostalo, length(razine)), razine)
  v[istaknuto] <- boja
  if (tip == "fill") scale_fill_manual(values = v) else scale_color_manual(values = v)
}

#' Hrvatski zapis broja na osima: decimalni zarez, razmak za tisućice.
#' scale_y_continuous(labels = hr_broj)
hr_broj <- function(x, decimala = 1) {
  if (!is.numeric(decimala) || length(decimala) != 1L ||
      !is.finite(decimala) || decimala < 0 || decimala %% 1 != 0) {
    stop("`decimala` mora biti jedan nenegativan cijeli broj.")
  }
  format(
    round(x, decimala),
    scientific = FALSE,
    big.mark = "\u202f",
    decimal.mark = ",",
    trim = TRUE,
    nsmall = as.integer(decimala)
  )
}

# --- zadano za cijelu knjigu ------------------------------------------------
# Geom zadane vrijednosti: podaci su u tinti, ne u okeru. Ispune stupaca idu
# u najsvjetliji ton palete da tekst iznad njih ostane čitljiv.
.st_tema <- new.env(parent = emptyenv())
.st_tema$varijanta <- "svijetla"
.st_tema$base_size <- 12.5

.azuriraj_geom <- function(geom, vrijednosti) {
  try(update_geom_defaults(geom, vrijednosti), silent = TRUE)
}

postavi_temu <- function(varijanta = c("svijetla", "tamna"),
                         base_size = 12.5) {
  varijanta <- match.arg(varijanta)
  tinta <- tok_boja("ink", varijanta)
  prigus <- tok_boja("ink-mute", varijanta)
  blijeda <- tok_boja("data-5", varijanta)

  theme_set(theme_knjiga(base_size = base_size, varijanta = varijanta))

  .azuriraj_geom("point", list(
    colour = tinta, fill = NA, size = 2, alpha = 0.82
  ))
  .azuriraj_geom("line", list(
    colour = tinta, linewidth = 0.65
  ))
  .azuriraj_geom("path", list(
    colour = tinta, linewidth = 0.65
  ))
  for (geom in c("segment", "abline", "hline", "vline",
                 "errorbar", "linerange", "pointrange")) {
    .azuriraj_geom(geom, list(colour = prigus, linewidth = 0.55))
  }
  for (geom in c("bar", "col", "boxplot", "violin")) {
    .azuriraj_geom(geom, list(fill = tok_boja("data-4", varijanta)))
  }
  .azuriraj_geom("density", list(
    colour = tok_boja("data-2", varijanta),
    fill = blijeda,
    linewidth = 0.65,
    alpha = 0.35
  ))
  .azuriraj_geom("ribbon", list(fill = blijeda, alpha = 0.35))
  .azuriraj_geom("area", list(fill = blijeda, alpha = 0.55))
  .azuriraj_geom("smooth", list(
    colour = tok_boja("data-2", varijanta),
    fill = blijeda,
    linewidth = 0.75,
    alpha = 0.3
  ))
  .azuriraj_geom("text", list(
    family = .pismo("mono"), size = 3.3, colour = prigus
  ))
  .azuriraj_geom("label", list(
    family = .pismo("mono"), size = 3.3, colour = prigus,
    fill = tok_boja("surface", varijanta)
  ))

  .st_tema$varijanta <- varijanta
  .st_tema$base_size <- base_size
  invisible(TRUE)
}

#' Iscrtaj postojeći ggplot u odabranoj varijanti i zatim vrati prethodnu temu.
#'
#' Služi za drugi, tamni HTML asset. Ako graf ima ručnu skalu, tamnom mu
#' pozivu treba dodati istu skalu s `varijanta = "tamna"`.
.prevedi_boju_teme <- function(vrijednost,
                               iz = tok,
                               u = tok_tamno) {
  if (!is.character(vrijednost)) return(vrijednost)
  indeks <- match(toupper(vrijednost), toupper(unname(iz)))
  zamijeni <- !is.na(indeks)
  vrijednost[zamijeni] <- unname(u[indeks[zamijeni]])
  vrijednost
}

.plot_za_varijantu <- function(plot,
                               varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  if (varijanta == "svijetla" || length(plot$theme) == 0L) return(plot)

  # Mijenjaju se samo semantičke boje u postojećim elementima teme. Tako tamni
  # asset zadržava autorove odluke o mreži, legendi, veličini i marginama.
  polja_boje <- c("colour", "color", "fill", "ink", "paper", "accent")
  for (ime in names(plot$theme)) {
    element <- plot$theme[[ime]]
    if (is.null(element) || !inherits(element, "element")) next
    for (polje in polja_boje) {
      vrijednost <- tryCatch(
        element[[polje]],
        error = function(cnd) NULL
      )
      if (is.null(vrijednost)) next
      element[[polje]] <- .prevedi_boju_teme(vrijednost)
    }
    plot$theme[[ime]] <- element
  }
  plot
}

iscrtaj_figuru <- function(plot, varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  prijasnja <- .st_tema$varijanta
  prijasnja_velicina <- .st_tema$base_size
  on.exit(postavi_temu(prijasnja, prijasnja_velicina), add = TRUE)

  postavi_temu(varijanta, prijasnja_velicina)
  print(.plot_za_varijantu(plot, varijanta))
  invisible(plot)
}

#' Spremi statičnog blizanca widgeta: SVG za web, PDF za tisak.
#' spremi_figuru(p, "08-clt", visina = 4)
spremi_figuru <- function(plot, naziv, sirina = 6.6, visina = 4.0,
                          mapa = "images",
                          varijanta = c("svijetla", "tamna")) {
  varijanta <- match.arg(varijanta)
  prijasnja <- .st_tema$varijanta
  prijasnja_velicina <- .st_tema$base_size
  on.exit(postavi_temu(prijasnja, prijasnja_velicina), add = TRUE)
  postavi_temu(varijanta, prijasnja_velicina)

  sufiks <- if (varijanta == "tamna") "-dark" else ""
  putanja <- file.path(mapa, paste0(naziv, sufiks))
  plot <- .plot_za_varijantu(plot, varijanta)
  dir.create(mapa, showWarnings = FALSE, recursive = TRUE)
  ggsave(paste0(putanja, ".svg"), plot,
         width = sirina, height = visina, device = "svg", bg = "transparent")
  ggsave(paste0(putanja, ".pdf"), plot,
         width = sirina, height = visina, device = grDevices::cairo_pdf, bg = "transparent")
  invisible(putanja)
}
