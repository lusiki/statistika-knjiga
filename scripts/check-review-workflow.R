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
  "P1C-INTEGRITY",
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
  check(is_scalar_text(packet$scope),
        "Packet lacks bounded scope: ", packet_id)
  check(length(or_empty(packet$outputs)) > 0L,
        "Packet lacks outputs: ", packet_id)
  check(length(or_empty(packet$exit_tests)) > 0L,
        "Packet lacks exit tests: ", packet_id)
  check(!is.null(packet$completion_evidence),
        "Packet lacks completion_evidence: ", packet_id)
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
  if (disposition %in% c("rejected_with_reason", "already_satisfied")) {
    check(identical(status, "accepted"),
          "Resolved disposition must use accepted status: ", item_id)
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

expected_sections <- sprintf("S%02d", 1:18)
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
for (section_id in intersect(expected_sections, coverage_ids)) {
  coverage <- register$source_coverage[[section_id]]
  check(identical(coverage$status, "complete"),
        "Incomplete source coverage: ", section_id)
  check(is_scalar_text(coverage$section),
        "Source coverage lacks section name: ", section_id)
  check(is_scalar_text(coverage$reconciliation),
        "Source coverage lacks reconciliation note: ", section_id)
  check(length(or_empty(coverage$unmapped_actionable)) == 0L,
        "Source coverage retains unmapped findings: ", section_id)
}

handoff_ids <- named_entries(handoff_ledger$handoffs)
check(!anyDuplicated(handoff_ids), "Handoff IDs must be unique.")

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

check(identical(dashboard_branch, register$control$branch),
      "Dashboard branch disagrees with register.")
check(identical(dashboard_active, active_id),
      "Dashboard active_write_packet disagrees with register.")
check(identical(dashboard_next, next_id),
      "Dashboard next_permitted_packet disagrees with register.")
check(identical(dashboard_last, register$execution$last_completed_packet),
      "Dashboard last_completed_packet disagrees with register.")

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
cat("- forward handoffs: ", length(handoff_ids), "\n", sep = "")
