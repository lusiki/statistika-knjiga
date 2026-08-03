# check-review-workflow.R ---------------------------------------------------
# Validates the comprehensive-review register, forward handoffs, and dashboard.
# Run through the project launcher; do not assume Rscript is on PATH:
#
#   python bookwright_plugin/bookwright/scripts/run_rscript.py \
#     scripts/check-review-workflow.R
# ---------------------------------------------------------------------------

if (!requireNamespace("yaml", quietly = TRUE)) {
  stop("Missing R package 'yaml'. Install it before checking review workflow state.")
}

root <- normalizePath(".", winslash = "/", mustWork = TRUE)
path <- function(...) file.path(root, ...)

register_path <- path(
  "notes", "reports", "comprehensive-review-implementation-register.yml"
)
handoff_path <- path(
  "notes", "reports", "comprehensive-review-forward-handoffs.yml"
)
dashboard_path <- path(
  "notes", "reports", "comprehensive-review-dashboard.md"
)

for (candidate in c(register_path, handoff_path, dashboard_path)) {
  if (!file.exists(candidate)) stop("Missing workflow file: ", candidate)
}

register <- yaml::read_yaml(register_path)
handoff_ledger <- yaml::read_yaml(handoff_path)
dashboard_lines <- readLines(dashboard_path, warn = FALSE, encoding = "UTF-8")

errors <- character()
add_error <- function(...) {
  errors <<- c(errors, paste0(...))
}
check <- function(condition, ...) {
  if (!isTRUE(condition)) add_error(...)
}
is_scalar_text <- function(value) {
  is.character(value) && length(value) == 1L && nzchar(value)
}
or_empty <- function(value) {
  if (is.null(value)) character() else unlist(value, use.names = FALSE)
}
named_entries <- function(value) {
  if (is.null(value)) character() else names(value)
}

allowed_work_statuses <- c(
  "proposed", "ratified", "in_progress", "implemented", "verified",
  "accepted", "deferred_v2_with_reason"
)
allowed_dispositions <- c(
  "accepted_first_edition", "already_satisfied", "rejected_with_reason",
  "deferred_v2_with_reason"
)
allowed_handoff_kinds <- c(
  "constraint", "prerequisite", "evidence", "risk", "decision",
  "invalidation"
)
allowed_handoff_gates <- c("before_start", "before_close")
allowed_delivery_states <- c(
  "pending", "acknowledged", "consumed", "waived", "superseded"
)
terminal_delivery_states <- c("consumed", "waived", "superseded")

check(identical(register$schema_version, 2L),
      "Register schema_version must be 2.")
check(identical(handoff_ledger$schema_version, 1L),
      "Handoff schema_version must be 1.")
check(identical(register$control$write_wip_limit, 1L),
      "write_wip_limit must be exactly 1.")

expected_defaults <- sprintf("D%02d", 1:16)
accepted_defaults <- or_empty(register$decisions$`G-A0`$accepted_defaults)
check(setequal(accepted_defaults, expected_defaults),
      "G-A0 must record exactly D01-D16 as accepted defaults.")
check(all(!unlist(register$authority[c("push", "merge", "tag", "archive", "deploy")])),
      "A0 must not authorise push, merge, tag, archive, or deployment.")

packet_ids <- named_entries(register$packets)
check(length(packet_ids) > 0L, "Register must contain packet records.")
check(!anyDuplicated(packet_ids), "Packet IDs must be unique.")
check(!any(grepl("\\.\\.|…|–", packet_ids)),
      "Packet IDs must be exact; ranges and ellipses are forbidden.")

required_exact_packets <- c(
  "P1C-INVENTORY",
  "P1C-INTEGRITY",
  "P7-PILOT",
  "P7-HTML",
  "P7-CLEAN-BUILD",
  "P8-SMOKE",
  "G-A6",
  paste0("P3-VERIFY-", LETTERS[1:4]),
  sprintf("C%02d", 0:18),
  sprintf("P5-CLOSURE-%02d", 0:18),
  paste0("G-A2b-", c("PREFACE", "I", "II", "III", "IV", "V", "FINALE")),
  paste0("P2-SPINE-", c("PREFACE", "I", "II", "III", "IV", "V", "FINALE")),
  c("G-A5a", "G-A5b", "G-A5c", "G-A5d"),
  c("G-A6-PUSH", "G-A6-TAG", "G-A6-ARCHIVE", "G-A6-DEPLOY")
)
missing_exact_packets <- setdiff(required_exact_packets, packet_ids)
if (length(missing_exact_packets)) {
  add_error("Missing exact packet catalogue entries: ",
            paste(missing_exact_packets, collapse = ", "))
}

