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

# Tema i paleta (čitaju design-tokens.yml).
source("R/theme_book.R")

# Knjižna pisma u grafovima. Ako showtext/sysfonts nisu instalirani ili
# preuzimanje ne uspije, tema tiho pada na sistemska pisma — graf se uvijek
# nacrta. Zato tryCatch, a ne stop.
.pisma_ok <- isTRUE(tryCatch(ucitaj_fontove(), error = function(e) FALSE))

# Tema + zadane vrijednosti geoma (točke u tinti, glatka krivulja u okeru).
postavi_temu()

# REPRODUCIBILNOST. Knjiga uči simulaciju prije formule, pa gotovo svaki
# statički graf uzorkuje. Fiksno sjeme znači da se ista slika ispisuje pri
# svakom renderu. Ako poglavlje treba drugo sjeme, postavlja ga lokalno.
set.seed(2026)

# fig.showtext se postavlja SAMO ako su pisma stvarno učitana. knitr uz
# fig.showtext = TRUE zove showtext::showtext_begin() pri otvaranju uređaja,
# pa bi bez instaliranog paketa srušio render — a CI ga ne mora imati.
knitr::opts_chunk$set(
  fig.align = "center",
  out.width = "100%",
  dpi = 300,
  fig.showtext = .pisma_ok
)

# Hrvatski zapis brojeva u ispisu (decimalni zarez).
options(OutDec = ",", scipen = 999)
