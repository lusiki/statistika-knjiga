# snimke-nastavnih-podataka.R -----------------------------------------------
# Deterministicka serijalizacija generiranih nastavnih skupova u CSV snimke.
#
# Ova datoteka definira SAMO funkcije i nema nuspojava. Pise ju
# scripts/build-data-snapshots.R, a provjerava scripts/check-data-integrity.R,
# pa obje strane dijele jednu definiciju oblika snimke.
#
# Cetiri pravila oblika, koja provodi i provjera:
#
#   1. UTF-8 bez BOM-a, zavrsetak retka LF, zarez kao razdjelnik polja.
#   2. Nijedna vrijednost ne sadrzi zarez, navodnik ni prijelom retka, pa se
#      datoteka cita bilo kojim alatom bez pravila o navodnicima.
#   3. Sifra faktora stoji uz hrvatsku oznaku, nikada umjesto nje.
#   4. Puna brojcana preciznost: realan broj zapisuje se najkracim zapisom koji
#      se cita natrag u istu vrijednost, pa u datoteci nema zaokruzivanja.
#      Zaokruzivanje postoji samo u prikazu u knjizi.
#
# LICENCA IZLAZA: snimke skupova `anketa_mreze` i `populacija_medija` su
# CC BY 4.0, nositelj prava Luka Sikic. Svaka snimka nosi obavijest uz sebe
# (vidi data/*.LICENCA.md i data/LICENCA-generirani-podaci.md). Kod ostaje MIT.
# ---------------------------------------------------------------------------

# --- brojevi ---------------------------------------------------------------

#' Najkraci zapis realnoga broja koji se cita natrag u istu vrijednost
#'
#' Bez ovoga bi `%.17g` posvuda ispisivao artefakte binarnoga zapisa, a bilo
#' koji kraci fiksni format tiho bi zaokruzio. Petlja bira prvi zapis koji je
#' dokazano povratan, pa je datoteka istovremeno citljiva i tocna.
tekst_broja <- function(x) {
  vapply(as.numeric(x), function(v) {
    for (znamenke in 15:17) {
      zapis <- sprintf(paste0("%.", znamenke, "g"), v)
      if (identical(as.numeric(zapis), v)) return(zapis)
    }
    sprintf("%.17g", v)
  }, character(1))
}

#' Zapis cijeloga broja; pada ako vrijednost nije cjelobrojna
tekst_cijeloga <- function(x) {
  v <- as.numeric(x)
  if (any(!is.finite(v)) || any(v != trunc(v))) {
    stop("Stupac deklariran kao cjelobrojan sadrzi necjelobrojnu vrijednost.")
  }
  sprintf("%.0f", v)
}

# --- redci -----------------------------------------------------------------

#' Pretvara okvir samih znakovnih stupaca u retke CSV snimke
csv_redci <- function(okvir) {
  if (!is.data.frame(okvir) || !ncol(okvir)) {
    stop("csv_redci ocekuje neprazan data.frame.")
  }
  for (ime in names(okvir)) {
    if (!is.character(okvir[[ime]])) {
      stop("Stupac nije znakovni prije zapisa: ", ime)
    }
    if (any(grepl('[,"\n\r]', okvir[[ime]]))) {
      stop("Vrijednost sadrzi zarez, navodnik ili prijelom retka: ", ime)
    }
    if (any(!nzchar(okvir[[ime]]))) {
      stop("Prazna celija nije dopustena; nedostajuca vrijednost ima vlastitu ",
           "sifru: ", ime)
    }
  }
  c(paste(names(okvir), collapse = ","),
    do.call(paste, c(unname(as.list(okvir)), sep = ",")))
}

#' Zapisuje retke kao UTF-8 bez BOM-a i s LF zavrsetkom retka
zapisi_snimku <- function(redci, putanja) {
  dir.create(dirname(putanja), showWarnings = FALSE, recursive = TRUE)
  veza <- file(putanja, open = "wb")
  on.exit(close(veza), add = TRUE)
  writeLines(enc2utf8(redci), veza, sep = "\n", useBytes = TRUE)
  invisible(putanja)
}

# --- analiticke snimke -----------------------------------------------------

redci_anketa <- function(skup) {
  data.frame(
    ispitanik = as.character(skup$ispitanik),
    dob = tekst_cijeloga(skup$dob),
    dobna_skupina_sifra = tekst_cijeloga(as.integer(skup$dobna_skupina)),
    dobna_skupina = as.character(skup$dobna_skupina),
    minute_dnevno = tekst_cijeloga(skup$minute_dnevno),
    povjerenje = tekst_cijeloga(skup$povjerenje),
    stringsAsFactors = FALSE
  )
}

redci_populacija <- function(skup) {
  data.frame(
    osoba = tekst_cijeloga(skup$osoba),
    dob = tekst_cijeloga(skup$dob),
    spol = as.character(skup$spol),
    obrazovanje_sifra = tekst_cijeloga(as.integer(skup$obrazovanje)),
    obrazovanje = as.character(skup$obrazovanje),
    izvor_vijesti_sifra = tekst_cijeloga(as.integer(skup$izvor_vijesti)),
    izvor_vijesti = as.character(skup$izvor_vijesti),
    povjerenje_medijima = tekst_cijeloga(skup$povjerenje_medijima),
    minute_medija = tekst_cijeloga(skup$minute_medija),
    spremnost_platiti = tekst_cijeloga(skup$spremnost_platiti),
    stringsAsFactors = FALSE
  )
}

