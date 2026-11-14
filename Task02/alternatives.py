"""Task 2 alternative: integer paise, float+round, Decimal - speed, memory, exactness."""
import sys, time
from decimal import Decimal

N = 100_000
payments = ["33.40"] * N + ["0.10"] * 3
exact = Decimal("33.40") * N + Decimal("0.30")

def t(f):
    s = time.perf_counter(); r = f(); return r, time.perf_counter() - s

def by_float_round():
    tot = 0.0
    for a in payments: tot = round(tot + float(a), 2)
    return tot

def by_float_plain():
    tot = 0.0
    for a in payments: tot += float(a)
    return tot

def by_paise():
    tot = 0                       # integer paise
    for a in payments: tot += int(Decimal(a) * 100)
    return Decimal(tot) / 100

def by_decimal():
    tot = Decimal("0")
    for a in payments: tot += Decimal(a)
    return tot

print(f"Exact bank total: {exact}   (n = {N + 3})")
for name, f in [("float (plain)", by_float_plain), ("float + round each", by_float_round),
                ("integer paise", by_paise), ("Decimal", by_decimal)]:
    r, sec = t(f)
    print(f"{name:20} total = {r!s:>20}  exact? {Decimal(str(r)) == exact!s:<5} time = {sec*1000:8.1f} ms")
print("\nMemory per value (sys.getsizeof):")
print("  float   :", sys.getsizeof(33.4), "bytes")
print("  int     :", sys.getsizeof(3340), "bytes (paise)")
print("  Decimal :", sys.getsizeof(Decimal('33.40')), "bytes")