contract_ids <- named_entries(register$packet_contracts)
check(length(contract_ids) > 0L,
      "Register must define reusable packet contracts.")

packet_status <- vapply(register$packets, function(packet) {
  if (is.null(packet$status)) NA_character_ else as.character(packet$status)
}, character(1))
bad_packet_status <- packet_ids[is.na(packet_status) |
                                  !packet_status %in% allowed_work_statuses]
if (length(bad_packet_status)) {
  add_error("Packets with invalid status: ",
            paste(bad_packet_status, collapse = ", "))
}

packet_sequence <- vapply(register$packets, function(packet) {
  if (is.null(packet$sequence)) NA_real_ else as.numeric(packet$sequence)
}, numeric(1))
if (anyNA(packet_sequence) || anyDuplicated(packet_sequence)) {
  add_error("Every packet must have one unique numeric sequence value.")
}
for (packet_id in packet_ids) {
  packet <- register$packets[[packet_id]]
  check(is_scalar_text(packet$phase),
        "Packet lacks an exact phase: ", packet_id)
  check(is_scalar_text(packet$kind),
        "Packet lacks a kind: ", packet_id)
  contract_id <- packet$contract
  check(is_scalar_text(contract_id) && contract_id %in% contract_ids,
        "Packet lacks a known contract: ", packet_id)
  if (is_scalar_text(contract_id) && contract_id %in% contract_ids) {
    contract <- register$packet_contracts[[contract_id]]
    check(identical(packet$kind, contract_id),
          "Packet kind and contract disagree: ", packet_id)
    contract_evidence <- or_empty(contract$required_evidence)
    contract_tests <- or_empty(contract$required_exit_tests)
    minimum_outputs <- suppressWarnings(as.numeric(contract$minimum_outputs))
    check(length(contract_evidence) > 0L,
          "Packet contract lacks required evidence: ", contract_id)
    check(length(contract_tests) > 0L,
          "Packet contract lacks exit tests: ", contract_id)
    check(length(minimum_outputs) == 1L && !is.na(minimum_outputs) &&
            minimum_outputs >= 1,
          "Packet contract lacks a valid minimum_outputs: ", contract_id)
    missing_contract_evidence <- setdiff(
      contract_evidence, or_empty(packet$required_evidence)
    )
    if (length(missing_contract_evidence)) {
      add_error("Packet omits contract evidence for ", packet_id, ": ",
                paste(missing_contract_evidence, collapse = ", "))
    }
    missing_contract_tests <- setdiff(contract_tests, or_empty(packet$exit_tests))
    if (length(missing_contract_tests)) {
      add_error("Packet omits contract exit tests for ", packet_id, ": ",
                paste(missing_contract_tests, collapse = ", "))
    }
    if (length(minimum_outputs) == 1L && !is.na(minimum_outputs)) {
      check(length(or_empty(packet$outputs)) >= minimum_outputs,
            "Packet has fewer outputs than its contract requires: ", packet_id)
    }
    check(length(or_empty(packet$exit_tests)) > length(contract_tests),
          "Packet lacks a packet-specific exit test beyond its reusable contract: ",
          packet_id)
  }
  check(is_scalar_text(packet$scope),
        "Packet lacks bounded scope: ", packet_id)
  check(length(or_empty(packet$outputs)) > 0L,
        "Packet lacks outputs: ", packet_id)
  check(length(or_empty(packet$exit_tests)) > 0L,
        "Packet lacks exit tests: ", packet_id)
  check(!is.null(packet$completion_evidence),
        "Packet lacks completion_evidence: ", packet_id)
  check("change_reference" %in% names(packet),
        "Packet lacks change_reference field: ", packet_id)
  if (packet$status %in% c("accepted", "deferred_v2_with_reason")) {
    check(length(or_empty(packet$completion_evidence)) > 0L,
          "Terminal packet lacks completion evidence: ", packet_id)
    check(is_scalar_text(packet$change_reference),
          "Terminal packet lacks change_reference: ", packet_id)
  }
  requirements <- or_empty(register$packets[[packet_id]]$requires)
  unknown_requirements <- setdiff(requirements, packet_ids)
  if (length(unknown_requirements)) {
    add_error("Unknown prerequisites for ", packet_id, ": ",
              paste(unknown_requirements, collapse = ", "))
  }
  known_requirements <- intersect(requirements, packet_ids)
  if (length(known_requirements)) {
    nonprior <- known_requirements[
      packet_sequence[known_requirements] >= packet_sequence[[packet_id]]
    ]
    if (length(nonprior)) {
      add_error("Packet prerequisites must have earlier sequence values for ",
                packet_id, ": ", paste(nonprior, collapse = ", "))
    }
  }
}

