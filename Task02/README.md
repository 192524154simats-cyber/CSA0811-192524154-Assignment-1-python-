# Task 2 – Explore Values and Types in the Interpreter (K4)

**Run (screenshot each):**
```
python explore_session.py            # replays the >>> session (or type the lines yourself in `python`)
python task2_decimal.py              # Complete-the-Code, TODO 1 done
python task2_decimal_from_float.py   # the "change to Decimal(float(amount))" experiment
python alternatives.py               # integer paise vs float+round vs Decimal
```

## Types (from the session)
| Expression | Type | Note |
|---|---|---|
| `10` | int | whole number |
| `10.0` | float | has a decimal point, so float |
| `"10"` | str | text; cannot be added to numbers |
| `True` | bool | a subclass of int: `True + True` is `2` (surprise) |
| `[10, 8.5]` | list | can hold mixed types |

## Division operators
- `7/2 = 3.5` true division, always float.
- `7//2 = 3` floor division.
- `7%2 = 1` remainder.
- `-7//2 = -4` (surprise): floor division rounds **down toward minus infinity**, not toward zero. So `-7%2 = 1`, keeping `(a//b)*b + a%b == a`.

## Why `0.1 + 0.2 == 0.3` is False
Computers store floats in binary. 0.1 and 0.2 have no exact binary form (like 1/3 in decimal), so each is stored as a very close value. Their sum is `0.30000000000000004`, which is not the stored value of 0.3. `Decimal("0.1") + Decimal("0.2") == Decimal("0.3")` is True because Decimal works in base 10.
(`sum([0.1]*10) == 1.0` shows True in Python 3.12 because the built-in `sum` uses compensated summation; a plain `+=` loop gives 0.9999999999999999. Don't rely on it.)

## Why money must not be float rupees
Small errors add up. 1,003 payments: float gives `33400.30000000061`, Decimal gives exactly `33400.30`. The bank counts exact paise, so the float total will differ "by a few paise" – this is the exact bug of the volunteer's calculator.
Alternatives: **integer paise** (3340 instead of 33.40), **round() after each step**, or **decimal module** (best; keeps the rupee form).

## Complete the Code result
Expected output reproduced:
```
float: 33400.30000000061
Decimal: 33400.30
False True
```
**After changing to `Decimal(float(amount))`:** total becomes `33400.29999999999857893118278`. Reason: `float("33.40")` is already inexact (it holds 33.39999999999999857891...), and Decimal faithfully copies that error. **Always build Decimal from the string, never from a float.**

## Alternative concept and complexity
| Method | Time per addition | Memory/value | Exact for n payments? |
|---|---|---|---|
| float | O(1), fastest | 24 bytes | No – error grows with n |
| float + round(…,2) each addition | O(1) (extra round call, slower) | 24 bytes | Looks right here, but not guaranteed (round of a binary approximation can misbehave at .xx5 values) |
| integer paise | O(1), fast | 28 bytes | **Yes**, always (ints are exact) |
| Decimal | O(1), slower than float | 104 bytes | **Yes**, always |

All are O(n) for n payments in time and O(1) extra space for the running total. Integer paise is the lightest exact method; Decimal is the most readable and has built-in rounding modes, so Decimal is chosen for this project. See `alternatives.py` output for your machine's timings.
