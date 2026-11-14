"""Same as task2_decimal.py but Decimal(float(amount)) - to see the problem come back."""
from decimal import Decimal
payments = ["33.40"] * 1000 + ["0.10"] * 3
total = Decimal("0")
for amount in payments:
    total += Decimal(float(amount))
print("Decimal(float(amount)) total:", total)
print("Decimal(33.4) really holds  :", Decimal(33.4))