alias_ids <- named_entries(register$packet_aliases)
for (alias_id in alias_ids) {
  target <- register$packet_aliases[[alias_id]]
  check(!alias_id %in% packet_ids,
        "Deprecated packet alias remains canonical: ", alias_id)
  check(is_scalar_text(target) && target %in% packet_ids,
        "Packet alias has an unknown canonical target: ", alias_id)
}

expected_aliases <- c(
  "P1C-CONFIG" = "P1C-INVENTORY",
  "P7-READER" = "P7-PILOT",
  "P7-MATRIX" = "P7-CLEAN-BUILD",
  "P8-SNAPSHOT" = "P8-SMOKE"
)
for (alias_id in names(expected_aliases)) {
  check(alias_id %in% alias_ids &&
          identical(register$packet_aliases[[alias_id]],
                    unname(expected_aliases[[alias_id]])),
        "Missing or incorrect stable packet alias: ", alias_id)
}

expansion_ids <- named_entries(register$packet_expansions)
for (expansion_id in expansion_ids) {
  targets <- or_empty(register$packet_expansions[[expansion_id]])
  check(length(targets) > 0L,
        "Packet expansion has no exact targets: ", expansion_id)
  unknown_targets <- setdiff(targets, packet_ids)
  if (length(unknown_targets)) {
    add_error("Packet expansion has unknown targets for ", expansion_id, ": ",
              paste(unknown_targets, collapse = ", "))
  }
}

check(setequal(or_empty(register$packet_expansions$`G-A6`),
               c("G-A6-PUSH", "G-A6-TAG", "G-A6-ARCHIVE", "G-A6-DEPLOY")),
      "G-A6 must expand to the four exact external-action gates.")

packet_requires <- function(packet_id) {
  or_empty(register$packets[[packet_id]]$requires)
}
required_wave_edges <- c(
  "WA-C00" = "P3-VERIFY-A",
  "WB-C04" = "P3-VERIFY-B",
  "WC-C12" = "P3-VERIFY-C",
  "WD-C13" = "P3-VERIFY-D",
  "WD-C17" = "P3-VERIFY"
)
for (target in names(required_wave_edges)) {
  if (target %in% packet_ids) {
    check(required_wave_edges[[target]] %in% packet_requires(target),
          "Missing just-in-time evidence edge: ", target, " <- ",
          required_wave_edges[[target]])
  }
}
for (target in c("WA-C00", "WB-C04", "WC-C12", "WD-C13")) {
  if (target %in% packet_ids) {
    check(!"P3-VERIFY" %in% packet_requires(target),
          "Early wave is incorrectly blocked by omnibus P3-VERIFY: ", target)
  }
}
if ("P3-VERIFY" %in% packet_ids) {
  check(setequal(packet_requires("P3-VERIFY"),
                 c(paste0("P3-VERIFY-", LETTERS[1:4]), "P3-TEXT")),
        "P3-VERIFY must aggregate only P3-VERIFY-A through D and P3-TEXT.")
}

in_progress <- packet_ids[packet_status == "in_progress"]
check(length(in_progress) <= register$control$write_wip_limit,
      "More than one packet is in_progress.")

active <- register$execution$active_write_packet
active_id <- if (is.null(active)) NULL else active$id
if (is.null(active_id)) {
  check(length(in_progress) == 0L,
        "An in_progress packet exists without an active write lock.")
} else {
  check(is_scalar_text(active_id), "Active packet ID must be non-empty text.")
  check(active_id %in% packet_ids, "Active packet is unknown: ", active_id)
  if (active_id %in% packet_ids) {
    check(identical(packet_status[[active_id]], "in_progress"),
          "Active packet must have status in_progress: ", active_id)
  }
  check(identical(in_progress, active_id),
        "The active write lock and in_progress packet do not agree.")
  check(length(or_empty(active$owned_paths)) > 0L,
        "Active packet must declare owned_paths.")
}

next_id <- register$execution$next_permitted_packet
if (is.null(active_id)) {
  check(is_scalar_text(next_id),
        "An idle workflow must name next_permitted_packet.")
  if (is_scalar_text(next_id)) {
    check(next_id %in% packet_ids,
          "next_permitted_packet is unknown: ", next_id)
    if (next_id %in% packet_ids) {
      check(!packet_status[[next_id]] %in% c("accepted", "deferred_v2_with_reason"),
            "next_permitted_packet is already terminal: ", next_id)
      requirements <- or_empty(register$packets[[next_id]]$requires)
      unknown_requirements <- setdiff(requirements, packet_ids)
      if (length(unknown_requirements)) {
        add_error("Unknown prerequisites for ", next_id, ": ",
                  paste(unknown_requirements, collapse = ", "))
      }
      unmet <- requirements[requirements %in% packet_ids &
                              packet_status[requirements] != "accepted"]
      if (length(unmet)) {
        add_error("next_permitted_packet has unmet prerequisites: ",
                  paste(unmet, collapse = ", "))
      }
    }
  }
} else {
  check(is.null(next_id),
        "next_permitted_packet must be null while a write packet is active.")
}

