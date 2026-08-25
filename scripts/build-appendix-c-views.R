#!/usr/bin/env Rscript

# Regenerira oba javna prikaza podataka iz kanonskoga kataloga. Katalog bira
# pakete, trake, datoteke i ugovorne granice; deklarirane agregatne datoteke
# daju neokrugljene vrijednosti za rucnu provjeru redaka.

builder_args <- commandArgs(trailingOnly = TRUE)

arg_value <- function(flag, default = NULL) {
  hit <- match(flag, builder_args)
  if (is.na(hit)) return(default)
  if (hit == length(builder_args)) stop("Nedostaje vrijednost nakon ", flag, ".")
  builder_args[[hit + 1L]]
}

route_root <- normalizePath(arg_value("--root", "."), mustWork = TRUE)
write_outputs <- "--write" %in% builder_args
root_file <- function(...) file.path(route_root, ...)

catalogue_path <- root_file("data", "katalog.yml")
if (!file.exists(catalogue_path)) stop("Nedostaje data/katalog.yml.")
catalogue <- yaml::read_yaml(catalogue_path)
if (!isTRUE(catalogue$sole_machine_readable_record)) {
  stop("Katalog se vise ne deklarira jedinim strojno citljivim zapisom.")
}

packages <- catalogue$packages
package_ids <- vapply(packages, function(package) package$id, character(1))
if (anyDuplicated(package_ids)) stop("Katalog ima udvostrucene identifikatore paketa.")

as_text <- function(value, empty = "nije zabilježeno") {
  if (is.null(value) || !length(value)) return(empty)
  value <- unlist(value, use.names = FALSE)
  value <- value[!is.na(value)]
  if (!length(value)) return(empty)
  paste(trimws(as.character(value)), collapse = "; ")
}

one_line <- function(value, empty = "nije zabilježeno") {
  text <- as_text(value, empty)
  text <- gsub("[\r\n]+", " ", text)
  gsub("[[:space:]]+", " ", text)
}

style_prose <- function(value, empty = "nije zabilježeno") {
  text <- one_line(value, empty)
  text <- gsub("Izvor: ", "Izvor je ", text, fixed = TRUE)
  text <- gsub("Source: ", "Izvor je ", text, fixed = TRUE)
  text <- gsub("opis obrade: ", "obrada je ", text, fixed = TRUE)
  text <- gsub("projekta: ", "projekta, i to ", text, fixed = TRUE)
  text <- gsub("agregatne tablice: ", "agregatne tablice. ", text, fixed = TRUE)
  text <- gsub("Korpus nije uzorak: objava", "Korpus nije uzorak. Objava", text, fixed = TRUE)
  text <- gsub(
    "Registar koji nije popis: obuhvat snimke",
    "Registar nije potpuni popis; prikazuje obuhvat snimke",
    text,
    fixed = TRUE
  )
  text <- gsub("Upravljanje: vrata", "Upravljanje ostaje otvoreno. Vrata", text, fixed = TRUE)
  text <- gsub("za Hrvatsku: Eurostat", "za Hrvatsku. To su Eurostat", text, fixed = TRUE)
  text <- gsub(
    "Preostaju dvije zapreke: Eurostat",
    "Preostaju dvije zapreke. Eurostat",
    text,
    fixed = TRUE
  )
  text <- gsub("preuzimanja: BS_TU11", "preuzimanja. BS_TU11", text, fixed = TRUE)
  text <- gsub("bezopasna: broj", "bezopasna. Broj", text, fixed = TRUE)
  text <- gsub(" — ", ", ", text, fixed = TRUE)
  text <- gsub(": ", "; ", text, fixed = TRUE)
  text <- gsub(
    "([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z)",
    "`\\1`",
    text,
    perl = TRUE
  )
  text <- gsub(
    "([[:alnum:]]+:0)(?=,|[[:space:]]|$)",
    "`\\1`",
    text,
    perl = TRUE
  )
  text <- gsub(
    "([0-9]+\\([0-9]+\\):[0-9]+-[0-9]+)",
    "`\\1`",
    text,
    perl = TRUE
  )
  text <- gsub(
    "(https?://[^[:space:];,)]+)",
    "[poveznica na izvor](\\1)",
    text,
    perl = TRUE
  )
  text
}

