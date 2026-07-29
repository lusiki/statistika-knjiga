# fetch-podaci.R ------------------------------------------------------------
# Dohvat javnih skupova podataka u data/.
#
#   Rscript R/fetch-podaci.R            # svi skupovi
#   Rscript R/fetch-podaci.R ess        # samo jedan, po ključu
#
# Pokreće se RUČNO, ne pri renderu. Izvori mijenjaju adrese sporije nego što
# se knjiga gradi, a render koji ovisi o mreži je render koji jednom pukne u
# najgorem trenutku. Preuzeti skupovi se urezuju (commit) zajedno s knjigom.
#
# STATUS: kostur. Registar ispod je prazan; svaki unos dodaje se tek kad je
# adresa provjerena i licenca zabilježena u Dodatku C.
# ---------------------------------------------------------------------------

REGISTAR <- list(
  # Obrazac unosa (kopiraj i popuni):
  #
  # ess = list(
  #   naziv   = "Europsko društveno istraživanje, hrvatski valovi",
  #   url     = "https://…",
  #   izlaz   = "data/ess-hr.csv",
  #   licenca = "…",
  #   napomena = "Traži besplatnu registraciju; datoteka se preuzima ručno."
  # )
)

# ---------------------------------------------------------------------------

dohvati <- function(unos, kljuc) {
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
          "a licence i opis varijabli u dodaci/c-katalog-podataka.qmd.")
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