expected_parents <- sprintf("R%02d", 1:36)
parent_ids <- named_entries(register$parents)
missing_parents <- setdiff(expected_parents, parent_ids)
extra_parents <- setdiff(parent_ids, expected_parents)
if (length(missing_parents)) {
  add_error("Missing review parents: ", paste(missing_parents, collapse = ", "))
}
if (length(extra_parents)) {
  add_error("Unexpected review parents: ", paste(extra_parents, collapse = ", "))
}

item_ids <- named_entries(register$items)
for (parent_id in intersect(expected_parents, parent_ids)) {
  parent <- register$parents[[parent_id]]
  check(identical(parent$closure_rule, "all_required_children_accepted"),
        parent_id, " must use all_required_children_accepted.")
  check(isTRUE(parent$children_inventory_complete),
        parent_id, " has an incomplete child inventory.")
  tracked <- or_empty(parent$tracked_children)
  children <- or_empty(parent$required_children)
  check(length(tracked) > 0L,
        parent_id, " has no tracked children.")
  unknown_tracked <- setdiff(tracked, item_ids)
  if (length(unknown_tracked)) {
    add_error(parent_id, " names unknown tracked children: ",
              paste(unknown_tracked, collapse = ", "))
  }
  unknown_children <- setdiff(children, item_ids)
  if (length(unknown_children)) {
    add_error(parent_id, " names unknown child items: ",
              paste(unknown_children, collapse = ", "))
  }
  expected_tracked <- item_ids[vapply(register$items, function(item) {
    parent_id %in% or_empty(item$parents)
  }, logical(1))]
  if (!setequal(tracked, expected_tracked)) {
    add_error(parent_id, " tracked_children disagree with item parent links.")
  }
  expected_required <- expected_tracked[vapply(
    register$items[expected_tracked],
    function(item) !identical(item$disposition, "deferred_v2_with_reason"),
    logical(1)
  )]
  if (!setequal(children, expected_required)) {
    add_error(parent_id,
              " required_children must contain every non-deferred tracked child.")
  }
  if (identical(parent$status, "accepted")) {
    check(length(children) > 0L,
          parent_id, " is accepted without required children.")
    if (length(children) && all(children %in% item_ids)) {
      child_statuses <- vapply(register$items[children], function(item) {
        as.character(item$status)
      }, character(1))
      check(all(child_statuses == "accepted"),
            parent_id, " is accepted before all required children.")
    }
  }
}

expected_sections <- sprintf("S%02d", 1:18)

