#!/usr/bin/env Rscript

# Gradi kanonski, strojno citljiv put Dodatka B iz prihvacene rute Dodatka A.
# Namjerno ne pokrece jamovi i ne tvrdi da je provedena provjera ciste
# instalacije; vlasnik te provjere odredjen je odlukom D09.

builder_args <- commandArgs(trailingOnly = TRUE)

arg_value <- function(flag, default = NULL) {
  hit <- match(flag, builder_args)
  if (is.na(hit)) return(default)
  if (hit == length(builder_args)) stop("Nedostaje vrijednost nakon ", flag, ".")
  builder_args[[hit + 1L]]
}

route_root <- normalizePath(arg_value("--root", "."), mustWork = TRUE)
artifact_path <- file.path(
  route_root,
  arg_value("--artifact", "config/appendix-b-jamovi-route.json")
)
write_artifact <- "--write" %in% builder_args

root_file <- function(...) file.path(route_root, ...)

route_environment <- new.env(parent = globalenv())
route_log <- capture.output(
  source(root_file("scripts", "appendix-a-route.R"), local = route_environment)
)
if (!any(grepl("APPENDIX_A_ROUTE_OK", route_log, fixed = TRUE))) {
  stop("Dodatak A nije prijavio uspjesnu kanonsku rutu.")
}

text_path <- root_file("data", "parlament_oznake.csv")
if (!file.exists(text_path)) stop("Nedostaje pripremljena tekstna tablica.")
if (unname(tools::md5sum(text_path)) != "55b1c4263009ab783911f094907312d9") {
  stop("Promijenio se MD5 pripremljene tekstne tablice.")
}
text_rows <- nrow(read.csv(text_path, stringsAsFactors = FALSE, check.names = FALSE))
if (text_rows != 2698L) stop("Pripremljena tekstna tablica nema 2698 redaka.")

results <- route_environment$results
key <- paste(results$chapter, results$metric, sep = ":")
value_by_key <- setNames(results$value, key)

golden <- function(keys) {
  missing <- setdiff(keys, names(value_by_key))
  if (length(missing)) stop("Nedostaju zlatne vrijednosti: ", paste(missing, collapse = ", "))
  as.list(value_by_key[keys])
}

row_filter <- function(data, label) {
  ids <- sort(as.integer(data$osoba))
  list(
    label = label,
    key = "osoba",
    selected_rows = length(ids),
    selected_ids = ids,
    jamovi_formula = paste0("osoba == ", ids, collapse = " or ")
  )
}

module <- list(
  product = "jamovi",
  product_version = "2.7.30.0",
  product_tag = "v2.7.30",
  core_module = "jmv",
  core_module_version = "2.7.7",
  core_module_commit = "8c07513626f458bf9d855ac3a8271a9de9c312f9"
)

documentation <- list(
  release = "https://github.com/jamovi/jamovi/releases/tag/v2.7.30",
  product_version = "https://raw.githubusercontent.com/jamovi/jamovi/v2.7.30/version",
  module_version = paste0(
    "https://raw.githubusercontent.com/jamovi/jmv/",
    module$core_module_commit,
    "/DESCRIPTION"
  ),
  data_and_filters = "https://docs.jamovi.org/usermanual/um_4_spreadsheet.html",
  functions = "https://docs.jamovi.org/data/data_5_list_of_functions.html",
  descriptives = "https://jamovi.readthedocs.io/en/latest/jmv/jmv_descriptives/",
  correlation = "https://jamovi.readthedocs.io/en/latest/jmv/jmv_corrMatrix/",
  independent_t = "https://jamovi.readthedocs.io/en/latest/jmv/jmv_ttestIS/",
  contingency = "https://jamovi.readthedocs.io/en/latest/jmv/jmv_contTables/",
  anova = "https://jamovi.readthedocs.io/en/latest/jmv/jmv_ANOVA/",
  regression = "https://jamovi.readthedocs.io/en/latest/analyses/jg_42_regression-linear/",
  archive = "https://jamovi.readthedocs.io/en/latest/developer/dh_info_file-format/"
)

