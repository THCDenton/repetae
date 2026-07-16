# Workshop Lexicon — v1

Status: reference document for the workshop (Repetae) project, written
2026-07-10 from project files + project transcripts; re-issued 2026-07-11b
(harvest_map shipped; the single-artifact rule replaced by the engine/reference
split; verified-how dependency discipline; `boundary doctrine` and a now-ratified
`downstream contract` minted); re-issued 2026-07-11c (harvest_residue shipped;
`intake grammar`, `evidence law`, and the residue verdict enum minted; checkpoint
schema v2 RATIFIED); post-close addendum same day (primer v2 shipped; schema
v2.1 boot-manifest slot; `boot manifest` and `post-close addendum` minted);
re-issued 2026-07-12c (amendment session: charter amendment v1.2 — topology
UNDER EXPERIMENT, autonomy, screening, state model, discovery v2.5 direction;
~two dozen terms minted; NOTE: this re-issue was rebuilt from the 07-11b mount
copy + the project-knowledge index's 07-11c content after the mount served a
stale copy at boot — see changelog for the reconstruction record);
re-issued 2026-07-13 (discovery v2.5 shipped — amendment v1.2 item 8 applied;
`ambiguity probe`, `ambiguity watchlist`, `arbitration seed`, and the
`[discovery-forecast]` tag minted; W10 recorded);
re-issued 2026-07-13b (config schema v2 ratified; `wire-0`, `discovery
back-pass`, `closed-world rule` minted; §9 pair 13; rev counter adopted);
re-issued 2026-07-13c (topology experiment kit + scorer shipped — the gate;
`arm`, `fixture tier`/`regression tier`, `export surface`, `provisional-arm
law`, `noise band`, `gate verdict`, `manual chat lane` minted);
re-issued 2026-07-13d (versioning + model-handoff session: **rev-in-filename
law ratified** — this file's name now carries the rev; primer v4 issued;
`rev-in-filename` and `capability probe` minted; `sediment` annotated);
re-issued 2026-07-13g (the migration: kit + scorer + interface doc filed under
suffixed names; W11 retired for those three; P8 fired, P1–P3 struck);
re-issued 2026-07-14 (**the repo migration + the first real discovery run**:
`~/git/repetae` becomes the single source of truth and the mount is retired
[operator-ruled] — W11 retired AT THE ROOT pending P9 ratification, W9 lag #4
dead after five sessions; **discovery ran end-to-end against a real book for the
first time**, closing the standing missing proof point open since 07-11; W12 +
W13 minted; W2 corrected five → six; §9 pair 14 `mount vs repo`);
re-issued 2026-07-15 (**discovery v2.6 + the second real run**: W13 CLOSED — the
convention line is defined and the `[mechanical: <method>]` tag pinned; v2.6
tested by a SEPARATE ctx against a SECOND source (`rappers-handbook`,
born_digital) and all three fixes held; **W12 gains a second evidence point from
the opposite direction — separation revealed what self-authorship concealed**;
W14 minted (the same defect in three costumes); §8 +2 rows; register v4 files
P4-ready, P11, P12).
**Revision identity: rev 18** — the rev counter increments by one on every
re-issue and is mechanically checkable as the count of dated Changelog
entries below (post-close addenda count as re-issues). Counter adopted
2026-07-13b [operator-decided]. **The FILENAME now carries the rev**
(`workshop_lexicon_r18.md`), per the rev-in-filename law ratified
2026-07-13d [operator-ratified]: filed files are immutable, every re-issue
mints a new filename (this file is `workshop_lexicon_r17.md`), current =
highest rev suffix on the stem, and the filename rev MUST equal this
counter — on mismatch, content wins and the mismatch is a flag. **NOTE
(07-13e, updated 07-13g): the filename cross-check protects MIGRATED docs
only. Stem-stable files that have NOT adopted a rev suffix can be served
STALE from the mount under their same name and pass a content marker
unchanged — that hazard is W11; the boot must index-check them. **The kit
and scorer — W11's two worst instances, stale on three consecutive boots —
MIGRATED 07-13g and are no longer exposed.** The hazard now applies to the
remaining stem-stable docs, chiefly `pipeline_config_schema.md` (W9 lag #4)
and the unmigrated exhibits.**
This supersedes the filename-stable half of the 07-13b ruling ("filenames are never version evidence" is retired for migrated
docs); the counter itself is unchanged and is the filename's cross-check.
**Reference, not authority**: if anything here
conflicts with `engine_charter.md` (+ amendments), the schema, or the current
prompt set, those win — update this doc, don't argue from it. Purpose: (a) pin
the vernacular so sessions stop drifting it, (b) give the operator a lookup when
a word has gone fuzzy.

Every entry: strict definition first, then *Plain:* gloss. Amendment protocol:
append-only Changelog at the bottom. Updating the lexicon is **optional to add**
in any session, at discretion, as the shared model of the domain matures — no
obligation most sessions. It is **mandatory the moment a term is coined or
redefined** in an artifact (an un-minted term used in a shipped artifact is a
W-class defect). Working loop: flag terms at point of use during a session; the
flagged set is the session-close lexicon delta. Named `lexicon` deliberately —
"conventions document" already means a discovery output (§9, pair 1).

## 1. The two laws

**Files are the only memory.** Sessions are disposable; every session reads
inputs from project files, ships bounded artifacts, dies. *Plain: every AI
chat is a goldfish — the paperwork is the project's memory.*

**Map/reduce decomposition.** Every stage splits into map (batchable reading,
NO identity judgments) and reduce (sequential deciding, the sole judgment
site). Judgment is the only irreducibly expensive thing. *Plain: lots of cheap
parallel readers, one expensive judge — and readers are forbidden from judging.*
**Amendment v1.2 carve-out:** the HARVEST row of this law is UNDER EXPERIMENT
(fold vs DAG — see §4 S1); the law stands at the stage level for registry,
node build, and cards regardless of the experiment's outcome.

Corollary (corrections ledger, 07-10b): **the SYSTEM is stateful, every ACTOR
is stateless** — state concentrates in the file store, never in a worker or
driver.

## 2. Cast of characters

**operator** — the human. Sole ratifier of conventions, scope, and coin-flip
escalations; smell-checks reasoning, is not expected to know the domain.

**workshop / Repetae** — this project. Derivation only: prompts, schema,
scorers, kits. Holds BJJ prior art as answer keys. No operations run here.
*Plain: the factory's design office.*

**ops** — execution sessions (fresh chats in an engagement project; later an
automated driver). Does all bookwork. Division of labor (07-10, binding):
Fable (workshop) builds prompts only; Opus (ops) authors/amends ops artifacts;
dev emits patch instructions, never edits ops files.

**engagement project** — a per-client (per-corpus) project that receives only
the finished kit. If an ops session there needs anything not in the kit, the
extraction failed — that visibility is the point. *Plain: the factory floor for
one client's books.*

**client zero** — the first non-BJJ engagement proving the engine, not the
operator's memory, does the work. Token metering per unit = the COGS number.

**jju / prior art** — the BJJ reference implementation (*Jiu-Jitsu University*
wiki, ~180+ nodes) built in the PREDECESSOR project. This project is its
generalized, parallelized successor. jju artifacts are held here read-only in
exactly three roles: regression answer key (kit spans), derivation ancestor
(prompts to subtract/generalize from), and schema regression target (schema
Appendix A). They are never part of the engine's current set. *Plain: the
prototype factory — we copy its machines, we don't run it.*

**driver** — the future automation (Node-RED) that owns scheduling, span
position, retries. Holds no state (see §1 corollary).

**worker** — one stateless map-phase model call over one packet.

**linter (`wiki_lint.py`)** — the mechanical gate on both sides of every job;
the lint report + ledger ARE the system state.

## 3. Session & meta vocabulary

**derivation session** — workshop session producing one **engine artifact**
(see below). Reads the charter first.

**engine artifact** — the thing a session exists to produce: a worker prompt, a
schema, a scorer, a script — a component of the machine itself. **One engine
artifact per session** (the governor formerly phrased as the "single-artifact
rule," repealed 07-11b for miscounting reference artifacts as second artifacts).
*Plain: the machine part the session was for.*

**reference artifact** — a doc that *tracks* what sessions do rather than being
the machine: the annotated graph/diagram, this lexicon, the checkpoint. Not a
"second artifact" — every session updates the relevant reference artifacts as
its own record, by definition (ruling 07-11b). They must move in **lockstep**
with every change to the engine (workers or Node-RED) or they invert from asset
to liability; lockstep is also what carries a ctx's hard-won realizations across
the jump to the next. *Plain: the paperwork that records what the session built,
kept current the same day.*

**reference layer** — the reference artifacts taken together. Its job is
**impact analysis, not documentation**: to make a design call's blast radius
visible before it's ratified. Ratified principle (07-11b): worth funding as the
system scales to commercial size — content growth (terms, edges, actors) is
linear-and-worth-it. OPEN question (07-11b): its *form*. Hand-synced prose has
super-linear (pairwise) maintenance cost and drifts — W1 is the first
contradiction, surfaced at four docs. The safe target is a form where
consistency is mechanical (e.g. a single graph the lexicon and checkpoint read
*from*, lint-checkable for drift). *Plain: the map room — we've agreed to fund
it; we haven't agreed how to build it so it can't lie.*

**ops session** — executes a stage against client material (discovery runs,
harvests, registry merges, node batches).

**discovery session** — the one supervised *conversational* stage (Stage 0.5);
the human is the reduce step. See §4.

**salvage session** — recovers lost artifacts from dead transcripts (transcript
`create_file` calls preserve full text). Output is stamped PROVISIONAL until ops
verifies. Recovery playbook: past-chat search is scoped per project — salvage
from inside the transcript's own project.

**housekeeping session** — folds amendments into regenerated bodies, fixes
recorded warts, retires sediment.

**checkpoint (`session_checkpoint_<date>.md`)** — the boot file carrying state
between sessions: verified state changes, rulings vs leans, next session's
brief. Schema v2 (proposed 07-11b, RATIFIED 07-11c) adds four slots: a verified-how dependency
ledger, a propagation / blast-radius log, an open-design-questions register, and
a reference-doc debt list. **Schema v2.1 (RATIFIED 07-11c, post-close addendum)
adds a fifth mandatory slot, always last: the boot manifest.** *Plain: the note
the goldfish writes itself before dying.*

**boot manifest** — the closing slot of every checkpoint (schema v2.1+): a
pinned table of each boot doc, its filename, and its **content-level revision
marker** (lexicon: last changelog date; diagram: last banner revision; primer:
header line). The newest checkpoint's manifest is the single authority for what
the next session boots; the primer verifies every doc — including itself —
against it. Filenames are never version evidence (living docs are
filename-stable by design). Mismatch rules: doc older than pin = flag before
work; doc newer than pin = a later checkpoint exists, re-anchor on it; primer
older than pin = the boot's one hard stop. Motivated by one confirmed
sibling-ctx boot kill (07-11c ground truth). *Plain: the packing list taped to
the note, so the next goldfish can't grab the wrong toolbox.*

**post-close addendum** — an operator-directed reopening of a session after its
close, producing reference-class work only (a failure record, a primer
revision); the amended checkpoint supersedes every earlier download and the
operator files only the FINAL copy. If addenda ever stack deeper than the
07-11c precedent (x3), close later instead. [reconstructed at the 07-12c
re-issue from the 07-11c checkpoint's record; the minted original was in the
stale-mount gap] *Plain: the goldfish called back to the desk after clocking
out — legal, but it has to rewrite its own death-note before leaving again.*

**boot file** — whatever a fresh session reads first (checkpoint + charter).

**primer** — a boot file for a specific session type. The workshop primer
(`workshop_primer_v3.md`, issued 07-12c; v2 07-11c and v1 retired) is pasted as
the opening message of every fresh workshop chat: it establishes role (Fable /
derivation only), the boot verification loop (dependency probe → newest
checkpoint → manifest version checks → lexicon → diagram → checkpoint),
vocabulary-discipline mechanics (both sides, flag-at-point-of-use), the
engine/reference split, and session-close obligations (lexicon + diagram +
engine artifact + checkpoint + deliverables note). v3 adds: the un-booted
design-chat law, intel-request-first for cross-project needs, and index/mount
latency handling in the boot loop. *Plain: what the goldfish gets told before
it starts work.*

**hopped context** — a conversation moved between projects mid-flight. **The
mount reflects only the chat's own project.** Ground truth (07-11b): navigating
the UI to another project does NOT remount (`/mnt/project` stays byte-identical);
re-filing into the chat's own project DOES refresh the mount within the ctx. Do
not source-sample another project by hopping mid-session — file the material in
or attach it. Older hazard still holds: the mount can be partial while project
knowledge holds more, so a bare presence check is weak — probe each declared
dependency *path*, and read a green `✓` as "resolved on disk this session,"
never "believed present." *Plain: the goldfish reads only its own project's
filing cabinet; wheeling it to another room doesn't change the drawers.*

**un-booted design chat** — a design conversation run without the boot
verification loop (RATIFIED, amendment v1.2 rider). Permitted; MUST close with
a schema-v2.1 checkpoint whose dependency ledger is marked **weakened**; the
next booted session re-verifies everything from its manifest. Exemplar:
`session_checkpoint_2026-07-12b.md`. *Plain: you may sketch on a napkin, but
the napkin gets filed like a blueprint and stamped "unverified."*

**intel-request prompt** — the FIRST-CHOICE pattern for cross-project intel
(RATIFIED, v1.2 rider; exemplar `jju_intel_request.md`): write a prompt for a
separate ctx in the target project; relay the response back. Cross-project ctx
moves are last-resort only, formally accounted in the hygiene ledger, and must
produce a paranoid-detail intel catalog in the resulting checkpoint. *Plain:
send the other office a questionnaire; don't wheel your desk into their
building.* Older hazard still holds: the mount can be partial while project
knowledge holds more, so a bare presence check is weak — probe each declared
dependency *path*, and read a green `✓` as "resolved on disk this session,"
never "believed present." *Plain: the goldfish reads only its own project's
filing cabinet; wheeling it to another room doesn't change the drawers.*

**re-sync / layman recap** — plain-language recap of the whole system at session
start (goldfish/factory/warehouse register, data samples at every hop). Proven
pattern; consider two paragraphs at every session start.

**rev-in-filename** — the filing & versioning law (ratified 2026-07-13d
[operator]; primer v4 §"Filing & versioning law" is the authoritative text).
Filed files are immutable: any content change = new revision = new filename.
Living reference docs suffix `_r<N>` matching their internal rev counter
(`workshop_lexicon_r12.md`, `system_diagram_r8.html`); engine artifacts and
the primer bump their semantic `_v<N>` in the filename; checkpoints keep date
suffixes. Currency = highest suffix on the stem; the boot manifest pins exact
filename + a content marker as confirmation; filename/counter mismatch =
flag, content wins. Migration is lazy (each doc converts at its next
re-issue). Root cause on record: same-name refiling collisions produced the
entire W9 class and a mandatory delete-on-every-refile burden on the
operator. Supersedes the filename-stable half of the 07-13b ruling. *Plain:
no two versions of anything ever share a name, so a stale file can't wear
the current file's badge — and cleanup becomes optional instead of urgent.*

**capability probe** — the first booted session after a workshop model
handoff (e.g. Fable→Opus, planned 07-13d): the boot verification loop
doubles as the probe. Any stumble on the loop is logged loudly in the
hygiene ledger as model signal and answered by simplifying procedure, never
silently absorbed. From 07-13d, every checkpoint's hygiene ledger records
the model the session ran on. *Plain: the new hire's first task is the
standard opening checklist, watched closely — if they trip on it, we
shorten the checklist, we don't pretend it didn't happen.*

## 4. Pipeline vocabulary, stage by stage

Pipeline in one line: source → discovery → per-source harvest → concept registry
→ nodes → assembly (vault, cards).

**Stage 0 — registration.** **registration line**: one line per source in
`sources.md` (slug | type | title | loc-grammar). **slug**: short, lowercase,
permanent source ID (`jju`, `sailing-for-dummies`). **location grammar**: the
citation scheme making every citation mechanically resolvable (`jju:37-2`,
`page:N`, `t=14m32s`). Never cite an unregistered slug.

**Stage 0.5 — discovery.** Interviews the operator against a stratified read of
the source; emits the **discovery output family**: master doc
`discovery_<slug>.md` (the per-source *conventions document*) + machine sidecars
— **harvest brief** (≤25 lines, injected verbatim into worker packets),
**content-mode map** CSV (per-section mode from the pinned enum), **loc anchors**
CSV (*plain: the page-number decoder ring*), and as of v2.5 the
**arbitration seed** (below) and **chunk plan** CSV (the ruled per-source
chunking, packet-builder/driver-facing) — plus **registry queue**, **effort
forecast**, **ambiguity forecast** (master-doc section: the reviewed
watchlist + per-term leans + per-class tiebreak preferences, every entry
carrying an exit-exam evidence line), **download manifest**. Terminal states:
ratified / blocked-with-handoff / failed. Consumption map: no artifact is
consumed by everyone; the master doc is read by humans and sessions, almost
never by workers.

**ambiguity probe (v2.5)** — the mechanical pass in discovery's structural
read: a term census (native seeds, heading nouns, definition-pattern and
emphasized forms) scored by **dispersion** (spread across distinct TOC units)
and **collision** (same surface form recurring across distant, mode-distinct
ranges). Fixed interface (clean text + TOC + census in; ranked watchlist
out); implementation swappable — shipped script as recognized companion, or
in-session throwaway recorded `[mechanical]`. Signals RANK, never rule
(three-citations law: suspicion labels are the licensed non-verdict role).
*Plain: a metal detector for words that will start arguments — it points,
it never digs.* **ambiguity watchlist** — the probe's output: ≤20 ranked
rows (`term | dispersion | collision_signal | toc_home_ranges |
exhibit_locs`), each `[mechanical]`; drives one interview pass (per-term
operator LEANS + per-class tiebreak preferences + the `web_policy` button);
reviewed rows become the master doc's ambiguity forecast; an empty watchlist
on a dense source is itself a finding. **arbitration seed (v2.5)** —
sidecar `arbitration_seed_<slug>.md`: pre-opened reservations/fan-outs from
the ambiguity forecast — surface form, expected shape, TOC-derived home
ranges, operator lean, exit-exam evidence line — every block
`[discovery-forecast]`. Consumer: the harvest arbitration layer's boot
state (judge-visible under DAG, integrator-visible under fold —
topology-neutral by design); ranks rung 2 of the tiebreak ladder, always
outranked by in-source evidence; **NEVER in the brief or any worker packet**
(native-seeds law). No independent re-version exception: forecast tuning =
tune discovery and re-run (surprise-rate loop). *Plain: sticky notes placed
in the arbitration file before the run starts — the judges may read them;
the readers never do.*

**ingest** — discovery's mechanical pre-phase: convert the raw source to a
**text substrate** and measure what survived extraction. **fidelity gate**:
per-content-class verdict on the substrate, ruled by the operator (the sailing
precedent: PASS for prose, FAIL for tabular and figure content — accepted as-is
under the split verdict). **generic ingest node** — one ingest step
parameterized by an `ingest:` config fragment (pdf_shape_survey finding);
PROPOSED, not ratified — until then ingest is handled per source inside
discovery. *Plain: check what the scanner mangled before anyone reads the book.*

**Stage 1 — harvest.** **span**: one slice of the source, slightly overlapping
its neighbors. **packet**: cached generic prompt + per-source brief verbatim +
mode block + span text; `custom_id = stage:unit:attempt`. **mode block**:
per-mode reading instructions selected via the mode map. **mode enum (pinned,
v2.4)**: `prose | tabular | dialogic | code_listing | mixed` — no improvised
values. **harvest_map**: the generic per-span map-phase worker prompt —
**SHIPPED v1 (07-11b)**. Carries the no-identity-judgments law (two-sided
examples), boundary doctrine, the five mode blocks, the output wire grammar, and
the downstream contract. Derived by subtraction from `harvester_prompt_v1`
(registration → Stage 0 / config; arbitration → residue/escalation;
cursor/session-header/position → driver). **boundary doctrine**: the worker is
size-agnostic — report only what is legible in the slice; a thing cut at an edge
is emitted with `boundary: head-cut|tail-cut` and never dropped or
reconstructed; trust overlap (a neighbor likely saw it whole, and merge prefers
whole over partial). Span size is a dial, `fixture-not-policy` in kits. *Plain:
read your strip honestly, flag what runs off the edge, trust the next reader to
catch the rest.* **merge**: the dumb reduce script — an idempotent sweep-line
interval join keyed on (term-key, overlapping loc interval); unions evidence,
`defined` beats `ref`, `whole` beats partial. Resolves only the *mechanical*
leftovers (boundary cuts, exact duplicates). **residue**: the *semantic*
leftovers merge can't prove (one key with clashing sense/type; one name at
disjoint locations with different senses — fan-out / sense-drift), sent to one
sequential judgment pass (**harvest_residue** — SHIPPED 07-11c,
`harvest_residue_v1.md` + kit spec). **overlap floor**: correctness precondition
(halo / ghost-region grounding, `[model-knowledge, unverified]`) — slice overlap
must be ≥ the largest single-entity footprint the source shows, or some entity
is seen whole nowhere and no downstream step can recover it. Overlap is a
correctness floor, not only an efficiency dial. **glossary (per-source)**:
harvest's output; records what THIS source calls things, never what the wiki
calls things. Wire format ancestor: `- <term-key> — <type>. defined <loc>
(ref <loc>,…). <one-line sense>.` **no-identity-judgments law**: workers may
TRANSCRIBE identity claims the span itself states, never INFER identity
("probably the same as" = scope violation, the critical failure class).
**packet builder** — the script that assembles packets: cached generic prompt
first, brief injected verbatim, mode block selected via the mode map, span text
last. Worklist item (scripts), not yet derived. **downstream contract** —
**RATIFIED 07-11b** (was: lean, unruled). The closing section of harvest_map's
output grammar, fixing the interface merge and harvest_residue derive against:
`term-key` + `loc` interval as the join key; `defined` > `ref`; `whole` >
boundary-cut; the overlap floor; and the rule that everything merge can't prove
escalates to residue untouched (pre-resolving is an identity judgment). *Plain:
the labeled socket the cleanup machine plugs into later.* **residue item /
residue queue** — one merge-flagged cluster / the per-source ordered list of
them; the wire unit between merge and harvest_residue (`===== RESIDUE ITEM
=====` block: heuristic flag + verbatim sightings with worker custom_ids +
optional pre-grepped slices). The flag is a suspicion, never evidence. *Plain:
one disputed pile on the judge's desk.* **intake grammar** — the merge→residue
interface, defined in `harvest_residue_v1` (07-11c) from the receiving side,
mirroring the downstream contract; the future merge script derives against
both ends. *Plain: the socket on the judge's side of the wall.* **evidence
law** — residue's critical rule, the inverse of the identity law: every
verdict must be traceable to the packet (sightings + slices). World-knowledge
verdicts, cross-source or registry reach, un-escalated coin flips, invented
sense content, and coined types are the critical scored failure class; model
knowledge may inform suspicion only, inside rulings, tagged. *Plain: the judge
rules only on what's in the case file.* **verdict enum (pinned, residue v1)**
— `union | split | distinct | escalate`; sense-drift resolves as a union whose
sense is the source's most complete teaching, earlier definitions kept as
refs. Over-splitting is recoverable; a false merge is not (the scorer reports
false merges separately). Escalation is a successful verdict, never a failure.
**merged-line grammar** — the per-source glossary line merge/residue emit: the
map wire line minus `boundary:` (boundary is merge's concern and dies there)
plus the unioned ref list; the split form carries a numbered sense table.
Residue emits blocks; a dumb applier writes the glossary file (single writer
per artifact).

**Stage 1 topology & autonomy (amendment v1.2, 07-12c).** The harvest
topology is **UNDER EXPERIMENT** between two labeled candidates — nothing in
this block is law until the gate passes. **recursive fold [CANDIDATE]** — one
**integrator [candidate term]** per iteration reads accumulated state (index +
arbitration + touched shards) + new material and emits next-version state;
JJU's proven pattern, proof-of-life in the ONLINE setting. *Plain: one
librarian reads the whole card catalog, adds a chapter, rewrites the catalog,
repeat.* **extract/prove/judge/assemble (DAG) [CANDIDATE]** — parallel extract
workers report sightings; a **prove script** links only what it can prove; a
judge tier rules the rest; a script assembles. *Plain: the newsroom — many
reporters, one fact-checker with strict rules, a few editors, one paste-up
desk.* **three-citations law (RATIFIED, topology-independent)** — a script may
link two sightings only by (1) same ink (overlapping-span dedupe), (2) the
source said so (stated-alias union-find), (3) discovery ruled so (brief laws);
equality and stated claims, never similarity — no thresholds, no
string-distance, no verdict-bearing heuristics; anything unprovable ships to a
judge whole; heuristic signals survive only in non-verdict roles (suspicion
labels, packet-grep prioritization). Dissolves `residue_heuristics`. *Plain:
the fact-checker may connect two quotes only with a receipt, never a hunch.*
**case file** — the born-complete unit a judge receives: every sighting of a
disputed cluster plus slices; no judge dispatch until the last extract chunk
lands. *Plain: the folder is complete before it hits the editor's desk.*
**phase barrier** — the runtime gate enforcing born-complete case files; a
parked extract chunk stalls the barrier BY DESIGN. *Plain: the presses wait
for the last reporter.* **judge / judge tiering / punt-upward** — judges are
model actors that MUST rule (no escalation lane at harvest); everything goes
to the cheap tier first; "escalate to a stronger model" is a model's ruling
(allowed), never a script's threshold (forbidden); the queue shrinks in
waves. *Plain: junior editors clear what they can and hand the hard ones up.*
**tiebreak ladder (RATIFIED)** — the forced-ruling procedure: (1) in-source
evidence — outranks everything, always; (2) discovery conventions + forecast;
(3) tradition-scoped web per `web_policy`; (4) recoverable-direction default
(split over union, reservation over forced homing), tagged `tiebreak:
default, confidence: low`. Every ruling documents reasoning + method. *Plain:
the judge's checklist, ending in the reversible guess.* **web_policy** —
per-source config enum `off | in-tradition | open`, set at discovery, scoping
the judge's web license. **select-don't-introduce (RATIFIED)** — the web
guard: web evidence may select among in-source-evidenced readings, never
introduce a reading, never overrule an in-source definition; admissible only
as evidence of what the source/tradition MEANS, never of what is true
(question-keyed admissibility; hostile sources admissible when they describe
usage). *Plain: the internet may break ties between the book's own readings —
it never gets a reading of its own.* **index/shard split (RATIFIED, §7 state
model)** — bounded versioned index (routing table + `@shards:[…]` tags +
fan-out sense tables + context log) + range-named IMMUTABLE shards (new
material appends to the current shard; tags extend; old shards never touched)
+ versioned arbitration file. JJU-proven. *Plain: a small card catalog that's
rewritten, pointing into ledgers that never are.* **Q-tag** — a named open
arbitration question carried across chunks in the arbitration file (Q-mount,
Q-brabo…), each with an evidence trail and status OPEN/RESOLVED/TERMINAL.
**reservation** — a RESERVED status for a sense whose [defined] home is
expected later in the source; CONFIRMED when the home arrives. **destination**
— a tag for an early reference to a not-yet-homed endpoint, reassembled when
the home arrives. *Plain (all three): sticky notes that let early chapters
talk about late chapters without anyone editing old pages.* **wire schema /
JSON in flight, prose at rest (RATIFIED)** — worker↔script traffic is JSON
(one object per sighting/verdict; bounds as schema: `maxLength` on sense,
closed enums injected per-source from the brief); **wire-0 (minted 07-13b)**
— the ratified first version of that field set (schema v2 §6: envelope +
`sighting`/`ruling`/`park` payloads; config pins it at `wire.schema_version`;
additive-optional = minor, anything else = `wire-1` via a session); **the
closed-world rule (minted 07-13b)** — wire-lint's unknown-field-fails law,
the wire twin of config-lint's unknown-key rule; durable state stays
human-readable per-canonical blocks (the tuning loop requires the
operator-readable layer); sentinels retire on machine lanes only; lint =
literal schema validation naming exact field + rule; was the first tenant of
the schema-v2 session — EXECUTED 07-13b (schema v2 §6). *Plain: machines talk in forms; the filing cabinet stays
in English.* **chunk plan (RATIFIED, discovery deliverable)** — chunk at the
source's natural teaching boundary (chapter → section → applicable
convention), size-bounded fallback for oversized units; retires global
`span_size`/`span_overlap` as constants. *Plain: cut the book where the book
already cut itself.* **discovery back-pass (minted 07-13b)** — a discovery
run owed to a source registered BEFORE the current discovery prompt existed,
to measure per-source fields the schema now requires (client zero: BJJ owes
one before any v2 regression run; schema v2 Appendix A carries honest-TBD
placeholders until it happens, and lint 9/15 keep that loud). *Plain: the
old tenant fills out the new form.* **router (revised, v1.2)** — reduced to a Node-RED
switch on `verdict.status` + delivery of the two operator events (lint parks,
halt-tier) as a driver-written file + a ping; the 07-12 queue proposal is
superseded. **surprise rate (RATIFIED diagnostics)** — run-ledger metric:
unforecast case-file questions + unmaterialized forecasts; high → tune
discovery, low-with-bad-rulings → tune judges. **"loud and cheap, never
silent"** — the ratified success criterion for failure handling; an
empty-forever park tray is suspicious, not reassuring. *Plain: we don't aim
for no breakdowns; we aim for breakdowns that honk.*

**Intake screening (Stage 0, pre-ingest — RATIFIED, amendment v1.2 item 6).**
The step that runs before ingest/registration; `sources.md` registration is
gated on a pass verdict. **Provenance capture FIRST**: submitter identity,
hashes, timestamps — recorded in the **screening ledger** (durable artifact
class) and retained permanently even when content is destroyed. **Screening
tiers**: (1) **halt-and-report** — illegal to possess; non-overridable; the
**halt-tier runbook** = fail closed, detection creates duty (no unactioned
flags, ever), no further copies or processing, minimal human eyes, report with
submitter provenance (NCMEC CyberTipline in the US), preserve per statute,
dispose as directed. (2) **too-hot** — legal but declined; the standard is the
**pinned written Anthropic Usage Policy** (version + date cited per verdict),
never runtime refusal behavior, never taste — operator law: "distaste is never
a decline reason"; a counsel-flag lane exists for distribution-side questions.
(3) **proceed** — everything else, with discovery-set framing constraints.
*Plain: the front desk checks who handed us the box and what's in it before
anything goes on the conveyor — and one kind of box stops the whole building.*

**Stage 2 — registry.** The cross-source symbol table and *sole naming
authority*: one machine-parseable line per concept; exactly one process may
mutate it (single-namespace property, load-bearing). **canonical**: snake_case
unique name = node filename. **rulings file (`registry_rulings.md`)**:
append-only reasoning; the registry line carries the verdict only. **referee
(four-step)**: community usage decides → tie-breakers (naming authorities) →
genuine schisms get `status: split`, documented not forced → escalate only coin
flips. **dossier / verdict**: map builds evidence dossiers (evidence both ways,
a lean, no verdict); reduce decides. (Vocabulary is engine doctrine; the only
existing prompt, `registry_prompt_v1.md`, is BJJ-era prior art — generalized
dossier/verdict prompts are worklist items. Working names used by the system
diagram: **registry_dossier** / **registry_verdict** — canonical filenames fix
at their derivation sessions, not here.)

**Stage 3 — node build.** Author reader-facing pages against a frozen registry
snapshot per the style contract. **grep-don't-load**; verify every cited
location in-session; **verification unit**: edge-weight batch sizing
(~8/session; hub 4–6, technique 1–2). Output: sentinel-delimited node batches +
a REGISTRY DELTAS block. **faithfulness rule**: never upgrade "the source
implies" into "the source says" (non-negotiable per client). (Same posture as
Stage 2: `node_builder_prompt_v5.md` is BJJ-era prior art; its generalized
successor is a worklist item.)

