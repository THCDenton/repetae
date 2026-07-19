"""
Rule definitions for the discovery output validator.

Every constant here traces to an explicit line in discovery_prompt_v2_8.md.
Nothing is invented. If a rule is not written down in the prompt, it does
not appear here.

REBUILD 2026-07-19 (Session C, chunk 1): re-grounded v2.5 -> v2.8. This pass
fixes the two red selftests (TAG_ILLEGAL specificity; TAG_MECHANICAL_NO_METHOD
false pass) and re-cites constants to v2.8. The graded-tag grammar, the
partial-on-universal rule, the container-keyed bound, and the coverage-
partition lint are Session C chunk 2 -- flagged inline as TODO(chunk-2), not
built here.

SCOPE (deliberate): this module validates the ENVELOPE only -- the file
family, master-doc section structure, provenance tags, forecast quarantine,
and the countable bounds. It does NOT validate the config fragment's field
names (master doc section 7). That schema boundary remains out of scope per
the P-2/P-3/P-4 sequencing flag in discovery_test_record_v1.md; v2.8 keeps it
a rule-not-copy boundary.

WHAT THIS CANNOT DO: this checks SHAPE, never TRUTH. A fabricated
[operator-decided] tag on a ruling no operator made is perfectly
well-formed and passes clean. See P-5 in the test record. Do not describe
a green verdict from this tool as provenance integrity.
"""

# --- Provenance tags -------------------------------------------------
# Source: discovery_prompt_v2_8.md "Provenance tags (mandatory on every
# convention line)". Closed world. A bare convention line is a defect by
# the prompt's own definition.

LEGAL_TAGS = frozenset({
    "operator-decided",
    "inferred-confirmed",
    "mechanical",
    "model-knowledge, unverified",
    "discovery-forecast",
    "default",
})

# --- Mechanical STRENGTH GRADES (v2.8, graded-tag lint 2026-07-19) ----
# discovery_prompt_v2_8.md, Provenance tags: a [mechanical: ...] tag must
# end in a strength grade, machine-extractable from the tag. The grade is
# the LAST ';'-delimited clause inside the bracket. Grade added v2.7;
# enforced here in chunk 2.
#
#   exhaustive -- count covers every site the claim ranges over; one
#                 counter-example would falsify it.
#   sampled    -- count covers a stated subset; holds on what was checked.
#   partial    -- count is real but does not settle the claim (proxy, or
#                 the claim ranges wider than the count). A partial grade
#                 on a universal claim is itself a defect -- checked by the
#                 partial-on-universal lint, NOT here.
LEGAL_GRADES = frozenset({"exhaustive", "sampled", "partial"})
MECHANICAL_GRADE_SEPARATOR = ";"

# --- Universal quantifiers (partial-on-universal lint, v2.8) ----------
# discovery_prompt_v2_8.md, Provenance tags: "A partial grade on a
# universal ('always', 'every', 'never') is a defect." The rappers-handbook
# audit generalized this: a claim carrying a universal, backed by a partial
# count, must carry the exception column or be downgraded to "usually/most"
# (evidence/discovery_eval_findings_rappers-handbook.md, generalizable rule).
#
# Scope is deliberately TIGHT and spec-anchored. Bare "fixed" and
# "throughout" are EXCLUDED: they appear in innocent prose (the valid
# fixture's "title case throughout" is exhaustive-graded and true), and a
# loose vocabulary would false-flag. Matched case-insensitively as whole
# words / phrases.
UNIVERSAL_QUANTIFIERS = (
    "always", "every", "never", "invariant", "fixed frame",
)

# --- Tag QUALIFIERS (fix, 2026-07-14, first real run) -----------------
# The prompt names the tags but nowhere forbids a qualifier inside the
# bracket. The Loeliger run wrote BOTH forms and both are compliant:
#
#   [mechanical]                      method stated in the line's prose
#   [mechanical: 21 matches]          method stated inside the bracket
#   [operator-decided, 2026-07-14]    ruling plus its date
#
# envelope-0 required an EXACT string match, so every qualified tag was
# reported TAG_ILLEGAL -- 45 of 49 violations on the first real run were
# this bug. The fixture suite missed it because the fixtures were authored
# from the same misreading as the code.
#
# A tag matches if the text BEFORE the first qualifier separator is a
# legal tag. `model-knowledge, unverified` contains a comma in the tag
# itself, so it is matched whole before separator-splitting is attempted.

TAG_QUALIFIER_SEPARATORS = (":", ",", " + ", " — ", " -- ")

# Downstream only -- figure-worker output. Not emitted by discovery itself,
# but named in the prompt, so accepted rather than flagged.
DOWNSTREAM_TAGS = frozenset({"model-vision"})

