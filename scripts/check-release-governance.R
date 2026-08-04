# check-release-governance.R -----------------------------------------------
# Validates the local pre-release governance mechanism. It never changes
# release state and performs no network or external action.
# Run through:
#   python bookwright_plugin/bookwright/scripts/run_rscript.py \
#     scripts/check-release-governance.R
# ---------------------------------------------------------------------------

for (package in c("yaml", "digest")) {
  if (!requireNamespace(package, quietly = TRUE)) {
    stop("Missing R package '", package, "'.")
  }
}

root <- normalizePath(".", winslash = "/", mustWork = TRUE)
at <- function(...) file.path(root, ...)

errors <- character()
check <- function(condition, message) {
  if (!isTRUE(condition)) errors <<- c(errors, message)
}
scalar_text <- function(value) {
  is.character(value) && length(value) == 1L && nzchar(value)
}
read_text <- function(path) {
  paste(readLines(at(path), warn = FALSE, encoding = "UTF-8"),
        collapse = "\n")
}

governance_path <- at("release", "governance.yml")
errata_path <- at("release", "errata.yml")
provenance_path <- at("release", "provenance.yml")

for (path in c(governance_path, errata_path, provenance_path)) {
  check(file.exists(path), paste("Missing governance file:", path))
}
if (length(errors)) stop(paste(errors, collapse = "\n"))

governance <- yaml::read_yaml(governance_path)
errata <- yaml::read_yaml(errata_path)
provenance <- yaml::read_yaml(provenance_path)
quarto <- yaml::read_yaml(at("_quarto.yml"))

check(identical(governance$schema_version, 1L),
      "Governance schema_version must be 1.")
check(identical(governance$current_state, "pre_release"),
      "Canonical release state must remain pre_release.")
check(identical(governance$book$working_title,
                "Osnove statistike za društvene znanosti"),
      "D14 working title has drifted.")
check(identical(governance$book$title_state, "working_not_frozen"),
      "Title must remain explicitly unfrozen.")
check(identical(quarto$book$title, governance$book$working_title),
      "_quarto.yml title disagrees with the D14 working title.")
check(identical(governance$book$authorship_state,
                "working_not_frozen"),
      "Authorship must remain explicitly unfrozen.")

for (field in c("edition", "version", "release_date")) {
  record <- governance[[field]]
  value <- if (identical(field, "edition")) record$label else record$value
  check(is.null(value), paste(field, "must remain unset in P1B-GOV."))
  check(identical(record$state, "unset_pre_release"),
        paste(field, "must be marked unset_pre_release."))
}
check(is.null(governance$citation$final_citation),
      "Final citation must remain unset.")
check(is.null(governance$citation$persistent_identifier),
      "Persistent identifier must remain unset.")

for (role in c("release", "archive", "errata")) {
  check(identical(governance$owners[[role]]$name, "Luka Sikic"),
        paste("Unexpected", role, "owner."))
}
check(is.null(governance$owners$term_freeze$name),
      "P1B-GOV must not appoint the later term-freeze owner.")
check(identical(governance$owners$term_freeze$state,
                "awaiting_G-A5c_owner_confirmation"),
      "Term-freeze ownership must remain gated by G-A5c.")

authority <- unlist(governance$authority, use.names = TRUE)
check(length(authority) == 7L && all(!authority),
      "Every external-action and inferred-authority flag must be false.")

mechanism_paths <- c(
  governance$mechanisms$changelog$path,
  governance$mechanisms$provenance$path,
  governance$mechanisms$archive_plan$path,
  governance$mechanisms$term_freeze_policy$path,
  governance$mechanisms$errata$page,
  governance$mechanisms$errata$log
)
for (path in mechanism_paths) {
  check(scalar_text(path) && file.exists(at(path)),
        paste("Missing mechanism path:", path))
}

transitions <- governance$state_machine$transitions
check(is.list(transitions) && length(transitions) == 7L,
      "Release state machine must define exactly seven transitions.")
check(length(governance$state_machine$persisted_transitions) == 0L,
      "P1B-GOV must not persist a release transition.")
external <- vapply(transitions, function(x) isTRUE(x$external_action),
                   logical(1))
for (transition in transitions[external]) {
  check(scalar_text(transition$authority_gate),
        "Every external transition must retain an exact authority gate.")
}
check(identical(governance$demonstration$mode,
                "in_memory_non_persisting"),
      "Demonstration must be non-persisting.")
check(identical(governance$demonstration$expected_result,
                "blocked_without_required_gate"),
      "Demonstration must prove the missing-gate block.")
