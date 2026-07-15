# Harvest brief — loeliger-til
WHAT COUNTS
- keyword: a named TIL word Ch.6 defines formally (Class:/Function:/Usage:), or Chs.1-5,7 teach as a word.
- concept: a named TIL mechanism taught in prose (threading, inner interpreter, dictionary header, vocabulary, mode).
NAMING WEATHER
- Keywords are ordinary English in caps: END, NEXT, DUP, CONSTANT, EXECUTE, FORGET, CURRENT, CODE, IF, ELSE, OK.
  Caps in code/example context = keyword; lowercase in prose = English. Never merge on surface form alone.
- Suffixes make DISTINCT words: `END` != `END,`. `:` `;` `;CODE` are keywords. Prefix `$` = routine ($CRLF, $KEY).
- Two CPUs (Z80 and 6800): same keyword, two code bodies. That is one keyword, not two.
NOISE THAT IS CONTENT
- `■` (~613x) is the book's PRINTED SYMBOL FOR ONE ASCII SPACE, not OCR noise. Source: "The only token separator
  is an ASCII space (■)". Preserve it — load-bearing in source examples.
- A quoted mnemonic = THAT KEY'S ASCII CODE, not the opcode: `CP "LD"` compares to the Line-Delete char, NOT the LD
  instruction. Same for "BS", "CR".
- `(HL)` vs `HL` is load-bearing (memory reference vs register). Text was repaired from `{HL}`; any stray `{...}`
  around a register is unrepaired damage — read as parens.
CONTENT THAT LOOKS LIKE NOISE
- Odd pages carry the chapter title as a running head; even pages carry "THREADED INTERPRETIVE LANGUAGES".
  Page furniture — never harvest as terms.
SKIP ON SIGHT
- Running heads/feet; the listing comment column where it merely restates the opcode.
LOCAL CITATION FORM
- `p:<printed page>` (number as shown in the running head). Figures: `fig:N.M`.
