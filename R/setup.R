# setup.R -------------------------------------------------------------------
# Zajedničko podešavanje za sva poglavlja. Na vrh svakog poglavlja ide:
#
#   ```{r}
#   #| include: false
#   source("R/setup.R")
#   ```
#
# Sve što poglavlje treba (paketi, tema grafova, sjeme slučajnih brojeva)
# dolazi odavde, pa nijedno poglavlje ne postavlja vlastite opcije.
# ---------------------------------------------------------------------------

suppressPackageStartupMessages({
  library(ggplot2)
  library(dplyr)
  library(tidyr)
})

# Hrvatski zapis brojeva mora biti postavljen prije nego što ggplot2 izradi
# oznake osi ili poglavlje ispiše tablicu.
options(OutDec = ",", scipen = 999)

# Tema i paleta (čitaju design-tokens.yml).
source("R/theme_book.R")

# Knjižna pisma u grafovima. Ako showtext/sysfonts nisu instalirani ili
# preuzimanje ne uspije, tema tiho pada na sistemska pisma — graf se uvijek
# nacrta. Zato tryCatch, a ne stop.
.pisma_ok <- isTRUE(tryCatch(ucitaj_fontove(), error = function(e) FALSE))

# Tema + zadane vrijednosti geoma. Analitičke oznake su neutralne; oker ulazi
# u graf samo kada ga autor izričito zatraži kao naglasak.
postavi_temu(base_size = if (knitr::is_html_output()) 12.5 else 10)

# REPRODUCIBILNOST. Knjiga uči simulaciju prije formule, pa gotovo svaki
# statički graf uzorkuje. Fiksno sjeme znači da se ista slika ispisuje pri
# svakom renderu. Ako poglavlje treba drugo sjeme, postavlja ga lokalno.
set.seed(2026)

# HTML dobiva vektorski uređaj: SVG ostaje oštar pri širini tijela i na uskom
# zaslonu, a za razliku od starog PNG izlaza ne donosi bijelo platno. PDF i
# DOCX zadržavaju uređaje iz svojih profila.
.opcije_figure <- list(
  fig.align = "center",
  out.width = "100%",
  dpi = 300,
  fig.bg = "transparent",
  fig.showtext = .pisma_ok
)

if (knitr::is_html_output()) {
  .html_uredaj <- if (requireNamespace("svglite", quietly = TRUE)) {
    "svglite"
  } else if (capabilities("cairo")) {
    "svg"
  } else {
    "png"
  }
  .opcije_figure$dev <- .html_uredaj
  .opcije_figure$dev.args <- stats::setNames(
    list(list(bg = "transparent")),
    .html_uredaj
  )
}

do.call(knitr::opts_chunk$set, .opcije_figure)

# Promjena zajedničke teme mora poništiti predmemoriju svih kasnijih blokova.
# Ovo namjerno ne rješava zamrznuti setup-blok: on mora ostati `cache: false`,
# a Quarto freeze mora biti isključen ili izričito osvježen u konfiguraciji.
.ovisnosti_figure <- c(
  "R/setup.R",
  "R/theme_book.R",
  "design-tokens.yml",
  "styles/_dark.scss"
)
.ovisnosti_figure <- .ovisnosti_figure[file.exists(.ovisnosti_figure)]
knitr::opts_chunk$set(
  cache.extra = paste(unname(tools::md5sum(.ovisnosti_figure)), collapse = "-")
)
