"""Task 5 - reading the clerk's entry, validating it, converting types, formatted output.
Run:  python read_input.py            -> demo with ready-made typed values
      python read_input.py --live     -> type the entries yourself (input())
"""
import sys
from decimal import Decimal

def is_number(text):
    """Return True if text looks like a plain decimal number such as 8 or 8.5 (string-method check)."""
    text = text.strip()
    if text.count(".") > 1 or text == "" or text == ".":
        return False
    return text.replace(".", "", 1).isdigit()      # no sign, no comma, no letters

def read_value(label, text):
    """Check first, then convert. Returns Decimal or None."""
    if is_number(text):
        return Decimal(text.strip())
    print(f"   ! invalid {label}: {text!r} (type digits with a '.' for decimals, e.g. 8.5)")
    return None

def process(litres_text, fat_text, snf_text):
    litres = read_value("litres", litres_text)
    fat = read_value("fat", fat_text)
    snf = read_value("snf", snf_text)
    if None in (litres, fat, snf):
        return None
    return litres, fat, snf

def show(farmer, litres, fat, snf):
    # f-string width and precision: {value:8.2f}
    print(f"{farmer:<6}{float(litres):8.2f} L{float(fat):6.1f} %{float(snf):6.1f} %")

def main():
    if "--live" in sys.argv:
        while True:
            farmer = input("Farmer ID (blank to stop): ").strip()
            if not farmer:
                break
            result = process(input("  litres: "), input("  fat %: "), input("  snf %: "))
            if result:
                show(farmer, *result)
    else:
        print("input() always returns str, e.g. typed 8 ->", repr("8"), type("8").__name__, "-> convert with int()/float()")
        print("int('8') =", int("8"), " float('8.5') =", float("8.5"))
        for bad in ("8,5", "eight"):
            try:
                float(bad)
            except ValueError as e:
                print(f"float({bad!r}) -> ValueError: {e}")
        print()
        samples = [("F001", "10", "3.5", "8.5"), ("F002", "8.5", "4.2", "8.7"),
                   ("F003", "12", "3,1", "8.3"), ("F004", "eight", "4.0", "8.5"), ("F005", "9", "4.0", "8.5.1")]
        for farmer, l, f, s in samples:
            print(f"Entry {farmer}: litres={l!r} fat={f!r} snf={s!r}")
            r = process(l, f, s)
            if r:
                show(farmer, *r)

if __name__ == "__main__":
    main()
