# Primer amendment proposals — addendum v5

Status: **OPEN REGISTER. Nothing here is law.** Issued 2026-07-13f (workshop);
re-filed as v2 on 2026-07-13g when P8's sunset clause TRIGGERED;
re-filed as v3 on 2026-07-14 (P9/P10 added — the repo migration);
re-filed as v4 on 2026-07-15 (P4 → 3 points, P11 drafted, P12 minted);
**re-filed as v5 on 2026-07-18 (Session A, clerical) — P13 + P14 filed from
their 07-15b drafts; P15 + P16 minted from the 07-18 audit-loop session;
coverage-by-silence evidence recorded.**

**v5 delta (read this first).** Four proposals join the register; none is new
theory — all four were owed and drafted before this session. This is a filing
session (roadmap Session A): the debt is paid, no proposal is ratified, no
primer is bumped.

**P13 filed** — the executable-snippet convention (the ctx emits per-session
shell snippets against the repo, BOTH directions). Drafted in the 07-15b
Rulings, unfiled across two sessions. Operator-requested outright, so it enters
at a higher-confidence footing than a failure-derived proposal.

**P14 filed** — the schema-lockstep rule. Drafted in 07-15b. **Its home is NOT
this register's target primer — it is charter amendment v1.3** (a genuine
engine-law change). It is carried here as a POINTER with its draft text so the
finding is not lost, and flagged for routing to the charter track. P14 and P11
are the same finding in two costumes (W14): a schema/prompt moved and the thing
that reads its output did not.

**P15 minted** — audit-prompt generalization (the audit prompt gets MORE GENERAL
as discovery evolves, never synced to it). A genuine second finding from 07-18,
distinct from P14 despite looking identical.

**P16 minted** — coverage-by-silence as a detector+re-verify loop, not a bare
lint. The chunk-plan coverage check must TRIGGER mandatory re-verification of
affected pages, not merely fail the run. Two independent witnesses this session
(Loeliger real gap; rappers cosmetic id-skip).

P3-R, P4, P9, P10, P11, P12 unaffected in status. P5–P7 unaffected.

**What this file is / is NOT / standing exception / promotion rule / evidence
discipline** — unchanged from v4; re-read the v4 header for the full statements.
Summary: this is a holding pen for proposed `workshop_primer` changes; it is not
law and binds no session; a proposal may be hand-applied only if the current
checkpoint's manifest instructs it; promotion needs an operator ruling or
(≥2 evidence points AND no counter); evidence count = sessions where the failure
ACTUALLY OCCURRED.

---

## Register summary

| # | Proposal | Evidence pts | Confidence | Status |
|---|---|---|---|---|
| **P3-R** | Never report a receipt for a step not performed | **3** (07-13e/f/g) | HIGH | **ready** |
| **P4** | Read the runbook before reasoning about feasibility | **3** (07-13f, 07-14b, 07-15) | HIGH | **READY** |
| **P5** | Search the transcripts before asserting project history | 1 (07-13f) | MEDIUM | accumulating |
| **P6** | Honest-TBD posture generalized | 1 + kit precedent | MEDIUM-HIGH | accumulating |
| **P7** | Bundled-button rulings ruled loudly | 1 (07-13f) | LOW-MEDIUM | accumulating |
| **P9** | Repo is single source of truth; mount cleared | 1 (07-14 ruling) | MEDIUM-HIGH | drafted — pairs with P10 |
| **P10** | Boot manifest = request list, not currency table | 2 (07-14, 07-14b) | MEDIUM-HIGH | drafted |
| **P11** | Validator is the ONLY door | **4** (07-14, 07-14b, 07-15, 07-18 — all non-occurrence) | MEDIUM | DRAFTED — blocked on fixture rebuild |
| **P12** | Self-authored suite is provisional until real output tests it | 2 (07-14b, 07-15) | HIGH | MINTED |
| **P13** | *(filed 07-18)* Ctx emits per-session shell snippets vs the repo, BOTH directions | **2** (07-15b request; 07-18b exercised at boot) | HIGH | **FILED — operator-requested** |
| **P14** | *(filed 07-18)* Schema is lockstep with the ends it touches | 2 (07-13b `span`; 07-15b diagnosis) | HIGH | **FILED as POINTER → charter v1.3, NOT primer** |
| **P15** | *(new 07-18)* Audit prompt generalizes as discovery evolves; never synced | 1 (07-18 ruling) | MEDIUM-HIGH | **MINTED** |
| **P16** | *(new 07-18)* Coverage-by-silence = detector + mandatory re-verify loop | **2** (Loeliger real gap; rappers cosmetic skip) | HIGH | **MINTED** |

