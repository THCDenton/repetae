# Arbitration seed — loeliger-til

Boot state for the harvest arbitration layer. Rung 2 of the tiebreak ladder
(discovery conventions + forecast). **In-source evidence outranks every seed, always.**
NEVER injected into the harvest brief or any worker packet.

Operator tiebreak preference for the dominant class ("TIL keyword drawn from ordinary
English"): **reservation-tolerant — let harvest decide** [operator-decided]. Seeding is
therefore deliberately sparse: only entries whose lean or evidence justifies pre-opening.

---

## END — fan-out  [discovery-forecast]
- Surface form: `END` (and the distinct form `END,`)
- Expected shape: **fan-out** [operator-decided: expected fan-out]
- TOC-derived home ranges: `p:39-74` (ch4, §4.4.1 BEGIN...END) | `p:103-182` (ch6 dictionary)
- Senses in evidence: (a) loop-terminating keyword, `BEGIN ... END`; (b) `END,` — a distinct
  comma-suffixed keyword that encloses the relative jump byte; (c) English "end".
- Mechanical signal: freq 78, dispersion 8, collision 8.55 [mechanical]
- **Exit-exam evidence:** CONFIRMED if Ch.6 contains separate dictionary entries for `END`
  and `END,` (each with its own `Class:` line). KILLED if Ch.6 has exactly one entry whose
  Function: text covers both forms, or if `END,` proves to be an OCR artifact of `END`.

## NEXT — watch  [discovery-forecast]
- Surface form: `NEXT`
- Expected shape: **watch** — no sense pre-opened.
- Operator lean: **none recorded** (answered "no opinion"; not mapped to the session's lean).
- TOC-derived home ranges: `p:9-28` (ch2) | `p:29-38` (ch3, inner interpreter) |
  `p:75-102` (ch5) | `p:103-182` (ch6)
- Senses in evidence: (a) the inner-interpreter routine — p:20 "When NEXT completes, it falls
  through to the routine called RUN"; (b) a keyword the user types that compiles a jump to
  that routine — p:22 `HEX ■ CREATE ■ DROP ■ E1 ■ C, ■ NEXT ■■OK`; (c) English "next".
- Mechanical signal: freq 116, dispersion 7, collision 7.44 [mechanical]
- **Exit-exam evidence:** CONFIRMED as fan-out if Ch.6 carries a `NEXT` entry whose Function:
  describes the compiled jump while Ch.3/Ch.5 prose defines the routine itself as a separate
  named thing. KILLED if Ch.6's `NEXT` entry and the Ch.3 routine prose describe one
  indivisible thing, making (a)/(b) a single sense viewed from two angles.

---

**Not seeded** (watchlist entries left entirely to harvest, per the reservation-tolerant
class preference): CONSTANT, DUP, EXECUTE, FORGET, CURRENT, CODE, IF, ELSE, OK, SEMI,
SEARCH, ASCII, BASIC, Z80.

**Excluded from the watchlist as probe artifacts, not terms** [mechanical]: THREADED,
INTERPRETIVE, LANGUAGES — these rank high (freq 124-125, dispersion 10) solely because they
are the verso running head on every even page. TIL (freq 227) is the book's subject; high
dispersion is expected and carries no ambiguity signal.
