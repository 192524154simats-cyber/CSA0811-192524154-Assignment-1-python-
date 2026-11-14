"""Task 11 - evidence for the final design at the three scales (uses the Task 9 calculator)."""
import time
from decimal import Decimal as D
from calculator import payout
import random
random.seed(7)

for label, farmers in (("centre", 300), ("block", 6000), ("district union", 150000)):
    entries_per_farmer = 20                       # 10 days x 2 shifts
    n = farmers * entries_per_farmer
    sample = [(D(f"{random.randint(200, 4000)/100:.2f}"), D(f"{random.randint(20, 70)/10:.1f}"), D(f"{random.randint(75, 95)/10:.1f}")) for _ in range(20000)]
    t0 = time.perf_counter()
    total = D("0.00")
    for l, f, s in sample:
        total += payout(l, f, s)
    per_entry = (time.perf_counter() - t0) / len(sample)
    print(f"{label:15} {farmers:>7} farmers -> {n:>9} entries per ten days; measured {per_entry*1e6:5.1f} us/entry -> estimated {per_entry*n:6.1f} s")