sentence_end <- function(value) {
  text <- one_line(value)
  if (grepl("[.!?]$", text)) text else paste0(text, ".")
}

lower_first <- function(value) {
  if (!nzchar(value)) return(value)
  paste0(tolower(substr(value, 1L, 1L)), substring(value, 2L))
}

escape_cell <- function(value) {
  text <- style_prose(value)
  text <- gsub("\\|", "\\\\|", text)
  text
}

code <- function(value) paste0("`", as.character(value), "`")
anchor_id <- function(id) gsub("_", "-", id, fixed = TRUE)

package_by_id <- function(id) {
  hit <- match(id, package_ids)
  if (is.na(hit)) stop("Katalog nema paket ", id, ".")
  packages[[hit]]
}

is_repo_path <- function(path) {
  grepl("^(data|R|scripts|notes|config|dodaci|chapters)/", path)
}

relative_target <- function(path, from_appendix = FALSE) {
  if (from_appendix) paste0("../", path) else path
}

file_display <- function(path, promoted, from_appendix = FALSE) {
  if (isTRUE(promoted) && is_repo_path(path)) {
    paste0("[", code(path), "](", relative_target(path, from_appendix), ")")
  } else {
    code(path)
  }
}

promoted_label <- function(package) {
  if (isTRUE(package$promoted)) {
    paste0("promoviran paketom ", code(package$promoted_by))
  } else {
    "nije promoviran"
  }
}

table_lines <- function(header, rows, caption = NULL) {
  divider <- paste(rep("---", length(header)), collapse = "|")
  result <- c(
    paste(header, collapse = "|"),
    paste0("|", divider, "|")
  )
  if (length(rows)) result <- c(result, rows)
  if (!is.null(caption)) result <- c(result, "", caption)
  result
}

file_summary_rows <- function(package, from_appendix = FALSE) {
  records <- package$file_records
  if (is.null(records) || !length(records)) {
    paths <- unlist(package$files, use.names = FALSE)
    if (!length(paths)) return("| nema datoteke | nije primjenjivo |")
    return(vapply(paths, function(path) {
      paste0("| ", file_display(path, package$promoted, from_appendix),
             " | nije materijalizirana javna ruta |")
    }, character(1)))
  }
  vapply(records, function(record) {
    paste0(
      "| ", file_display(record$path, package$promoted, from_appendix),
      " | uloga ", code(record$role),
      "; ", record$rows, " redaka; ključ ", code(record$key), " |"
    )
  }, character(1))
}

file_variable_rows <- function(package) {
  records <- package$file_records
  if (is.null(records) || !length(records)) {
    paths <- unlist(package$files, use.names = FALSE)
    if (!length(paths)) return("| nema datoteke | nije primjenjivo |")
    return(vapply(paths, function(path) {
      paste0("| ", code(path), " | nije zabilježeno |")
    }, character(1)))
  }
  vapply(records, function(record) {
    variables <- vapply(record$columns, function(column) column$name, character(1))
    paste0(
      "| ", code(record$path),
      " | ", paste(code(variables), collapse = ", "), " |"
    )
  }, character(1))
}

file_record_blocks <- function(package, from_appendix = FALSE) {
  records <- package$file_records
  if (is.null(records) || !length(records)) {
    paths <- unlist(package$files, use.names = FALSE)
    if (!length(paths)) return("Paket nema materijaliziranu datoteku.")
    result <- character()
    for (path in paths) {
      result <- c(
        result,
        paste0("#### ", code(path)),
        "",
        "Datoteka nije materijalizirana kao javna ruta.",
        ""
      )
    }
    return(result)
  }
  result <- character()
  for (record in records) {
    variables <- vapply(record$columns, function(column) column$name, character(1))
    result <- c(
      result,
      paste0("#### ", file_display(record$path, package$promoted, from_appendix)),
      "",
      paste0(
        "**Uloga i opseg.** Uloga je ", code(record$role), ", datoteka ima ",
        record$rows, " redaka, a ključ je ", code(record$key), "."
      ),
      "",
      "**Varijable.**\\",
      paste0(
        code(variables),
        ifelse(seq_along(variables) == length(variables), ".", ",\\")
      ),
      ""
    )
  }
  result
}

