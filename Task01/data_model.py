"""Task 1 - Identify the data: constants, types, validation rules, and the
alternative design (separate variables vs one tuple per entry)."""
import sys
import time
from decimal import Decimal

# ---- Named constants (never change during a run) ----
BASE_RATE = Decimal("30.00")      # Rs/litre at 3.5% fat and 8.5% SNF
STD_FAT = Decimal("3.5")
STD_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")  # Rs per 0.1% fat
SNF_STEP_VALUE = Decimal("0.30")  # Rs per 0.1% SNF
STEP = Decimal("0.1")
FAT_MIN, FAT_MAX = Decimal("2.0"), Decimal("7.0")
SNF_MIN, SNF_MAX = Decimal("7.0"), Decimal("10.0")   # assumption
LITRES_MAX = Decimal("200")                          # assumption per shift

# ---- One entry = one tuple (farmer_id:str, litres:Decimal, fat:Decimal, snf:Decimal, shift:str)
entry = ("F001", Decimal("8.5"), Decimal("4.2"), Decimal("8.7"), "M")
print("One entry as a tuple :", entry)
print("Types                :", [type(v).__name__ for v in entry])

def is_valid(litres, fat, snf):
    """True if the entry satisfies every payment rule."""
    return 0 < litres <= LITRES_MAX and FAT_MIN <= fat <= FAT_MAX and SNF_MIN <= snf <= SNF_MAX

print("valid(8.5,4.2,8.7)   :", is_valid(*entry[1:4]))
print("valid(-1,4.2,8.7)    :", is_valid(Decimal("-1"), Decimal("4.2"), Decimal("8.7")))
print("valid(8,9.0,8.7)     :", is_valid(Decimal("8"), Decimal("9.0"), Decimal("8.7")))

# ---- Alternative concept: separate variables vs list of tuples ----
print("\n--- Separate variables (litres1, fat1, snf1, ...) for 300 farmers ---")
src = "\n".join(f"litres{i}, fat{i}, snf{i} = 10, 3.5, 8.5" for i in range(1, 301))
print("Lines needed just to create the variables:", len(src.splitlines()))
print("Names to type in the total (3 per farmer):", 300 * 3, "-> code grows with n, must be edited for 301 farmers")

def total_with_loop(entries):
    total = 0
    for litres, fat, snf in entries:
        total += litres * 3.5
    return total

for n in (300, 6000, 150000):
    data = [(10.0, 3.5, 8.5)] * n
    t0 = time.perf_counter()
    total_with_loop(data)
    t1 = time.perf_counter()
    print(f"n={n:>7}: loop over list of tuples took {(t1-t0)*1000:8.3f} ms, list size ~{sys.getsizeof(data)} bytes (+ tuples)")