# --- agregatne snimke ------------------------------------------------------
#
# Agregat postoji da bi se isti zakljucak mogao provjeriti rukom i u tisku.
# Zato svaki udio nosi i brojnik i nazivnik, a svaki prosjek i svoj zbroj, pa
# se citatelj nikada ne mora osloniti na zaokruzeni prosjek.

agregiraj <- function(skup, kljuc, sume = character(), pozitivni = character()) {
  razine <- levels(skup[[kljuc]])
  komadi <- lapply(seq_along(razine), function(i) {
    dio <- skup[as.integer(skup[[kljuc]]) == i, , drop = FALSE]
    broj <- nrow(dio)
    zapis <- list(sifra = i, oznaka = razine[[i]], broj = broj,
                  ukupno = nrow(skup))
    for (stupac in sume) {
      zapis[[paste0("zbroj_", stupac)]] <- sum(as.numeric(dio[[stupac]]))
    }
    for (stupac in pozitivni) {
      zapis[[paste0("pozitivni_", stupac)]] <- sum(as.numeric(dio[[stupac]]) > 0)
    }
    zapis
  })
  komadi
}

redci_agregat_anketa <- function(skup) {
  d <- agregiraj(skup, "dobna_skupina",
                 sume = c("minute_dnevno", "povjerenje"))
  broj <- vapply(d, function(x) x$broj, numeric(1))
  ukupno <- vapply(d, function(x) x$ukupno, numeric(1))
  zbroj_minuta <- vapply(d, function(x) x$zbroj_minute_dnevno, numeric(1))
  zbroj_povjerenja <- vapply(d, function(x) x$zbroj_povjerenje, numeric(1))
  data.frame(
    dobna_skupina_sifra = tekst_cijeloga(vapply(d, function(x) x$sifra, numeric(1))),
    dobna_skupina = vapply(d, function(x) x$oznaka, character(1)),
    broj = tekst_cijeloga(broj),
    ukupno = tekst_cijeloga(ukupno),
    udio = tekst_broja(broj / ukupno),
    zbroj_minuta = tekst_cijeloga(zbroj_minuta),
    prosjek_minuta = tekst_broja(zbroj_minuta / broj),
    zbroj_povjerenja = tekst_cijeloga(zbroj_povjerenja),
    prosjek_povjerenja = tekst_broja(zbroj_povjerenja / broj),
    stringsAsFactors = FALSE
  )
}

redci_agregat_populacija <- function(skup) {
  d <- agregiraj(skup, "izvor_vijesti",
                 sume = c("povjerenje_medijima", "minute_medija",
                          "spremnost_platiti"),
                 pozitivni = "spremnost_platiti")
  broj <- vapply(d, function(x) x$broj, numeric(1))
  ukupno <- vapply(d, function(x) x$ukupno, numeric(1))
  zbroj_povjerenja <- vapply(d, function(x) x$zbroj_povjerenje_medijima, numeric(1))
  zbroj_minuta <- vapply(d, function(x) x$zbroj_minute_medija, numeric(1))
  zbroj_spremnosti <- vapply(d, function(x) x$zbroj_spremnost_platiti, numeric(1))
  broj_platio <- vapply(d, function(x) x$pozitivni_spremnost_platiti, numeric(1))
  data.frame(
    izvor_vijesti_sifra = tekst_cijeloga(vapply(d, function(x) x$sifra, numeric(1))),
    izvor_vijesti = vapply(d, function(x) x$oznaka, character(1)),
    broj = tekst_cijeloga(broj),
    ukupno = tekst_cijeloga(ukupno),
    udio = tekst_broja(broj / ukupno),
    zbroj_povjerenja = tekst_cijeloga(zbroj_povjerenja),
    prosjek_povjerenja = tekst_broja(zbroj_povjerenja / broj),
    zbroj_minuta = tekst_cijeloga(zbroj_minuta),
    prosjek_minuta = tekst_broja(zbroj_minuta / broj),
    broj_platio = tekst_cijeloga(broj_platio),
    udio_platio = tekst_broja(broj_platio / broj),
    zbroj_spremnosti = tekst_cijeloga(zbroj_spremnosti),
    prosjek_spremnosti = tekst_broja(zbroj_spremnosti / broj),
    stringsAsFactors = FALSE
  )
}

# --- popis snimaka ---------------------------------------------------------

#' Kanonski popis snimaka koje ovaj repozitorij drzi
#'
#' Redoslijed i putanje moraju se poklapati s poljem `files` u
#' data/katalog.yml. Provjera to i trazi.
snimke_nastavnih_podataka <- function() {
  list(
    list(paket = "anketa_mreze", uloga = "analysis",
         putanja = "data/anketa-mreze.csv",
         redci = function() redci_anketa(anketa_mreze)),
    list(paket = "anketa_mreze", uloga = "aggregate",
         putanja = "data/anketa-mreze-agregat.csv",
         redci = function() redci_agregat_anketa(anketa_mreze)),
    list(paket = "populacija_medija", uloga = "analysis",
         putanja = "data/populacija-medija.csv",
         redci = function() redci_populacija(populacija_medija)),
    list(paket = "populacija_medija", uloga = "aggregate",
         putanja = "data/populacija-medija-agregat.csv",
         redci = function() redci_agregat_populacija(populacija_medija))
  )
}