download_links <- function(package, from_appendix = FALSE) {
  if (!isTRUE(package$promoted)) return("Nema javne lokalne datoteke. Paket nije promoviran.")
  paths <- unlist(package$files, use.names = FALSE)
  if (!length(paths)) return("Promovirani paket nema deklariranu datoteku.")
  paste(vapply(paths, file_display, character(1), promoted = TRUE,
               from_appendix = from_appendix), collapse = ", ")
}

aggregate_rows <- function(package) {
  path <- package$aggregate_view
  if (is.null(path) || !nzchar(path)) stop(package$id, " nema agregatni prikaz.")
  full <- root_file(path)
  if (!file.exists(full)) stop("Nedostaje deklarirani agregat ", path, ".")
  read.csv(
    full,
    stringsAsFactors = FALSE,
    check.names = FALSE,
    colClasses = "character",
    fileEncoding = "UTF-8"
  )
}

aggregate_tables <- function(package, prefix) {
  data <- aggregate_rows(package)
  contract <- package$aggregate_reconciliation
  group_label <- contract$group_label
  shares <- contract$shares
  sums <- contract$sums

  share_rows <- character()
  for (share in shares) {
    for (row in seq_len(nrow(data))) {
      share_rows <- c(share_rows, paste0(
        "| ", escape_cell(data[[group_label]][[row]]),
        " | ", code(share$share),
        " | ", code(data[[share$numerator]][[row]]),
        " / ", code(data[[share$denominator]][[row]]),
        " = ", code(data[[share$share]][[row]]), " |"
      ))
    }
  }

  mean_rows <- character()
  for (sum_contract in sums) {
    for (row in seq_len(nrow(data))) {
      mean_rows <- c(mean_rows, paste0(
        "| ", escape_cell(data[[group_label]][[row]]),
        " | ", code(sum_contract$mean),
        " | zbroj ", code(data[[sum_contract$total]][[row]]),
        "; prosjek ", code(data[[sum_contract$mean]][[row]]), " |"
      ))
    }
  }

  slug <- anchor_id(package$id)
  c(
    paste0("### ", package$name, " — provjera retka {#provjera-", prefix, "-", slug, "}"),
    "",
    paste0(
      "Udio u @tbl-", prefix, "-", slug,
      "-udjeli uvijek nosi vlastiti brojnik i nazivnik. Prosjek u @tbl-",
      prefix, "-", slug,
      "-prosjeci uvijek stoji uz cjelobrojni zbroj iz iste skupine."
    ),
    "",
    table_lines(
      c("Skupina", "Udio", "Brojnik / nazivnik = točna vrijednost"),
      share_rows,
      paste0(": Udio s brojnikom i nazivnikom. {#tbl-", prefix, "-", slug, "-udjeli}")
    ),
    "",
    table_lines(
      c("Skupina", "Prosjek", "Cjelobrojni zbroj i točna vrijednost"),
      mean_rows,
      paste0(": Prosjek s pripadajućim cjelobrojnim zbrojem. {#tbl-", prefix, "-", slug, "-prosjeci}")
    )
  )
}

