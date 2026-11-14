"""Task 4 - expressions: precedence, float surprises, round/int/floor, chaining."""
import math

print("--- Precedence and associativity ---")
print("2 + 3 * 4        =", 2 + 3 * 4, "  (* before +)")
print("(2 + 3) * 4      =", (2 + 3) * 4)
print("2 ** 3 ** 2      =", 2 ** 3 ** 2, "  (** is RIGHT-associative: 2**(3**2))")
print("-2 ** 2          =", -2 ** 2, "  (** binds tighter than unary minus: -(2**2))")
print("(-2) ** 2        =", (-2) ** 2)
print("10 - 4 - 3       =", 10 - 4 - 3, "  (left-associative)")

print("\n--- Surprises ---")
print("1. (4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1, " <- expected 7.0")
print("2. (3.1 - 3.5) / 0.1 =", (3.1 - 3.5) / 0.1, " <- expected -4.0")
print("3. 0.1 * 3 =", 0.1 * 3, " <- expected 0.3")
print("4. round(2.5) =", round(2.5), ", round(3.5) =", round(3.5), " <- banker's rounding (half to even)")
print("5. round(2.675, 2) =", round(2.675, 2), " <- expected 2.68")

print("\n--- round() fixes the step count ---")
fat_steps = round((4.2 - 3.5) / 0.1)
print("round((4.2-3.5)/0.1) =", fat_steps, type(fat_steps).__name__)

print("\n--- round vs int vs floor ---")
print(f"{'x':>6} {'round':>6} {'int':>5} {'floor':>6}")
for x in (2.7, 2.5, -2.7, -2.5, -3.999999999999999):
    print(f"{x:>6} {round(x):>6} {int(x):>5} {math.floor(x):>6}")

print("\n--- Comparison chaining and Boolean operators ---")
fat = 4.2
print("2.0 <= fat <= 7.0           :", 2.0 <= fat <= 7.0)
print("2.0 <= fat and fat <= 7.0   :", 2.0 <= fat and fat <= 7.0, "(same meaning)")
print("not (2.0 <= 8.1 <= 7.0)     :", not (2.0 <= 8.1 <= 7.0))
print("1 < 2 < 3 > 2               :", 1 < 2 < 3 > 2)
print("True or 1/0                 :", True or 1 / 0, "(short-circuit: 1/0 never runs)")
