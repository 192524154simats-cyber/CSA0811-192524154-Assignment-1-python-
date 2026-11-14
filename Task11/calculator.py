"""Ksheera milk co-operative payment calculator (Decimal, paise-exact).
Run directly for a small demo, or `python calculator.py --live` to type entries."""
import sys
from decimal import Decimal, ROUND_HALF_UP

# ---- Rate card: the ONLY place rates and limits are written ----
BASE_RATE = Decimal("30.00")
STD_FAT, STD_SNF, STEP = Decimal("3.5"), Decimal("8.5"), Decimal("0.1")
FAT_STEP_VALUE, SNF_STEP_VALUE = Decimal("0.40"), Decimal("0.30")
FAT_MIN, FAT_MAX = Decimal("2.0"), Decimal("7.0")
SNF_MIN, SNF_MAX = Decimal("7.0"), Decimal("10.0")
LITRES_MAX = Decimal("200")
PAISA = Decimal("0.01")

def to_paise(value):
    """Round to 2 decimals, halves up."""
    return value.quantize(PAISA, rounding=ROUND_HALF_UP)

def is_number(text):
    """True for plain unsigned numbers such as 8 or 8.5."""
    text = str(text).strip()
    return text.count(".") <= 1 and text.replace(".", "", 1).isdigit()

def parse_entry(litres_text, fat_text, snf_text):
    """Return (litres, fat, snf) as Decimals, or raise ValueError with a clear message."""
    for label, text in (("litres", litres_text), ("fat", fat_text), ("snf", snf_text)):
        if str(text).strip().startswith("-"):
            raise ValueError(f"{label} cannot be negative, got {text!r}")
        if not is_number(text):
            raise ValueError(f"{label} must be a number like 8.5, got {text!r}")
    litres, fat, snf = Decimal(str(litres_text).strip()), Decimal(str(fat_text).strip()), Decimal(str(snf_text).strip())
    if not 0 < litres <= LITRES_MAX:
        raise ValueError(f"litres must be above 0 and at most {LITRES_MAX}, got {litres}")
    if not FAT_MIN <= fat <= FAT_MAX:
        raise ValueError(f"fat must be between {FAT_MIN} and {FAT_MAX}, got {fat}")
    if not SNF_MIN <= snf <= SNF_MAX:
        raise ValueError(f"snf must be between {SNF_MIN} and {SNF_MAX}, got {snf}")
    return litres, fat, snf

def steps(reading, standard):
    """Whole number of 0.1 steps between reading and standard."""
    return int(((reading - standard) / STEP).to_integral_value())

def rate_per_litre(fat, snf):
    """Price per litre (Decimal, 2 places)."""
    return to_paise(BASE_RATE + steps(fat, STD_FAT) * FAT_STEP_VALUE + steps(snf, STD_SNF) * SNF_STEP_VALUE)

def payout(litres, fat, snf):
    """Amount payable for one entry (Decimal, 2 places)."""
    return to_paise(litres * rate_per_litre(fat, snf))

def ten_day_total(entries):
    """Sum of the rounded payments of (litres, fat, snf) tuples."""
    total = Decimal("0.00")
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return total

def main():
    if "--live" in sys.argv:
        entries = []
        while True:
            l = input("litres (blank to finish): ").strip()
            if not l:
                break
            try:
                e = parse_entry(l, input("fat %: "), input("snf %: "))
            except ValueError as err:
                print("  invalid entry:", err); continue
            entries.append(e)
            print(f"  rate {rate_per_litre(e[1], e[2]):>6}  amount {payout(*e):>8}")
        print("Ten-day total:", ten_day_total(entries))
        return
    demo = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7"), ("12", "3.1", "8.3"), ("-5", "4.0", "8.5"), ("9", "eight", "8.5"), ("9", "7.5", "8.5")]
    good = []
    for l, f, s in demo:
        try:
            e = parse_entry(l, f, s)
            good.append(e)
            print(f"{l:>5} L fat {f:>5} snf {s:>4}  rate {rate_per_litre(e[1], e[2]):>6}  amount {payout(*e):>8}")
        except ValueError as err:
            print(f"{l:>5} L fat {f:>5} snf {s:>4}  REJECTED: {err}")
    print("Ten-day total of the valid entries:", ten_day_total(good))

if __name__ == "__main__":
    main()