dzs_table <- function(prefix) {
  package <- package_by_id("dzs_turizam")
  records <- package$source_reconciliation
  result_rows <- vapply(records, function(record) {
    kind <- if (identical(as.integer(record$tolerance), 0L)) {
      "administrativno prebrojavanje"
    } else {
      "anketna procjena"
    }
    paste0(
      "| ", escape_cell(record$id),
      " | ", kind,
      " | ", record$comparisons, " usporedbi; tolerancija ",
      record$tolerance, "; najveći ostatak ", record$max_abs_residual, " |"
    )
  }, character(1))
  file_rows <- vapply(records, function(record) {
    sources <- unique(c(record$total$file, record$parts$file))
    paste0(
      "| ", escape_cell(record$id),
      " | ", paste(code(sources), collapse = ", "), " |"
    )
  }, character(1))
  c(
    "## Dvije DZS-ove mjere nisu jedna serija {#sec-dzs-dvije-mjere}",
    "",
    paste(
      "Tablice BS_TU11 i BS_TU12 bilježe administrativne eVisitor dolaske,",
      "dok je T03 uzoračka anketa o procijenjenim putovanjima stanovnika.",
      "Dolazak nije osoba, a putovanje nije dolazak; te se brojke ne zbrajaju",
      "i ne prikazuju kao usporedive serije."
    ),
    "",
    paste0(
      "Administrativne provjere u @tbl-", prefix,
      "-dzs imaju najveći ostatak točno `0`. Sve tri anketne razgradnje, ",
      "koje obuhvaćaju odredište, trajanje i dobnu skupinu, imaju najveći ostatak točno `1`, ",
      "jer su objavljene ćelije zasebno zaokružene procjene."
    ),
    "",
    table_lines(
      c("Provjera", "Vrsta mjere", "Rezultat usklađenja"),
      result_rows,
      paste0(": Usklađenja dviju različitih DZS-ovih mjera. {#tbl-", prefix, "-dzs}")
    ),
    "",
    table_lines(
      c("Provjera", "Datoteke"),
      file_rows,
      paste0(": Datoteke uključene u DZS-ova usklađenja. {#tbl-", prefix, "-dzs-datoteke}")
    )
  )
}

compact_package <- function(package) {
  id <- anchor_id(package$id)
  c(
    paste0("### ", package$name, " {#podaci-", id, "}"),
    "",
    paste0("**Identifikator.** ", code(package$id), "."),
    "",
    paste0("**Pitanje.** ", one_line(package$question)),
    "",
    paste0(
      "**Status i pristup.** ", promoted_label(package), "; traka ",
      code(package$lane), "; jedinica je ", lower_first(sentence_end(package$unit))
    ),
    "",
    paste0("**Datoteke.** ", download_links(package, FALSE)),
    "",
    paste0(
      "[Puni zapis u Dodatku C](dodaci/c-katalog-podataka.qmd#sec-data-",
      id, ")."
    )
  )
}

