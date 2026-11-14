# Task 5 – Read Input and Convert Types (K3)

**Run:** `python read_input.py` (demo with ready-made typed values) · `python read_input.py --live` (you type, via `input()`) · `python alternatives.py`

## Why input() always returns a string
Whatever the clerk types (`8.5`), `input()` gives the text `"8.5"`. You must convert: `int("8")` → 8, `float("8.5")` → 8.5 (we use `Decimal("8.5")` for money-related values). Without conversion, `"8.5" * 2` gives `"8.58.5"` and `"8.5" + 1` is an error.

## What happens with "8,5" or "eight"
`float("8,5")` and `float("eight")` raise `ValueError: could not convert string to float`. The program would crash in front of the clerk, so the entry must be checked first.

## Checking before converting (string methods)
`is_number(text)`: strip spaces, allow at most one `.`, remove it, then test `.isdigit()`. `"8.5"` ✔, `"8,5"` ✘ (comma), `"eight"` ✘, `"8.5.1"` ✘ (two dots), `""` ✘. Message tells the clerk what to fix.

## Formatted output with f-strings
`f"{amount:8.2f}"` = width 8, 2 decimals, right-aligned; `{farmer:<6}` left-aligned. This makes the columns line up in the report.

## Alternative concept: try/except
```python
try:
    value = float(text)
except ValueError:
    print("invalid")
```
| Input | string check | try/except |
|---|---|---|
| "8.5" | valid | valid |
| "8,5" | invalid | invalid |
| "eight" | invalid | invalid |
| "-3" | invalid (no sign allowed) | **valid** – negative passes, need a separate rule |
| "1e3", "nan", "inf" | invalid | **valid** (float accepts them!) |

Time per entry is O(length of text) = O(1) for short entries in both; try/except is faster when the input is valid and slower when it is invalid (raising an exception costs more) – see measured µs. Space is O(1). The string check is stricter and gives clearer control (e.g. rejects "nan"); try/except is shorter and handles more number formats, but accepts surprises. Recommended: string check (or try/except followed by range checks) for this project.
