"""Task 4 alternative: int() / math.floor() instead of round() for the step count."""
import math, timeit

BASE, FAT_V, SNF_V = 30.0, 0.40, 0.30

def rate(fat, snf, conv):
    return round(BASE + conv((fat - 3.5) / 0.1) * FAT_V + conv((snf - 8.5) / 0.1) * SNF_V, 2)

print(f"{'fat':>4} {'raw steps':>22} {'round':>6} {'int':>5} {'floor':>6} | rate(round)  rate(int)  rate(floor)   (snf = 8.5)")
for fat in (4.2, 3.1):
    raw = (fat - 3.5) / 0.1
    print(f"{fat:>4} {raw:>22} {round(raw):>6} {int(raw):>5} {math.floor(raw):>6} | "
          f"{rate(fat, 8.5, round):>10} {rate(fat, 8.5, int):>10} {rate(fat, 8.5, math.floor):>12}")

for name, conv in (("round", round), ("int", int), ("floor", math.floor)):
    t = timeit.timeit(lambda: conv((4.2 - 3.5) / 0.1), number=1_000_000)
    print(f"{name:6} 1,000,000 conversions: {t*1000:7.1f} ms  -> O(1) time, O(1) space")
