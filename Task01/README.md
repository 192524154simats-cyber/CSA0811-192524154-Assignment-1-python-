# Task 1 – Understand the Problem and Identify the Data (K4)

**Run:** `python data_model.py`

## 1. What the program must do (simple words)
For every farmer, every shift, the clerk types litres, fat % and SNF %. The program finds the **rate per litre**, then the **amount** to pay, and after 10 days adds everything into a **ten-day total** for each farmer. Every payment must be right to the paisa.

## 2. Inputs and outputs
| Kind | Name | Meaning | Type | Why this type |
|---|---|---|---|---|
| Input | farmer_id | e.g. "F001" | text (str) | It is a label, we never do arithmetic on it; may have letters / leading zeros |
| Input | litres | milk quantity | fractional (Decimal) | 8.5 L is normal; money depends on it, so exact |
| Input | fat % | e.g. 4.2 | fractional (Decimal) | Read from a tester; must not carry float error |
| Input | SNF % | e.g. 8.7 | fractional (Decimal) | same |
| Input | shift | "M" / "E" | text | Only two labels |
| Output | rate per litre | Rs/litre | Decimal (2 places) | money |
| Output | amount | litres × rate | Decimal (2 places) | money, paid to bank |
| Output | ten-day total | sum of 20 amounts | Decimal (2 places) | money |
| Counter | number of steps | (fat−3.5)/0.1 | whole number (int) | steps are counted in whole units |

## 3. Named constants (never change during a run)
`BASE_RATE = 30.00`, `STD_FAT = 3.5`, `STD_SNF = 8.5`, `FAT_STEP_VALUE = 0.40`, `SNF_STEP_VALUE = 0.30`, `STEP = 0.1`, `FAT_MIN/FAT_MAX = 2.0/7.0`, `SNF_MIN/SNF_MAX`, `LITRES_MAX`.
**Why constants:** the problem said "rates are typed in several places, so a revision was applied only partly". One name, one place = one edit.

## 4. Whole / fractional / text
- Whole numbers (int): step counts, number of entries, days (10).
- Fractional: litres, fat, SNF, rates, amounts (use `Decimal`, not float – see Task 2).
- Text: farmer ID, shift, the clerk's raw typing (input() always gives text).

## 5. Rules every correct payment must satisfy
1. litres > 0 (a negative or zero quantity is not milk). Upper limit assumed 200 L per shift (a typing slip like 8500 is caught).
2. 2.0 ≤ fat ≤ 7.0 (given in the problem; outside means tester fault / adulteration).
3. SNF within 7.0 – 10.0 (**assumption**, the problem gives no SNF limit but SNF must not be absurd).
4. Fat and SNF must be numbers (not "eight", not "8,5").
5. The amount is rounded **to paise once per payment** and the ten-day total is the sum of those rounded payments (the bank pays each amount in paise).

## 6. Assumptions
- Shift is "M" (morning) or "E" (evening); 10 days × 2 shifts = up to 20 entries per farmer.
- Fat/SNF are typed with one decimal (two decimals in Task 12).
- Rounding rule: half-up to the paisa.

## 7. Alternative concept – three separate variables per farmer
For 300 farmers you would write `litres1, fat1, snf1 = ...` up to `litres300, fat300, snf300` (900 names), and the total would be a 300-term expression `payout(litres1,fat1,snf1)+payout(litres2,...)+...`. For 6,000 farmers it is 18,000 names; for 150,000 farmers 450,000 names – and a 301st farmer needs the **program to be edited**.

| | Separate variables | List of tuples |
|---|---|---|
| Time to process n entries | O(n) to run, but you must *write* O(n) lines by hand | O(n) with one 3-line loop |
| Space | O(n) names + O(n) values | O(n) values |
| Code size | grows with n | constant (same 3 lines for any n) |
| Can be looped / sorted / filtered | No (names can't be iterated) | Yes |

Both use O(n) memory for the data itself, but only the list design has **O(1) code size**, so it scales to 150,000 farmers. Run `data_model.py` to see the measured loop times.
