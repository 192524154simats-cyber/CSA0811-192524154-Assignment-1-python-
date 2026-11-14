# Task 10 – Compare Expectations with Execution (K4)

**Run:** `python compare.py` and `python alternatives.py` (data is made with a fixed random seed, so the totals are the same on every machine; timings will differ).

## What I expected
- Float and Decimal totals would be nearly the same, with a tiny drift that grows with n.
- Rounding each payment or only the total would give the same answer.

## What happened (seed 2026, litres with 2 decimals as read from a scale)
| n | Decimal, round each payment (bank amount) | float, unrounded | float, round(…,2) each | Decimal, round only total |
|---|---|---|---|---|
| 300 | 221710.02 | 221709.867 (off 0.153) | 221709.92 (off 0.10) | 221709.87 (off 0.15) |
| 6,000 | 4183470.43 | 4183467.773 (off 2.657) | 4183467.87 (off 2.56) | 4183467.77 (off 2.66) |
| 150,000 | 106891834.56 | 106891769.637 (off 64.92) | 106891771.06 (off 63.50) | 106891769.64 (off 64.92) |

Time (typical): Decimal 0.5 ms / 9 ms / 240 ms; float 0.1 ms / 2 ms / 60 ms for 300 / 6,000 / 150,000 (both grow in proportion to n = O(n); Decimal is ~4× slower but 150,000 payments still take well under a second).

## Reasons for the differences (my expectation was partly wrong)
1. **Rounding policy matters much more than float error.** A farmer is paid whole paise for *each* payment, so the bank total is the sum of the **rounded** payments. Rounding only the total (or not rounding at all) loses/gains the fractions of paise: about half a paisa per payment on average, so the gap grows with n (0.15 → 2.66 → 64.92). That is the volunteer's "few paise" bug on a larger scale.
2. **Float `round()` is unreliable at half-paise.** A value like 7.625 is exact in decimal, but a float product may be stored as 7.62499999… and round down, while Decimal ROUND_HALF_UP gives 7.63. So even "float, rounded each" is off (0.10 at n = 300).
3. **Float's own representation error** (Task 2) adds a further tiny drift (1e-9 scale here), invisible next to reason 1 but still non-zero.
(If litres only had one decimal and rates are multiples of 0.10, products would already be exact in paise and the policies would not differ; the two-decimal scale readings and the Task 12 analyser readings make the policy important.)

**Conclusion:** use Decimal and round each payment half-up to the paisa; the ten-day total is the sum of the paid amounts.

## Alternative concept: a rate table (dictionary)
```python
table = {}
key = (fat_text, snf_text)
if key not in table: table[key] = rate_per_litre(...)
```
- Time per entry: dictionary lookup O(1) (average) versus recalculating the rate (step counts, Decimal arithmetic) – also O(1) but a larger constant. Measured for n = 150,000: ~230 ms recalculated vs ~95 ms with the table (the answers are identical).
- Extra space: O(k) for k distinct (fat, snf) pairs; here k ≤ 51 × 21 = 1,071 entries (about 100–200 KB), independent of n.
- Worth it when n is large and k is small, as at the district union. A rate revision must clear the table (stale rates are a risk).
