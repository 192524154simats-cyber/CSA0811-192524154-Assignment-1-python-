"""Task 3 - named constants, dynamic typing, multiple assignment, swapping."""
from decimal import Decimal

# ---- ONE place for every rate and limit (UPPER_CASE = "please do not change") ----
BASE_RATE = Decimal("30.00")
STD_FAT = Decimal("3.5")
STD_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP = Decimal("0.1")
FAT_MIN, FAT_MAX = Decimal("2.0"), Decimal("7.0")

print("Rate card:", BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE)

# ---- No true constants: Python lets you overwrite (only convention protects) ----
BASE_RATE = Decimal("99")      # legal! Python does not stop you
print("Overwritten (bad practice) BASE_RATE =", BASE_RATE)
BASE_RATE = Decimal("30.00")   # restore

# ---- Dynamic typing ----
x = 10
print("x =", x, type(x))
x = "ten"
print("x =", x, type(x), " (same name, new type - no error)")
try:
    print(x + 5)
except TypeError as e:
    print("But mixing them fails at run time ->", e)

# ---- Multiple assignment and swap ----
litres, fat, snf = 8.5, 4.2, 8.7
print("litres, fat, snf =", litres, fat, snf)
a, b = 1, 2
a, b = b, a
print("after swap a, b =", a, b)
