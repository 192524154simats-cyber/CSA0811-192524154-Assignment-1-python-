# Task 12 – Re-evaluate and Adapt the Design (K5, Day-4 Design Challenge)

**Run (screenshot each):**
```
python evaluate_original.py   # Part B: what the old design does with the new readings
python milkrate_v2.py         # Part C: the new design, small demo
python test_v2.py             # Part D: 22 tests for both seasons and the bonus
```
**Decision: MODIFY.** Keep the structure (one rate-card module, same function names, Decimal, round each payment half-up); change how steps are counted, how the rate card is chosen, and add a bonus function.

---
## A. Impact Analysis
**What changed**
1. Fat/SNF now have **two decimals** (4.25, 8.63) from an analyser.
2. **Seasonal rate card** (April–June: base 32.00, fat step 0.45, SNF step 0.30; other months: 30.00 / 0.40 / 0.30).
3. **Ten-day bonus**: Rs 0.50 on *all* litres if the ten-day litres are strictly more than 500 (exactly 500 gets nothing); applies in both seasons; added to the ten-day total.

**What is affected**
| Part of design | Affected? | How |
|---|---|---|
| Constants `BASE_RATE`, `FAT_STEP_VALUE` | **Yes** | now two sets (normal, seasonal); `SNF_STEP_VALUE` is the same in both but kept inside each card so the card is complete |
| New constants | added | `SEASONAL_MONTHS`, `BONUS_THRESHOLD_LITRES = 500`, `BONUS_PER_LITRE = 0.50` |
| Step expression `round((fat-3.5)/0.1)` | **Yes** | with two decimals a reading can lie *between* steps: 4.25 is 7.5 steps. Rounding to a whole step throws away up to 0.05 % (Rs 0.20 per litre normal, Rs 0.225 seasonal). I use the **exact fractional step count** in Decimal (each 0.01 % is worth a tenth of a step value) |
| `rate_per_litre(fat, snf)` | **Yes** | needs a season / rate card |
| `payout(...)` | **Yes** | passes the season |
| `ten_day_total(...)` | **Yes** | needs each entry's month and the ten-day litres to decide the bonus |
| New function | `season_of(month)`, `get_rate_card(season)`, `bonus(total_litres)` | |
| Rounding | **Yes** | fractional steps create values like 35.765 → rounding rule (half-up) now matters for the rate itself, not only for the amount |
| Validation | No change (2.0–7.0 etc.); inputs may carry 2 decimals | |

---
## B. Evaluation of the Original Design (output of `evaluate_original.py`)
Original = float arithmetic, `round()` steps, one rate card.

| fat / SNF | float steps | `round()` gives | true steps | old rate | true rate (normal) |
|---|---|---|---|---|---|
| 4.25 / 8.63 | 7.5 | 8 | 7.5 | 33.50 | **33.39** |
| 4.35 / 8.63 | 8.499999999999996 | 8 | 8.5 | 33.50 | **33.79** |
| 4.45 / 8.63 | 9.500000000000002 | 10 | 9.5 | 34.30 | **34.19** |
| 3.74 / 8.50 | 2.400000000000002 | 2 | 2.4 | 30.80 | **30.96** |

Findings:
- **Constants:** a single `BASE_RATE` cannot hold two seasons → not appropriate. (The *idea* of named constants in one module remains right.)
- **Functions:** the `round()` step rule breaks: 4.25 rounds *up* (banker's rounding, 7.5 → 8) while 4.35 rounds *down* (float error: 8.4999… → 8) – the same kind of half-step reading is treated inconsistently, and rates are wrong by up to Rs 0.29 per litre (hundreds of rupees across a farmer's ten-day milk). 
- **Float arithmetic:** again unsafe (Task 2 and 10).
- **Module structure:** a module with rate functions is still the right shape; only its content changes.
- **Bonus:** the original functions see one entry at a time and cannot know the ten-day litres → needs a new function.
So: retain the module idea, names and Decimal/rounding policy; **modify** constants, step rule and functions. A full redesign is not needed.

---
## C. Adaptation (code in `milkrate_v2.py`)
- `RATE_CARDS = {"normal": {...}, "seasonal": {...}}` – a dictionary of rate cards, all values `Decimal` from strings; one place to revise each card.
- `season_of(month)` → `"seasonal"` for 4–6 else `"normal"`; `get_rate_card(season)` selects the card.
- `steps(reading, standard)` = `(reading − standard) / 0.1` in Decimal – exact and possibly fractional.
- `rate_per_litre(fat, snf, season="normal")` – season passed as a parameter (default keeps old calls working); result rounded half-up to paise.
- `payout(litres, fat, snf, season)` – litres × rate, rounded half-up.
- `bonus(total_litres)` – separate function: `0.00` unless litres **> 500**, then `litres × 0.50` for **all** litres.
- `ten_day_total(entries)` – entries carry `(litres, fat, snf, month)`; the season is chosen per entry's month; it keeps **running totals** of the amount and the litres (O(1) memory), then adds `bonus(total_litres)` once at the end.
Assumption: the season is decided by the month of each entry (a ten-day period crossing 31 March/1 April therefore uses both cards, tested below).

---
## D. Evidence-Based Defence (`test_v2.py`, 22 / 22 pass)
| Area | Test | Expected | Result |
|---|---|---|---|
| Normal season | 4.25 / 8.63 | 30 + 7.5×0.40 + 1.3×0.30 = 33.39 | PASS |
| Seasonal | 4.25 / 8.63 | 32 + 7.5×0.45 + 1.3×0.30 = 35.765 → **35.77** | PASS |
| Seasonal | 4.0 / 8.5 ; 3.5 / 9.0 ; 3.1 / 8.3 | 34.25 ; 33.50 (SNF step still 0.30) ; 29.60 | PASS |
| Payout | 10 L at 4.25 / 8.63 | normal 333.90 ; seasonal 357.70 | PASS |
| Bonus boundary | 499.99 / 500 / 500.01 / 501 L | 0.00 / 0.00 / 250.01 / 250.50 | PASS |
| Ten days Nov | 500 L exactly | 15000.00 (no bonus) | PASS |
| Ten days Nov | 501 L | 15030.00 + 250.50 = 15280.50 | PASS |
| Ten days May | 501 L | 14400 + 1632 + 250.50 = 16282.50 | PASS |
| Across March/April | 600 L | 9000 + 9600 + 300 = 18900.00 | PASS |

**Trade-offs and why this decision**
- *Exact fractional steps vs rounding to a whole step:* fractional steps pay the farmer for what the analyser measured, and are exact in Decimal; the cost is rates with 3 decimals before rounding (35.765), so the rounding rule (half-up) must be fixed in writing. If the union prefers "nearest whole step", change only `steps()`.
- *Dictionary of rate cards vs if/else:* a third season is one more dictionary entry and one more month tuple; the formula is written once. Cost: a tiny dictionary lookup per entry (O(1)).
- *Running totals vs storing all entries:* the bonus needs the **total litres of the period**, but not each entry, so two running totals are enough (O(1) space). Entries must still be stored if a per-day statement is printed.
- *Bonus as a separate function:* it can be tested alone (boundary 500) and changed without touching the rate code.
- *Not redesigned:* Decimal, the module, input validation and tests from the original design all survived unchanged in idea – that is evidence the original structure was sound; only the data it was built around had to be extended.
