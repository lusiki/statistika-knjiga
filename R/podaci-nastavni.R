# podaci-nastavni.R ---------------------------------------------------------
# Simulirani nastavni podaci knjige. Ovi skupovi NISU empirijski nalaz i
# nikada se ne opisuju kao tvrdnja o stvarnoj populaciji (Dodatak C, odjeljak
# o simuliranim nastavnim podacima). Služe da poglavlja o opisivanju podataka
# rade na istim ispitanicima, pa čitatelj prepoznaje isti uzorak u sažecima,
# grafovima i koeficijentima.
#
# Skripta se poziva iz R/setup.R, pa je `anketa_mreze` dostupna svakom
# poglavlju bez dodatnog učitavanja.
# ---------------------------------------------------------------------------

#' Simulirana anketa o korištenju društvenih mreža
#'
#' Vraća uzorak s dobnom strukturom, desno asimetričnim dnevnim vremenom
#' korištenja i ordinalnom mjerom povjerenja u sadržaj. Raspodjela vremena je
#' lognormalna po dobnoj skupini, što reproducira oblik koji metrike angažmana
#' u digitalnim medijima redovito imaju.
#'
#' @param n Broj ispitanika.
#' @param sjeme Sjeme generatora. Zadana vrijednost drži skup nepromijenjenim
#'   kroz sve rendere i sva poglavlja.
simuliraj_anketu <- function(n = 300, sjeme = 4001) {
  # Poglavlja simuliraju i nakon učitavanja podataka, a R/setup.R je već
  # postavio knjižno sjeme. Lokalno sjeme zato mora vratiti zatečeno stanje
  # generatora, inače bi puko učitavanje ovog skupa pomaknulo svaki kasniji
  # slučajni izvlak u poglavlju.
  staro <- if (exists(".Random.seed", envir = globalenv())) {
    get(".Random.seed", envir = globalenv())
  } else {
    NULL
  }
  on.exit(
    {
      if (is.null(staro)) {
        if (exists(".Random.seed", envir = globalenv())) {
          rm(".Random.seed", envir = globalenv())
        }
      } else {
        assign(".Random.seed", staro, envir = globalenv())
      }
    },
    add = TRUE
  )
  set.seed(sjeme)

  razine <- c("18 do 24", "25 do 34", "35 do 44", "45 i više")

  # Struktura uzorka. Mlađe skupine namjerno su brojnije jer poglavlje treba
  # zbirnu raspodjelu u kojoj skupine povlače sredinu u različitim smjerovima.
  okvir <- tibble::tibble(
    skupina = razine,
    udio = c(0.30, 0.28, 0.22, 0.20),
    dob_min = c(18, 25, 35, 45),
    dob_max = c(24, 34, 44, 70),
    # Medijan dnevnih minuta po skupini prije slučajnog rasipanja.
    tipicno = c(75, 48, 28, 14),
    rasipanje = c(0.55, 0.55, 0.60, 0.65),
    # Očekivano povjerenje na ljestvici od 1 do 10.
    povjerenje_sredina = c(6.4, 5.6, 4.9, 4.3)
  )

  broj <- diff(c(0, round(cumsum(okvir$udio) * n)))
  indeks <- rep(seq_len(nrow(okvir)), times = broj)

  dob <- stats::runif(
    n,
    min = okvir$dob_min[indeks],
    max = okvir$dob_max[indeks] + 1
  )

  minute <- stats::rlnorm(
    n,
    meanlog = log(okvir$tipicno[indeks]),
    sdlog = okvir$rasipanje[indeks]
  )

  povjerenje <- stats::rnorm(
    n,
    mean = okvir$povjerenje_sredina[indeks],
    sd = 1.7
  )

  tibble::tibble(
    ispitanik = sprintf("I%03d", seq_len(n)),
    dob = floor(dob),
    dobna_skupina = factor(okvir$skupina[indeks], levels = razine),
    minute_dnevno = pmax(1, round(minute)),
    povjerenje = pmin(10, pmax(1, round(povjerenje)))
  )
}

# Kanonski nastavni uzorak. Poglavlja ga koriste pod ovim imenom.
anketa_mreze <- simuliraj_anketu()
