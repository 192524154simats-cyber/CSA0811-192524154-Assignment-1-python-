"""Task 3 alternatives: magic numbers vs named constants vs RATE_CARD dictionary."""
import time

# 1. Magic numbers - the rate 30.0 is typed in k places
def rate_a(fat_steps, snf_steps):
    return 30.0 + fat_steps * 0.40 + snf_steps * 0.30
def report_a(fat_steps, snf_steps):
    return 30.0 + fat_steps * 0.40 + snf_steps * 0.30   # typed AGAIN -> forgotten in a revision

# 2. Named constants (module level)
BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE = 30.0, 0.40, 0.30
def rate_b(f, s): return BASE_RATE + f * FAT_STEP_VALUE + s * SNF_STEP_VALUE

# 3. Dictionary
RATE_CARD = {"base": 30.0, "fat": 0.40, "snf": 0.30}
def rate_c(f, s): return RATE_CARD["base"] + f * RATE_CARD["fat"] + s * RATE_CARD["snf"]

N = 1_000_000
for name, fn in [("magic numbers", rate_a), ("named constants", rate_b), ("dictionary", rate_c)]:
    t0 = time.perf_counter()
    for _ in range(N):
        fn(7, 2)
    print(f"{name:16} {N} calls: {(time.perf_counter()-t0)*1000:7.1f} ms")
