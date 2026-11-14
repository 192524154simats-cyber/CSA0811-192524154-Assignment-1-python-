"""Task 8 alternative: store every entry in a list vs keep a running total."""
import tracemalloc, time
from decimal import Decimal as D

def entries_stream(n):                      # generator: produces one entry at a time
    for i in range(n):
        yield D(10 + i % 5), D("3.5"), D("8.5")

def amount(l, f, s):
    return l * D("30.00")

def list_then_sum(n):
    amounts = [amount(*e) for e in entries_stream(n)]   # O(n) space
    return sum(amounts, D("0"))

def running_total(n):
    total = D("0")
    for e in entries_stream(n):                         # O(1) space
        total += amount(*e)
    return total

for n in (300, 6000, 150000):
    row = []
    for fn in (list_then_sum, running_total):
        tracemalloc.start(); t = time.perf_counter()
        r = fn(n)
        sec = time.perf_counter() - t
        peak = tracemalloc.get_traced_memory()[1]; tracemalloc.stop()
        row.append(f"{fn.__name__}: {sec*1000:7.1f} ms, peak {peak/1024:9.1f} KiB")
    print(f"n={n:>6} | " + " | ".join(row))