full_package <- function(package) {
  id <- anchor_id(package$id)
  passport <- if (!is.null(package$passport)) {
    paste0("[", code(package$passport), "](", relative_target(package$passport, TRUE), ")")
  } else {
    "nije objavljena"
  }
  notice <- if (!is.null(package$snapshot_notice)) {
    paste0("[", code(package$snapshot_notice), "](", relative_target(package$snapshot_notice, TRUE), ")")
  } else {
    "nije objavljena"
  }
  licence <- style_prose(package$licence)
  if (!is.null(package$licence_uri)) {
    licence <- paste0(licence, " ([uvjeti licence]", "(", package$licence_uri, "))")
  }
  ethics <- package$ethics
  ethics_rows <- vapply(names(ethics), function(name) {
    paste0("| ", code(name), " | ", escape_cell(ethics[[name]]), " |")
  }, character(1))
  permissible_rows <- vapply(unlist(package$permissible_claims, use.names = FALSE), function(claim) {
    paste0("| dopuštena | ", escape_cell(claim), " |")
  }, character(1))
  unavailable_rows <- vapply(unlist(package$unavailable_claims, use.names = FALSE), function(claim) {
    paste0("| nedostupna | ", escape_cell(claim), " |")
  }, character(1))

  result <- c(
    paste0("## ", package$name, " {#sec-data-", id, "}"),
    "",
    paste0("Sažeti javni zapis nalazi se na [stranici Podaci](../podaci.qmd#podaci-", id, ")."),
    "",
    paste0("**Identifikator.** ", code(package$id), "."),
    "",
    paste0("**Status.** ", promoted_label(package), "."),
    "",
    paste0("**Dizajn.** ", code(package$design), "."),
    "",
    paste0("**Domena.** ", style_prose(package$domain), "."),
    "",
    paste0("**Jedinica.** ", sentence_end(style_prose(package$unit))),
    "",
    paste0("**Pitanje.** ", sentence_end(style_prose(package$question))),
    "",
    paste0("**Uloga.** ", sentence_end(style_prose(package$role))),
    "",
    paste0("**Potrošači.** ", style_prose(package$consumers), "."),
    "",
    paste0("**Traka.** ", code(package$lane), "."),
    "",
    paste0("**Razred osvježavanja.** ", code(package$refresh_class), "."),
    "",
    paste0("**Inačica.** ", sentence_end(style_prose(package$version))),
    "",
    "### Izvor, prava i pristup",
    "",
    paste0("**Izvor.** ", style_prose(package$source)),
    "",
    paste0("**Licenca.** ", licence),
    "",
    paste0("**Atribucija.** ", style_prose(package$attribution)),
    "",
    paste0("**Pristup.** ", style_prose(package$access)),
    "",
    paste0("**Redistribucija.** ", style_prose(package$redistribution)),
    "",
    paste0("**Zakonita zamjena.** ", style_prose(package$fallback)),
    "",
    paste0("**Putovnica.** ", passport, "."),
    "",
    paste0("**Obavijest uz snimku.** ", notice, "."),
    "",
    "### Datoteke i varijable",
    "",
    file_record_blocks(package, TRUE),
    "",
    "### Dopuštene i nedostupne tvrdnje",
    "",
    table_lines(
      c("Status", "Granica tvrdnje"),
      c(permissible_rows, unavailable_rows)
    ),
    "",
    "### Etička putovnica",
    "",
    table_lines(c("Pitanje", "Odgovor"), ethics_rows)
  )
  if (!is.null(package$caveats) && length(package$caveats)) {
    caveats <- unlist(package$caveats, use.names = FALSE)
    caveat_rows <- vapply(seq_along(caveats), function(index) {
      paste0("| ", index, " | ", escape_cell(caveats[[index]]), " |")
    }, character(1))
    result <- c(
      result,
      "",
      "### Ograničenja",
      "",
      table_lines(c("Redni broj", "Ograničenje"), caveat_rows)
    )
  }
  result
}

lane_counts <- table(vapply(packages, function(package) package$lane, character(1)))
promoted_count <- sum(vapply(packages, function(package) isTRUE(package$promoted), logical(1)))

overview_rows <- vapply(packages, function(package) {
  id <- anchor_id(package$id)
  paste0(
    "| [", escape_cell(package$name), "](#podaci-", id, ")",
    " | ", code(package$lane),
    " | ", escape_cell(promoted_label(package)),
    " | ", escape_cell(package$question), " |"
  )
}, character(1))

public_lines <- c(
  "---",
  "title: \"Podaci\"",
  "toc: true",
  "number-sections: false",
  "lang: hr-HR",
  "body-classes: \"standalone-page support-page podaci-page\"",
  "format:",
  "  html:",
  "    page-layout: full",
  "    code-tools: false",
  "---",
  "",
  "<!-- Generira scripts/build-appendix-c-views.R iz data/katalog.yml. -->",
  "",
  "Ovo je sažeti javni prikaz kanonskoga kataloga podataka. Svaki zapis vodi",
  "do punoga zapisa u Dodatku C; status promocije, pristupna traka, datoteke i",
  "granice tvrdnji dolaze iz `data/katalog.yml`, a ne iz zasebno održavanoga popisa.",
  "",
  "## Stanje kataloga {#sec-podaci-stanje}",
  "",
  paste0(
    "Katalog sadrži ", length(packages), " paketa. Među njima je ",
    unname(lane_counts[["bundled"]]), " u traci `bundled`, ",
    unname(lane_counts[["portal-mediated"]]), " u traci `portal-mediated` i ",
    unname(lane_counts[["external-only"]]), " u traci `external-only`. ",
    "Promovirano ih je ", promoted_count, ". Promocija je zasebna odluka; ",
    "sama dostupnost datoteke ne mijenja status."
  ),
  "",
  table_lines(
    c("Skup", "Traka", "Status", "Pitanje"),
    overview_rows,
    ": Sažeti popis paketa iz kanonskoga kataloga. {#tbl-podaci-paketi}"
  ),
  "",
  "## Provjerljivi redci generiranih skupova {#sec-podaci-provjera}",
  "",
  paste(
    "Agregatne datoteke dvaju generiranih nastavnih skupova omogućuju provjeru",
    "bez analitičkoga softvera. Vrijednosti ispod prepisuju se kao znakovni",
    "zapisi iz datoteka koje katalog izrijekom proglašava agregatnim prikazima."
  ),
  "",
  aggregate_tables(package_by_id("anketa_mreze"), "podaci"),
  "",
  aggregate_tables(package_by_id("populacija_medija"), "podaci"),
  "",
  dzs_table("podaci"),
  "",
  "## Svi paketi {#sec-podaci-svi}",
  ""
)
for (package in packages) public_lines <- c(public_lines, compact_package(package), "")

