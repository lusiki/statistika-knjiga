# fetch-podaci.R ------------------------------------------------------------
# Dohvat licenčno provjerenih skupova podataka u data/.
#
#   Rscript R/fetch-podaci.R            # svi skupovi
#   Rscript R/fetch-podaci.R dzs_turizam # samo jedan, po ključu
#
# Pokreće se RUČNO, ne pri renderu. Izvori mijenjaju adrese sporije nego što
# se knjiga gradi, a render koji ovisi o mreži je render koji jednom pukne u
# najgorem trenutku. U repozitorij se smiju urezati samo paketi u traci
# `bundled`; tehnički dohvat sam po sebi nije dopuštenje za redistribuciju.
# Paketi u trakama `portal-mediated` i `external-only` nikada se ne preuzimaju
# ovom skriptom.
#
# STATUS: kostur. Registar ispod je prazan; svaki unos dodaje se tek kad je
# izvorna inačica određena, licenca i atribucija provjerene, redistribucija
# izričito dopuštena, a zakonita zamjena za obvezne zadatke zabilježena.
# ---------------------------------------------------------------------------

REGISTAR <- list(
  # Obrazac unosa (kopiraj i popuni):
  #
  # dzs_turizam = list(
  #   naziv   = "DZS turizam",
  #   izvor   = "mjerodavna stranica izvora",
  #   verzija = "točno izdanje ili val",
  #   url     = "https://…",
  #   izlaz   = "data/dzs-turizam.csv",
  #   licenca = "…",
  #   atribucija = "…",
  #   pristup = "…",
  #   redistribucija = "provjerena",
  #   traka = "bundled",
  #   zamjena = "licenčno čista datoteka ili agregat za obvezni put",
  #   napomena = "…"
  # )
)

# ---------------------------------------------------------------------------

dohvati <- function(unos, kljuc) {
  if (!identical(unos$traka, "bundled") ||
      !identical(unos$redistribucija, "provjerena")) {
    stop(
      "[", kljuc, "] dohvat odbijen: samo paket s provjerenom ",
      "redistribucijom i trakom bundled smije u data/."
    )
  }

  cilj <- file.path(getwd(), unos$izlaz)
  dir.create(dirname(cilj), showWarnings = FALSE, recursive = TRUE)

  if (file.exists(cilj)) {
    message("[", kljuc, "] već postoji, preskačem: ", unos$izlaz)
    return(invisible(FALSE))
  }
  if (is.null(unos$url)) {
    message("[", kljuc, "] nema automatskog preuzimanja. ", unos$napomena)
    return(invisible(FALSE))
  }

  message("[", kljuc, "] preuzimam ", unos$url)
  ok <- tryCatch({
    utils::download.file(unos$url, cilj, mode = "wb", quiet = TRUE)
    TRUE
  }, error = function(e) {
    message("[", kljuc, "] NEUSPJEH: ", conditionMessage(e))
    FALSE
  })
  if (ok) message("[", kljuc, "] spremljeno u ", unos$izlaz)
  invisible(ok)
}

args <- commandArgs(trailingOnly = TRUE)
kljucevi <- if (length(args)) args else names(REGISTAR)

if (!length(REGISTAR)) {
  message("Registar je prazan. Dodaj skupove podataka na vrh ove skripte, ",
          "a izvor, inačicu, licencu, atribuciju, pristup, redistribuciju, ",
          "traku i zamjenu u kanonski katalog.")
} else {
  for (k in kljucevi) {
    if (is.null(REGISTAR[[k]])) {
      message("Nepoznat ključ: ", k, ". Dostupni: ",
              paste(names(REGISTAR), collapse = ", "))
      next
    }
    dohvati(REGISTAR[[k]], k)
  }
}