---

## P13 — The ctx emits per-session shell snippets against the repo, BOTH directions

**[operator-requested, 07-15b:** *"I want that convention of you generating a
custom snippet every time you need something. it really saves me time."]*

Verbatim draft (07-15b Rulings), filed here to spec:

> The ctx emits per-session shell snippets against the repo, in BOTH directions:
> an inbound **requisition** snippet (probe declared dependency paths, md5+lines,
> loud `MISSING:` branch) and an outbound **repo-sync** snippet (file the
> session's new artifacts under their suffixed names, print a close-state
> confirmation). Supersedes P10's SHAPE without replacing it: P10 made the boot
> manifest a request list; P13 makes the request list executable.

**Scoped to BOTH halves deliberately** — inbound requisition AND outbound sync
are one mechanism; splitting them would name the thing by symptom instead of
mechanism (the P4 error). Required property, earned in 07-15b: a loud `MISSING:`
branch — an absence you can SEE. A manifest cannot observe an absence; a script
can. This is the W14 shape turned into a tool: a manifest asserted an absence a
script falsified (the audit-findings-in-repo surprise, 07-18 item 6).

**Evidence:** 07-15b (operator request) + 07-18b (the boot manifest's
requisition snippet was exercised at this session's boot and worked — the whole
Session-A dependency probe ran off it).

**Strongest counter:** an executable convention encodes the operator's exact
environment (Pop!_OS, X11, `xclip`); a snippet that assumes `xclip` or a path
layout breaks silently on a different machine. **Response:** the snippet is a
courtesy artifact regenerated per session, not filed law — it costs nothing to
re-emit for a new environment, and the `MISSING:` branch degrades loudly, not
silently. Confidence HIGH (operator-requested, and it has now run clean).

---

## P14 — The config schema is lockstep with the ends it touches

**[operator-ruled, 07-15b:** *"in the future, schema should be lockstep with the
ends it touches."]* **HOME: charter amendment v1.3, NOT the primer.** Carried
here as a pointer + draft so the finding survives; routed to the charter track.

Verbatim draft (07-15b Rulings):

> The config schema is a contract with ends. Any change to a schema field — add,
> remove, rename, retag — is not complete until every artifact that WRITES that
> field and every artifact that READS it has moved with it, in the same session
> or on a named docket item with an owner. A schema session that ships without
> touching its writers has not shipped; it has created a debt that will be paid
> by a run, silently, against a lint.

**P14 and P11 are the same finding in two costumes (W14).** Schema v2 removed
`span` on 07-13b; discovery kept emitting it for two sessions and two books; the
validator that reads discovery output never moved. P11 (validator-is-the-door)
is blocked on the fixture rebuild — which IS the writer-side of the same lockstep
break. **Recorded here explicitly so a fourth session does not re-derive it.**

**Evidence:** 07-13b (the `span` removal that started the drift) + 07-15b (the
diagnosis that named it a lockstep failure). **Strongest counter:** lockstep is
expensive — it can turn a one-line schema tweak into a multi-artifact session.
**Response:** the alternative is a debt paid by a run against a lint, silently,
which is strictly worse; the rule permits a *named docket item with an owner* as
the escape valve, so lockstep need not be same-session, only same-accountability.

---

## P15 — The audit prompt generalizes as discovery evolves; it is never synced to it

**[operator-reasoned, ctx-confirmed, 07-18].** A genuine second finding, distinct
from P14 despite the surface resemblance.

> The audit prompt's value is that it does NOT know what the discovery prompt
> says — it reads discovery output cold. Syncing the audit prompt to discovery
> leaks the answer key and destroys the audit's independence. The correct
> coupling is one-way and abstracting: as discovery evolves, the audit prompt
> gets MORE GENERAL (drops version-specific rosters for the principle that
> generates them), never synced. Every version-specific detail in the audit
> prompt is BOTH a staleness bug AND a contamination risk.

**Why this is NOT P14.** P14 says two coupled artifacts must move together. P15
says two artifacts must be kept APART — coupling them is the defect. They look
identical ("keep X in sync with Y") and rule in opposite directions; that is
exactly why the distinction is owed to the register rather than folded into P14.
Applied this session: audit prompt v2 replaced its hard-coded five-sidecar
roster with the principle that generates it (07-18 verified-state 2).

**Evidence:** 1 (07-18 ruling + the v2 generalization it drove). **Strongest
counter:** an audit prompt that knows nothing about discovery may miss a
discovery-specific defect class a synced prompt would catch. **Response:** that
is the point — a defect only a synced auditor catches is a defect the auditor was
TOLD to look for, i.e. not an independent finding. Independence is the asset;
coverage of known classes is the validator's job, not the auditor's.

---

## P16 — Coverage-by-silence is caught by a detector + mandatory re-verify loop, not a bare lint

**[operator-sharpened, 07-18:** from "lint" to "detector + re-verify loop"].**

> Chunk-plan coverage is verified by arithmetic: every in-scope page lands in
> exactly one chunk. A gap or overlap does not merely FAIL the run — it TRIGGERS
> mandatory re-verification of the affected pages (rasterize, read, then
> chunk-or-evidence-exclude). The rule's teeth: *a page may not be dropped by
> silence; it is dropped only by a stated, page-checked reason.* This is the
> identical confirmer→detector upgrade v2.7 made to the raster rule, one level
> up: a check that only confirms lets a clean-looking gap ship; a check that
> detects forces a look.

**Evidence: 2, both this session's filing check.**
1. **Loeliger — a REAL gap.** Printed p174–179 (§6.2 + §6.3) covered by no
   chunk; c086 ends p173, c054 starts p180. Confirmed by three independent
   methods (auditor arithmetic 07-18; 07-18 raster read; Session-A arithmetic
   re-derivation). Already docketed as `docket_chunk_coverage_reverify_v1.md`.
2. **Rappers — a cosmetic id-skip.** chunk-id `ch18` skipped (ch17 merge, never
   renumbered); coverage genuinely fine (219/219). Same organ, harmless
   instance — the class a lint catches free and no human notices, in a
   `ratified` artifact (07-15b open-question 5).

**Home ruling (from the docket):** BOTH — a prompt rule in discovery v2.8
(roadmap B.1) AND a lint twin in the validator (roadmap C.2), on the
schema-lockstep precedent. **Strongest counter:** a mandatory re-verify loop is
heavier than a fail-and-report lint and could stall a run on a benign overlap.
**Response:** the loop only fires on a coverage arithmetic failure, which by
construction means pages are unaccounted for — never benign; and the resolution
(state a reason or chunk it) is exactly the provenance the system exists to
produce.

---

## Evidence increments log (per the register's own rule)

- **2026-07-18 (Session A, clerical)** — **P13 and P14 FILED** from their 07-15b
  drafts (three sessions and two costumes overdue between them). **P15 and P16
  MINTED** from the 07-18 audit-loop session. **P11 incremented to 4** — the
  07-18 loop ran runner + auditor with the validator touching neither pile;
  fourth non-occurrence point. **The coverage-by-silence class (P16) was
  re-confirmed a third time** by this session's own filing arithmetic before
  filing the Loeliger pile — logged as the filing check doing its job, not just
  the run. No proposal ratified; no primer bumped; this is a filing session.

*(Prior increments — 2026-07-15, 2026-07-13g — carried forward from v4
unchanged; see v4 for their full text.)*

---

## How to use this register at a close

*(Unchanged from v4.)*
1. If you built on a hand-applied protection, increment its evidence count and
   add the session ID. One line. Do not restate the proposal.
2. If a session surfaced a NEW recurring failure, add a proposal with 1 evidence
   point, drafted, with its strongest counter stated.
3. If a proposal was argued against, record the argument.
4. Do not bump the primer from this file without an operator ruling.
5. When the operator ratifies a batch, the ratifying session issues the next
   `workshop_primer_v<N>.md`, strikes the ratified proposals, and re-files this
   register with the survivors.

**Routing note (v5):** P14 is charter-amendment territory (v1.3), not primer
territory. When the charter track next opens, P14 leaves this register for the
charter and is struck here with a pointer.

## Changelog

- 2026-07-18 — **v5 issued (Session A, clerical filing).** P13 + P14 filed from
  07-15b drafts; P15 + P16 minted from the 07-18 audit-loop session; P11 → 4
  points; coverage-by-silence evidence (Loeliger real + rappers cosmetic)
  recorded under P16. P14 flagged for the charter track (v1.3), carried here as
  a pointer only. No ratification, no primer bump — debt paid, nothing decided.
  v4 is sediment.
- *(v4, v3, v2, v1 changelog entries carried forward unchanged — see v4.)*