common <- list(
  module = module,
  documentation_checked_at = "2026-08-25",
  weights = "Nema tezina; katalog za ove ulaze izrijekom zabranjuje izmisljanje praznoga stupca tezina.",
  export = "Spremiti radnu datoteku .omv, koja cuva podatke, postavke i rezultate, te uz nju izvesti samo tablicu koja nosi imenovanu zlatnu vrijednost.",
  verification = "Usporediti neokrugljenu vrijednost s config/appendix-b-jamovi-route.json; odstupanje se ne tumaci nego prijavljuje vlasniku ciste instalacije.",
  claim_boundary = "Sinteticki podaci ne podupiru tvrdnju o stvarnoj populaciji; rezultat opisuje samo imenovani skup i postupak.",
  clean_install = list(
    owner = "Luka Sikic",
    roles = c("autor", "vlasnik kolegija"),
    status = "pending_owner_verification",
    claimed_by_packet = FALSE,
    note = "P5-B ne tvrdi da je ruta provjerena na cistoj instalaciji."
  )
)

route <- function(id, chapter, dataset, file, question, variables, import_types,
                  analysis, menu_path, settings, filter, expected_keys,
                  interpretation, support_status = "documented_pending_clean_install",
                  extra_boundary = NULL, docs) {
  c(
    list(
      id = id,
      chapter = chapter,
      dataset = dataset,
      file = file,
      question = question,
      variables = variables,
      import_types = import_types,
      analysis = analysis,
      menu_path = menu_path,
      settings = settings,
      filter = filter,
      expected_output = expected_keys,
      golden_values = golden(expected_keys),
      interpretation = interpretation,
      support_status = support_status,
      additional_claim_boundary = extra_boundary,
      documentation = docs
    ),
    common
  )
}

q_anketa <- unique(results$question[results$dataset == "anketa_mreze"])
q_populacija <- unique(results$question[results$dataset == "populacija_medija"])
q_rrr <- unique(results$question[results$dataset == "rrr_lab_effects"])
q_text <- "Kako se ton parlamentarnih iskaza razlikuje s obzirom na stranacku pripadnost?"
q_text_canonical <- "Kako se ton parlamentarnih iskaza razlikuje s obzirom na stranačku pripadnost?"
if (!any(grepl(q_text_canonical, readLines(root_file("scripts", "appendix-a-route.R"), encoding = "UTF-8"), fixed = TRUE))) {
  stop("Tekstno pitanje vise nije jednako pitanju Dodatka A.")
}

