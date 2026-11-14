"""Second script: uses milkrate as a module - three import styles."""
import sys
import math
import milkrate                       # use as milkrate.payout(...)
from milkrate import payout           # use as payout(...)
import milkrate as mr                 # short alias

print("(No rate table was printed above: the __main__ block did not run on import.)")
print("milkrate.payout(8.5, 4.2, 8.7) =", milkrate.payout(8.5, 4.2, 8.7))
print("payout(12, 3.1, 8.3)           =", payout(12, 3.1, 8.3))
print("mr.rate_per_litre(3.5, 8.5)    =", mr.rate_per_litre(3.5, 8.5))
print("math.floor(-2.5)               =", math.floor(-2.5), "(standard module)")
print("module name inside milkrate    =", milkrate.__name__, "(not '__main__')")
print("milkrate loaded once in sys.modules:", "milkrate" in sys.modules)
print("Python searches these places (sys.path[0] is this script's folder):")
for p in sys.path[:3]:
    print("  ", p)
