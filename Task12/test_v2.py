"""Task 12-D tests: both seasons, two-decimal readings, bonus boundaries. Run: python test_v2.py"""
from decimal import Decimal as D
from milkrate_v2 import rate_per_litre, payout, ten_day_total, bonus, season_of

rows = []
def check(case, expected, actual):
    ok = D(expected) == actual
    rows.append((case, expected, str(actual), ok))
    assert ok, f"{case}: expected {expected}, got {actual}"

# ---- Season selection (month boundaries) ----
for m, s in ((3, "normal"), (4, "seasonal"), (6, "seasonal"), (7, "normal"), (11, "normal")):
    rows.append((f"season of month {m}", s, season_of(m), season_of(m) == s)); assert season_of(m) == s

# ---- Rates: normal card (30.00 / 0.40 / 0.30) ----
check("normal std 3.5/8.5", "30.00", rate_per_litre(D("3.5"), D("8.5"), "normal"))
check("normal 4.25/8.63 (7.5 & 1.3 steps)", "33.39", rate_per_litre(D("4.25"), D("8.63"), "normal"))     # 30+3.00+0.39
# ---- Rates: seasonal card (32.00 / 0.45 / 0.30) ----
check("seasonal std 3.5/8.5", "32.00", rate_per_litre(D("3.5"), D("8.5"), "seasonal"))
check("seasonal 4.0/8.5", "34.25", rate_per_litre(D("4.0"), D("8.5"), "seasonal"))                      # 32+5*0.45
check("seasonal 4.25/8.63 (35.765 -> half up)", "35.77", rate_per_litre(D("4.25"), D("8.63"), "seasonal"))  # 32+3.375+0.39
check("seasonal SNF step still 0.30: 3.5/9.0", "33.50", rate_per_litre(D("3.5"), D("9.0"), "seasonal"))  # 32+5*0.30
check("seasonal low 3.1/8.3", "29.60", rate_per_litre(D("3.1"), D("8.3"), "seasonal"))                  # 32-1.80-0.60 -> 29.60
# ---- Payouts ----
check("payout normal 10 L 4.25/8.63", "333.90", payout(D("10"), D("4.25"), D("8.63"), "normal"))
check("payout seasonal 10 L 4.25/8.63", "357.70", payout(D("10"), D("4.25"), D("8.63"), "seasonal"))
# ---- Bonus boundaries ----
check("bonus 499.99 L", "0.00", bonus(D("499.99")))
check("bonus exactly 500 L", "0.00", bonus(D("500")))
check("bonus 500.01 L (all litres)", "250.01", bonus(D("500.01")))   # 500.01*0.50 = 250.005 -> 250.01
check("bonus 501 L", "250.50", bonus(D("501")))

# ---- Ten-day totals (worked by hand) ----
std = lambda litres, month: (D(litres), D("3.5"), D("8.5"), month)
exactly_500 = [std("50", 11)] * 10                                  # 10 x 50 L x 30.00 = 15000.00, no bonus
check("ten days Nov, exactly 500 L: total", "15000.00", ten_day_total(exactly_500)[2])
over_501_nov = [std("50", 11)] * 9 + [std("51", 11)]               # 13500+1530 = 15030 + 250.50
check("ten days Nov, 501 L: total", "15280.50", ten_day_total(over_501_nov)[2])
over_501_may = [std("50", 5)] * 9 + [std("51", 5)]                 # 50*32=1600 x9=14400 + 1632 = 16032 + 250.50
check("ten days May, 501 L: total", "16282.50", ten_day_total(over_501_may)[2])
cross = [std("60", 3)] * 5 + [std("60", 4)] * 5                    # 9000 + 9600 = 18600 + (600*0.5=300)
check("ten days across March/April, 600 L: total", "18900.00", ten_day_total(cross)[2])

print(f"{'Case':<48}{'Expected':>10}{'Actual':>10}  Result")
for case, exp, act, ok in rows:
    print(f"{case:<48}{exp:>10}{act:>10}  {'PASS' if ok else 'FAIL'}")
print(f"\n{sum(r[3] for r in rows)} / {len(rows)} tests passed")