appendix_lines <- c(
  "---",
  "title: \"Katalog podataka\"",
  "---",
  "",
  "<!-- Generira scripts/build-appendix-c-views.R iz data/katalog.yml. -->",
  "",
  "Dodatak C je čitateljski prikaz kanonskoga kataloga podataka. Paket bez",
  "provjerljivoga podrijetla, licence, pristupne trake i granice tvrdnje ne",
  "postaje obvezni podatkovni put. Strojno čitljiv izvor ostaje isključivo",
  "`data/katalog.yml`; ovaj se dodatak i stranica Podaci regeneriraju zajedno.",
  "",
  "## Kako čitati katalog {#sec-c-kako-citati}",
  "",
  paste(
    "Traka `bundled` znači da se deklarirane datoteke smiju isporučiti uz",
    "zabilježene uvjete. `portal-mediated` vodi čitatelja službenomu izvoru, a",
    "`external-only` ostavlja paket izvan repozitorija. Ni jedna traka sama po",
    "sebi nije promocija."
  ),
  "",
  "Za javnu rutu i dokaz regeneracije služi",
  "[`config/appendix-c-data-route.json`](../config/appendix-c-data-route.json).",
  "",
  "## Provjerljivi redci generiranih skupova {#sec-c-provjera}",
  "",
  aggregate_tables(package_by_id("anketa_mreze"), "c"),
  "",
  aggregate_tables(package_by_id("populacija_medija"), "c"),
  "",
  dzs_table("c"),
  "",
  "## Zapisi paketa {#sec-c-paketi}",
  "",
  paste(
    "Svaki zapis u nastavku čuva isto pitanje, jedinicu, traku, status,",
    "datoteke i granice tvrdnje koje katalog vodi za taj paket."
  ),
  ""
)
for (package in packages) appendix_lines <- c(appendix_lines, full_package(package), "")

normalise_output <- function(lines) {
  while (length(lines) && identical(tail(lines, 1), "")) {
    lines <- head(lines, -1)
  }
  text <- paste(lines, collapse = "\n")
  text <- gsub("\n{3,}", "\n\n", text)
  paste0(sub("[\r\n]+$", "", text), "\n")
}

public_text <- normalise_output(public_lines)
appendix_text <- normalise_output(appendix_lines)
public_path <- root_file("podaci.qmd")
appendix_path <- root_file("dodaci", "c-katalog-podataka.qmd")

write_utf8 <- function(text, path) {
  dir.create(dirname(path), recursive = TRUE, showWarnings = FALSE)
  writeChar(enc2utf8(text), path, eos = NULL, useBytes = TRUE)
}

