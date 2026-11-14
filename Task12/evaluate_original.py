"""Task 12-B: how the ORIGINAL design (float, round() steps, one rate card) copes with the new readings."""
from decimal import Decimal as D
import original_milkrate as old

print("Original code on two-decimal readings (litres = 10, SNF 8.63):")
print(f"{'fat':>6} {'raw fat steps (float)':>24} {'round()':>8} {'true steps':>11} {'old rate':>9} {'true rate (normal card)':>24}")
for fat_text, snf_text in (("4.25", "8.63"), ("4.35", "8.63"), ("4.45", "8.63"), ("3.74", "8.50")):
    fat, snf = float(fat_text), float(snf_text)
    raw = (fat - 3.5) / 0.1
    true_fat = (D(fat_text) - D("3.5")) / D("0.1")
    true_snf = (D(snf_text) - D("8.5")) / D("0.1")
    true_rate = D("30") + true_fat * D("0.40") + true_snf * D("0.30")
    print(f"{fat_text:>6} {raw:>24} {round(raw):>8} {true_fat:>11} {old.rate_per_litre(fat, snf):>9} {true_rate:>24}")

print("\nOriginal module has only ONE rate card; May rate cannot be expressed (BASE_RATE is fixed at 30.0):")
print("old.rate_per_litre(3.5, 8.5) =", old.rate_per_litre(3.5, 8.5), "(seasonal rate should be 32.00)")
print("Original module has no way to see the 10-day litres, so the 500-litre bonus cannot be added.")
