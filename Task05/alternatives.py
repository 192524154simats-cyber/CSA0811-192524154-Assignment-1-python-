"""Task 5 alternative: try/except ValueError versus string-method check."""
import timeit
from read_input import is_number

def with_try(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

print(f"{'input':>8} | string check | try/except")
for t in ("8.5", "8,5", "eight", "-3", "1e3", "nan"):
    print(f"{t!r:>8} | {str(is_number(t)):>12} | {with_try(t)}")

N = 500_000
for t in ("8.5", "eight"):
    a = timeit.timeit(lambda: is_number(t), number=N)
    b = timeit.timeit(lambda: with_try(t), number=N)
    print(f"{t!r:>8}: string check {a*1000/N*1000:6.2f} us/entry | try/except {b*1000/N*1000:6.2f} us/entry")
