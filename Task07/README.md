# Task 7 – Build a Module (K4)

**Run:**
```
python milkrate.py                 # runs the module directly -> prints the 3-row table
python use_milkrate.py             # imports it from a second script -> no table, calls payout()
python import_without_guard.py     # what goes wrong without the __main__ guard
python alternatives.py             # import cost
```
Complete-the-Code: both TODOs are done in `milkrate.py`; output matches the expected output exactly:
```
   10 L fat 3.5 snf 8.5 rate  30.00 pay   300.00
  8.5 L fat 4.2 snf 8.7 rate  33.40 pay   283.90
   12 L fat 3.1 snf 8.3 rate  27.80 pay   333.60
```

## Three import styles
| Statement | How you call it | Effect |
|---|---|---|
| `import milkrate` | `milkrate.payout(...)` | whole module under its own name; clear where a name comes from |
| `from milkrate import payout` | `payout(...)` | brings only that name into your script; shorter but may clash with your own names |
| `import milkrate as mr` | `mr.payout(...)` | module under a short alias |

## `if __name__ == "__main__":`
When a file is run directly, Python sets `__name__` to `"__main__"`; when it is imported, `__name__` is the module name (`"milkrate"`). So the code under the guard runs only when you run the file itself. **Without it**, importing the module executes the test table every time (see `import_without_guard.py`). That is why the table is **not printed** when `use_milkrate.py` imports `milkrate`.

## Standard modules
`math` (floor, ceil…) and `decimal` (exact money, from Task 2 onward) ship with Python – just `import` them.

## Where Python looks for a module
1. the folder of the running script (so `milkrate.py` in the same folder is found), 2. directories in `PYTHONPATH`, 3. the standard library and site-packages. The final list is `sys.path` (printed by `use_milkrate.py`).

## Alternative concept: copying the functions into every script
If copied into k scripts, a rate or rule change must be made in **k files** (and one forgotten copy gives different payments – the original problem). With a module: **1 file**. Import cost: the first `import` reads and compiles the file once (tens of µs, measured); later imports find it in `sys.modules` (sub-µs) – O(1) time per repeat import and one copy of the code in memory, instead of k copies.