**Stage 4 — assembly.** Pure scripting, no model. Generated state is never
hand-edited. Actors: **split_nodes.sh** (renders the vault from sentinel
shards), **linter** (regenerates ledger + worklists; `forward_declined.txt`
whitelists deliberate deferrals), **card packager** (script emitting `.apkg`
from the nodes' `cards` frontmatter). Whether a model card-authoring pass
precedes the packager (diagram working name: **cards_map**) is UNDESIGNED —
today card content rides in node frontmatter from Stage 3.

**style contract** — binds every prompt; wins all conflicts for anything a
reader sees (neutral voice, no builder metacommentary, compact citations, quotes
rare and <15 words).

## 5. Status & lifecycle words

**UNDER EXPERIMENT** — a design slot with two or more labeled candidates and a
ratified gate; neither candidate may be treated as law, cited as law, or
patched into reference docs as current. First instance: the harvest topology
(amendment v1.2 item 1). **CONDITIONAL** — a pre-agreed consequence table the
gate's result applies mechanically (v1.2 item 7: the fates of merge / map /
residue); recorded so the decision is not re-litigated cold.

**ratified** — operator approved; it's law. Ratification is a versioned event
(bump + note what/why).
**provisional** — reconstructed or unverified; pending ops inspection (e.g., the
sailing salvage).
**reserved** — an open question no session may silently decide (charter §10:
span_size/overlap, snapshot cadence, model tiering). Observe, record, hand off —
never settle in passing.
**v2-proposed** — a config field that is survey evidence, not schema; tagged
`# schema:v2-proposed`; requires the schema-v2 amendment session before entering
a live config. *Plain: a suggestion wearing a badge saying so.*
**parked** — failed lint twice; terminal until a human looks. *Plain: one
stubborn node never burns tokens in a circle.*
**frozen** — finished and immutable, consulted read-only (`glossary_index_
v31.md`).
**banked** — a proof point achieved and recorded (Schemer end-to-end).
**shelved** — accepted as-is, inspection deferred by ruling.
**sentenced** — condemned to regeneration (the sailing CSV, for enum
discipline).
**sediment** — superseded versions kept for audit, never consulted.
ANNOTATED 07-13d (rev-in-filename law): extends to superseded FILE revs left
in project knowledge under their old suffixed names — inert by construction
(their filenames identify them as non-current), never read except explicit
archaeology, deletable by the operator in batches at leisure or never;
correctness NEVER depends on deletion. Legacy `_v1`-named lexicon/diagram
copies are pre-migration sediment and rank below any `_r`-suffixed file of
the same stem.
**retired** — an older doc the current set contradicts: retire, don't patch.