for (item_id in item_ids) {
  item <- register$items[[item_id]]
  status <- as.character(item$status)
  check(status %in% allowed_work_statuses,
        "Invalid item status for ", item_id, ": ", status)
  disposition <- as.character(item$disposition)
  check(disposition %in% allowed_dispositions,
        "Invalid item disposition for ", item_id, ": ", disposition)
  if (disposition %in% c("rejected_with_reason", "deferred_v2_with_reason")) {
    check(is_scalar_text(item$disposition_reason),
          "Reason-required disposition lacks a reason: ", item_id)
  }
  if (identical(disposition, "deferred_v2_with_reason")) {
    check(identical(status, "deferred_v2_with_reason"),
          "Deferred item must use deferred_v2_with_reason status: ", item_id)
  }
  if (identical(disposition, "already_satisfied")) {
    check(identical(status, "accepted"),
          "Already-satisfied disposition must use accepted status: ", item_id)
  }
  if (identical(disposition, "rejected_with_reason")) {
    check(status %in% c("ratified", "accepted"),
          "Rejected-scope item must be ratified or accepted: ", item_id)
  }
  linked_parents <- or_empty(item$parents)
  check(length(linked_parents) > 0L,
        "Item has no parent: ", item_id)
  unknown_parents <- setdiff(linked_parents, parent_ids)
  if (length(unknown_parents)) {
    add_error("Item ", item_id, " names unknown parents: ",
              paste(unknown_parents, collapse = ", "))
  }
  packet <- item$packet
  check(is_scalar_text(packet) && packet %in% packet_ids,
        "Item has an unknown packet: ", item_id)
  check(is.list(item$source), "Item source must be a mapping: ", item_id)
  check(is_scalar_text(item$source$review_section),
        "Item lacks review section anchor: ", item_id)
  check(is_scalar_text(item$source$fingerprint),
        "Item lacks source fingerprint: ", item_id)
  check(is_scalar_text(item$source$fingerprint_id),
        "Item lacks stable fingerprint_id: ", item_id)
  source_sections <- or_empty(item$source$sections)
  check(length(source_sections) > 0L,
        "Item lacks exact source section IDs: ", item_id)
  check(!anyDuplicated(source_sections),
        "Item repeats an exact source section ID: ", item_id)
  unknown_source_sections <- setdiff(source_sections, expected_sections)
  if (length(unknown_source_sections)) {
    add_error("Item ", item_id, " has unknown source section IDs: ",
              paste(unknown_source_sections, collapse = ", "))
  }
  check(is_scalar_text(item$source$location),
        "Item lacks exact source location: ", item_id)
  check(is_scalar_text(item$description),
        "Item lacks an atomic description: ", item_id)
  check(is_scalar_text(item$owner), "Item lacks owner: ", item_id)
  check(is_scalar_text(item$approval_owner),
        "Item lacks approval owner: ", item_id)
  check(length(or_empty(item$scope)) > 0L,
        "Item lacks affected scope: ", item_id)
  check(!is.null(item$prerequisites),
        "Item lacks prerequisites field: ", item_id)
  check(length(or_empty(item$evidence_requirements)) > 0L,
        "Item lacks evidence requirements: ", item_id)
  check(length(or_empty(item$acceptance_tests)) > 0L,
        "Item lacks acceptance tests: ", item_id)
  check(!is.null(item$completion_evidence),
        "Item lacks completion_evidence: ", item_id)
  check("change_reference" %in% names(item),
        "Item lacks change_reference field: ", item_id)
  if (status %in% c("accepted", "deferred_v2_with_reason")) {
    check(length(or_empty(item$completion_evidence)) > 0L,
          "Terminal item lacks completion evidence: ", item_id)
    check(is_scalar_text(item$change_reference),
          "Terminal item lacks change_reference: ", item_id)
  }
  check(is.list(item$blocker) && is.logical(item$blocker$active) &&
          length(item$blocker$active) == 1L,
        "Item lacks explicit blocker state: ", item_id)

  prerequisites <- or_empty(item$prerequisites)
  unknown_prerequisites <- setdiff(prerequisites, c(packet_ids, item_ids))
  if (length(unknown_prerequisites)) {
    add_error("Item ", item_id, " has unknown prerequisites: ",
              paste(unknown_prerequisites, collapse = ", "))
  }
  if (identical(status, "in_progress")) {
    check(!is.null(active_id) && identical(packet, active_id),
          "In-progress item belongs to a non-active packet: ", item_id)
  }
}

fingerprint_ids <- vapply(register$items, function(item) {
  as.character(item$source$fingerprint_id)
}, character(1))
if (anyDuplicated(fingerprint_ids)) {
  add_error("Item fingerprint_id values must be unique and stable.")
}

generic_descriptions <- c(
  "Address the review finding.", "Implement the recommendation.",
  "Complete this parent item."
)
generic_items <- item_ids[vapply(register$items, function(item) {
  item$description %in% generic_descriptions
}, logical(1))]
if (length(generic_items)) {
  add_error("Generic placeholder item descriptions are forbidden: ",
            paste(generic_items, collapse = ", "))
}

inventory <- register$atomic_inventory
check(inventory$status %in% c("incomplete", "complete"),
      "atomic_inventory.status must be incomplete or complete.")
if (identical(inventory$status, "complete")) {
  check(as.numeric(inventory$unmapped_actionable_findings) == 0,
        "A complete atomic inventory must report zero unmapped findings.")
  check(as.numeric(inventory$mapped_children) == length(item_ids),
        "mapped_children must equal the number of item records.")
  check(as.numeric(inventory$total_actionable_findings) == length(item_ids),
        "total_actionable_findings must equal the number of item records.")
  check(length(item_ids) > 0L,
        "A complete atomic inventory cannot be empty.")
  incomplete_parents <- parent_ids[!vapply(register$parents, function(parent) {
    isTRUE(parent$children_inventory_complete)
  }, logical(1))]
  if (length(incomplete_parents)) {
    add_error("Complete inventory has incomplete parents: ",
              paste(incomplete_parents, collapse = ", "))
  }
}

