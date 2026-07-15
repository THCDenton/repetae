# Harvest brief — little-schemer

WHAT COUNTS (one line per type):
- primitive: a built-in named as given (car, cdr, cons, null?, atom?, eq?, zero?, add1, sub1, number?).
- special_form: define, lambda, cond, quote, and, or.
- defined_function: any function the text builds via (define <name> ...) or Q&A derivation (rember, insertL, multirember, eqlist?, evens-only*, ...).
- law: a "The Law of X" framed box (Car/Cdr/Cons/Null/Eq) — a stated rule about a primitive.
- commandment: a "The Nth Commandment" framed box — a numbered recursion-technique rule.
- concept: taught vocabulary (atom, S-expression, list, recursion, accumulator).

NAMING WEATHER:
- Trailing * is significant: rember vs rember* are DIFFERENT entities (list-of-lists variant).
- Suffixes -f / -g mark higher-order variants (insertL-f, insert-g) — distinct entities.
- Functions are revised across chapters; capture each definition, let MERGE consolidate.

NOISE vs CONTENT:
- Parenthesized S-expressions are CONTENT, never noise (even the TOC is written this way).
- OCR lies in code: "( cdr" means "(cdr"; "atom ?" means "atom?"; "}" / "{" in nested lists mean ")" / "(". Repair, don't drop.
- Ruled horizontal lines between Q&A are layout furniture — ignore. There are NO real captioned figures.

SKIP ON SIGHT:
- Index, Intermission/bibliography, front matter, decorative drawings.

LOCAL CITATION FORM:
- Cite by PRINTED page number (the one in the book). Resolver maps printed -> physical via +16.
