# podaci-nastavni.R ---------------------------------------------------------
# Simulirani nastavni podaci knjige. Ovi skupovi NISU empirijski nalaz i
# nikada se ne opisuju kao tvrdnja o stvarnoj populaciji (Dodatak C, odjeljak
# o simuliranim nastavnim podacima). Služe da poglavlja o opisivanju podataka
# rade na istim ispitanicima, pa čitatelj prepoznaje isti uzorak u sažecima,
# grafovima i koeficijentima.
#
# Skripta se poziva iz R/setup.R, pa su `anketa_mreze` i `populacija_medija`
# dostupni svakom poglavlju bez dodatnog učitavanja.
#
# LICENCA IZLAZA: skupovi `anketa_mreze` i `populacija_medija`, kao i njihove
# neizmijenjene datotečne snimke, dostupni su pod licencom Creative Commons
# Imenovanje 4.0 međunarodna (CC BY 4.0). Nositelj prava je Luka Sikic, 2026.
# Pri dijeljenju navedite autora, knjigu, ime skupa, ovu skriptu i licencu te
# označite izmjene. Puna obavijest je u data/LICENCA-generirani-podaci.md.
# Licenca izlaznih podataka ne mijenja MIT licencu ovoga koda.
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

#' Simulirana populacija poznatih parametara
#'
#' Vraća 50 000 odraslih osoba izmišljenoga grada s poznatim populacijskim
#' vrijednostima. Dio III treba populaciju čija je istina unaprijed poznata,
#' jer se samo tako može pokazati koliko dobro uzorak pogađa ono što u
#' stvarnom istraživanju nikada ne vidimo. Primarni izvor vijesti ovisi o
#' dobi, povjerenje o izvoru i dobi, a spremnost na plaćanje ima mnogo nula i
#' dugačak desni rep, pa služi kao izrazito asimetrična varijabla u
#' demonstraciji središnjega graničnog teorema.
#'
#' @param N Veličina populacije.
#' @param sjeme Sjeme generatora. Zadana vrijednost drži populaciju
#'   nepromijenjenom kroz sve rendere i sva poglavlja.
simuliraj_populaciju <- function(N = 50000, sjeme = 8001) {
  # Isti razlog kao kod ankete. Generator vraća zatečeno stanje RNG-a, pa
  # učitavanje populacije ne pomiče nijednu kasniju simulaciju u poglavlju.
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

  razine_izvora <- c("portal", "društvene mreže", "TV", "radio", "tisak")
  razine_obrazovanja <- c("osnovna", "srednja", "viša", "diplomska")

  dob <- pmin(80, 18 + stats::rgamma(N, shape = 2.00, scale = 12.70))

  # Koeficijenti su birani tako da se rubni udjeli izvora poklope sa
  # zadanom strukturom populacije, a da izbor izvora i dalje ovisi o dobi.
  tezine <- cbind(
    exp(0.535 - 0.012 * dob),
    exp(2.005 - 0.055 * dob),
    exp(-1.710 + 0.030 * dob),
    exp(-1.932 + 0.022 * dob),
    exp(-2.406 + 0.028 * dob)
  )
  tezine <- tezine / rowSums(tezine)
  for (j in 2:ncol(tezine)) {
    tezine[, j] <- tezine[, j - 1] + tezine[, j]
  }
  izvor <- razine_izvora[
    max.col(stats::runif(N) < tezine, ties.method = "first")
  ]

  obrazovanje <- sample(
    razine_obrazovanja,
    N,
    replace = TRUE,
    prob = c(0.18, 0.47, 0.24, 0.11)
  )

  ucinak_izvora <- c(
    portal = 0, `društvene mreže` = -0.55, TV = 0.35,
    radio = 0.60, tisak = 0.50
  )[izvor]

  povjerenje <- 4.81 + 0.028 * (dob - 42.7) + ucinak_izvora +
    stats::rnorm(N, 0, 1.88)
  povjerenje <- pmin(10, pmax(1, round(povjerenje)))

  minute <- stats::rgamma(
    N,
    shape = 7.2,
    scale = 174 * exp(0.006 * (dob - 42.7)) / 7.2
  )

  placa <- stats::runif(N) < stats::plogis(
    -1.35 + 0.16 * (povjerenje - 4.87) +
      0.45 * (obrazovanje %in% c("viša", "diplomska"))
  )
  iznos <- ifelse(placa, stats::rlnorm(N, meanlog = 3.05, sdlog = 0.62), 0)

  tibble::tibble(
    osoba = seq_len(N),
    dob = floor(dob),
    spol = ifelse(stats::runif(N) < 0.51, "ženski", "muški"),
    obrazovanje = factor(obrazovanje, levels = razine_obrazovanja),
    izvor_vijesti = factor(izvor, levels = razine_izvora),
    povjerenje_medijima = povjerenje,
    minute_medija = round(minute),
    spremnost_platiti = round(iznos)
  )
}

# Kanonska nastavna populacija. Poglavlja Dijela III koriste je pod ovim
# imenom, a njezini parametri smiju se izračunati jer je cijela poznata.
populacija_medija <- simuliraj_populaciju()