coverage_ids <- named_entries(register$source_coverage)
missing_sections <- setdiff(expected_sections, coverage_ids)
extra_sections <- setdiff(coverage_ids, expected_sections)
if (length(missing_sections)) {
  add_error("Missing source-coverage records: ",
            paste(missing_sections, collapse = ", "))
}
if (length(extra_sections)) {
  add_error("Unexpected source-coverage records: ",
            paste(extra_sections, collapse = ", "))
}
expected_section_headings <- setNames(c(
  "§1 How to read this report",
  "§2 Source and edition verification",
  "§3 Executive overview",
  "§4 Technical state of the book",
  "§5 Complete content and progress map",
  "§6 Structural architecture and dependency graph",
  "§7 Chapter connection matrix",
  "§8 Chapter-by-chapter content review",
  "§9 Appendices and alternative learning pathways",
  "§10 Writing style, voice, rhythm, and transitions",
  "§11 Figures, graphs, widgets, and accessibility",
  "§12 Data, notation, and internal consistency",
  "§13 Evidence and factual integrity",
  "§14 Panel synthesis: agreement, disagreement, and scores",
  "§15 Ranked master issue list",
  "§16 Recommended revision sequence",
  "§17 Alternative structures",
  "§18 Final synthesis"
), expected_sections)

manifest_union <- character()
for (section_id in intersect(expected_sections, coverage_ids)) {
  coverage <- register$source_coverage[[section_id]]
  check(identical(coverage$status, "complete"),
        "Incomplete source coverage: ", section_id)
  check(is_scalar_text(coverage$section),
        "Source coverage lacks section name: ", section_id)
  check(identical(coverage$section, expected_section_headings[[section_id]]),
        "Source coverage uses the wrong exact heading: ", section_id)
  check(is_scalar_text(coverage$reconciliation),
        "Source coverage lacks reconciliation note: ", section_id)
  check(length(or_empty(coverage$unmapped_actionable)) == 0L,
        "Source coverage retains unmapped findings: ", section_id)
  mapped <- or_empty(coverage$mapped_fingerprint_ids)
  manifest_union <- c(manifest_union, mapped)
  mapped_count <- suppressWarnings(as.numeric(coverage$mapped_count))
  check(length(mapped_count) == 1L && !is.na(mapped_count) &&
          mapped_count == length(mapped),
        "Source coverage mapped_count disagrees with its manifest: ", section_id)
  check(!anyDuplicated(mapped),
        "Source coverage manifest repeats a fingerprint: ", section_id)
  unknown_fingerprints <- setdiff(mapped, fingerprint_ids)
  if (length(unknown_fingerprints)) {
    add_error("Source coverage manifest has unknown fingerprints for ",
              section_id, ": ", paste(unknown_fingerprints, collapse = ", "))
  }
  section_items <- item_ids[vapply(register$items, function(item) {
    section_id %in% or_empty(item$source$sections)
  }, logical(1))]
  expected_fingerprints <- fingerprint_ids[section_items]
  if (!setequal(mapped, expected_fingerprints)) {
    add_error("Source coverage manifest disagrees with item section links: ",
              section_id)
  }
  if (length(mapped) == 0L) {
    check(is_scalar_text(coverage$zero_unique_reason),
          "Zero-item source section lacks a reconciliation reason: ", section_id)
  }
}
check(setequal(manifest_union, fingerprint_ids),
      "The union of source-section manifests must equal the complete fingerprint set.")

handoff_ids <- named_entries(handoff_ledger$handoffs)
check(!anyDuplicated(handoff_ids), "Handoff IDs must be unique.")
handoff_child_count <- suppressWarnings(
  as.numeric(handoff_ledger$inventory_child_count)
)
check(length(handoff_child_count) == 1L && !is.na(handoff_child_count) &&
        handoff_child_count == length(item_ids),
      "Handoff ledger inventory_child_count disagrees with the register.")