if (write_outputs) {
  write_utf8(public_text, public_path)
  write_utf8(appendix_text, appendix_path)
} else {
  if (!file.exists(public_path) || !file.exists(appendix_path)) {
    stop("Nedostaje jedan od dvaju javnih prikaza.")
  }
  current_public <- paste0(paste(readLines(public_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n"), "\n")
  current_appendix <- paste0(paste(readLines(appendix_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n"), "\n")
  if (!identical(current_public, public_text)) stop("podaci.qmd nije svjeze regeneriran.")
  if (!identical(current_appendix, appendix_text)) stop("Dodatak C nije svjeze regeneriran.")
}

aggregate_contract <- lapply(c("anketa_mreze", "populacija_medija"), function(id) {
  package <- package_by_id(id)
  list(
    id = id,
    aggregate_view = package$aggregate_view,
    reconciliation = package$aggregate_reconciliation,
    rows = aggregate_rows(package)
  )
})

dzs <- package_by_id("dzs_turizam")
route_records <- lapply(packages, function(package) {
  id <- anchor_id(package$id)
  list(
    id = package$id,
    lane = package$lane,
    promoted = isTRUE(package$promoted),
    public_anchor = paste0("podaci.qmd#podaci-", id),
    appendix_anchor = paste0("dodaci/c-katalog-podataka.qmd#sec-data-", id),
    declared_files = unname(unlist(package$files, use.names = FALSE))
  )
})

artifact <- list(
  schema_version = "appendix-c-data-route-v1",
  packet = "P5-C",
  generated_at = "2026-08-25",
  canonical_catalogue = list(
    path = "data/katalog.yml",
    md5 = unname(tools::md5sum(catalogue_path)),
    sole_machine_readable_record = isTRUE(catalogue$sole_machine_readable_record)
  ),
  public_promise = paste(
    "Dodatak C i stranica Podaci nastaju zajedno iz data/katalog.yml; svaki",
    "paket ima podudarne sidrene rute, a deklarirane agregatne datoteke cuvaju",
    "neokrugljene vrijednosti potrebne za rucnu provjeru."
  ),
  counts = list(
    packages = length(packages),
    promoted = promoted_count,
    bundled = unname(lane_counts[["bundled"]]),
    portal_mediated = unname(lane_counts[["portal-mediated"]]),
    external_only = unname(lane_counts[["external-only"]])
  ),
  generated_views = list(
    list(path = "podaci.qmd", md5 = unname(tools::md5sum(public_path)), anchors = length(route_records)),
    list(path = "dodaci/c-katalog-podataka.qmd", md5 = unname(tools::md5sum(appendix_path)), anchors = length(route_records))
  ),
  package_routes = route_records,
  aggregate_hand_checks = aggregate_contract,
  dzs_reconciliation = list(
    source = "data/katalog.yml#packages.dzs_turizam.source_reconciliation",
    administrative = Filter(function(record) identical(as.integer(record$tolerance), 0L), dzs$source_reconciliation),
    survey = Filter(function(record) identical(as.integer(record$tolerance), 1L), dzs$source_reconciliation),
    measures_are_comparable_series = FALSE
  ),
  readme_status = lapply(
    c("digikat_mediji", "rdp_potpore", "bdp_dugi_niz"),
    function(id) {
      package <- package_by_id(id)
      list(id = id, promoted = isTRUE(package$promoted), promoted_by = package$promoted_by)
    }
  )
)

artifact_path <- root_file("config", "appendix-c-data-route.json")
artifact_json <- paste0(jsonlite::toJSON(
  artifact,
  auto_unbox = TRUE,
  pretty = TRUE,
  digits = NA,
  na = "null",
  null = "null"
), "\n")

if (write_outputs) {
  write_utf8(artifact_json, artifact_path)
} else {
  if (!file.exists(artifact_path)) stop("Nedostaje route artefakt Dodatka C.")
  current_artifact <- paste0(paste(readLines(artifact_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n"), "\n")
  if (!identical(current_artifact, artifact_json)) {
    stop("Route artefakt Dodatka C nije jednak svjeze izgradjenomu.")
  }
}

cat(
  "APPENDIX_C_VIEWS_OK",
  paste0("packages=", length(packages)),
  paste0("promoted=", promoted_count),
  "views=2",
  paste0("routes=", length(route_records)),
  paste0("aggregate_rows=", sum(vapply(aggregate_contract, function(record) nrow(record$rows), integer(1)))),
  paste0("dzs_admin=", length(artifact$dzs_reconciliation$administrative)),
  paste0("dzs_survey=", length(artifact$dzs_reconciliation$survey)),
  "\n"
)