routes <- list(
  route(
    "B-C06-PEARSON", "6", "anketa_mreze", "data/anketa-mreze.csv", q_anketa,
    c("minute_dnevno", "povjerenje"),
    list(minute_dnevno = "Continuous/Integer", povjerenje = "Continuous/Integer"),
    "Pearsonova korelacijska matrica",
    c("Analyses", "Regression", "Correlation Matrix"),
    list(variables = c("minute_dnevno", "povjerenje"), pearson = TRUE, spearman = FALSE, kendall = FALSE, report_n = TRUE),
    list(active = FALSE, formula = NULL),
    "6:pearson_r",
    "Predznak daje smjer, a velicina linearnu povezanost; rasprseni prikaz ostaje obvezna provjera oblika.",
    docs = c(documentation$correlation, documentation$archive)
  ),
  route(
    "B-C07-UVJETNI-UDIO", "7", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    c("dob", "izvor_vijesti"),
    list(dob = "Continuous/Integer", izvor_vijesti = "Nominal/Text"),
    "Frekvencije nakon uvjetnoga filtra",
    c("Analyses", "Exploration", "Descriptives"),
    list(variables = "izvor_vijesti", frequency_tables = TRUE, ratio = "društvene mreže / svi uključeni redci"),
    list(active = TRUE, label = "dob_do_29", jamovi_formula = "dob <= 29"),
    "7:p_mreze_dob_le_29",
    "Udio je uvjetovan dobi do i ukljucivo 29 godina; nazivnik su samo ukljuceni redci.",
    docs = c(documentation$data_and_filters, documentation$descriptives)
  ),
  route(
    "B-C08-STANDARDNA-POGRESKA", "8", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    "povjerenje_medijima",
    list(povjerenje_medijima = "Continuous/Integer"),
    "Opisna provjera populacijske standardne pogreske za n = 100",
    c("Data", "Compute"),
    list(
      computed_variable = "se_n100",
      jamovi_formula = "SQRT((VROWS(povjerenje_medijima) - 1) / VROWS(povjerenje_medijima)) * VSTDEV(povjerenje_medijima) / SQRT(100)"
    ),
    list(active = FALSE, formula = NULL),
    "8:se_povjerenje_n_100",
    "Ovo je poznata standardna pogreska za izvlake velicine 100 iz generirane populacije, a ne procjena iz stvarne populacije.",
    docs = c(documentation$functions, documentation$data_and_filters)
  ),
  route(
    "B-C09-INTERVAL", "9", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    c("osoba", "povjerenje_medijima"),
    list(osoba = "ID/Integer", povjerenje_medijima = "Continuous/Integer"),
    "Sredina i standardna pogreska istoga fiksnog uzorka",
    c("Analyses", "Exploration", "Descriptives"),
    list(variables = "povjerenje_medijima", statistics = c("N", "Mean", "SE"), interval_rule = "Mean +/- 1.96 * SE"),
    row_filter(route_environment$uzorak9, "uzorak_poglavlje_09"),
    c("9:mean_povjerenje", "9:ci95_lower", "9:ci95_upper"),
    "Interval opisuje postupak ponavljanoga uzorkovanja; jedna dobivena granica nije vjerojatnost da parametar lezi u njoj.",
    docs = c(documentation$data_and_filters, documentation$descriptives)
  ),
  route(
    "B-C10-RAZLIKA", "10", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    c("osoba", "izvor_vijesti", "povjerenje_medijima"),
    list(osoba = "ID/Integer", izvor_vijesti = "Nominal/Text", povjerenje_medijima = "Continuous/Integer"),
    "Opisna razlika sredina istoga fiksnog uzorka",
    c("Analyses", "Exploration", "Descriptives"),
    list(variables = "povjerenje_medijima", split_by = "izvor_vijesti", retained_levels = c("portal", "tisak"), difference_order = "portal minus tisak"),
    row_filter(route_environment$dvije10, "uzorak_poglavlje_10"),
    "10:mean_difference_portal_minus_tisak",
    "Razlika sredina nije permutacijski p niti uzrocni ucinak.",
    extra_boundary = "Ugradjeni jmv 2.7.7 nema dokumentiran tocno isti test s 4000 permutacija i +1 korekcijom; 10:permutation_p_two_sided ostaje samo u Dodatku A.",
    docs = c(documentation$data_and_filters, documentation$descriptives)
  ),
  route(
    "B-C11-COHEN-D", "11", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    c("izvor_vijesti", "povjerenje_medijima"),
    list(izvor_vijesti = "Nominal/Text", povjerenje_medijima = "Continuous/Integer"),
    "Standardizirana razlika dviju skupina",
    c("Analyses", "T-Tests", "Independent Samples T-Test"),
    list(dependent_variables = "povjerenje_medijima", grouping_variable = "izvor_vijesti", retained_levels = c("portal", "tisak"), group_order = "portal minus tisak", students = TRUE, effect_size = TRUE),
    list(active = TRUE, label = "portal_ili_tisak", jamovi_formula = "izvor_vijesti == 'portal' or izvor_vijesti == 'tisak'"),
    "11:cohen_d_portal_minus_tisak",
    "Cohenov d izrazava razliku u jedinicama zajednicke standardne devijacije; ne daje prakticnu vaznost sam po sebi.",
    docs = c(documentation$data_and_filters, documentation$independent_t)
  ),
  route(
    "B-C13-HI-KVADRAT", "13", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    c("osoba", "obrazovanje", "izvor_vijesti"),
    list(osoba = "ID/Integer", obrazovanje = "Nominal/Text", izvor_vijesti = "Nominal/Text"),
    "Kontingencijska tablica i hi-kvadrat",
    c("Analyses", "Frequencies", "Contingency Tables", "Independent Samples"),
    list(rows = "obrazovanje", columns = "izvor_vijesti", chi_square = TRUE, expected_counts = TRUE, cramers_v = TRUE),
    row_filter(route_environment$uzorak13, "uzorak_poglavlje_13"),
    c("13:chi_squared", "13:cramers_v"),
    "Hi-kvadrat sazimlje odstupanja opazenih od ocekivanih frekvencija, a Cramerov V velicinu povezanosti.",
    docs = c(documentation$data_and_filters, documentation$contingency)
  ),
  route(
    "B-C14-WELCH", "14", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    c("osoba", "izvor_vijesti", "povjerenje_medijima"),
    list(osoba = "ID/Integer", izvor_vijesti = "Nominal/Text", povjerenje_medijima = "Continuous/Integer"),
    "Welchova usporedba dviju skupina",
    c("Analyses", "T-Tests", "Independent Samples T-Test"),
    list(dependent_variables = "povjerenje_medijima", grouping_variable = "izvor_vijesti", retained_levels = c("TV", "društvene mreže"), group_order = "TV minus društvene mreže", students = FALSE, welchs = TRUE, mean_difference = TRUE, confidence_interval = 95),
    row_filter(route_environment$dvije14, "uzorak_poglavlje_14"),
    c("14:mean_difference_tv_minus_mreze", "14:welch_ci95_lower", "14:welch_ci95_upper"),
    "Procjena i interval vode tumacenje; rezultat ne pretvara skupine u randomizirani pokus.",
    docs = c(documentation$data_and_filters, documentation$independent_t)
  ),
  route(
    "B-C15-ANOVA", "15", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    c("osoba", "izvor_vijesti", "povjerenje_medijima"),
    list(osoba = "ID/Integer", izvor_vijesti = "Nominal/Text", povjerenje_medijima = "Continuous/Integer"),
    "Jednofaktorska klasicna ANOVA",
    c("Analyses", "ANOVA", "ANOVA"),
    list(dependent_variable = "povjerenje_medijima", fixed_factors = "izvor_vijesti", sums_of_squares = 3, effect_size = "eta squared", welch = FALSE),
    row_filter(route_environment$uzorak15, "uzorak_poglavlje_15"),
    c("15:anova_f", "15:eta_squared"),
    "F-omjer je zbirna usporedba, a eta-kvadrat udio varijabilnosti povezan s faktorom u ovom uzorku.",
    docs = c(documentation$data_and_filters, documentation$anova)
  ),
  route(
    "B-C16-REGRESIJA", "16", "populacija_medija", "data/populacija-medija.csv", q_populacija,
    c("dob", "izvor_vijesti", "povjerenje_medijima"),
    list(dob = "Continuous/Integer", izvor_vijesti = "Nominal/Text", povjerenje_medijima = "Continuous/Integer"),
    "Visestruka linearna regresija",
    c("Analyses", "Regression", "Linear Regression"),
    list(dependent_variable = "povjerenje_medijima", covariates = "dob", factors = "izvor_vijesti", factor_reference = "portal", estimates = TRUE, model_fit = TRUE),
    list(active = FALSE, formula = NULL),
    c("16:slope_dob", "16:coefficient_drustvene_mreze", "16:adjusted_r_squared"),
    "Koeficijent dobi drzi izvor vijesti stalnim, a kategorijski koeficijent usporedjuje mreze s referentnim portalom; model nije uzrocna tvrdnja.",
    docs = c(documentation$regression, documentation$archive)
  ),
  c(
    list(
      id = "B-TEXT-PREPARED",
      chapter = "A-tekst",
      dataset = "parlasent_hr",
      file = "data/parlament_oznake.csv",
      question = q_text_canonical,
      variables = c("record_id", "source_document_id", "derived_split", "recorded_label", "label_path"),
      import_types = list(record_id = "ID/Text", source_document_id = "ID/Integer", derived_split = "Nominal/Text", recorded_label = "Nominal/Text", label_path = "Nominal/Text"),
      analysis = "Pregled pripremljene tablice i frekvencija putova oznake",
      menu_path = c("Analyses", "Exploration", "Descriptives"),
      settings = list(variables = c("derived_split", "recorded_label", "label_path"), frequency_tables = TRUE, expected_rows = text_rows),
      filter = list(active = FALSE, formula = NULL),
      expected_output = "A-tekst:prepared_rows",
      golden_values = list("A-tekst:prepared_rows" = as.numeric(text_rows)),
      interpretation = "Jedan redak je jedna oznacena recenica; zabiljezena oznaka nije istina o recenici ni govorniku.",
      support_status = "documented_pending_clean_install",
      additional_claim_boundary = "Datoteka nema stranacku pripadnost, pa ovo nije analiza razlika medju strankama; put samo provjerava pripremljenu tablicu koju Dodatak A vec imenuje.",
      documentation = c(documentation$descriptives, documentation$archive)
    ),
    common
  )
)