incoming <- setNames(vector("list", length(packet_ids)), packet_ids)
for (handoff_id in handoff_ids) {
  handoff <- handoff_ledger$handoffs[[handoff_id]]
  source <- handoff$source_packet
  check(is_scalar_text(source) && source %in% packet_ids,
        "Handoff has unknown source packet: ", handoff_id)
  check(handoff$kind %in% allowed_handoff_kinds,
        "Handoff has invalid kind: ", handoff_id)
  check(isTRUE(handoff$required),
        "Current schema requires an explicit required: true: ", handoff_id)
  flattened <- unlist(handoff, recursive = TRUE, use.names = FALSE)
  if (any(grepl("plugins/cache", flattened, fixed = TRUE))) {
    add_error("Handoff points into installed plugin cache: ", handoff_id)
  }

  deliveries <- handoff$deliveries
  check(length(deliveries) > 0L,
        "Handoff has no deliveries: ", handoff_id)
  delivery_targets <- vapply(deliveries, function(delivery) {
    as.character(delivery$target_packet)
  }, character(1))
  if (anyDuplicated(delivery_targets)) {
    add_error("Handoff repeats a target packet: ", handoff_id)
  }

  for (delivery in deliveries) {
    target <- delivery$target_packet
    gate <- delivery$gate
    state <- delivery$state
    check(is_scalar_text(target) && target %in% packet_ids,
          "Handoff delivery has unknown target: ", handoff_id)
    check(gate %in% allowed_handoff_gates,
          "Handoff delivery has invalid gate: ", handoff_id, " -> ", target)
    check(state %in% allowed_delivery_states,
          "Handoff delivery has invalid state: ", handoff_id, " -> ", target)

    if (source %in% packet_ids && target %in% packet_ids &&
        !identical(handoff$kind, "invalidation")) {
      check(packet_sequence[[target]] > packet_sequence[[source]],
            "Non-invalidation handoff targets an earlier packet: ",
            handoff_id, " -> ", target)
    }

    if (target %in% packet_ids) {
      incoming[[target]] <- c(incoming[[target]], list(list(
        id = handoff_id,
        gate = gate,
        state = state
      )))
    }

    if (identical(state, "consumed")) {
      check(is_scalar_text(delivery$disposition),
            "Consumed delivery lacks disposition: ", handoff_id, " -> ", target)
      check(length(or_empty(delivery$evidence)) > 0L,
            "Consumed delivery lacks evidence: ", handoff_id, " -> ", target)
    }
    if (identical(state, "waived")) {
      check(is_scalar_text(delivery$waiver_reason),
            "Waived delivery lacks reason: ", handoff_id, " -> ", target)
      check(is_scalar_text(delivery$author_approval),
            "Waived delivery lacks author approval: ", handoff_id, " -> ", target)
    }
    if (identical(state, "superseded")) {
      replacement <- delivery$replacement_handoff
      check(is_scalar_text(replacement) && replacement %in% handoff_ids,
            "Superseded delivery lacks valid replacement: ",
            handoff_id, " -> ", target)
    }
  }
}

packet_reviews <- handoff_ledger$packet_reviews
accepted_packets <- packet_ids[packet_status == "accepted"]
for (packet_id in accepted_packets) {
  review <- packet_reviews[[packet_id]]
  check(!is.null(review),
        "Accepted packet lacks handoff review: ", packet_id)
  if (!is.null(review)) {
    check(identical(review$declaration, "all_future_effects_recorded"),
          "Invalid handoff review declaration for ", packet_id)
    outgoing <- or_empty(review$outgoing)
    unknown_outgoing <- setdiff(outgoing, handoff_ids)
    if (length(unknown_outgoing)) {
      add_error("Packet review names unknown handoffs for ", packet_id, ": ",
                paste(unknown_outgoing, collapse = ", "))
    }
    wrong_source <- outgoing[outgoing %in% handoff_ids &
                               vapply(handoff_ledger$handoffs[outgoing],
                                      function(h) h$source_packet != packet_id,
                                      logical(1))]
    if (length(wrong_source)) {
      add_error("Packet review claims handoffs from another source for ",
                packet_id, ": ", paste(wrong_source, collapse = ", "))
    }
    source_handoffs <- handoff_ids[vapply(handoff_ledger$handoffs,
                                          function(h) h$source_packet == packet_id,
                                          logical(1))]
    missing_outgoing <- setdiff(source_handoffs, outgoing)
    if (length(missing_outgoing)) {
      add_error("Accepted packet review omits outgoing handoffs for ",
                packet_id, ": ", paste(missing_outgoing, collapse = ", "))
    }
  }

  packet_incoming <- incoming[[packet_id]]
  if (length(packet_incoming)) {
    nonterminal <- vapply(packet_incoming, function(delivery) {
      !delivery$state %in% terminal_delivery_states
    }, logical(1))
    if (any(nonterminal)) {
      labels <- vapply(packet_incoming[nonterminal], function(delivery) {
        paste0(delivery$id, "(", delivery$state, ")")
      }, character(1))
      add_error("Accepted packet has nonterminal incoming handoffs: ",
                packet_id, " <- ", paste(labels, collapse = ", "))
    }
  }
}