ALL_ACCEPTED_TAGS = LEGAL_TAGS | DOWNSTREAM_TAGS

# --- Master doc sections ---------------------------------------------
# Source: discovery_prompt_v2_8.md "Output family" section 1. Nine sections,
# named, in this order.

MASTER_SECTIONS = (
    "Conventions",
    "Ambiguity forecast",
    "Escalations",
    "Registry queue",
    "Effort forecast",
    "Config fragment",
    "Kit nominations",
    "Sidecar manifest",
    "Changelog",
)

# --- File family ------------------------------------------------------
# Source: discovery_prompt_v2_8.md "Output family" sections 1-6.
# <slug> is substituted at check time.

MASTER_DOC = "discovery_{slug}.md"

SIDECARS = (
    "harvest_brief_{slug}.md",
    "content_mode_map_{slug}.csv",
    "loc_anchors_{slug}.csv",
    "arbitration_seed_{slug}.md",
    "chunk_plan_{slug}.csv",
)

# --- Pinned enums -----------------------------------------------------
# Source: discovery_prompt_v2_8.md section 3 -- "Pinned enum in `mode`".

CONTENT_MODES = frozenset({
    "prose",
    "tabular",
    "dialogic",
    "code_listing",
    "mixed",
})

# Source: discovery_prompt_v2_8.md section 6 -- chunk plan boundary_type.
BOUNDARY_TYPES = frozenset({
    "chapter",
    "section",
    "convention",
    "fallback_split",
})

CHUNK_PLAN_COLUMNS = (
    "chunk_id",
    "boundary_type",
    "loc_start",
    "loc_end",
    "est_size",
    "notes",
)

# --- Countable bounds -------------------------------------------------
# Every bound below is stated numerically in the prompt.

WATCHLIST_MAX_ROWS = 20          # "the reviewed watchlist (<=20 rows...)"
ESCALATION_MAX_LINES = 12        # "Escalations  <=12 lines each"
BRIEF_MAX_LINES = 25             # "Hard budget: <=25 lines / ~350 tokens"
EXHIBIT_MAX_LINES = 5            # "exhibits <=5 lines each, per axis"
# Source: discovery_prompt_v2_8.md "Bounds (re-ruled in v2.6)". The bound is
# now CONTAINER-KEYED: born_digital <=50, scan_ocr <=75. v2.5's flat ~45
# "counted nothing in particular" (first real run: 88 vs 62 on one document).
# CHUNK-1 SCOPE: only the born_digital default is wired. The validator does
# not yet read container class off the run.
# TODO(chunk-2): key this to container class per v2.8 bounds section --
#   born_digital <=50 / scan_ocr <=75 -- by reading the class from the run
#   (content_mode_map or master-doc ingest read-back). Until then a scan_ocr
#   run is checked against the too-strict 50 and may false-flag; note it in
#   the real-pile findings, do not silently pass it.
MASTER_MAX_CONVENTION_LINES_BORN_DIGITAL = 50   # "born_digital sources: <=50"
MASTER_MAX_CONVENTION_LINES_SCAN_OCR = 75       # "scan_ocr sources: <=75"
MASTER_MAX_CONVENTION_LINES = MASTER_MAX_CONVENTION_LINES_BORN_DIGITAL  # chunk-1 default
MASTER_MAX_TOTAL_LINES = 300     # "Total master doc <=300 lines before the YAML"

# --- Forecast quarantine ----------------------------------------------
# Source: discovery_prompt_v2_8.md section 2 complementarity rule --
# "NO forecasts and NO arbitration content" in the brief; and section 5 --
# "NEVER injected into the brief or any worker packet".
#
# [discovery-forecast] content is legal in exactly two files. Anywhere
# else is a critical, silent contamination class: a leaked forecast
# reaches a worker that treats a prediction as a fact about the source,
# and nothing downstream detects it by reading.

FORECAST_TAG = "discovery-forecast"

FORECAST_PERMITTED_FILES = (
    MASTER_DOC,
    "arbitration_seed_{slug}.md",
)

# --- Status line ------------------------------------------------------
# Source: discovery_prompt_v2_8.md section 1 -- the master doc's line 2.
STATUS_PREFIX = "Status: conventions ratified"

# --- Registration line ------------------------------------------------
# Source: "Final line: the registration line for `sources.md`"
# Format: - <slug> | <type> | <title / author / year> | loc-grammar: <grammar>
REGISTRATION_FIELD_COUNT = 4
REGISTRATION_GRAMMAR_PREFIX = "loc-grammar:"
