#!/usr/bin/env python3
"""
Builds the negative fixture set: one broken run per violation code.

Each case starts from the valid fixture and breaks EXACTLY ONE rule, so a
test that expects code X and gets X+Y has caught a bug in the validator's
specificity, not just its sensitivity.

SYNTHETIC. These fixtures were authored against discovery_prompt_v2_5.md's
stated rules, not derived from a real discovery run. Only one ratified
discovery run exists (sailing, 2026-07-09) and it predates several of the
rules checked here. Treat green against these fixtures as evidence the
validator implements the spec -- NOT as evidence the spec matches reality.
"""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALID = ROOT / "fixtures" / "valid" / "sample_run"
INVALID = ROOT / "fixtures" / "invalid"


def fresh(name):
    """Copy the valid run to a new invalid case dir."""
    dest = INVALID / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(VALID, dest)
    return dest


def edit(path, old, new, count=1):
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"ANCHOR MISS in {path.name}: {old!r}")
    if text.count(old) != count:
        raise SystemExit(
            f"ANCHOR AMBIGUOUS in {path.name}: {old!r} "
            f"appears {text.count(old)}x, expected {count}"
        )
    path.write_text(text.replace(old, new), encoding="utf-8")


CASES = {}


def case(code):
    def deco(fn):
        CASES[code] = fn
        return fn
    return deco


@case("TAG_BARE")
def _(d):
    edit(d / "discovery_synth.md",
         "- Front matter and index are out of scope [default]",
         "- Front matter and index are out of scope")


@case("TAG_ILLEGAL")
def _(d):
    edit(d / "discovery_synth.md",
         "- Front matter and index are out of scope [default]",
         "- Front matter and index are out of scope [operator-vibes]")


@case("TAG_MULTIPLE")
def _(d):
    edit(d / "discovery_synth.md",
         "- Front matter and index are out of scope [default]",
         "- Front matter and index are out of scope [default] "
         "[mechanical: x count]")


@case("TAG_MECHANICAL_NO_METHOD")
def _(d):
    edit(d / "discovery_synth.md",
         "- Aliases appear as parenthetical glosses on first use "
         "[mechanical: census of 62 first-use sites]",
         "- Aliases appear as parenthetical glosses on first use [mechanical]")


@case("FORECAST_LEAK")
def _(d):
    p = d / "harvest_brief_synth.md"
    text = p.read_text(encoding="utf-8")
    p.write_text(
        text.replace(
            "- page.line, e.g. 42.17",
            "- page.line, e.g. 42.17\n- tack will fan out [discovery-forecast]",
        ),
        encoding="utf-8",
    )


@case("BRIEF_TOO_LONG")
def _(d):
    p = d / "harvest_brief_synth.md"
    text = p.read_text(encoding="utf-8")
    p.write_text(text + "\n" + "\n".join(f"- filler line {i}" for i in range(12)),
                 encoding="utf-8")


@case("SECTION_MISSING")
def _(d):
    edit(d / "discovery_synth.md", "## Kit nominations", "## Kit nominatons")


@case("STATUS_LINE_MISSING")
def _(d):
    edit(d / "discovery_synth.md",
         "Status: conventions ratified 2026-07-14, discovery_prompt_v2.5.",
         "Ratified on 2026-07-14.")


@case("FAMILY_SIDECAR_MISSING")
def _(d):
    (d / "loc_anchors_synth.csv").unlink()


@case("MODEMAP_BAD_ENUM")
def _(d):
    edit(d / "content_mode_map_synth.csv",
         "ch03,dialogic,teaching dialogue",
         "ch03,conversational,teaching dialogue")


@case("MODEMAP_EMPTY_CELL")
def _(d):
    edit(d / "content_mode_map_synth.csv", "ch01,prose,~", "ch01,prose,")


@case("CHUNKPLAN_BAD_ENUM")
def _(d):
    edit(d / "chunk_plan_synth.csv",
         "c02,chapter,42.1,54.19,940 lines,~",
         "c02,paragraph,42.1,54.19,940 lines,~")


@case("CHUNKPLAN_NO_REASON")
def _(d):
    edit(d / "chunk_plan_synth.csv",
         "c03,fallback_split,55.1,70.12,1400 lines,chapter exceeds ruled "
         "bound; split at section head",
         "c03,fallback_split,55.1,70.12,1400 lines,~")


@case("CHUNKPLAN_COLUMNS")
def _(d):
    edit(d / "chunk_plan_synth.csv",
         "chunk_id,boundary_type,loc_start,loc_end,est_size,notes",
         "chunk_id,boundary_type,loc_start,loc_end,size,notes")


@case("WATCHLIST_TOO_LONG")
def _(d):
    p = d / "discovery_synth.md"
    extra = "\n".join(
        f"- term{i} — reservation [discovery-forecast]" for i in range(21)
    )
    edit(p,
         "- sheet — reservation, rope sense dominates [discovery-forecast]",
         "- sheet — reservation, rope sense dominates [discovery-forecast]\n"
         + extra)


@case("REGISTRATION_FIELDS")
def _(d):
    edit(d / "discovery_synth.md",
         "- synth | book | A Synthetic Source / Anon / 2026 | "
         "loc-grammar: page.line",
         "- synth | book | A Synthetic Source / Anon / 2026")


@case("REGISTRATION_GRAMMAR")
def _(d):
    edit(d / "discovery_synth.md",
         "- synth | book | A Synthetic Source / Anon / 2026 | "
         "loc-grammar: page.line",
         "- synth | book | A Synthetic Source / Anon / 2026 | page.line")


@case("MANIFEST_OMITS_FILE")
def _(d):
    edit(d / "discovery_synth.md",
         "- content_mode_map_synth.csv\n", "")


def build_all():
    INVALID.mkdir(parents=True, exist_ok=True)
    for code, fn in CASES.items():
        d = fresh(code.lower())
        fn(d)
        print(f"  built {code}")
    print(f"\n{len(CASES)} negative fixtures built")
    return 0


if __name__ == "__main__":
    sys.exit(build_all())