if (!is.null(active_id) && active_id %in% packet_ids) {
  active_incoming <- incoming[[active_id]]
  if (length(active_incoming)) {
    unresolved_start <- vapply(active_incoming, function(delivery) {
      delivery$gate == "before_start" &&
        !delivery$state %in% terminal_delivery_states
    }, logical(1))
    pending_close <- vapply(active_incoming, function(delivery) {
      delivery$gate == "before_close" && delivery$state == "pending"
    }, logical(1))
    if (any(unresolved_start)) {
      add_error("Active packet has unresolved before_start handoffs: ", active_id)
    }
    if (any(pending_close)) {
      add_error("Active packet has unacknowledged before_close handoffs: ", active_id)
    }
  }
}

dashboard_value <- function(field) {
  match_line <- grep(paste0("^", field, ":"), dashboard_lines, value = TRUE)
  if (length(match_line) != 1L) return(NULL)
  value <- trimws(sub(paste0("^", field, ":"), "", match_line))
  if (value %in% c("", "null", "~")) NULL else gsub('^"|"$', "", value)
}

dashboard_branch <- dashboard_value("branch")
dashboard_active <- dashboard_value("active_write_packet")
dashboard_next <- dashboard_value("next_permitted_packet")
dashboard_last <- dashboard_value("last_completed_packet")
dashboard_number <- function(field) {
  value <- dashboard_value(field)
  if (is.null(value)) return(NULL)
  suppressWarnings(as.numeric(value))
}
dashboard_atomic <- dashboard_number("atomic_children")
dashboard_packets <- dashboard_number("packet_count")
dashboard_sections <- dashboard_number("source_coverage_sections")
dashboard_unmapped <- dashboard_number("unmapped_actionable")
dashboard_handoffs <- dashboard_number("forward_handoffs")

check(identical(dashboard_branch, register$control$branch),
      "Dashboard branch disagrees with register.")
check(identical(dashboard_active, active_id),
      "Dashboard active_write_packet disagrees with register.")
check(identical(dashboard_next, next_id),
      "Dashboard next_permitted_packet disagrees with register.")
check(identical(dashboard_last, register$execution$last_completed_packet),
      "Dashboard last_completed_packet disagrees with register.")
check(length(dashboard_atomic) == 1L && !is.na(dashboard_atomic) &&
        dashboard_atomic == length(item_ids),
      "Dashboard atomic_children disagrees with register.")
check(length(dashboard_packets) == 1L && !is.na(dashboard_packets) &&
        dashboard_packets == length(packet_ids),
      "Dashboard packet_count disagrees with register.")
check(length(dashboard_sections) == 1L && !is.na(dashboard_sections) &&
        dashboard_sections == length(coverage_ids),
      "Dashboard source_coverage_sections disagrees with register.")
check(length(dashboard_unmapped) == 1L && !is.na(dashboard_unmapped) &&
        dashboard_unmapped == as.numeric(inventory$unmapped_actionable_findings),
      "Dashboard unmapped_actionable disagrees with register.")
check(length(dashboard_handoffs) == 1L && !is.na(dashboard_handoffs) &&
        dashboard_handoffs == length(handoff_ids),
      "Dashboard forward_handoffs disagrees with handoff ledger.")

git_branch <- tryCatch(
  system2("git", c("rev-parse", "--abbrev-ref", "HEAD"), stdout = TRUE),
  error = function(error) character()
)
if (length(git_branch) == 1L) {
  check(identical(git_branch, register$control$branch),
        "Checked-out Git branch disagrees with register: ", git_branch)
}

prompt_packet <- if (is.null(active_id)) next_id else active_id
if (is_scalar_text(prompt_packet)) {
  check(any(grepl(prompt_packet, dashboard_lines, fixed = TRUE)),
        "Dashboard does not name the packet in its continuation prompt: ",
        prompt_packet)
}

if (length(errors)) {
  cat("Comprehensive-review workflow: FAILED\n")
  for (error in errors) cat("- ", error, "\n", sep = "")
  quit(status = 1L)
}

inventory_label <- if (identical(inventory$status, "complete")) {
  paste0(length(item_ids), " children; zero unmapped")
} else {
  "incomplete (P0-REGISTER remains required)"
}
current_label <- if (is.null(active_id)) "none" else active_id
next_label <- if (is.null(next_id)) "none while a packet is active" else next_id

cat("Comprehensive-review workflow: OK\n")
cat("- branch: ", register$control$branch, "\n", sep = "")
cat("- active packet: ", current_label, "\n", sep = "")
cat("- next permitted packet: ", next_label, "\n", sep = "")
cat("- review parents: ", length(parent_ids), "\n", sep = "")
cat("- atomic inventory: ", inventory_label, "\n", sep = "")
cat("- exact packets: ", length(packet_ids), "\n", sep = "")
cat("- source manifests: ", length(coverage_ids), "\n", sep = "")
cat("- forward handoffs: ", length(handoff_ids), "\n", sep = "")