unsupported <- list(
  list(
    chapter = "10",
    metric_keys = "10:permutation_p_two_sided",
    dataset = "populacija_medija",
    file = "data/populacija-medija.csv",
    question = q_populacija,
    variables = c("osoba", "izvor_vijesti", "povjerenje_medijima"),
    reason = "Ugradjeni jmv 2.7.7 ne dokumentira tocno 4000 preslagivanja uz +1 korekciju Dodatka A; vrijednost se ne reproducira drugim testom."
  ),
  list(
    chapter = "12",
    metric_keys = c(
      "12:raw_fixed_effect_estimate", "12:raw_ci95_lower", "12:raw_ci95_upper",
      "12:standardized_fixed_effect_estimate", "12:standardized_ci95_lower", "12:standardized_ci95_upper"
    ),
    dataset = "rrr_lab_effects",
    file = "notes/reports/p3-evidence12-rrr-lab-effects.csv",
    question = q_rrr,
    variables = c("raw_se", "raw_mean_difference", "d_se", "cohen_d"),
    reason = "Fiksni dokazni spoj iz Dodatka A nije dokumentiran postupak u ugradjenom jmv 2.7.7; vanjski modul nije uveden bez vlasnicke provjere ciste instalacije."
  )
)

supported_keys <- unlist(lapply(routes, function(x) x$expected_output), use.names = FALSE)
unsupported_keys <- unlist(lapply(unsupported, function(x) x$metric_keys), use.names = FALSE)
all_values <- as.list(value_by_key)
all_values[["A-tekst:prepared_rows"]] <- as.numeric(text_rows)
appendix_a_contract <- lapply(seq_len(nrow(results)), function(i) {
  as.list(results[i, c("chapter", "dataset", "file", "question", "metric", "value")])
})
appendix_a_contract[[length(appendix_a_contract) + 1L]] <- list(
  chapter = "A-tekst",
  dataset = "parlasent_hr",
  file = "data/parlament_oznake.csv",
  question = q_text_canonical,
  metric = "prepared_rows",
  value = as.numeric(text_rows)
)

