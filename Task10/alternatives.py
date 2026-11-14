"""Task 10 alternative: precompute a rate table (dictionary) instead of recalculating every entry."""
import time
from decimal import Decimal as D
from compare import make_entries
from calculator import rate_per_litre, to_paise

n = 150000
data = make_entries(n)

def recalc(entries):
    t = D("0.00")
    for l, f, s in entries:
        t += to_paise(D(l) * rate_per_litre(D(f), D(s)))
    return t

def with_table(entries):
    table = {}                                     # (fat, snf) -> rate, built on demand
    t = D("0.00")
    for l, f, s in entries:
        key = (f, s)                               # strings as keys, exact
        if key not in table:
            table[key] = rate_per_litre(D(f), D(s))
        t += to_paise(D(l) * table[key])
    return t, len(table)

t0 = time.perf_counter(); a = recalc(data); ta = time.perf_counter() - t0
t0 = time.perf_counter(); b, k = with_table(data); tb = time.perf_counter() - t0
assert a == b
print(f"n={n}: recalculate every entry {ta*1000:8.1f} ms | dictionary rate table {tb*1000:8.1f} ms | same total {a}")
print(f"distinct (fat, snf) pairs k = {k}  -> the table stores only k rates (extra space O(k), k <= 51 x 21 = 1071), independent of n")
