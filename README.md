# CSA08-<RegisterNumber>-Assignment1 – Ksheera Village Milk Producers' Co-operative

| | |
|---|---|
| Name | `<your name>` |
| Register number | `<your register number>` |
| Python version | 3.12 |
| Libraries | none to install – only the Python standard library (see `requirements.txt`) |
| GitHub link | `<paste your repository link here>` |

> Replace the `<...>` parts, and rename the folder to `CSA08-<RegisterNumber>-Assignment1` before pushing.

## How to use this folder
1. Open the folder in VS Code (File → Open Folder).
2. Open a terminal (Ctrl + `), go into a task folder, run the commands below, and take a screenshot of each output.
3. Upload the screenshots into the matching task folder on GitHub.
4. Commit **one task at a time** (e.g. `git add Task01 && git commit -m "Task 1: data analysis"`) – the evaluator checks the commit history.

Every task folder has a `README.md` with the written answers (definitions, discussion, the *Alternative Concept and Complexity Analysis*) and the Python files for that task. Optional: `python run_all.py` runs everything in one go.

## Commands and what each task shows
| Task | Folder | Run (inside the folder) | Result |
|---|---|---|---|
| 1 Understand the data | Task01 | `python data_model.py` | inputs/outputs/constants/rules; separate variables vs tuples |
| 2 Values and types | Task02 | `python explore_session.py` · `python task2_decimal.py` · `python task2_decimal_from_float.py` · `python alternatives.py` | `>>>` session; float 33400.30000000061 vs Decimal 33400.30 |
| 3 Constants | Task03 | `python constants_demo.py` · `python alternatives.py` | naming, dynamic typing, swap; magic numbers vs constants vs dict |
| 4 Expressions | Task04 | `python expressions.py` · `python alternatives.py` | precedence, surprises, round/int/floor |
| 5 Input | Task05 | `python read_input.py` (or `--live`) · `python alternatives.py` | validation, f-string formatting, try/except comparison |
| 6 Functions | Task06 | `python functions.py` · `python alternatives.py` | rate_per_litre, payout, ten_day_total, scope |
| 7 Module | Task07 | `python milkrate.py` · `python use_milkrate.py` · `python import_without_guard.py` · `python alternatives.py` | expected 3-row table; `__main__` guard |
| 8 Algorithm | Task08 | `python trace.py` · `python alternatives.py` | pseudocode, flowchart (in README), hand trace; list vs running total |
| 9 Calculator + tests | Task09 | `python calculator.py` · `python test_calculator.py` · `python alternatives.py` | 15/15 tests PASS, 5-entry total 2080.00 |
| 10 Compare | Task10 | `python compare.py` · `python alternatives.py` | float vs Decimal at 300 / 6,000 / 150,000; timings; rate table |
| 11 Final design | Task11 | `python scale_check.py` · `python json_rate_card.py` | scale evidence; JSON rate card |
| 12 Design challenge | Task12 | `python evaluate_original.py` · `python milkrate_v2.py` · `python test_v2.py` | seasons, two-decimal readings, bonus, 22/22 PASS |

## Short result note per task
1. Identified 5 inputs, 3 outputs, named constants and 5 validation rules; list/tuple design scales, separate variables do not.
2. Float total drifts (33400.30000000061); Decimal built from strings is exact; Decimal(float) brings the error back.
3. All rates in one place as UPPER_CASE constants; dynamic typing and swapping demonstrated.
4. `round()` gives the correct step count; `int()` fails for fat 3.1; three+ surprises explained.
5. `input()` gives text; string check rejects "8,5" and "eight" before conversion.
6. Small functions with docstrings; return vs print and local vs global shown.
7. `milkrate.py` module gives the expected output; import style and `__main__` guard shown.
8. Pseudocode, flowchart and hand trace match `trace.py` (917.50).
9. Working Decimal calculator; 15 tests pass.
10. Rounding policy mattered most (off by 64.92 at 150,000 entries); Decimal ~4× slower than float but fast enough.
11. Recommended Decimal + round each payment + one rate-card module; scales to the district union.
12. Modified design: seasonal rate cards, fractional steps, separate bonus function; 22 tests pass.
