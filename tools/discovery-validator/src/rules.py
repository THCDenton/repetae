"""
Rule definitions for the discovery output validator.

Every constant here traces to an explicit line in discovery_prompt_v2_5.md.
Nothing is invented. If a rule is not written down in the prompt, it does
not appear here.

SCOPE (deliberate): this module validates the ENVELOPE only -- the file
family, master-doc section structure, provenance tags, forecast quarantine,
and the countable bounds. It does NOT validate the config fragment's field
names (master doc section 7). That schema boundary is under revision
(discovery_prompt v2.6 owed) and is explicitly out of scope per the
P-2/P-3/P-4 sequencing flag in discovery_test_record_v1.md.

WHAT THIS CANNOT DO: this checks SHAPE, never TRUTH. A fabricated
[operator-decided] tag on a ruling no operator made is perfectly
well-formed and passes clean. See P-5 in the test record. Do not describe
a green verdict from this tool as provenance integrity.
"""

# --- Provenance tags -------------------------------------------------
# Source: discovery_prompt_v2_5.md "Provenance tags (mandatory on every
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
# Source: discovery_prompt_v2_5.md "Output family" section 1. Nine sections,
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
# Source: discovery_prompt_v2_5.md "Output family" sections 1-6.
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
# Source: discovery_prompt_v2_5.md section 3 -- "Pinned enum in `mode`".

CONTENT_MODES = frozenset({
    "prose",
    "tabular",
    "dialogic",
    "code_listing",
    "mixed",
})

# Source: discovery_prompt_v2_5.md section 6 -- chunk plan boundary_type.
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
MASTER_MAX_CONVENTION_LINES = 45  # "master doc <= ~45 convention lines"
MASTER_MAX_TOTAL_LINES = 300     # "<=300 total before the YAML"

# --- Forecast quarantine ----------------------------------------------
# Source: discovery_prompt_v2_5.md section 2 complementarity rule --
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
# Source: discovery_prompt_v2_5.md section 1 -- the master doc's line 2.
STATUS_PREFIX = "Status: conventions ratified"

# --- Registration line ------------------------------------------------
# Source: "Final line: the registration line for `sources.md`"
# Format: - <slug> | <type> | <title / author / year> | loc-grammar: <grammar>
REGISTRATION_FIELD_COUNT = 4
REGISTRATION_GRAMMAR_PREFIX = "loc-grammar:"
