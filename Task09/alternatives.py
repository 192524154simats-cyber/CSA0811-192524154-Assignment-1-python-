"""Task 9 alternative: manual testing vs assert tests - how long to re-run after each change?"""
import time, subprocess, sys
t = time.perf_counter()
subprocess.run([sys.executable, "test_calculator.py"], capture_output=True)
auto = time.perf_counter() - t
print(f"Automatic: all tests re-run in {auto:.2f} s (including Python start-up) - same time after every change.")
cases = 15
print(f"Manual   : {cases} cases x 3 values x ~5 s typing + checking = about {cases*3*5/60:.0f} minutes after EVERY change,")
print("           and a tired tester can mistype or skip a case.  Time grows O(k) in tests k, done by a human each time.")
