"""Task 7 alternative: copy the functions vs import; one-time import cost and sys.modules cache."""
import time, sys, importlib

t0 = time.perf_counter(); import milkrate; t1 = time.perf_counter()
print(f"First import took  {(t1 - t0) * 1e6:8.1f} microseconds (file read + compiled once)")
t0 = time.perf_counter()
for _ in range(1000):
    import milkrate                       # found in sys.modules, nothing reloaded
t1 = time.perf_counter()
print(f"1000 repeat imports took {(t1 - t0) * 1e6:8.1f} microseconds in total ({(t1 - t0) * 1e3:.3f} us each)")
print("Same object every time:", sys.modules["milkrate"] is milkrate)
