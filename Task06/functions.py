"""Task 6 - the calculation split into small functions (Decimal money, paise-exact)."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
STD_FAT, STD_SNF, STEP = Decimal("3.5"), Decimal("8.5"), Decimal("0.1")
FAT_STEP_VALUE, SNF_STEP_VALUE = Decimal("0.40"), Decimal("0.30")
PAISA = Decimal("0.01")

def to_paise(value):
    """Round a Decimal to 2 places, halves go up (Rs 0.005 -> 0.01)."""
    return value.quantize(PAISA, rounding=ROUND_HALF_UP)

def steps(reading, standard):
    """Return the number of 0.1 steps (int) between a reading and its standard."""
    return int(((reading - standard) / STEP).to_integral_value())

def rate_per_litre(fat, snf):
    """Return the price per litre (Decimal, 2 places) for the given fat % and SNF %."""
    rate = BASE_RATE + steps(fat, STD_FAT) * FAT_STEP_VALUE + steps(snf, STD_SNF) * SNF_STEP_VALUE
    return to_paise(rate)

def payout(litres, fat, snf):
    """Return the amount payable for one entry (Decimal, 2 places). Does not print."""
    return to_paise(litres * rate_per_litre(fat, snf))

def ten_day_total(entries):
    """Return the sum of payouts for a list of (litres, fat, snf) tuples."""
    total = Decimal("0.00")
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return total

def show_payout(litres, fat, snf):
    """Print (not return) one payment line; returns None."""
    print(f"{litres:>6} L  rate {rate_per_litre(fat, snf):>6}  amount {payout(litres, fat, snf):>8}")

if __name__ == "__main__":
    D = Decimal
    entries = [(D("10"), D("3.5"), D("8.5")), (D("8.5"), D("4.2"), D("8.7")), (D("12"), D("3.1"), D("8.3"))]
    for e in entries:
        show_payout(*e)
    print("ten-day total:", ten_day_total(entries))

    # returning vs printing
    x = payout(*entries[1])          # a value we can reuse
    y = show_payout(*entries[1])     # prints, but returns None
    print("returned value:", x, "| print-only function returned:", y)

    # local vs global
    def bad_rate(fat):
        BASE_RATE = Decimal("1")     # creates a LOCAL name, global untouched
        return BASE_RATE
    bad_rate(4)
    print("global BASE_RATE after bad_rate():", BASE_RATE)
