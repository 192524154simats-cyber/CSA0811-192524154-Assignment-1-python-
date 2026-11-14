"""Assert-based tests + a printed test table. Run: python test_calculator.py"""
from decimal import Decimal as D
from calculator import parse_entry, rate_per_litre, payout, ten_day_total

rows = []   # (case, input, expected, actual, pass?)

def check_pay(case, l, f, s, expected_rate, expected_pay):
    e = parse_entry(l, f, s)
    r, p = rate_per_litre(e[1], e[2]), payout(*e)
    ok = r == D(expected_rate) and p == D(expected_pay)
    rows.append((case, f"{l} L, fat {f}, snf {s}", f"{expected_rate} / {expected_pay}", f"{r} / {p}", ok))
    assert ok, case

def check_invalid(case, l, f, s):
    try:
        parse_entry(l, f, s); actual, ok = "accepted", False
    except ValueError:
        actual, ok = "rejected", True
    rows.append((case, f"{l} L, fat {f}, snf {s}", "rejected", actual, ok))
    assert ok, case

# ---- Normal entries in each direction (expected values worked out by hand) ----
check_pay("fat above, snf above", "8.5", "4.2", "8.7", "33.40", "283.90")     # 30+7*.4+2*.3
check_pay("fat below, snf below", "12", "3.1", "8.3", "27.80", "333.60")      # 30-4*.4-2*.3
check_pay("fat above, snf below", "10", "4.0", "8.0", "30.50", "305.00")      # 30+5*.4-5*.3
check_pay("fat below, snf above", "10", "3.0", "9.0", "29.50", "295.00")      # 30-5*.4+5*.3
# ---- Boundaries ----
check_pay("standard milk 3.5 / 8.5", "10", "3.5", "8.5", "30.00", "300.00")
check_pay("lowest allowed fat 2.0", "10", "2.0", "8.5", "24.00", "240.00")    # 30-15*.4
check_pay("highest allowed fat 7.0", "10", "7.0", "8.5", "44.00", "440.00")   # 30+35*.4
check_pay("half-paisa rounds up", "0.25", "4.0", "8.0", "30.50", "7.63")      # 7.625 -> 7.63
# ---- Invalid entries ----
check_invalid("text litres", "eight", "4.0", "8.5")
check_invalid("comma decimal", "8", "4,2", "8.5")
check_invalid("negative litres", "-5", "4.0", "8.5")
check_invalid("zero litres", "0", "4.0", "8.5")
check_invalid("fat below 2.0", "8", "1.9", "8.5")
check_invalid("fat above 7.0", "8", "7.1", "8.5")

# ---- Hand-calculated set of 5 entries: total must be exactly 2080.00 ----
five = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7"), ("12", "3.1", "8.3"), ("20", "2.0", "8.5"), ("15", "7.0", "9.0")]
# 300.00 + 283.90 + 333.60 + 480.00 + 682.50 = 2080.00
total = ten_day_total([parse_entry(*e) for e in five])
rows.append(("5-entry total", "see five list", "2080.00", str(total), total == D("2080.00")))
assert total == D("2080.00")

print(f"{'Case':<24}{'Input':<28}{'Expected (rate/pay)':<22}{'Actual':<22}Result")
for case, inp, exp, act, ok in rows:
    print(f"{case:<24}{inp:<28}{exp:<22}{act:<22}{'PASS' if ok else 'FAIL'}")
print(f"\n{sum(r[4] for r in rows)} / {len(rows)} tests passed")
