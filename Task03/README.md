# Task 3 – Choose Variables and Name the Constants (K3)

**Run:** `python constants_demo.py` and `python alternatives.py`

## Naming rules
- Letters, digits, underscore; cannot start with a digit; no spaces; not a keyword (`if`, `for`, `class`…); case-sensitive (`Fat` ≠ `fat`).
- Convention (PEP 8): `snake_case` for variables/functions (`fat_steps`, `rate_per_litre`), `UPPER_CASE` for constants (`BASE_RATE`), names that tell the meaning (`FAT_STEP_VALUE`, not `x2`).

## Why Python has no true constants
Python has no `const` keyword. `BASE_RATE = 99` later in the program is legal. So we depend on the **UPPER_CASE convention** and on keeping all constants together at the top of one module (Task 7). `constants_demo.py` shows the overwrite being accepted.

## Dynamic typing
A name just points to an object. `x = 10` then `x = "ten"` works; the *object* has a type, not the name. Danger: `x + 5` now fails at run time with `TypeError`. That is why Task 5 checks input types explicitly.

## Multiple assignment and swapping
`litres, fat, snf = 8.5, 4.2, 8.7` assigns three names in one line. `a, b = b, a` swaps without a temporary variable (right side is evaluated fully first).

## The constants chosen
`BASE_RATE=30.00`, `STD_FAT=3.5`, `STD_SNF=8.5`, `FAT_STEP_VALUE=0.40`, `SNF_STEP_VALUE=0.30`, `STEP=0.1`, `FAT_MIN=2.0`, `FAT_MAX=7.0`. A rate revision = change one line.

## Alternative concept and complexity
| Design | Places to edit on a rate revision | Time | Memory |
|---|---|---|---|
| Magic numbers in expressions | **k** places (every copy; the "partly applied" bug) | O(1) per use | no storage |
| `RATE_CARD` dictionary | **1** place | O(1) per use, slightly slower (hash lookup each time) | one small dict (~200 bytes) |
| Named constants | **1** place | O(1) | 3 names |

Running time and memory change only by a tiny constant factor (see `alternatives.py` output); the real difference is **maintenance**: k edits versus one. The dictionary is a good choice when rate cards need to be switched (seasons, Task 12).
