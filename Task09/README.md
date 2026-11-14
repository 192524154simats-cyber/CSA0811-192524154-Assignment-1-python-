# Task 9 – Implement and Test the Calculator (K3)

**Run:**
```
python calculator.py            # demo with good and bad entries
python calculator.py --live     # type entries yourself (blank litres to finish)
python test_calculator.py       # assert tests + the test table (take this screenshot)
python alternatives.py          # manual vs automatic testing time
```
Design: `Decimal` money, rate card constants at top, `parse_entry()` validates (text, negative, fat/SNF range, litres range), `rate_per_litre()`, `payout()`, `ten_day_total()`; each payment rounded to the paisa (half-up) before being added.

## Test table (printed by `test_calculator.py`; all 15 PASS)
| Case | Input | Expected rate / pay | Why (by hand) |
|---|---|---|---|
| fat above, snf above | 8.5 L, 4.2, 8.7 | 33.40 / 283.90 | 30 + 7×0.4 + 2×0.3 |
| fat below, snf below | 12 L, 3.1, 8.3 | 27.80 / 333.60 | 30 − 4×0.4 − 2×0.3 |
| fat above, snf below | 10 L, 4.0, 8.0 | 30.50 / 305.00 | 30 + 5×0.4 − 5×0.3 |
| fat below, snf above | 10 L, 3.0, 9.0 | 29.50 / 295.00 | 30 − 5×0.4 + 5×0.3 |
| standard | 10 L, 3.5, 8.5 | 30.00 / 300.00 | no steps |
| lowest fat | 10 L, 2.0, 8.5 | 24.00 / 240.00 | 30 − 15×0.4 |
| highest fat | 10 L, 7.0, 8.5 | 44.00 / 440.00 | 30 + 35×0.4 |
| half paisa | 0.25 L, 4.0, 8.0 | 30.50 / 7.63 | 7.625 rounds up |
| invalid: text, "4,2", −5, 0, fat 1.9, fat 7.1 | | rejected | rules of Task 1 |
| 5-entry set | 10/3.5/8.5, 8.5/4.2/8.7, 12/3.1/8.3, 20/2.0/8.5, 15/7.0/9.0 | total **2080.00** | 300.00 + 283.90 + 333.60 + 480.00 + 682.50 |

## Alternative concept: testing by typing inputs by hand
Manual: type every input, compare with a paper list, repeat after every change. About 4 minutes for 15 cases (estimated), grows with the number of tests k and depends on a human – errors and skipped cases are likely. With `assert` tests: all cases run in ~0.02 s every time (measured), and a failing assert names the case. Time to re-run: O(k) computer-time for the machine versus O(k) *human*-time for the manual way, with a constant millions of times larger. Tests are also kept in the repository as proof for the evaluator.