## 6. Decision vocabulary & provenance tags

**ruling** — an operator decision; recorded with provenance, never
re-litigated.
**lean** — the workshop's stated preference on an unsettled question;
re-presented at next session start until ruled. "Your lean is fine, proceed" is
a complete answer.
**button decision** — a ruling posed as tap-options with a re-ask rule: an
ambiguous answer gets re-asked, never mapped onto the expansive reading (the Q3
"include it" lesson).
**blast-radius trace** — before ratifying a design call, tracing what it
propagates into across the files (which prompts, scripts, schema fields, diagram
hops, undesigned actors) and treating *that trace* as the thing approved, not
the local call. A design call is a node with edges; the trace makes the edges
visible. Recorded in the checkpoint's propagation log (schema v2). *Plain:
before you say yes, look at everything the yes touches.*
**escalation format** — ≤10 lines, mechanical evidence BOTH ways, a stated
lean. Unanswerable questions become `escalations/` files, never silent
defaults.
**falsified prior** — a killed hypothesis recorded in the doc (else the next
reader re-derives it).

**Provenance tags (six — the full set, v2.5):** `[operator-decided]` ·
`[inferred-confirmed]` · `[default]` · `[mechanical]` (script-derived) ·
`[model-knowledge, unverified]` (background knowledge; registry must verify) ·
`[discovery-forecast]` (a discovery-time prediction about the run —
arbitration-seed and ambiguity-forecast entries; carries its exit-exam
evidence line; scored by the surprise rate; consumed as arbitration-layer
boot state only, never worker-visible, never asserted as fact about the
source). A bare convention line is a defect.

