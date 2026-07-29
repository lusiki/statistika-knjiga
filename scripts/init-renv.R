# init-renv.R ---------------------------------------------------------------
# Jednokratna inicijalizacija reproducibilnog R okruženja.
#
#   Rscript scripts/init-renv.R
#
# Rezultat: renv/ direktorij + renv.lock s fiksiranim verzijama. Nakon toga
# .Rprofile automatski aktivira renv u svakoj sesiji, a CI (publish.yml)
# prelazi s ad-hoc instalacije paketa na obnovu iz lockfilea.
#
# Suradnici poslije samo pokreću:  renv::restore()
# ---------------------------------------------------------------------------

if (!requireNamespace("renv", quietly = TRUE)) {
  install.packages("renv", repos = "https://cloud.r-project.org")
}

# Paketi koje knjiga stvarno koristi. Dopuni kad poglavlje uvede novi.
paketi <- c(
  "ggplot2", "dplyr", "tidyr",       # jezgra svih poglavlja (R/setup.R)
  "yaml", "jsonlite",                # build skripte + tema čita design-tokens.yml
  "stringr", "stringi",              # build-ai-exports.R, build-concept-graph.R
  "knitr", "rmarkdown",              # render
  "downlit", "xml2"                  # code-link: true u _quarto.yml
)

message("Instaliram pakete u projektnu biblioteku…")
renv::init(bare = TRUE, restart = FALSE)
renv::install(paketi)
renv::snapshot(prompt = FALSE)

message("Gotovo. renv.lock zapisan — urezni ga (commit) zajedno s renv/activate.R.")