check(identical(governance$demonstration$persisted, FALSE),
      "Demonstration must not persist release state.")

check(identical(errata$schema_version, 1L),
      "Errata schema_version must be 1.")
check(identical(errata$owner$name, "Luka Sikic"),
      "Errata owner must be Luka Sikic.")
check(identical(errata$route$state, "source_ready_not_public"),
      "Errata route must remain locally ready and publicly inactive.")
check(is.null(errata$route$submission_target),
      "Public errata submission target must remain unset.")
check(identical(errata$route$activation_gate, "G-A6-DEPLOY"),
      "Errata activation must remain gated by G-A6-DEPLOY.")
check(length(errata$entries) == 0L,
      "The pre-release errata log must not invent entries.")

changelog <- read_text("CHANGELOG.md")
index <- read_text("index.qmd")
colophon <- read_text(file.path("tex", "colophon.tex"))
archive_plan <- read_text(file.path("release", "archive-plan.md"))
term_policy <- read_text(file.path("release", "term-freeze-policy.md"))
errata_page <- read_text("errata.qmd")
quarto_text <- read_text("_quarto.yml")

check(grepl("## Neobjavljeno", changelog, fixed = TRUE) &&
        grepl("4. kolovoza 2026.", changelog, fixed = TRUE),
      "Croatian changelog lacks its dated unpublished entry.")
check(grepl("## Kako citirati ovu knjigu {#kako-citirati}", index,
            fixed = TRUE) &&
        grepl("predobjavni radni nacrt", index, fixed = TRUE),
      "Landing page lacks the explicit pre-release citation block.")
check(grepl("Predobjavni nacrt", colophon, fixed = TRUE) &&
        grepl("P8-META", colophon, fixed = TRUE),
      "Colophon lacks the non-final citation boundary.")
check(grepl("G-A6-ARCHIVE", archive_plan, fixed = TRUE) &&
        grepl("Nije arhivski polog", archive_plan, fixed = TRUE),
      "Archive plan does not preserve its no-deposit boundary.")
check(grepl("G-A5c", term_policy, fixed = TRUE) &&
        grepl("G-A6-DEPLOY", term_policy, fixed = TRUE),
      "Term-freeze policy lacks its owner and activation gates.")
check(grepl("4. kolovoza 2026.", errata_page, fixed = TRUE) &&
        grepl("Luka Sikic", errata_page, fixed = TRUE) &&
        grepl("nije javno aktiviran", errata_page, fixed = TRUE),
      "Errata page lacks its date, owner, or inactive-state warning.")
check(grepl('text: "Ispravci"', quarto_text, fixed = TRUE) &&
        grepl("href: errata.qmd", quarto_text, fixed = TRUE),
      "Local errata route is not wired into Quarto.")

check(identical(provenance$schema_version, 1L),
      "Provenance schema_version must be 1.")
check(identical(provenance$record_type,
                "pre_release_governance_demonstration"),
      "Unexpected provenance record type.")
check(identical(provenance$source$immutable_release_state, FALSE),
      "Provenance demonstration must not claim immutable release state.")
check(is.null(provenance$release_candidate$commit) &&
        is.null(provenance$release_candidate$tag) &&
        is.null(provenance$release_candidate$persistent_identifier),
      "Release-candidate or immutable identifiers must remain unset.")
check(length(provenance$release_artifacts) == 0L,
      "P1B-GOV must not record public release artifacts.")

manifest <- provenance$manifest
check(is.list(manifest) && length(manifest) >= 10L,
      "Provenance manifest is incomplete.")
if (is.list(manifest)) {
  paths <- vapply(manifest, function(x) x$path, character(1))
  check(!anyDuplicated(paths), "Provenance manifest repeats a path.")
  for (record in manifest) {
    path <- record$path
    full <- at(path)
    check(file.exists(full), paste("Manifest path is missing:", path))
    if (file.exists(full)) {
      actual <- tolower(digest::digest(file = full, algo = "sha256"))
      check(identical(actual, tolower(record$sha256)),
            paste("SHA-256 mismatch for", path))
    }
  }
}

if (length(errors)) {
  stop(paste(c("Release-governance validation failed:", errors),
             collapse = "\n- "))
}

cat("Release governance: OK\n")
cat("- state: pre_release\n")
cat("- D14 working title retained; final metadata unset\n")
cat("- owners: release/archive/errata = Luka Sikic\n")
cat("- mechanisms: changelog, citation, provenance, archive, term freeze, errata\n")
cat("- demonstration: missing G-A5b blocks transition; no state persisted\n")
cat("- external authority: all false\n")
