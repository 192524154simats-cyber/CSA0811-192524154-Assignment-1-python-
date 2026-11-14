"""Rate card and calculator - version 2 (two-decimal readings, seasonal rates, ten-day bonus).
Design: MODIFIED from the original. Same function names, Decimal arithmetic, rate card chosen by season."""
from decimal import Decimal, ROUND_HALF_UP

D = Decimal
# ---------- the only place where rates are written ----------
STD_FAT, STD_SNF, STEP = D("3.5"), D("8.5"), D("0.1")
RATE_CARDS = {
    "normal":   {"base": D("30.00"), "fat_step": D("0.40"), "snf_step": D("0.30")},
    "seasonal": {"base": D("32.00"), "fat_step": D("0.45"), "snf_step": D("0.30")},   # April - June
}
SEASONAL_MONTHS = (4, 5, 6)
BONUS_THRESHOLD_LITRES = D("500")     # strictly MORE than this earns the bonus
BONUS_PER_LITRE = D("0.50")
FAT_MIN, FAT_MAX = D("2.0"), D("7.0")
SNF_MIN, SNF_MAX = D("7.0"), D("10.0")
LITRES_MAX = D("200")
PAISA = D("0.01")

def to_paise(value):
    """Round to 2 decimals, halves up."""
    return value.quantize(PAISA, rounding=ROUND_HALF_UP)

def season_of(month):
    """Return 'seasonal' for April-June (month 4-6), otherwise 'normal'."""
    if not 1 <= month <= 12:
        raise ValueError(f"month must be 1-12, got {month}")
    return "seasonal" if month in SEASONAL_MONTHS else "normal"

def get_rate_card(season):
    """Return the rate-card dictionary of a season."""
    return RATE_CARDS[season]

def steps(reading, standard):
    """Exact number of 0.1 steps (may be fractional, e.g. 4.25 -> 7.5 steps). No float error: Decimal."""
    return (reading - standard) / STEP

def rate_per_litre(fat, snf, season="normal"):
    """Price per litre in the given season (Decimal, rounded to the paisa)."""
    card = get_rate_card(season)
    return to_paise(card["base"] + steps(fat, STD_FAT) * card["fat_step"] + steps(snf, STD_SNF) * card["snf_step"])

def payout(litres, fat, snf, season="normal"):
    """Amount payable for one entry (Decimal, 2 places)."""
    return to_paise(litres * rate_per_litre(fat, snf, season))

def bonus(total_litres):
    """Bonus for a ten-day period: Rs 0.50 on ALL litres if litres > 500, else 0.00."""
    if total_litres > BONUS_THRESHOLD_LITRES:
        return to_paise(total_litres * BONUS_PER_LITRE)
    return D("0.00")

def ten_day_total(entries):
    """entries: list of (litres, fat, snf, month). Returns (milk_amount, bonus_amount, grand_total, total_litres)."""
    milk, litres_sum = D("0.00"), D("0")
    for litres, fat, snf, month in entries:
        milk += payout(litres, fat, snf, season_of(month))   # season chosen per entry date
        litres_sum += litres                                  # running totals: O(1) memory
    b = bonus(litres_sum)
    return milk, b, milk + b, litres_sum

def validate(litres, fat, snf):
    """Raise ValueError if an entry breaks a rule (litres > 0, fat/SNF ranges)."""
    if not 0 < litres <= LITRES_MAX:
        raise ValueError(f"litres out of range: {litres}")
    if not FAT_MIN <= fat <= FAT_MAX:
        raise ValueError(f"fat out of range: {fat}")
    if not SNF_MIN <= snf <= SNF_MAX:
        raise ValueError(f"snf out of range: {snf}")

if __name__ == "__main__":
    print("Reading 4.25 % fat, 8.63 % SNF, 10 L:")
    for month, name in ((11, "November"), (5, "May")):
        s = season_of(month)
        print(f"  {name:9} ({s:8}) rate {rate_per_litre(D('4.25'), D('8.63'), s):>6}  amount {payout(D('10'), D('4.25'), D('8.63'), s):>8}")
    ten = [(D("50"), D("3.5"), D("8.5"), 11)] * 9 + [(D("51"), D("3.5"), D("8.5"), 11)]
    print("Ten days, 501 L in November:", ten_day_total(ten))
