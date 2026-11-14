# Task 6 – Organise the Logic into Functions (K3)

**Run:** `python functions.py` and `python alternatives.py`

## Functions, parameters, return values
| Function | Parameters | Returns | Job |
|---|---|---|---|
| `to_paise(value)` | Decimal | Decimal (2 places) | one rounding rule used everywhere (half-up) |
| `steps(reading, standard)` | two Decimals | int | counts 0.1% steps from the standard |
| `rate_per_litre(fat, snf)` | two Decimals | Decimal | price per litre |
| `payout(litres, fat, snf)` | three Decimals | Decimal | amount for one entry |
| `ten_day_total(entries)` | list of (litres, fat, snf) | Decimal | sum of payouts |
| `show_payout(...)` | three Decimals | None | **prints** one line |

## Returning vs printing
`payout()` **returns** a value that can be stored, added, tested. `show_payout()` only **prints** and returns `None` (the demo prints `None`). Calculation functions should return; only the outer program prints, so the same function works in tests (Task 9) and reports.

## Local and global names
`BASE_RATE` etc. are global; functions may **read** them freely. Assigning `BASE_RATE = ...` inside a function creates a new **local** name and leaves the global unchanged (shown in the demo: global stays 30.00), so a "rate change" inside a function would silently do nothing. Rates are changed only at the top of the module (or with `global`, which we avoid).

## Docstrings
Every function has a docstring (first line inside the function); `help(payout)` shows it.

## Alternative concept: one long script / lambda
- **One long script**: the step/rate/rounding code is copied wherever it is needed – k copies mean k places to fix a rule error, and no reusable tests.
- **lambda**: `lam = lambda l, f, s: payout(l, f, s)` is fine for tiny one-line jobs, but it has no docstring, a nameless traceback, and only one expression.
- **Speed**: function-call overhead is about 0.1 µs – negligible compared with the Decimal arithmetic. In the output, the inline script is not faster (it was even slower because it rebuilds Decimal constants each iteration). All three are O(n) time and O(1) extra space; the cost of functions is not noticeable even for 150,000 entries, so choose them for clarity and reuse.
