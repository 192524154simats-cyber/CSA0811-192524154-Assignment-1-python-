"""Task 10 - expectation vs execution: float vs Decimal totals, timing, round-each vs round-total."""
import random, time
from decimal import Decimal as D
from calculator import payout, rate_per_litre

random.seed(2026)          # same data every run

def make_entries(n):
    """Random valid entries as strings, e.g. ('12.25', '4.2', '8.7'). Litres have 2 decimals (scale reading)."""
    return [(f"{random.randint(200, 4000) / 100:.2f}", f"{random.randint(20, 70) / 10:.1f}", f"{random.randint(75, 95) / 10:.1f}") for _ in range(n)]

def float_payout_raw(l, f, s):
    rate = 30.0 + round((f - 3.5) / 0.1) * 0.40 + round((s - 8.5) / 0.1) * 0.30
    return l * rate                                   # NOT rounded

def float_total_raw(entries):          # float all the way
    t = 0.0
    for l, f, s in entries:
        t += float_payout_raw(float(l), float(f), float(s))
    return t

def float_total_rounded_each(entries):  # round each payment to 2 places, add as float
    t = 0.0
    for l, f, s in entries:
        t += round(float_payout_raw(float(l), float(f), float(s)), 2)
    return t

def decimal_total_each(entries):        # recommended: round each payment (paise), add exactly
    t = D("0.00")
    for l, f, s in entries:
        t += payout(D(l), D(f), D(s))
    return t

def decimal_total_once(entries):        # add unrounded amounts, round only the total
    t = D("0")
    for l, f, s in entries:
        t += D(l) * rate_per_litre(D(f), D(s))
    return t.quantize(D("0.01"))

def main():
    print(f"{'n':>7} | {'Decimal (round each)':>22} | {'float raw':>20} diff | {'float round each':>18} diff | {'Decimal (round once)':>22} diff")
    for n in (300, 6000, 150000):
        data = make_entries(n)
        t0 = time.perf_counter(); exact = decimal_total_each(data); t_dec = time.perf_counter() - t0
        t0 = time.perf_counter(); fr = float_total_raw(data); t_fl = time.perf_counter() - t0
        fe = float_total_rounded_each(data)
        once = decimal_total_once(data)
        print(f"{n:>7} | {exact:>22} | {fr:>20.6f} {abs(D(repr(fr)) - exact):>.8f} | {fe:>18.6f} {abs(D(repr(fe)) - exact):>.8f} | {once:>22} {abs(once - exact)}")
        print(f"{'':>7}   time: Decimal {t_dec*1000:8.1f} ms | float {t_fl*1000:8.1f} ms")

if __name__ == "__main__":
    main()