artifact <- list(
  schema_version = "appendix-b-jamovi-route-v1",
  packet = "P5-B",
  decision = "D09",
  generated_at = "2026-08-25",
  canonical_appendix_a_route = "scripts/appendix-a-route.R",
  public_promise = paste(
    "Dokumentirana ruta za jezgrene analize koje moze izvesti ugradjeni jmv",
    "2.7.7 u jamoviju 2.7.30.0, uz iste kanonske datoteke, varijable, pitanja",
    "i zlatne vrijednosti kao Dodatak A; cista instalacija jos ceka vlasnika."
  ),
  product = module,
  clean_install = common$clean_install,
  scope = list(
    supported_metric_keys = supported_keys,
    unsupported_metric_keys = unsupported_keys,
    all_appendix_a_metric_keys = names(all_values),
    no_extra_metrics = identical(sort(c(supported_keys, unsupported_keys)), sort(names(all_values)))
  ),
  golden_values = all_values,
  appendix_a_contract = appendix_a_contract,
  routes = routes,
  unsupported_in_pinned_core = unsupported,
  documentation = documentation
)

if (!isTRUE(artifact$scope$no_extra_metrics)) {
  stop("Podrzane i nepodrzane metrike nisu tocna particija Dodatka A.")
}

json <- jsonlite::toJSON(
  artifact,
  auto_unbox = TRUE,
  pretty = TRUE,
  digits = NA,
  na = "null",
  null = "null"
)
json <- paste0(json, "\n")

if (write_artifact) {
  dir.create(dirname(artifact_path), recursive = TRUE, showWarnings = FALSE)
  writeChar(enc2utf8(json), artifact_path, eos = NULL, useBytes = TRUE)
} else {
  if (!file.exists(artifact_path)) stop("Nedostaje kanonski artefakt: ", artifact_path)
  existing <- paste(readLines(artifact_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  existing <- paste0(existing, "\n")
  if (!identical(existing, json)) stop("Kanonski artefakt nije jednak svjeze izgradjenoj ruti.")
}

cat(
  "APPENDIX_B_ROUTE_OK",
  paste0("product=", module$product_version),
  paste0("module=", module$core_module_version),
  paste0("supported=", length(supported_keys)),
  paste0("guarded=", length(unsupported_keys)),
  paste0("total=", length(all_values)),
  "clean_install=pending_owner",
  "\n"
)
