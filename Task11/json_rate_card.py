"""Task 11 alternative: read the rate card from rate_card.json at start-up."""
import json, time, sys
from decimal import Decimal as D
from pathlib import Path

def load_rate_card(path):
    """Read the JSON file; values are strings so Decimal stays exact. Stops with a clear error if a key is missing."""
    data = json.loads(Path(path).read_text())
    need = ("base_rate", "std_fat", "std_snf", "fat_step_value", "snf_step_value")
    missing = [k for k in need if k not in data]
    if missing:
        raise KeyError(f"rate_card.json is missing: {missing}")
    return {k: D(v) for k, v in data.items()}

def rate(card, fat, snf):
    fs = int(((fat - card["std_fat"]) / D("0.1")).to_integral_value())
    ss = int(((snf - card["std_snf"]) / D("0.1")).to_integral_value())
    return (card["base_rate"] + fs * card["fat_step_value"] + ss * card["snf_step_value"]).quantize(D("0.01"))

t0 = time.perf_counter()
card = load_rate_card(Path(__file__).with_name("rate_card.json"))
load_ms = (time.perf_counter() - t0) * 1000
print("Loaded rate card:", card)
print(f"Start-up cost: {load_ms:.3f} ms once; space: {sys.getsizeof(card)} bytes for the dict (+ 5 Decimals)")
print("rate(4.2, 8.7) =", rate(card, D("4.2"), D("8.7")))

# Rate revision demo: edit the file, no code change
card2 = dict(card); card2["base_rate"] = D("31.00")
print("After revising base_rate to 31.00 in the file ->", rate(card2, D("4.2"), D("8.7")))