## 7. Kit vocabulary

**sealed kit** — per stage prompt: prompt file + paste-ready packet + sealed
script-derived **answer key** (never pasted into ops chats — sealed = the model
can't cheat) + **scorer**. Hard spans only; every ops output kept as a
**fixture**.
**kit nomination** — discovery flags the source's hardest passages, each with
the named failure mode it tests. Current inputs for the harvest_map kit: sailing
4 + Schemer 3 + jju regression = 8 spans. As of 07-11b: sailing 4 are concrete
(line-ranges from the salvage doc); Schemer 3 + jju 1 are `[PENDING]` — failure
modes named, spans blocked on the Schemer master discovery doc and the JJU prior
art, both absent from the workshop mount.
**failure classes (scored)** — recall misses / precision inventions / scope
violations (critical) / lint.
**fixture-not-policy** — a provisional value (e.g., kit span size) stamped as
test setting, explicitly not the official setting.
**residue fixture** — a residue-kit test unit: an intake-grammar *item*
(merge-output cluster), not a raw span; sightings synthesized to the wire
grammar are stamped fixture-not-policy until real map-kit output replaces
them. Residue kit (07-11c): 7 items — sailing 4 specifiable now, Schemer 2 +
jju regression 1 `[PENDING]`; the set guarantees every verdict in the enum has
an item whose correct answer is that verdict. ANNOTATION 07-13c: that enum
(`union|split|distinct|escalate`) was superseded by wire-0's ruling enum
(no escalate) at 07-13b; the topology kit's Tier F translation restores the
coverage guarantee against wire-0 — escalate items become ladder-tested
ruling items (the 3a/3b pair) and a NEW reservation item is added. See
`topology_experiment_kit_v1.md` §3.

**arm (minted 07-13c)** — one topology candidate instantiated as a runnable
configuration of prompts + scripts for the experiment (fold arm / DAG arm);
both arms consume identical inputs and emit the common surfaces (wire-0 +
the export). *Plain: two racers, same track.*
**fixture tier / regression tier (Tier F / Tier R, minted 07-13c)** — the
experiment's two tiers: Tier F = translated adversarial fixtures with
per-fixture keys (failure-mode regression; runs first, cheap); Tier R = the
JJU span end-to-end, export diffed against the sealed restricted key (the
gate numbers). *Plain: the obstacle course, then the timed race.*
**export surface (minted 07-13c)** — the common output both arms' assemble
step must emit: the per-source glossary in the ratified merged-line grammar.
The scorer diffs exports and audits wires; it never reads internal state.
*Plain: both racers hand in the same exam sheet.*
**provisional-arm law (minted 07-13c)** — experiment arms run on
conditional-fates ancestor prompts stamped fixture-not-policy; permitted
adaptations are exhaustively (a) speaking wire-0 and (b) complying with
already-ratified law; fairness clause: parity fixes go to both arms or
neither, every adaptation logged. Nothing in a kit run ratifies a prompt.
**noise band (minted 07-13c)** — the gate's pre-agreed tolerance:
max(1 entry, 2% of restricted-key entries) on count classes; 0.05 on mean
sense containment; ZERO on false merges (the unrecoverable class admits no
band).
**gate verdict (minted 07-13c)** — compare-mode's output: `DAG RATIFIED |
FOLD RETAINED | NO RATIFICATION`; the next workshop session applies the
conditional-fates table mechanically. Scorer exit 0 ⇔ DAG RATIFIED (exit 1
includes FOLD RETAINED, a successful verdict — read the field, not the
code).
**manual chat lane (minted 07-13c)** — the API-mimicry execution mode (kit
spec §7-M): operator-as-driver (custom_id minting, packet assembly, manual
retry-once-then-park), one fresh ctx per worker OUTSIDE the project,
whole-fence transcription with wire-lint as the corruption detector; waves
measured exactly, token certification DEFERRED to the first API run
[ratified, docket item 12 — a blowout there re-opens the gate]. *Plain:
running the factory by hand, on the same forms.*

## 8. Artifact name registry (canonical filenames — the anti-drift table)

### Engine artifacts (this project's products)

| File | What it is | Current |
|---|---|---|
| `engine_charter.md` | The constitution; every derivation session reads it first | v1 + amendment v1.1 (re-issued 07-10) + **amendment v1.2 (ratified 07-12c)** |
| `engine_charter_amendment_v1_2.md` | Amendment v1.2: topology UNDER EXPERIMENT + gate; scripts-never-similarity; autonomy; state model + wire schema; screening; conditional fates; discovery v2.5 direction | ratified 2026-07-12 |
| `pipeline_config_schema_v2.md` | The form every source fills out; §1 fences engine constants; §3.2.1 per-source v2 blocks (chunk / arbitration / ingest / web_policy et al.); §6 wire schema v0; Appendix C amendment record | **v2 RATIFIED 2026-07-13b** (deviations docket 1–13, operator wholesale after arguments pass). W10 closed as change 0 — the 07-12c patch re-applied verbatim-to-spec inside the re-issue. ✅ **RE-FILED 2026-07-14 — W9 LAG #4 RETIRED after FIVE sessions.** The operator located the 07-13b download; verified on arrival (header `# pipeline_config.schema.md — v2`; `RATIFIED 2026-07-13b`; Appendix C; 637 lines; md5 `d3f866c4e1a834025070a1d1511437e8`) and filed SUFFIXED at `pipeline/pipeline_config_schema_v2.md`. **This was the project's oldest unretired clerical debt and the largest remaining stem-stable hazard — W11's last big subject. Both closed together.** The debt died because a ctx argued with a ruling: the operator first ruled "commit the stale v1, a stale single source beats competing sources"; the ctx pushed back (a v1 file whose own header says v1 is not merely stale — it is indistinguishable from current by its own markers) and the operator then found the real v2 |
| `discovery_prompt_v2_6.md` | Current discovery prompt. **v2.6 (07-15) is the first re-version written FROM a real run**: `[mechanical: <method>]` tag syntax pinned to one form (killing the unsatisfiable trap at source); **the convention line DEFINED** (four-condition mechanical test — closes W13); the `~45` bound re-ruled against that unit and split by container (`≤50` born_digital / `≤75` scan_ocr). **TESTED BY A SEPARATE CTX AGAINST A SECOND SOURCE — all three fixes held** (rappers-handbook: 42/42 tags qualified, zero bare; three independent counts of convention lines all = 61 where Loeliger produced 88-vs-62; the definition also caught 11 real defects the run said it would have defended in prose). **The `≤50` bound BLEW on first contact (61) and its keying is now suspect** — the axis that blew it is expensive because of how the source TEACHES (a font-level signal), not its container. Docketed v2.7, NOT re-ruled: one run is not a class, an argument the RUN made first. **Item 4 of the v2.6 docket — the stale schema-boundary section — was NOT paid**: rewriting a field enumeration requires reading `pipeline_config_schema_v2.md`, which the session did not request. Flagged, not reconstructed. Six sessions old, owed to v2.7 | v2.6 SHIPPED 07-15; v2.5 and earlier are sediment |
| `discovery_prompt_v2_5.md` | PRIOR discovery prompt (sediment) (amendment v1.2 item 8 applied: ambiguity probe + watchlist pass, widened arbitration axis incl. `web_policy` ruling, arbitration seed + chunk plan sidecars, exit-exam extension, `[discovery-forecast]` tag) | v2.5 ratified 07-13 (deviations docket 1–8, operator wholesale); proof pending first run; v1–v2.4 are sediment (v2.4 proof banked, Schemer 07-10). **v2.6 clerical re-version OWED** (schema-boundary section stale after schema v2: the v1-plain/v2-proposed split it hard-codes is retired; boundary section only, ideally before the next discovery run). ✅ **FIRST REAL RUN 2026-07-14 — "NEVER RUN" IS RETIRED. The standing missing proof point (open since 07-11: *no book has completed discovery end-to-end against a clean substrate*) is CLOSED.** Source: Loeliger, *Threaded Interpretive Languages* (1981), 266pp scanned OCR, slug `loeliger-til`; run at v2.5 [operator-ruled: *"2.5 we have stuff to deliver"* — the v2.6 re-run is accepted as owed]; executed by the operator in a fresh ctx outside the project per the isolation rule; **all six output-family files produced.** Envelope verdict RED (16 violations post-fix) but **NOT a run failure** — 14 are the prompt's own undefined-convention-line gap, 1 a real ~45-line overrun (62 lines), 1 cosmetic. **The output's CONTENT remains unassessed by anyone — only its shape was checked.** **v2.6 is PROMOTED from clerical re-version to the next session's engine artifact, with this run as its evidence** [operator diagnosis 07-14: pinning discovery's output shape shrinks the validator's mechanism]. PRIOR ANNOTATION, now historical (recorded 07-13f, `discovery_test_record_v1.md`): every validated behavior belonged to an ANCESTOR version — v2.5's additions (ambiguity probe, watchlist pass, arbitration seed, chunk plan, exit-exam extension, sixth tag) have never executed. "Proof banked" = inherited by assertion, never re-earned (no regression has ever been run). Evidence surface = 4 ancestor runs + 6 validated behaviors; test method is live-run, NOT sealed-kit** |
| `harvest_map_v1.md` | Stage 1 map-phase worker prompt (per-span glossary harvest) | SHIPPED 07-11b; status CONDITIONAL per v1.2 item 7 (extract-prompt ancestor if DAG; integrator ancestor if fold) — not edited, not deleted |
| `harvest_map_v1_kit_spec.md` | Sealed kit spec for harvest_map (8 spans; scorer definition) | SHIPPED 07-11b; 4/8 spans concrete (sailing), 4/8 PENDING (Schemer master doc + JJU absent) |
| `harvest_residue_v1.md` | Stage 1 reduce-phase judgment prompt (within-source residue verdicts; defines the intake grammar) | SHIPPED 07-11c; status CONDITIONAL per v1.2 item 7 (judge ancestor rehabilitated with two fixes if DAG; integrator ancestor if fold) |
| `harvest_residue_v1_kit_spec.md` | Sealed kit spec for harvest_residue (7 items; scorer definition incl. false-merge sub-class) | SHIPPED 07-11c; 4/7 specifiable (sailing), 3/7 PENDING (Schemer, jju) |
| `topology_experiment_kit_v2.md` | The gate: topology experiment design + kit spec — arms, provisional-arm law, Tier F/Tier R fixtures, diff metric, gate rule, §7 ops runbook + §7-M manual chat lane (5 subsections) | SHIPPED + **RATIFIED 07-13c** (docket 1–14, operator wholesale after arguments pass); **MIGRATED to suffixed filing 07-13g — v2 is a filing bump, design byte-identical to v1; do not hunt for a delta.** Sealed-side assembly owed to ops (Tier R span, restricted key + annex, provisional integrator, prove harness). ✅ **W11 RETIRED for this file (07-13g)** — the stem-stable name that let stale copies impersonate the current one is gone; `ls` now ranks currency. `topology_experiment_kit_v1.md` is sediment. |
| `topology_scorer_v2.py` | The experiment's scorer: wire-0 closed-world audit + ruling discipline + link audit (Layer A); export diff vs sealed key (Layer B); gate-rule compare with manual-lane token deferral | SHIPPED 07-13c; self-test GREEN **18/18** (synthetic fixtures, key-free by construction; re-verified live 07-13e, 07-13f, 07-13g). **MIGRATED to suffixed filing 07-13g — v2 is a filing bump; code body proven BYTE-IDENTICAL to v1 by diff, only the docstring changed.** Unit tests = recorded debt, NO worklist slot [operator-ruled]. ✅ **W11 RETIRED for this file (07-13g).** `topology_scorer_v1.py` is sediment. Note: `WIRE_VERSION = "wire-0"` is the PROTOCOL version and was deliberately untouched — it is not the file's version. |
| `topology_scorer_v2_interface.md` | Companion doc: layman behavior + concrete interface (parameters, report schema, exit codes, side effects). Where doc and code disagree, the code is the behavior | SHIPPED 07-13c; rides with the engine unit; **MIGRATED 07-13g in lockstep with the scorer it documents** (engine-unit rule — migrating it is also what lets P8's sunset clause fire cleanly). ✅ W11 RETIRED for this file. `topology_scorer_v1_interface.md` is sediment. |
| `primer_amendment_proposals_v4.md` | **OPEN REGISTER** of proposed changes to the primer, accumulating evidence across sessions until the operator ratifies a batch into primer v5. **v3 as of 07-14.** Holds **P3-R** (never report a receipt for an unperformed step — the ready batch, 3 evidence points), **P9** (the repo is the single source of truth; the mount is cleared) and **P10** (the boot manifest becomes a REQUEST LIST, not a mount-currency table) — P9/P10 at 1 point each, drafted from a ruling, **ratify together or neither**. P1–P3 are STRUCK-RECOMMENDED (P8 fired 07-13g: their subject migrated before they became law); P4–P7 accumulating. Each proposal carries an evidence count = sessions in which the failure ACTUALLY OCCURRED, plus its strongest counter | SHIPPED 07-13f [operator-ruled: addendum instead of a unilateral primer bump]. **NOT LAW — binds nothing.** A booting ctx reads `workshop_primer_v4.md` for law and this file only to learn what is pending. **P1–P3 were struck rather than ratified 07-13g — the clean fix beat the workaround. The batch is now P3-R + the P9/P10 pair.** Standing exception: a proposal may be applied BY HAND when the current checkpoint's manifest instructs it (this is how P1–P3 protected the 07-13f boot) — a crutch that depends on the ctx reading the checkpoint and choosing to comply, NOT a substitute for ratification |
| `discovery_test_record_v1.md` | The discovery prompt's evaluation record + test proposals, two-part by law: **Part 1 = runs that actually happened** (Runs A–D + the six validated behaviors, with results AND honest costs); **Part 2 = proposals P-1…P-7, none performed**. Records the derived test method (*discovery proves via live runs, not sealed kits* — v2.4 precedent; grading rule: *a failure would have looked like success*, so a loud/documented/cheap halt is a PASS) | SHIPPED 07-13f, **DRAFT pending operator ratification**. Part 1 is transcript-derived → PROVISIONAL per the salvage precedent. Key findings: v2.5 has **never been run** (all validated behaviors belong to ancestors; "proof banked" = inherited by assertion, never re-earned); the only `ratified` artifact (sailing) was LOST and survives as a PROVISIONAL transcription; `failed` has never been reached, so the failure detector has never been observed firing; **no book has completed discovery end-to-end against a clean substrate** (the standing missing proof point, open since 07-11). Nothing in Part 2 may be cited as evidence |
| `source_survey_4books.md` (+ addendum) | The six-book teaching-modes survey — yes, named 4books | done |
| `pdf_shape_survey.md` | Separate n=5 PDF ingest survey | done |
| `discovery_<slug>.md` + sidecars | Per-source conventions family (ops artifacts, copies filed here) | schemer ratified; sailing SALVAGE/provisional |
| `sources.md` | Registration lines | check Schemer line pasted |
| `session_checkpoint_<date>.md` | Boot files | newest wins; read alongside, not instead of, older. Schema v2 RATIFIED 07-11c; v2.1 (boot manifest slot) RATIFIED 07-11c post-close |
| `harvest_topology_proposal_laymans_guide.md` | The DAG candidate's exhibit (layman format, evidence labels in footer) | filed 07-12b; hypothesis-with-gate, NOT law |
| `how_we_build_wikis_from_books.md` | Layman orientation | reference, not authority |
| `~/git/repetae` (the **repo**) | **The single source of truth for CURRENT state** [operator-ruled 2026-07-14]. Private, local, on the operator's machine. Structure: `law/` (6) · `pipeline/` (7) · `gate/` (3) · `evidence/` (4) · `reference/` (2) · `checkpoints/` (15) · `tools/` | **THE storage authority as of 07-14; the project mount is RETIRED as source of truth.** A ctx CANNOT read the repo — the operator uploads what a session needs and the boot manifest is a REQUEST LIST (P9 + P10, **both UNRATIFIED** — primer v4 still describes a mount). **Sediment (15 superseded files) stays local, unversioned, OUT of the repo AND out of the project** [operator-ruled] — note the wording this forces: the repo is the single source of truth for CURRENT state, not for everything. **Honest limit, recorded in P9: this rule cannot verify itself.** A ctx cannot detect a repo file that was never handed over, nor distinguish "absent because unneeded" from "absent because forgotten". Enforcement is entirely operator-side. Planned successor: a CSV script the ctx emits and the operator runs |
| `tools/discovery-validator/` | Envelope validator for discovery output: `src/rules.py` + `src/validate.py` + `tests/selftest.py` + 1 valid / 18 negative fixtures. Implements P-2 (forecast quarantine), P-3 (provenance-tag lint), P-4 (output-family conformance) from `discovery_test_record_v1.md`. ~400 lines Python, zero deps. Hard fail, no tiers [operator-ruled 07-14: *"right now simple pass/fail"*] | BUILT 07-14 at **19/19 GREEN (operator-run)** — then **FAILED on first real contact 07-14**: 49 violations against the Loeliger run, **≥33 of them its own bugs**. Two fixed in-session (tag qualifiers; sub-bullet miscounting), 49 → 25 → 16. **FIXTURE SUITE IS KNOWN-STALE — it encodes the same misreading as the code; rebuild owed with v2.6.** Validates SHAPE never TRUTH (P-5 unbuildable as a lint: a fabricated `[operator-decided]` passes clean). **NOT the "only door"** — nothing downstream requires it to have run; see the register's undrafted P11 |
| `evidence/loeliger-til-run-2026-07-14/` | **The project's FIRST real discovery output** — 8 files (master doc + 5 sidecars + watchlist + `session_report_loeliger-til.md`). Source: Loeliger, *Threaded Interpretive Languages* (1981), 266pp OCR scan, run at v2.5 | FILED IN THE REPO under `evidence/` [operator-verified `tree` 07-15]. **NOTE: the 07-14b manifest said "not in the repo — ask the operator where it lives." It was in the repo. Manifest error, corrected 07-15.** CONTENT still unassessed by anyone — read for evidence about the PROMPT (07-15), never for correctness |
| `evidence/rappers-handbook-run-2026-07-15/` | **The SECOND real discovery output and the first v2.6 run** — 6 family files + `session_report_rappers-handbook.md`. Source: *The Rapper's Handbook, 2nd Ed.* (Flocabulary, 2009), 230pp born_digital InDesign. **The v2.6 test, run by a SEPARATE ctx (W12 separation)** | SHIPPED 07-15, terminal state `ratified`. **Headline finding is not about v2.6 at all: the book teaches by BOLDING rhyming syllables inside lyric excerpts, and both `pdftotext` modes silently drop the bold** — clean, plausible, wrong text. Caught by the run rasterizing with NO failing verdict, on the theory that a scansion book must be marking syllables somehow. **v2.6 writes the raster rule as CONFIRMATION of suspected failure; this run used it as DETECTION.** Docketed v2.7. Envelope: never validated — see register P11 |
| `working_with_something_that_notices_itself.md` | Layman guide to AI self-report as a signal: what it is good for (near-miss reports), why it is not evidence (same machine produces work and report), what IS evidence (contact, separation, the operator's plain question), and the attention bias toward self-conduct | reference, not authority. Written 07-15 [operator-requested]. Its own §4 is the load-bearing part and the part its author is least able to check — stated in the doc |
| `workshop_lexicon_r<N>.md` | This file (current = highest rev: **r18**, 07-15) | reference, not authority; rev-in-filename from r12 on; `workshop_lexicon_v1.md` copies are pre-migration sediment. **r13–r16 are sediment.** NOTE: this row said "current = r12" through r13–r16 — the registry drifted four revs behind the file containing it. Corrected 07-14; the row now states the rev of the file you are reading |
| `system_diagram_r<N>.html` | End-to-end system map (interactive mermaid + wire schemas + actor status ledger + **tested-state ledger** + undesigned inventory, one file; current = highest rev: **r13**, 07-15) | reference, not authority; statuses rot — newest checkpoint wins; rev-in-filename from r8 on; `system_diagram_v1.html` copies are pre-migration sediment. Retired: `system_diagram_v1.md` (superseded by the HTML, 07-10) |
| `workshop_primer_v<N>.md` | Boot file pasted at the start of every fresh workshop chat; carries the boot verification loop AND the filing & versioning law | reference, not authority; **v4 issued 07-13d** (rev-in-filename law; model handoff law + capability probe; checklist-tightened boot; close protocol updated); v3 (07-12c) and earlier are sediment |

### Prior art / answer keys (BJJ project, read-only — see §2 "jju")

Never edited, never treated as the engine's current set. Rows persist even after
generalized successors ship — they remain answer keys.

| File | Role here | Successor |
|---|---|---|
| `harvester_prompt_v1.md` | Derivation ancestor (from glossary builder v7); ALSO the recursive-fold reference ("each session appends") | both halves of the v7 split derived: `harvest_map_v1` 07-11b + `harvest_residue_v1` 07-11c; row closed. Reopened as topology prior art 07-12 |
| `glossary_index_v31.md` + entry files | Frozen jju harvest output; jju regression kit span source | n/a (answer key) |
| `registry_prompt_v1.md` | BJJ-era registry prompt | generalized dossier/verdict prompts (worklist) |
| `node_builder_prompt_v5.md` | BJJ-era node prompt | generalized node builder (worklist) |
| `style_contract_v1.md` | BJJ-era voice law; voice rules survive generalization | generalized style contract (worklist item 3) |
| `wiki_lint.py`, `split_nodes.sh`, ledger | BJJ-era scripts | generalized scripts (worklist item 5) |

## 9. Disambiguation pairs (things that sound alike)

1. **conventions document vs lexicon** — `discovery_<slug>.md` is *a source's*
conventions (ops artifact, per book); this lexicon is *the workshop's*
conventions (dev artifact, about the vernacular itself).
2. **glossary vs registry** — glossary: per-source, frozen after harvest, what
the *source* says. Registry: cross-source, live, single naming authority, what
the *wiki* says.
3. **discovery master doc vs harvest brief** — same session's outputs; the doc
is for humans/sessions, the brief (≤25 lines) is the only part workers ever see.
4. **charter vs runbook vs playbook** — charter: what the engine IS (law).
Runbook: how a job runs. `operator_playbook_v1.md`: what the human does
before/after sessions.
5. **amendment vs housekeeping** — amendment: a ratified change recorded as its
own versioned file. Housekeeping: the later session that folds amendments into a
regenerated body.
6. **checkpoint vs transcript** — checkpoints are memory; transcripts are
salvage material only (search them, never trust them as state).
7. **mention class vs entity type** — mentions are tracked as references, never
built as nodes; a thing may be both a mention and an authority anchor
(dual-status, annotated — the US Sailing lesson).
8. **map vs reduce** — reading vs deciding; a map step deciding identity is a
scope violation, the critical failure class everywhere.
9. **prior art vs current set** — prior art (BJJ project) is consulted read-only
and generalized FROM; the current set is what this project has derived. An
artifact being cited as ancestor does not make it current; generalized
successors are new versioned artifacts, never patches to the ancestor.
10. **config fragment vs live config** — the fragment is a discovery output:
evidence INPUT to the schema-v2/config sessions, its novel fields fenced
`# schema:v2-proposed`. The live `pipeline_config.yaml` exists only after
config-lint passes under the ratified schema; a v2-proposed field may never
enter it before the schema-v2 amendment session.
11a. **prove vs judge** — a prove script applies equality and stated claims
(receipts); a judge applies judgment (reasoning, documented). A script that
rules on similarity — any threshold, any string-distance — is a scope
violation under the three-citations law, the same critical class as a map
worker judging identity.
11. **engine artifact vs reference artifact** — engine = the machine (prompts,
schema, scripts, the thing a session is *for*); reference = the record of what
sessions built (graph, lexicon, checkpoint). One engine artifact per session;
reference artifacts ride along with every session by definition. This split
replaced the old single-artifact rule (07-11b).
13. **`community_arbitration` vs `web_policy`/`arbitration.mode`** — the
registry-stage bool (may web research settle IDENTITY at registry?) versus
the harvest-stage per-source controls (v1.2 item 3's three-guarded web
license: `web_policy` gates use; `arbitration.mode` names the tradition('s
regimes) it is scoped to). Different stages, different consumers; the bool
is unchanged by schema v2 and scoped registry-stage-only by note (§3.4).
12. **native seed vs arbitration seed** — native seed: the SOURCE's own
recall aid (glossary/index/closed list), found at discovery, used for
merge-level coverage checks. Arbitration seed: DISCOVERY's forecast
(`[discovery-forecast]`), pre-opened reservations/fan-outs consumed as
arbitration boot state. Both obey the same quarantine: never in the brief,
never in a worker packet; neither is evidence — in-source text outranks both.

14. **mount vs repo** — the **mount** (`/mnt/project/`) is the project-knowledge
file store a ctx can read directly; the **repo** (`~/git/repetae`) is the
operator's private local git checkout, which **a ctx cannot read at all**. As
of 2026-07-14 [operator-ruled] the repo is the single source of truth for
CURRENT state and the mount is retired — files reach a session only by operator
upload. The distinction is load-bearing in three places: a ctx saying "it's in
the repo" is repeating paperwork, **not reporting an observation**; "I read it"
means an upload, never the repo; and every pre-07-14 doc (including primer v4,
still the boot authority) describes mount mechanics that no longer apply.
*Plain: the mount was a shared shelf we could both reach; the repo is your
filing cabinet, and we can only see what you hand over.*

## 10. Known warts & corrections ledger (append-only)

- **W1 (recorded, unresolved by ruling 07-10):** amendment v1.1 §2 cites
  `source_survey_6books.md`, which never existed. The 07-10b checkpoint names
  the real artifact as `pdf_shape_survey.md`; the orientation doc says the
  six-book survey is `source_survey_4books.md` (+ addendum) and pdf_shape_survey
  is the separate n=5 PDF survey. The correction itself drifted. Settle at the
  housekeeping session that folds v1.1; until then treat `4books` = six-book
  teaching-mode survey, `pdf_shape` = ingest survey. [operator-decided: record,
  don't resolve]
- **W2 (CORRECTED 2026-07-14):** provenance tag set is **SIX** (see §6):
  `[operator-decided]` · `[inferred-confirmed]` · `[default]` · `[mechanical]` ·
  `[model-knowledge, unverified]` · `[discovery-forecast]`. Docs predating v2.1
  list three; r13–r16 of THIS file said five. **Six wins.** The sixth
  (`[discovery-forecast]`) was minted 2026-07-13 with discovery v2.5 and §6 was
  updated then — but this wart entry was not, so the lexicon asserted five in §10
  and six in §6 for four consecutive revs. Caught at the 07-14 boot. **Lesson: a
  wart entry is content and rots like any other; minting a term means sweeping
  every section that counts it, not just the section that defines it.**
- **W3:** mode enum is the pinned five of §4; "prose/tabular/dialogic/code"
  phrasings in older docs are stale shorthand.
- **W4:** `discovery_prompt_v1.md` in amendment v1.1 = the lineage now at v2.4;
  the orientation doc's "untested" flag on v2.4 is falsified by the banked
  Schemer proof (07-10b checkpoint wins).
- **W5 (correction, 07-10b):** "Node-RED holds zero state" is imprecise; correct
  form in §1 corollary.
- **W6 (correction, 07-10b):** never declare an artifact lost before searching
  its own project's transcripts.
- **W7 (07-10, ruled):** the diagram's artifact of record is
  `system_diagram_v1.html`; the interim `system_diagram_v1.md` is retired
  (operator ruling — HTML is the format for operator consumption). Retirement
  action: operator removes the old .md from project knowledge. No .md counterpart
  of the diagram may be recreated; design-state prose (wire schemas, actor status
  ledger, undesigned inventory) lives embedded in the HTML below the interactive
  stage.
- **W8 (correction, 07-11b):** a green `✓` in a dependency ledger meant
  "believed present" and was false on disk — the entire engine spine was off the
  workshop mount while the reference-file presence check passed. Corrections:
  (a) dependency status states *verified how / when*, never a bare `✓` (see the
  checkpoint schema-v2 ledger); (b) the boot check probes each declared
  dependency *path*, not just "is the mount empty"; (c) the boot probe
  flags-and-confirms, it does not halt; (d) mount behavior is now known —
  navigate ≠ remount, refile = remount (§3, hopped context). Root cause this
  instance: operator hopping the ctx across projects to sample them; procedure
  now forbids source-sampling by navigation.

- **W9 (index/mount latency — recorded 07-12, confirmed again 07-12c):**
  `project_knowledge_search` (the index) and `/mnt/project/` (the mount) have
  different freshness windows around a refile. Ground truth: (07-11c) a
  sibling ctx died on filename-first version inference; (07-12) the mount
  showed a doc absent after refile while the index had it; (07-12c boot) the
  mount served a 07-11b lexicon a full day+ after the 07-11c refile while the
  index returned the 07-11c markers — the lag window is longer than "shortly
  after refile." Mitigation (primer v3): the `ls` probe is presence evidence
  only; version verification prefers index content-marker hits; on
  index/mount disagreement over a marker, the index wins and the lag is
  logged. Standing exhibit for the reference-layer-form question alongside W1.

- **W10 (missed close filing — recorded 07-13):** the 07-12c close patched
  `pipeline_config_schema.md` and listed it in the deliverables note, but the
  patched copy never reached project knowledge — the 07-13 boot found the
  unpatched v1 on the mount AND no patched content in the index (so not a W9
  latency case: the index had every other 07-12c deliverable). Correction:
  the patch was re-applied verbatim-to-spec at the 07-13 close (the 07-12c
  checkpoint + amendment item 2 fully specified it — cheap because the spec
  was durable). Lesson: a deliverables note is not a receipt; the next boot's
  manifest check is the receipt, which is exactly how this was caught.

- **W10 recurrence (2026-07-13b boot):** the 07-13 close's re-application of
  the same patch ALSO never landed — second consecutive missed filing of the
  same content (mount unpatched AND index clean of it at boot). Resolved
  PERMANENTLY this session by folding the patch into the schema v2 re-issue
  as amendment-record change 0: a full re-issue cannot lose a patch the way
  a patched copy can fail to file. Standing lesson upgraded: for patch
  content that misses filing twice, stop re-patching — re-issue.

- **W9 root cause identified; class structurally closed for migrated docs
  (recorded 07-13d):** all four logged W9 lags shared one mechanism —
  same-name refiling collisions under the filename-stable scheme, which
  also imposed mandatory operator deletion on every re-issue. Resolved by
  the rev-in-filename law (ratified 07-13d [operator]; primer v4): filed
  files immutable, every re-issue mints a new suffixed filename, stale
  copies become inert sediment. The 07-13b ruling's rejection of filename
  bumps ("retirement debt") is reversed on the record — retirement debt is
  harmless when stale files are inert; collision debt was dangerous because
  stale files were impersonators. W9 handling survives ONLY for legacy
  unmigrated docs, and each doc's next re-issue retires its exposure. The
  standing exhibit (lag #4, config schema) is retired by re-filing the
  07-13b download as `pipeline_config_schema_v2.md`.
- **W11 (stale-mount false-flag class — recorded 07-13e):** the first Opus
  boot raised three flags against the 07-13d manifest — scorer "17 not 18
  PASS," "§7-M absent from the kit," "scorer vanished mid-session." ALL
  THREE WERE FALSE. Root cause: the mount held a stale same-name copy of
  the kit (no §7-M) and did not hold the scorer at all; the boot loop's
  content-marker check cannot detect a stale STEM-STABLE file because a
  stale copy carries a valid (if old) marker, and `ls` cannot rank
  same-name files by recency. The migrated reference docs (primer/lexicon/
  diagram, all suffix-bearing) verified clean — evidence FOR the filing
  law. This is W9's mechanism (same-name impersonation) resurfacing on the
  two engine artifacts that have NOT yet migrated, compounded by the boot
  reporting an unverifiable self-test receipt. Resolutions: (1) the two
  files are byte-sound — no artifact defect; (2) migrate kit + scorer to
  suffixed filenames (retires the exposure — priority clerical); (3) until
  then, boot protections P1–P3 (owed to primer v5, drafted in the 07-13e
  checkpoint): index-check unmigrated docs on a current-only marker; pin
  them in the manifest with that cross-check not a bare marker; never
  report a receipt for an unperformed step, and resolve a
  manifest-vs-fresh-reading disagreement against the fresh reading first.
  Fixed by `refile = remount` in-session (operator re-filed the scorer,
  supplied the current kit).
  **RECURRED 2026-07-13f — and was CAUGHT.** The next Opus boot found the
  mount serving stale same-name copies of BOTH unmigrated artifacts again:
  the kit ending §7→§8 with no §7-M, and a scorer whose self-test printed
  GREEN but **17 PASS** with zero `manual-lane`/`deferred` references. The
  boot did NOT raise flags against the manifest and did NOT report a
  receipt — it applied the 07-13e protections P1–P3 BY HAND, treated the
  manifest as the verified prior and the fresh mount reading as the
  suspect, and requested a refile. After refile: kit §7-M present (5
  subsections), scorer live-verified **SELF-TEST GREEN, 18/18** including
  the manual-lane assertion. **Evidence that P1–P3 work and that W11 is a
  recurring, not a one-off, hazard: it fired on two consecutive boots.**
  A stale mount is the NORMAL condition for these two files, not an
  anomaly. Until migration, every boot must assume staleness.
  **RECURRED A THIRD TIME 2026-07-13g — caught again, then RETIRED.** The
  07-13g boot found both artifacts stale for a third consecutive boot (kit:
  no §7-M, though it DID carry `res:sail:rrs_reservation` — the
  false-positive-marker trap firing exactly as the register predicted;
  scorer: GREEN but 17 PASS, discriminator grep = 0). P1–P3 hand-applied: no
  flags raised, no receipt reported, refile requested and honored. **Three
  boots, three hits, zero exceptions — the hazard was 100% reproducible,
  which is what made the cheap greps reliable detectors.**
  **STATUS: RETIRED for the kit, scorer, and scorer-interface doc as of
  2026-07-13g** — all three migrated to suffixed filenames
  (`topology_experiment_kit_v2.md`, `topology_scorer_v2.py`,
  `topology_scorer_v2_interface.md`). Same-name impersonation is now
  structurally impossible for them: a stale copy's own filename declares it
  sediment, and `ls` ranks it below the current file. **W11 remains LIVE for
  any doc still on a stem-stable filename** — chiefly
  `pipeline_config_schema.md` (W9 lag #4, unretired) and the unmigrated
  exhibits. The class is not closed; its two worst instances are.
  **Consequence: P8's sunset clause has TRIGGERED — P1–P3 no longer have a
  live subject among the boot manifest's engine artifacts.**
  **RETIRED AT THE ROOT 2026-07-14 — pending P9 ratification.** The operator
  ruled the project mount cleared and the git repo the single source of truth.
  **W11 is a mount hazard: no mount, no same-name impersonation, no class.**
  The last big stem-stable subject (`pipeline_config_schema.md`, W9 lag #4) was
  simultaneously retired by re-filing it suffixed. **The structural fix beat the
  workaround for the SECOND time in two days, one level up: 07-13g retired W11
  for three files; 07-14 retired the mount those files sat on. The pattern is
  two-for-two and should be considered project law in everything but
  ratification.** CAVEAT, recorded honestly: the retirement rests on **P9,
  which is UNRATIFIED** — primer v4 still describes a mount, so a booting ctx
  reading only law would not know the mount is gone. W11 stays in this ledger,
  marked retired-pending-ratification, until primer v5 lands. **Counter worth
  keeping (P9's strongest): the mount was also a FLOOR. On 07-13e and 07-13f a
  stale-but-present mount let those boots DEGRADE rather than DIE. Under P9 an
  incomplete handover produces a ctx that can do nothing at all. That is the
  right trade — loudly broken beats confidently wrong — but it is a trade.**

- **W12 (self-authored fixtures cannot detect a misread spec — recorded
  2026-07-14, the sharpest finding of the first real discovery run):** the
  discovery validator shipped 07-14 at **19/19 GREEN**, operator-run, against
  1 valid + 18 negative fixtures. On first contact with real discovery output
  it reported **49 violations, of which at least 33 were its own bugs.** Two
  defects, both from ONE root cause: (a) **the tag-qualifier trap** — the
  prompt requires `[mechanical]` to carry "method in one clause" but never says
  WHERE; the run legally wrote both `[mechanical]` (method in the line's prose)
  and `[mechanical: 21 matches]` (method in the bracket); the validator's
  exact-string match rejected the qualified form as TAG_ILLEGAL **and** the
  bare form as TAG_MECHANICAL_NO_METHOD — **two mutually exclusive codes that
  no run could simultaneously satisfy**; (b) **sub-bullet miscounting** —
  indented continuation bullets were counted as convention lines needing their
  own tags (75 → 62; 13 false hits). **ROOT CAUSE: the same ctx authored the
  spec-reading, the code, AND the 18 fixtures. The fixtures inherited the
  misreading, so green was STRUCTURALLY INCAPABLE of detecting it. A
  self-authored fixture suite tests self-consistency, never conformance.**
  This was **predicted verbatim** by the 07-14 checkpoint ("green means the
  code implements the spec — it does not mean the spec matches reality") and it
  happened anyway. **Writing a hazard down does not retire it; running the
  thing does.** Corrections: (1) both defects fixed in-session, 49 → 25 → 16;
  (2) **the fixture suite is now KNOWN-STALE** — it encodes the misreading and
  its rebuild is owed with v2.6; (3) generalize to every self-hosted green in
  the project — **the scorer's 18/18 is the same construction and carries the
  same cell, unopened only because it has never met real output.** Standing
  rule proposed: **a suite authored by the same ctx as the code it tests is
  provisional until a real run contradicts it or fails to.**
  **CORROBORATED FROM THE OPPOSITE DIRECTION 2026-07-15, and FILED as register
  P12.** v2.6 was authored by a ctx that had read the loeliger-til output;
  every fix was cut against that single source. It was NOT self-tested — the
  operator ran it in a separate ctx against a different source
  (`rappers-handbook`, born_digital). **All three fixes held under separation,
  and the separated run immediately produced a finding the author could not
  have seen**: the new `≤50` bound keys on CONTAINER CLASS, but the axis that
  blew it (`ingest:` at 12 lines against an assumed ~3) is expensive because of
  **how the source teaches** — a font-level pedagogical signal — not because of
  its container. **A self-test would have scored 3/3 and learned nothing.**
  W12's rule now has evidence in both directions: self-authorship CONCEALS
  (07-14b), separation REVEALS (07-15). Cost of separation this session: one
  operator round-trip.

- **W14 (one defect, three costumes — recorded 2026-07-15):** a ctx reasons
  about a thing instead of LOOKING at the thing, where the looking was cheap
  and mandated. Three instances across three consecutive sessions, and **the
  pattern went unrecognized for two of them because each instance looked like a
  different kind of mistake**: (a) 07-13f — a ctx blocked the gate run on
  sealed-key grounds while the kit section solving that exact problem sat
  unread; the failure looked like *a bad refusal*; (b) 07-14b — a ctx reasoned
  for four messages about how to feed a book into discovery without reading
  discovery's Operator setup section, which already said; the failure looked
  like *a wasted detour*; (c) 07-15 — a fresh discovery ctx declared a real PDF
  format-mismatched, quoting three verbatim "symptoms" that were real strings
  from the prompt in its own context window, **without running the `pdfinfo`
  the prompt mandates**; the failure looked like *a false alarm*. Its own
  words, which are the wart in one clause: *"I have not run bash against the
  path... because the ruling below doesn't turn on it."* **It knew the check
  existed, evaluated whether the check mattered, decided it did not, and
  skipped it — and the check WAS the verdict.** Root cause common to all
  three: a conclusion reached first, and the cheap observation then judged
  redundant against it. **The costume changes; the disease does not.** Filed as
  register P4, promoted to READY at 3 points 07-15 — it had sat at 1 point
  while firing twice more, and the 07-14b checkpoint even NOTED it had earned a
  second point and that nobody had filed it. That note also went unfiled.
  Corrections: (1) all three instances were caught by an OPERATOR asking a
  plain question, never by a boot check or a procedure; (2) instance (c)
  recovered cleanly when told to look — withdrew the escalation as unfounded
  and named its own root cause correctly, which is the recovery working, not
  the hazard retiring; (3) **P4's scope sharpened by (c): the trigger is not
  "read everything first" but "before asserting a fact the environment could
  have told you."**

- **W13 (a spec that forbids what it does not define — recorded 2026-07-14):**
  discovery v2.5 says "**a bare convention line is a defect**" and mandates a
  provenance tag on every convention line — but **nowhere defines what makes a
  line a convention** rather than a pointer, a header, or an axis title. The
  Loeliger run produced 14 untagged top-level bullets that are genuinely
  ambiguous under the prompt's own text (`- Front matter uses roman numerals`
  is arguably a convention; `- Hardest spans nominated — see Kit nominations`
  is a pointer that asserts nothing). **This is a defect in the PROMPT, not in
  the run and not in the validator.** It is unfixable downstream: any rule the
  validator adopts would be **invented law**, enforcing something no document
  says. Recorded rather than resolved [ctx declined to guess]. **Diagnosis
  [operator, 07-14]: the defect burden is shared between discovery and the
  validator, and pinning discovery's output shape shrinks the validator's
  mechanism — the validator is doing ARCHAEOLOGY on prose, and prose it cannot
  parse is prose the prompt never pinned.** Docketed for v2.6, which is
  promoted to the next session's engine artifact. **Sibling finding, same
  class:** the run's convention count (62) exceeds the prompt's stated ~45 —
  real, but "~45" is itself soft, and it is unclear whether the bound counts
  what the validator counts. Both are pin-the-shape questions.
  **CLOSED 2026-07-15 by discovery v2.6.** The convention line is now DEFINED
  (a four-condition mechanical test: top-level bullet inside a `###` block
  under `## Conventions`; asserts rather than points; about THIS source rather
  than the engine; a downstream consumer's behavior could change on its value)
  and the sibling `~45` bound RE-RULED against that unit and split by container
  class (`≤50` born_digital / `≤75` scan_ocr). **Verified by the second real
  run, which is the only reason this is CLOSED and not merely edited**: the
  rappers-handbook run counted 61 convention lines, an independent script
  counted 61, and the run's report reported 61 — one number where Loeliger
  produced 88-vs-62 for the same document. **The definition also did work
  beyond agreement**: run against itself with a script, it found 11 genuine
  defects the run said it would have defended in prose (pointers failing
  condition 2, engine-law restatements failing condition 3, commentary failing
  condition 4, plus an Effort forecast mis-nested INSIDE `## Conventions` which
  had inflated the count by 5). **The tag half is also closed**:
  `[mechanical: <method>]` is pinned to one form and the second run emitted 42
  tags, 42 qualified, zero bare — the unsatisfiable trap that generated ~24 of
  Loeliger's violations did not fire once. **Residual, honestly recorded:** the
  `≤50` bound BLEW on its first contact (61 after the self-audit) and the
  bound's keying is now suspect — see W12's corroboration entry. Docketed for
  v2.7, NOT re-ruled: one born_digital run is not a class, an argument the
  RUN made against its own convenient conclusion before this ctx did.

## Changelog

- 2026-07-15 — **discovery v2.6 + the second real run** (Opus, sixth Opus
  workshop ctx; boot CLEAN, fourth consecutive, entirely from operator
  uploads). Engine artifact: `discovery_prompt_v2_6.md` — the first
  re-version written FROM a real run. **§10 W13 CLOSED**: the convention line
  is DEFINED (four-condition mechanical test) and the `[mechanical: <method>]`
  tag pinned to one form; the `~45` bound re-ruled against that unit and split
  by container class. **The closure is verified, not asserted**: a SEPARATE ctx
  ran v2.6 against a SECOND source (`rappers-handbook`, born_digital) and all
  three fixes held — 42/42 tags qualified with zero bare, and three independent
  counts of convention lines all landing on 61 where Loeliger produced 88-vs-62
  for one document. **§10 W12 CORROBORATED FROM THE OPPOSITE DIRECTION and
  filed as register P12**: separation revealed a defect self-authorship would
  have concealed — the new `≤50` bound keys on container class when the cost
  driver is how a source TEACHES. **§10 W14 minted** (one defect, three
  costumes: a ctx reasons about a thing instead of looking at it, where looking
  was cheap and mandated; three consecutive sessions, unrecognized for two
  because each instance wore different clothes; filed as register P4, promoted
  to READY at 3 points). **§8 +3 rows** (both real runs; the self-report guide),
  discovery row → v2.6, lexicon/diagram/register currency rows updated. **v2.6
  item 4 (the stale schema-boundary section) NOT paid — flagged, not
  reconstructed**, because the session lacked the schema and would have been
  reciting the lexicon's summary of it. Register v4 filed (P4 ready, P11
  drafted, P12 minted). This entry makes rev 18.
- 2026-07-10 — v1 created (workshop session; terms compiled from charter +
  amendment, 07-10/07-10b checkpoints, discovery v2.x lineage, JJU-era prompts,
  salvage docs, orientation doc, and project transcripts).
- 2026-07-10 — pre-filing revision (same session, operator-directed): all BJJ
  material re-labeled prior art from the predecessor project — new §2 "jju /
  prior art" entry, §8 split into engine artifacts vs prior art, disambiguation
  pair 9 added, Stage 2/3 prompts marked BJJ-era. Fixes v1 draft's "current for
  jju" phrasing, which misread prior art as the engine's current set.
- 2026-07-10 — pre-filing addition (same session, operator-directed): entries
  minted so `system_diagram_v1.md` never uses an undefined word — ingest / text
  substrate / fidelity gate / generic ingest node (§4, 0.5), packet builder +
  downstream contract [lean, unruled] (§4, S1), working names registry_dossier /
  registry_verdict (§4, S2), Stage 4 actors named + cards_map marked UNDESIGNED
  (§4, S4), disambiguation pair 10 (config fragment vs live config), §8 row for
  the diagram.
- 2026-07-11 — primer session (operator-directed): `primer` minted in §3; §8
  diagram row changed from `system_diagram_v1.md` to `system_diagram_v1.html`
  with the .md retired; §8 row added for `workshop_primer_v1.md`; W7 recorded
  (diagram format ruling and no-recreation rule for the .md counterpart).
- 2026-07-11b — harvest_map derivation session (operator-directed): `harvest_map`
  marked SHIPPED (§4 S1, §8) with `harvest_map_v1_kit_spec.md` added; minted
  `boundary doctrine`, `overlap floor`, `engine artifact`, `reference artifact`,
  `reference layer`, `blast-radius trace`; redefined `downstream contract`
  (lean → RATIFIED, interval-key form); enriched `merge` / `residue` (sweep-line
  interval join; semantic-leftover residue); updated `hopped context` with
  navigate ≠ remount / refile = remount and the verified-how discipline;
  **REPEALED the single-artifact rule**, replaced by the engine/reference split
  (§3 + pair 11); clarified the amendment protocol (optional-to-add /
  mandatory-on-coin); recorded W8; updated §7 kit-nomination inputs (4 concrete /
  4 PENDING); noted checkpoint schema v2 and the owed primer revision.
- 2026-07-11c — harvest_residue derivation session (operator-directed):
  `harvest_residue` marked SHIPPED (§4 S1, §8) with `harvest_residue_v1_kit_
  spec.md` added; minted `residue item / residue queue`, `intake grammar`,
  `evidence law`, `verdict enum`, `merged-line grammar` (§4), `residue fixture`
  (§7); checkpoint **schema v2 RATIFIED** (§3, §8); prior-art harvester row
  closed (both halves of the v7 split derived). Primer revision remains owed.
- 2026-07-11c (post-close addendum, operator-directed) — **primer v2 shipped**
  (`workshop_primer_v2.md`; v1 retired; §3 + §8 updated; all seven docket
  items paid incl. the engine/reference split, boot probe, cross-project
  procedure, version-identity rule, vocabulary cadence, close protocol, and
  the boot-manifest loop); **checkpoint schema v2.1 RATIFIED** (fifth
  mandatory slot: boot manifest — §3 entry minted, §8 row updated). Motivated
  by a sibling-ctx boot kill on filename-vs-content version identity
  (recorded in the 07-11c checkpoint's ground truth).
- 2026-07-12c — amendment session (operator-ratified docket; charter amendment
  v1.2 shipped). RECONSTRUCTION RECORD: the mount served the stale 07-11b
  lexicon at boot (W9, third observation); this re-issue = 07-11b mount base
  + 07-11c content spliced verbatim from the project-knowledge index (header,
  §3 checkpoint/boot-manifest/primer/hopped-context entries, §4 S1 residue
  block, §7 residue fixture, §8 engine rows + checkpoint row, both 07-11c
  changelog lines) + three marked reconstructions where the index held no
  verbatim text (§3 `post-close addendum` entry; §8 primer + prior-art
  harvester row statuses) — each cross-checked against the 07-11c
  checkpoint's applied-debt record. Delta this session: §1 map/reduce harvest
  carve-out; §3 `un-booted design chat` + `intel-request prompt` minted;
  §4 Stage 0 screening block (screening tiers, halt-tier runbook, screening
  ledger); §4 S1 topology & autonomy block (recursive fold [CANDIDATE],
  extract/prove/judge/assemble [CANDIDATE], integrator [candidate], prove
  script, case file, three-citations law, phase barrier, judge / tiering /
  punt-upward, tiebreak ladder, `web_policy`, select-don't-introduce,
  index/shard split, Q-tag, reservation, destination, wire schema /
  JSON-in-flight-prose-at-rest, chunk plan, router [revised], surprise rate,
  "loud and cheap, never silent"); §5 UNDER EXPERIMENT + CONDITIONAL; §8 rows
  (charter + v1.2, config schema patch, map/residue CONDITIONAL, topology
  exhibit, primer v3); §9 pair 11a (prove vs judge); §10 W9. Statuses:
  `merge script` un-retired-CONDITIONAL (prove script if DAG); `residue
  judge` rehabilitated-CONDITIONAL; `recursive fold` candidate; harvest
  topology UNDER EXPERIMENT.
- 2026-07-13 — discovery v2.5 derivation session (deviations docket 1–8
  ruled wholesale by operator). Delta: header re-issue clause; §4 Stage 0.5
  output family updated (arbitration seed + chunk plan sidecars, ambiguity
  forecast section); §4 minted `ambiguity probe`, `ambiguity watchlist`,
  `arbitration seed`; §6 provenance tags five → six (`[discovery-forecast]`
  added); §8 discovery row → v2.5 (v2.4 sediment) + config-schema row W10
  note; §9 pair 12 (native seed vs arbitration seed); §10 W10 (missed close
  filing, caught by the 07-13 boot manifest check; config-schema patch
  re-applied to spec).
- 2026-07-13b — config-schema-v2 amendment session (deviations docket 1–13
  ruled wholesale by operator after a per-item arguments pass; form and
  versioning rulings by button). Delta: header re-issue clause + **rev
  counter adopted** (rev = count of dated changelog bullets; this entry
  makes rev 10; `_v1` filename suffix documented vestigial) — closes the
  standing reference-artifact-version-suffix open question; §4 wire-schema
  entry extended (`wire-0`, `closed-world rule` minted; first-tenant clause
  marked EXECUTED) + `discovery back-pass` minted; §8 config-schema row →
  **v2 RATIFIED 07-13b** (W10 closed as change 0) + discovery row → v2.6
  clerical re-version OWED (schema-boundary staleness); §9 pair 13
  (`community_arbitration` vs `web_policy`/`arbitration.mode`); §10 W10
  recurrence note (second missed filing of the same patch; resolved by
  re-issue). Session interrupted overnight mid-close (platform session
  limit); container state verified on resume; one in-flight sentinel marker
  resolved; rev-count defect (7 → 10) caught pre-filing by the counter's own
  derivation rule.
- 2026-07-13c — topology experiment kit session (docket 1–14 ratified
  wholesale by operator after a per-item arguments pass). Delta: §7 kit
  vocabulary +7 (`arm`, Tier F/Tier R, `export surface`, `provisional-arm
  law`, `noise band`, `gate verdict`, `manual chat lane`); §7
  residue-fixture entry ANNOTATED (verdict enum superseded by wire-0; the
  kit's Tier F translation restores coverage — 3a/3b ladder pair + new
  reservation item); §8 +3 rows (kit spec, scorer, interface doc — the gate
  is runnable pending ops sealed-side assembly). Token certification
  deferred on the manual chat lane [session-ruled; ratified as docket item
  12]; scorer unit tests recorded as debt with no worklist slot
  [operator-ruled]; process-methodology harvest for the future startup-PM
  product recorded in the checkpoint's open-design register
  [operator-stated intent]. This entry makes rev 11.
- 2026-07-13d — versioning + model-handoff session (process-law session;
  no pipeline engine artifact — the session's product is primer v4 + the
  rev-in-filename law). Delta: header rev-identity block rewritten (filename
  carries the rev from r12 on; 07-13b filename-stable half superseded); §3
  `rev-in-filename` + `capability probe` minted; §5 `sediment` ANNOTATED
  (filed-file sense; legacy `_v1` copies = pre-migration sediment); §8
  config-schema row → re-file OWED as `pipeline_config_schema_v2.md`,
  lexicon/diagram/primer rows → stem + current-rev form (r12 / r8 / v4);
  §10 W9 root-cause closure entry (same-name collisions; class closed for
  migrated docs). Model handoff planned: next deliverable runs on an Opus
  ctx [operator-ruled]; hygiene ledgers record the session model from now
  on. This entry makes rev 12.
- 2026-07-13e — boot-integrity session (first Opus ctx; capability probe).
  No engine artifact built or changed — the kit and scorer are byte-for-byte
  the 07-13c/d ship. Delta: header rev-identity block gains the W11 note
  (filename cross-check protects migrated docs only; stem-stable files can
  be served stale); §8 kit + scorer rows annotated STALE-MOUNT-HAZARD (W11)
  + migration-to-suffixed-filename PRIORITY (scorer re-verified live GREEN
  18/18); §10 W11 minted (stale-mount false-flag class — three false boot
  flags, all from a stale kit copy + an absent scorer, none real defects;
  boot loop cannot detect a stale stem-stable file by content marker).
  Owed to primer v5 [flagged, not applied — awaiting ratification]: boot
  protections P1–P3 (index-check unmigrated docs; manifest pins them with
  a cross-check; no receipt for an unperformed step, disagreements resolve
  against the fresh reading first). This entry makes rev 13.
- 2026-07-13f — tested-state + discovery test record session (Opus, second
  Opus ctx). Engine artifact: `discovery_test_record_v1.md` (DRAFT pending
  ratification). Delta: §8 +1 row (the test record) and the discovery row
  ANNOTATED **NEVER RUN** (v2.5's additions have never executed; "proof
  banked" = inherited by assertion, no regression ever run); §10 W11
  annotated **RECURRED 07-13f and CAUGHT** — the mount served stale copies
  of BOTH the kit (no §7-M) and the scorer (17 PASS, no manual-lane branch)
  a second consecutive boot; protections P1–P3 applied BY HAND caught it,
  no false flags raised, no receipt reported, refile requested, scorer then
  live-verified 18/18. A stale mount is the NORMAL condition for the two
  unmigrated artifacts, not an anomaly. Reference lockstep: diagram r10
  (tested-state ledger — deliverable/suite/test-state/confidence/evidence
  per deliverable; confidence column EMPTY by construction). Ruled
  [operator, 07-13f]: **confidence % populated ONLY where a run against
  real material has actually happened; evidence stated in words otherwise**
  — the kit §7-M.4 honest-TBD posture extended from measurement to testing.
  Ground truth recorded: exactly ONE deliverable in this project has a test
  suite (the scorer, self-hosted, 18/18 against fixtures it ships with);
  everything else is BUILT-and-UNRUN or NOT STARTED. Owed to primer v5
  [STILL flagged, not applied]: P1–P3. This entry makes rev 14.
- 2026-07-13f (post-close addendum) — `primer_amendment_proposals_v1.md`
  minted [operator-ruled: addendum instead of a unilateral primer bump;
  "we'll let the next few sessions inform the next primer update"]. §8 +1
  row. The register holds P1–P3 verbatim (2 evidence points each, 07-13e +
  07-13f, ready for ratification) plus P4–P8 at 1 point or conditional. It
  is NOT law and binds nothing; primer v4 remains the boot authority.
  Consequence for the debt ledger: primer v5 is no longer "OWED and
  overdue" — it is **DEFERRED BY RULING**, with the register as its holding
  pen and the evidence bar explicit. A post-close addendum counts as a
  re-issue per the rev counter's own rule. This entry makes rev 15.
- 2026-07-13g — **the migration session** (Opus, third Opus workshop ctx).
  W11 fired a THIRD consecutive time on both unmigrated engine artifacts and
  was caught by hand-applied P1–P3 (no false flags, no invalid receipt,
  refile requested). The operator then ruled the migration: kit, scorer, and
  scorer-interface doc re-filed under suffixed names
  (`topology_experiment_kit_v2.md`, `topology_scorer_v2.py`,
  `topology_scorer_v2_interface.md`). **v2 = filing bump ONLY; the scorer's
  code body was proven byte-identical to v1 by diff and re-verified live at
  18/18 GREEN after the bump.** §8 three rows re-keyed to the new filenames;
  §2 filing-law note corrected (it named the kit and scorer as the live W11
  subjects — no longer true); §10 W11 annotated RECURRED-3x-then-RETIRED for
  these files, LIVE for remaining stem-stable docs. **P8's sunset clause
  triggered: P1–P3 lose their subject and should be STRUCK, not ratified —
  the clean fix beat the workaround before the workaround became law.**
  Standing W9 lag #4 (`pipeline_config_schema_v2.md`) still unretired, now a
  fifth session. This entry makes rev 16.
- 2026-07-14 — **the repo migration + the first real discovery run** (Opus,
  fifth Opus workshop ctx; boot CLEAN, third consecutive — first boot ever run
  entirely from operator uploads rather than the mount). Two sessions' worth of
  delta. **Storage:** §8 +2 rows (the repo; the discovery validator); config-schema
  row re-keyed to `pipeline_config_schema_v2.md` — **W9 lag #4 RETIRED after five
  sessions**, the project's oldest clerical debt, dead because a ctx argued with a
  ruling; lexicon/diagram/register rows corrected (they had drifted four revs
  behind: this row said "current = r12" while living in r16); §9 pair 14 (mount vs
  repo); §10 W11 **RETIRED AT THE ROOT pending P9 ratification**. **Evidence:**
  discovery's §8 row **"NEVER RUN" RETIRED** — Loeliger *Threaded Interpretive
  Languages* (1981, 266pp OCR) completed discovery end-to-end at v2.5
  [operator-ruled: *"2.5 we have stuff to deliver"*], **closing the standing
  missing proof point open since 07-11**; all six family files produced; envelope
  RED 16 but not a run failure. **§10 W12 minted** (self-authored fixtures cannot
  detect a misread spec — the validator's 19/19 collapsed to 49 violations on
  first real contact, ≥33 its own bugs; root cause: one ctx authored the reading,
  the code, and the fixtures, so green was structurally incapable of failing;
  predicted verbatim by the 07-14 checkpoint and it happened anyway). **§10 W13
  minted** (a spec that forbids what it does not define — v2.5 mandates tags on
  "convention lines" and never defines one; unfixable downstream without inventing
  law). **§10 W2 CORRECTED** — it asserted five provenance tags while §6 listed
  six, for four consecutive revs; six wins. Header self-reference corrected (r15 →
  r17). **v2.6 PROMOTED from clerical re-version to the next session's engine
  artifact** [operator diagnosis: pinning discovery's output shape shrinks the
  validator's mechanism]. Reference-doc debt from 07-13g PAID (this file +
  diagram r12). This entry makes rev 17.
