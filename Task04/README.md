# Task 4 – Write Correct Expressions (K4)

**Run:** `python expressions.py` and `python alternatives.py`

## The expressions used in the project
```
fat_steps  = round((fat - STD_FAT) / STEP)          # whole number of 0.1% steps
snf_steps  = round((snf - STD_SNF) / STEP)
rate       = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
amount     = round(litres * rate, 2)
valid      = 2.0 <= fat <= 7.0 and litres > 0
```

## Precedence and associativity (simple words)
- `**` first, then unary minus, then `* / // %`, then `+ -`, then comparisons, then `not`, `and`, `or`.
- `2 ** 3 ** 2 = 512` because `**` groups from the **right**; `10 - 4 - 3 = 3` because `-` groups from the **left**.
- `-2 ** 2 = -4` (not 4) because `**` is stronger than the unary minus. Use `(-2) ** 2` for 4.
- In `rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + ...` multiplication happens before addition, so no brackets are needed.

## Three (here five) surprising results
1. `(4.2 - 3.5) / 0.1` gives `7.000000000000002`, not 7.0: 4.2, 3.5 and 0.1 are not exact in binary. Using this directly as "number of steps" is wrong; `round()` gives the correct whole number 7.
2. `(3.1 - 3.5) / 0.1` gives `-3.999999999999999`. Truncating with `int()` would give −3 (wrong, should be −4).
3. `round(2.5)` is 2 and `round(3.5)` is 4 – Python rounds half to the nearest **even** number ("banker's rounding"). `round(2.675, 2)` is 2.67 because 2.675 is stored slightly below 2.675. Both matter for money, which is why Decimal with ROUND_HALF_UP is used in the final design.
4. `0.1 * 3 = 0.30000000000000004`.
5. `-2 ** 2 = -4`.

## round() vs int() vs math.floor() for negatives
| x | round | int (cuts toward 0) | floor (toward −∞) |
|---|---|---|---|
| 2.7 | 3 | 2 | 2 |
| −2.7 | −3 | −2 | −3 |
| −3.999999999999999 | −4 | **−3** | −4 |
`int` and `floor` differ for negative numbers; only `round` gives the nearest step.

## Comparison chaining and Boolean operators
`2.0 <= fat <= 7.0` means `2.0 <= fat and fat <= 7.0` (fat is evaluated once). `and`/`or` short-circuit: `True or 1/0` never evaluates `1/0`. `not` reverses a result.

## Alternative concept: int() or floor() instead of round()
| fat | raw steps | round | int | floor | rate (SNF 8.5) |
|---|---|---|---|---|---|
| 4.2 | 7.000000000000002 | 7 | 7 | 7 | 32.80 in all three |
| 3.1 | −3.999999999999999 | −4 | **−3** | −4 | round 28.40, **int 28.80 (wrong)**, floor 28.40 |

`int()` is wrong for fat 3.1 (+Rs 0.40 per litre error). `floor()` happened to be right here but is wrong whenever float error lands slightly *above* a whole number on the negative side (and for fat 4.2 when the error goes below 7.0, e.g. 6.999999 → 6). Only `round()` is safe because the true value is always a whole number plus a tiny error. All three are O(1) time and O(1) space; the speed difference (see output) is negligible.
