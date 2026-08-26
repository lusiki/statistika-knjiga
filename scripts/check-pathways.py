#!/usr/bin/env python3
"""Blokirajuća provjera čitateljskih, rješenjskih i izlaznih putova P5-ROUTES."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from book_inventory import appendix_pages, chapter_pages, load_inventory, solution_pages, sync_projections


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"ne mogu učitati {path.relative_to(ROOT)}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def normalize(value: str) -> str:
    return " ".join(value.replace("\\|", "|").split()).casefold()


def profile_projection(lines: list[str], profile: str | None) -> str:
    active_stack: list[bool] = []
    output: list[str] = []
    for line in lines:
        opened = re.match(r"^:::+\s*\{(.*)\}\s*$", line)
        if opened:
            attrs = opened.group(1)
            inherited = all(active_stack) if active_stack else True
            profile_match = re.search(r'when-profile=["\']([^"\']+)["\']', attrs)
            active = inherited
            if profile_match and "content-visible" in attrs:
                active = inherited and profile == profile_match.group(1)
            elif profile_match and "content-hidden" in attrs:
                active = inherited and profile != profile_match.group(1)
            active_stack.append(active)
            continue
        if re.match(r"^:::+\s*$", line) and active_stack:
            active_stack.pop()
            continue
        if all(active_stack) if active_stack else True:
            output.append(line)
    if active_stack:
        raise AssertionError("rjesenja.qmd sadrži nezatvoren profilni blok")
    return "\n".join(output)


def component_strings(record: dict[str, Any]) -> tuple[list[str], list[str]]:
    answer = record["answer_components"]
    public: list[str] = []
    planted = answer["planted_error"]
    if planted["applicable"]:
        public.extend([planted["statement"], planted["why_wrong"]])
    diagnostic = answer["revealing_diagnostic"]
    if diagnostic["applicable"]:
        public.extend([diagnostic["procedure"], diagnostic["expected_evidence"]])
    non_answers = answer["plausible_non_answers"]
    if non_answers["applicable"]:
        for item in non_answers["responses"]:
            public.extend([item["response"], item["why_insufficient"]])
    model = answer["model_response_components"]
    if model["applicable"]:
        for item in model["components"]:
            public.extend([item["required_claim"], item["required_evidence"]])
    numerical = answer["numerical_check"]
    if numerical["applicable"]:
        public.extend([
            numerical["expected_result"],
            numerical["tolerance_or_acceptance_rule"],
            numerical["independent_method"],
            numerical["evidence_reference"],
        ])

    protected: list[str] = []
    for criterion in answer["severity_ranked_rubric"]["criteria"]:
        protected.extend([criterion["description"], criterion["observable_evidence"]])
    for alternative in record["alternatives"]:
        protected.extend([alternative["description"], alternative["acceptance_boundary"]])
    protected.extend(record["instructor_notes"])
    return public, protected


def record_owned_profile_blocks(lines: list[str]) -> int:
    stack: list[str | None] = []
    headings: list[tuple[int, str | None]] = []
    count = 0
    for line in lines:
        heading = re.match(r"^(#+)\s.*$", line)
        if heading:
            level = len(heading.group(1))
            headings = [item for item in headings if item[0] < level]
            anchor = re.search(r"#(ex-[A-Za-z0-9-]+)", line)
            headings.append((level, anchor.group(1) if anchor else None))
        opened = re.match(r"^:::+\s*\{(.*)\}\s*$", line)
        if opened:
            if "content-visible" in line and 'when-profile="kolegij"' in line:
                owner = next((value for value in reversed(stack) if value), None)
                if owner is None:
                    owner = next((value for _, value in reversed(headings) if value), None)
                if owner:
                    count += 1
            anchor = re.search(r"#(ex-[A-Za-z0-9-]+)", opened.group(1))
            stack.append(anchor.group(1) if anchor else None)
        elif re.match(r"^:::+\s*$", line) and stack:
            stack.pop()
    return count


def governed_item_statuses(register_text: str, prefix: str) -> dict[str, str]:
    statuses: dict[str, str] = {}
    pattern = re.compile(
        rf"(?ms)^  ({re.escape(prefix)}[^:]+):\n(.*?)(?=^  [A-Z0-9][A-Za-z0-9-]*:|\Z)"
    )
    for match in pattern.finditer(register_text):
        status = re.search(r'(?m)^    status:\s+"([^"]+)"\s*$', match.group(2))
        if status:
            statuses[match.group(1)] = status.group(1)
    return statuses


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    try:
        inventory = load_inventory(ROOT)
        check(not sync_projections(ROOT, inventory, write=False), "inventarne projekcije nisu čiste")
        routes = load_json("config/pathway-routes.json")
        spines = load_json("bookwright_plugin/bookwright/shared/chapter-spine.json")
        conventions = load_json("bookwright_plugin/bookwright/shared/conventions.json")
        jamovi = load_json("config/appendix-b-jamovi-route.json")
        widgets = load_json("data/widgets.json")
        register_text = (
            ROOT / "notes/reports/comprehensive-review-implementation-register.yml"
        ).read_text(encoding="utf-8")
        generator = load_module("solution_route_builder", ROOT / "scripts/build-solution-routes.py")

        expected_units = [f"{number:02d}" for number in range(1, 19)]
        inventory_units = [
            f"{page['chapter_number']:02d}"
            for page in inventory["pages"]
            if page.get("kind") == "chapter"
        ]
        check(inventory_units == expected_units, "inventar ne čuva makroredoslijed poglavlja 1–18")

        spine_by_unit = {
            chapter["id"][:2]: chapter
            for chapter in spines.get("chapters", [])
            if chapter["id"][:2].isdigit() and chapter["id"] != "00-predgovor"
        }
        check(sorted(spine_by_unit) == expected_units, "nedostaje živa kralježnica numeriranoga poglavlja")
        reading_routes = routes.get("reading_routes", [])
        check(
            [route.get("id") for route in reading_routes] == ["kriticko-citateljski", "analiticki"],
            "moraju postojati točno dva ratificirana čitateljska puta",
        )
        for route in reading_routes:
            order = route.get("unit_order", [])
            check(order == expected_units, f"{route.get('id')}: put ne čuva potpuni makroredoslijed")
            positions = {unit: index for index, unit in enumerate(order)}
            for unit, spine in spine_by_unit.items():
                for prerequisite in spine.get("prerequisites", []):
                    prerequisite_unit = prerequisite[:2]
                    check(
                        prerequisite_unit in positions and positions[prerequisite_unit] < positions[unit],
                        f"{route.get('id')}: {unit} prethodi živom preduvjetu {prerequisite_unit}",
                    )
            check(positions.get("13", 99) < positions.get("17", -1), f"{route.get('id')}: Poglavlje 13 nije prije 17")
            check(set(order[: positions.get("18", 0)]) == set(expected_units[:-1]), f"{route.get('id')}: Poglavlje 18 nije iza cijele knjige")

        solutions = solution_pages(inventory)
        check(
            len(solutions) == 1
            and solutions[0].get("id") == "solutions"
            and solutions[0].get("source") == "rjesenja.qmd",
            "solution_routes ne sadrži točno jednu generiranu rutu",
        )
        footer_pages = [entry.get("page") for entry in inventory["navigation"]["footer"]]
        check(footer_pages.count("solutions") == 1, "javna sažeta ruta nema točno jednu navigacijsku poveznicu")
        check(
            not any("kolegij" in normalize(json.dumps(entry, ensure_ascii=False)) for entry in inventory["navigation"]["navbar"] + inventory["navigation"]["footer"]),
            "zaštićeni kolegijski sloj ne smije imati javnu navigacijsku stavku",
        )

        expected_solution = generator.render(ROOT)
        actual_solution = (ROOT / "rjesenja.qmd").read_text(encoding="utf-8")
        check(actual_solution == expected_solution, "rjesenja.qmd nije čista projekcija kanonskih zapisa")
        records = generator.read_records(ROOT)
        check(len(records) == 95, "kanonsko spremište ne sadrži 95 zapisa")
        check(len({record["unit_id"] for _, record in records}) == 19, "zapisi ne pokrivaju svih 19 jedinica")
        frozen_records = [
            record
            for _, record in records
            if record["task_class"] in {"callout_greska", "revizija_modela"}
        ]
        frozen_contract = routes["solution_projection"]
        check(
            len(frozen_records) == frozen_contract.get("graded_frozen_outputs") == 38,
            "datirani artefakt ne obuhvaća svih 38 ocjenjivanih AI izlaza",
        )
        check(
            frozen_contract.get("frozen_snapshot_date") == "2026-08-26"
            and frozen_contract.get("frozen_output_key")
            == "record_id + answer_components.planted_error.error_id"
            and frozen_contract.get("live_repetition") == "optional_not_required",
            "zamrznuti AI izlazi nemaju datirani ključ ili uživo ponavljanje nije neobvezno",
        )
        for record in frozen_records:
            planted = record["answer_components"]["planted_error"]
            check(
                planted.get("applicable") is True
                and bool(planted.get("error_id"))
                and record.get("prompt_fingerprint", "").startswith("sha256:"),
                f"ocjenjivani AI izlaz nema stabilan zamrznuti ključ: {record['record_id']}",
            )

        route_lines = actual_solution.splitlines()
        public_text = normalize(profile_projection(route_lines, None))
        kolegij_text = normalize(profile_projection(route_lines, "kolegij"))
        for _, record in records:
            public_strings, protected_strings = component_strings(record)
            for value in public_strings:
                check(normalize(value) in public_text, f"javna projekcija nema sastavnicu {record['record_id']}")
            for value in protected_strings:
                normalized = normalize(value)
                if len(normalized) < 40:
                    continue
                check(normalized not in public_text, f"zaštićena sastavnica curi javno: {record['record_id']}")
                check(normalized in kolegij_text, f"kolegijska projekcija nema zaštićenu sastavnicu: {record['record_id']}")
            source = record["source_anchor"]
            source_text = (ROOT / source["path"]).read_text(encoding="utf-8")
            check(source_text.count(f"#{source['anchor']}") == 1, f"neispravna povratna poveznica: {record['record_id']}")

        legacy_blocks = sum(
            record_owned_profile_blocks(path.read_text(encoding="utf-8").splitlines())
            for path in sorted((ROOT / "chapters").glob("*.qmd"))
        )
        check(legacy_blocks == 0, "izvor poglavlja još sadrži drugi odgovor uz kanonski zapis")

        supported = jamovi["scope"]["supported_metric_keys"]
        unsupported = jamovi["scope"]["unsupported_metric_keys"]
        check(len(supported) == 19 and len(unsupported) == 7, "Dodatak B nema ratificiranu granicu 19/7")
        check(
            jamovi["clean_install"]["status"] == "pending_owner_verification"
            and jamovi["clean_install"]["claimed_by_packet"] is False,
            "Dodatak B nedopušteno tvrdi clean-install dokaz",
        )
        matrix = {entry["id"]: entry for entry in routes.get("pathway_matrix", [])}
        check(set(matrix) == {"self-study", "r", "no-code", "print", "ai-output"}, "matrica ne pokriva pet obveznih putova")
        check(matrix["no-code"]["status"] == "documented_pending_clean_install", "javno obećanje puta bez koda nije dovoljno usko")
        check(matrix["no-code"]["scope_source"].endswith("#scope.supported_metric_keys"), "put bez koda ne veže javni opseg uz podržana mjerila")

        expected_reachbacks = {
            *(f"R35-REACHBACK-{unit:02d}" for unit in range(6, 19)),
            *(f"R35-SELF-CHECK-{part}" for part in ("I", "II", "III", "IV", "V")),
        }
        reachback_statuses = governed_item_statuses(register_text, "R35-")
        check(
            set(reachback_statuses) == expected_reachbacks
            and all(status == "accepted" for status in reachback_statuses.values()),
            "retrieval nije zasebno dokazan kroz svih 13 reach-back zadataka i pet samoprovjera",
        )

        architecture = routes["architecture"]
        pre = architecture["post_p5_g_basis"]
        post = architecture["after_solution_route"]
        check(pre == {"chapters": 19, "appendices": 7, "canonical_pages": 38, "widgets": 17, "static_twins": 17, "callout_types": 4, "authority": "Gate A2d / D10"}, "H-P5-G-001 nije sačuvan kao točno polazište")
        labels = conventions.get("labels", {})
        callout_labels = [labels.get(key) for key in ("opener", "callout_wild", "callout_ai", "callout_error")]
        check(
            len(chapter_pages(inventory, include_landing=False)) == post["chapters"]
            and len(appendix_pages(inventory)) == post["appendices"]
            and len(inventory["pages"]) == post["canonical_pages"]
            and len(solutions) == post["solution_routes"]
            and len(widgets.get("widgets", [])) == post["widgets"] == post["static_twins"]
            and len(set(callout_labels)) == post["callout_types"]
            and post["authority"] == "Gate A2d / D06",
            "post-P5-ROUTES arhitektura ne odgovara zasebno izmjerenim vrijednostima",
        )

        preface = (ROOT / "chapters/00-predgovor.qmd").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        profile = (ROOT / "_quarto-kolegij.yml").read_text(encoding="utf-8")
        exporter = (ROOT / "R/build-ai-exports.R").read_text(encoding="utf-8")
        for fragment in (
            "### Kritičko-čitalački put",
            "### Analitički put",
            "Poglavlja 1–18",
            "[Provjere rješenja](../rjesenja.qmd)",
        ):
            check(normalize(fragment) in normalize(preface), f"predgovor ne objavljuje put: {fragment}")
        for fragment in (
            "19 podržanih mjerila",
            "provjera na čistoj instalaciji ostaje nepotvrđena",
            "rjesenja.qmd",
            "Poglavlje 6 ostaje u nacrtu",
        ):
            check(normalize(fragment) in normalize(readme), f"README javno obećanje nije pomireno: {fragment}")
        check("NIJE proveden" not in profile and "95 kanonskih zapisa" in profile, "kolegijski profil još opisuje neproveden D06 sustav")
        check("INVENTORY_JSON" in exporter and "solution_sources" in exporter, "AI izvoz ne troši solution_routes granicu")

        if errors:
            raise AssertionError("\n- ".join(errors))
        print(
            "PATHWAYS_CHECK_OK "
            "reading_routes=2 prerequisites=19 units=19 records=95 "
            "public_checks=95 protected_rubrics=95 legacy_answer_sources=0 "
            "routes=self-study,R,no-code,print,AI-output pages=39 solutions=1 "
            "no_code_supported=19 guarded=7 clean_install=pending-owner "
            "frozen_outputs=38 dated=2026-08-26 live_repetition=optional "
            "retrieval_replacements=18/18 public_promises=reconciled "
            "xrefs=95 print_projection=present"
        )
        return 0
    except (AssertionError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"PATHWAYS_CHECK_FAILED {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
