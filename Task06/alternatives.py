"""Task 6 alternative: one long script, and a lambda version; function-call overhead."""
import time, random
from decimal import Decimal
from functions import payout

random.seed(1)
D = Decimal
def make(n):
    return [(D(str(random.randint(5, 40))), D(f"{random.uniform(2, 7):.1f}"), D(f"{random.uniform(7.5, 9.5):.1f}")) for _ in range(n)]

def inline_script(data):                       # no functions: the maths is repeated inline
    total = D("0")
    for l, f, s in data:
        fs = int(((f - D("3.5")) / D("0.1")).to_integral_value())
        ss = int(((s - D("8.5")) / D("0.1")).to_integral_value())
        r = (D("30.00") + fs * D("0.40") + ss * D("0.30")).quantize(D("0.01"))
        total += (l * r).quantize(D("0.01"))
    return total

lam = lambda l, f, s: payout(l, f, s)          # lambda: same speed, but no docstring / name in errors
def with_functions(data):
    total = D("0")
    for e in data: total += payout(*e)
    return total
def with_lambda(data):
    total = D("0")
    for e in data: total += lam(*e)
    return total

for n in (300, 6000, 150000):
    data = make(n)
    out = []
    for fn in (inline_script, with_functions, with_lambda):
        t = time.perf_counter(); r = fn(data); out.append((fn.__name__, r, (time.perf_counter() - t) * 1000))
    assert out[0][1] == out[1][1] == out[2][1]
    print(f"n={n:>6}: " + " | ".join(f"{a} {c:8.1f} ms" for a, _, c in out), "| same total:", out[0][1])
