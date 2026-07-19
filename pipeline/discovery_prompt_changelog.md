# Discovery Prompt — version-note changelog

This file holds the stacked version notes fossilized out of the discovery
prompt at v2.8 (2026-07-19, roadmap Session B, patch 2). The prompt keeps a
one-line pointer here instead of carrying ~85 lines of its own history inline;
the pointer-not-copy rule the prompt applies to the config schema, applied to
the prompt itself. Newest note first, as in the prompt's original ordering.

Amendment protocol: when the discovery prompt is re-versioned, its new
version note is prepended here and the prompt keeps only its pointer.

---

Version note (v2.6 → v2.7, 2026-07-18): **the schema-boundary fix, plus the
graded mechanical tag.** Four ruled changes, all evidenced by the two real
runs (Loeliger + rappers-handbook) and the rappers audit:
(1) the schema-boundary section STOPS ENUMERATING schema fields and becomes a
rule that points at `pipeline_config_schema_v2.md` — the old copy had rotted
(it listed the removed field `span` as plain v1, listed `text_path` in two
lists at once, and instructed the retired `# schema:v2-proposed` tag; both
real runs obeyed and emitted lint-failing fragments). A copy of another
document's field list will always drift from it; a pointer cannot.
(2) the `[mechanical: <method>]` tag gains a STRENGTH GRADE — a count proves
counting happened, not that the claim it backs is sound. The rappers run
shipped "gestures are always `The <Name>`" tagged `[mechanical: heading
census]`; the census was real and the claim was false (its own range contained
the exceptions). A graded tag makes "I counted" and "this holds" different
assertions.
(3) the raster rule becomes a DETECTOR, not only a confirmer.
None is speculative; each names its run.

Version note (v2.5 → v2.6, 2026-07-15): **the first re-version written from
a real run.** v2.5 executed end-to-end against R.G. Loeliger, *Threaded
Interpretive Languages* (1981, 266pp, OCR scan, slug `loeliger-til`) on
2026-07-14 — the project's first complete discovery run. The run adhered.
**What broke was everywhere the prompt told a run to obey something it had
never defined.** Every change below carries that run as its evidence; none
is speculative.

1. **`[mechanical]` tag syntax PINNED to one form** — `[mechanical: <method>]`,
   method inside the bracket. v2.5 required "method in one clause" and never
   said where the clause lives, so the run legally wrote both forms (17 bare,
   8 qualified) and no lint could accept both. Fixes the defect that made the
   validator reject every qualified tag as illegal AND every bare tag as
   method-less — two mutually exclusive codes, unsatisfiable by construction.
2. **"Convention line" DEFINED** (Provenance tags § — a four-condition
   mechanical test). v2.5 declared a bare convention line a defect and never
   said what a convention line is, which made the rule unenforceable and left
   14 lines of the first run genuinely un-adjudicable. **A spec may not forbid
   what it does not define.**
3. **The ≤45 bound RE-RULED and SPLIT by container class** (≤50 born_digital
   / ≤75 scan_ocr), with its unit pinned to the definition in (2). v2.5's
   bound counted nothing in particular: the run reported 88 convention lines
   and its lint reported 62, both honest. The run's own verdict is adopted —
   a collision doctrine that fires on every run of a source class is a
   mis-set constant, not a safety valve.
4. **Schema boundary section — NOT YET UPDATED. Still stale.** The v1-plain /
   v2-proposed split this prompt hard-codes was retired when config schema v2
   was ratified 2026-07-13b (future proposals mint `v3-proposed`). The debt is
   real, five sessions old, and was NOT paid here: rewriting a field
   enumeration requires reading `pipeline/pipeline_config_schema_v2.md`, which
   this session did not have. **Flagged rather than reconstructed from
   secondhand summaries.** Owed to v2.7.

Docketed for v2.7, NOT fixed here (both surfaced 2026-07-15, one evidence
point each — recorded so a future session does not re-derive them cold):
- **Chunk-plan rows may defer instead of chunking.** The Loeliger plan shipped
  7 rows reading `boundary_type: section` + `est_size: ~16,952 tok` +
  `notes: "split at numbered sections"` against a ruled 1,200-token fallback —
  a note saying "cut this later," not a cut. The spec was NOT ambiguous here;
  the run's own report never mentions it. **A conformance failure, not a
  specification gap** — the two need different fixes, and this one belongs to
  a lint (`boundary_type: section` with `est_size` > `chunk_fallback_max` is
  detectable by arithmetic). One artifact, one reader, no second witness: the
  next real run confirms or kills it.
- **A post-ratification session report as a deliverable.** The Loeliger run
  produced one on request and it is the highest-value document the run emitted
  — but only its "friction worth reporting upstream" section compounds across
  books. See v2.7 docket.

All v2.5 machinery retained. Version note for v2.4 → v2.5 preserved below.

Version note (v2.4 → v2.5, 2026-07-13): applies charter amendment v1.2
(ratified 2026-07-12), item 8 plus the item 2/3 consequences that touch
this stage. New: **mechanical ambiguity probe** in the structural read (ranked
watchlist, `[mechanical]`); **arbitration axis widened** (mode + `web_policy`
ruling + tiebreak preferences + ambiguity forecast; watchlist-driven
interview pass; operator leans captured per term and per ambiguity class);
new sidecar **`arbitration_seed_<slug>.md`** (`[discovery-forecast]`
provenance, harvest-arbitration boot state, NEVER in the brief); **chunk
plan as a deliverable** (new axis + `chunk_plan_<slug>.csv` sidecar —
retires the span-sizing reserved question per item 8); **exit-exam
extension** (every forecast names the in-source evidence that would confirm
or kill it — the surprise rate's denominator); provenance tag
`[discovery-forecast]` added; schema boundary updated (`residue_heuristics`
dissolved per item 2; `span_size`/`span_overlap` retired as constants).
Master-doc bound raised ≤250 → ≤300 to absorb the two new sections
(flagged in Deviations discipline below). All v2.4 machinery retained.
