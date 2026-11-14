# Task 11 – Recommend and Defend the Final Design (K5)

**Run:** `python scale_check.py` (scale evidence), `python json_rate_card.py` (JSON alternative). Core code = `calculator.py` (same as Task 9).

## Recommended design
| Decision | Choice | Evidence from my experiments |
|---|---|---|
| Money type | `decimal.Decimal`, built from **strings** | Task 2: float total 33400.30000000061 vs exact 33400.30; `Decimal(float(x))` brings the error back |
| Step count | `round()` of (reading − standard)/0.1 (done in Decimal, so exact) | Task 4: `int()` gave rate 28.80 instead of 28.40 for fat 3.1 |
| Rounding rule | round **each payment** to the paisa, ROUND_HALF_UP; total = sum of paid amounts | Task 10: rounding only the total was off by 64.92 at 150,000 entries; float `round()` also wrong at half-paise |
| Constants | one rate card at the top of one module, imported everywhere | Task 3/7: 1 place to edit instead of k |
| Validation | string check, then range rules (litres > 0, fat 2.0–7.0, SNF 7.0–10.0) | Task 5/9: all 6 invalid cases rejected |
| Tests | `assert` tests + 5-entry hand total 2080.00 | Task 9: 15/15 pass in ~0.02 s |

## How a rate revision is carried out
Edit the constants (e.g. `BASE_RATE`) at the top of the rate-card module, run `python test_calculator.py` (expected values are recalculated by hand for the new rates and changed in the tests), commit to GitHub with a message such as "Rate revision 1 April: base 32.00", and distribute the one file. Nothing else contains a rate.

## Limitations
- Rates change only by editing code (fine for a few revisions a year, awkward for non-programmers).
- Assumed SNF limits (7.0–10.0) and maximum 200 L per shift are my assumptions – the co-operative must confirm them.
- Python's Decimal is about 4× slower than float (Task 10); acceptable but not the fastest.
- Single-threaded, no database or audit log; paying a farmer still needs bank-file output, not covered here.
- Seasonal rates and the bonus are not covered by this design (see Task 12 for the extension).

## Does it stay correct at district-union scale?
Correctness does not depend on n: every payment is computed independently in exact Decimal, so the answer for 3,000,000 entries per ten days (150,000 farmers × 20 entries) is exact. Measured speed is ~1.7 µs per entry, so 3,000,000 entries take about 5 s (estimate printed by `scale_check.py`); memory stays O(1) with a running total (Task 8). If the entries have to be stored for statements, ~3M tuples need a database or file streaming rather than one in-memory list.

## Alternative concept: rate card in a JSON file
```json
{"base_rate": "30.00", "fat_step_value": "0.40", ...}
```
- Start-up: reading and parsing the file takes ~0.1 ms **once** per run (O(size of file), tiny); space ~200 bytes for 5 values.
- Benefit: a revision = edit a text file, no code change or redistribution of the program; the same file can hold a season table (Task 12).
- Cost/risks: a typo in the file breaks the run at start-up (needs the validation the loader has: missing keys), the file must be kept with the program, and values must be stored as **strings** so Decimal stays exact (JSON numbers like 0.40 would become floats).
- My recommendation: keep constants in the module while rates change rarely (simple, version-controlled by GitHub); move to a JSON file when revisions become frequent or are done by non-programmers.
