"""Task 8 - the algorithm exactly as written in pseudocode.md, with a printed hand trace."""
from decimal import Decimal, ROUND_HALF_UP
D = Decimal

def payout(litres, fat, snf):
    fat_steps = int(((fat - D("3.5")) / D("0.1")).to_integral_value())
    snf_steps = int(((snf - D("8.5")) / D("0.1")).to_integral_value())
    rate = (D("30.00") + fat_steps * D("0.40") + snf_steps * D("0.30")).quantize(D("0.01"), ROUND_HALF_UP)
    return rate, (litres * rate).quantize(D("0.01"), ROUND_HALF_UP)

def ten_day_total(entries):
    total = D("0.00")
    print(f"{'#':>2} {'litres':>6} {'fat':>4} {'snf':>4} {'valid':>5} {'rate':>6} {'amount':>8} {'total':>9}")
    for i, (litres, fat, snf) in enumerate(entries, 1):
        if litres > 0 and D("2.0") <= fat <= D("7.0"):
            rate, amount = payout(litres, fat, snf)
            total += amount
            print(f"{i:>2} {litres:>6} {fat:>4} {snf:>4} {'yes':>5} {rate:>6} {amount:>8} {total:>9}")
        else:
            print(f"{i:>2} {litres:>6} {fat:>4} {snf:>4} {'NO':>5} {'-':>6} {'-':>8} {total:>9}   invalid entry")
    return total

print("OUTPUT:", ten_day_total([(D("10"), D("3.5"), D("8.5")), (D("8.5"), D("4.2"), D("8.7")), (D("12"), D("3.1"), D("8.3")), (D("-5"), D("4.0"), D("8.5"))]))
