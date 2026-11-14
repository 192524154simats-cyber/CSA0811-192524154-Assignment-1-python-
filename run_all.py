"""Optional helper: runs every non-interactive program task by task. Usage: python run_all.py"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).parent
PLAN = {
    "Task01": ["data_model.py"],
    "Task02": ["explore_session.py", "task2_decimal.py", "task2_decimal_from_float.py", "alternatives.py"],
    "Task03": ["constants_demo.py", "alternatives.py"],
    "Task04": ["expressions.py", "alternatives.py"],
    "Task05": ["read_input.py", "alternatives.py"],
    "Task06": ["functions.py", "alternatives.py"],
    "Task07": ["milkrate.py", "use_milkrate.py", "import_without_guard.py", "alternatives.py"],
    "Task08": ["trace.py", "alternatives.py"],
    "Task09": ["calculator.py", "test_calculator.py", "alternatives.py"],
    "Task10": ["compare.py", "alternatives.py"],
    "Task11": ["scale_check.py", "json_rate_card.py"],
    "Task12": ["evaluate_original.py", "milkrate_v2.py", "test_v2.py"],
}
for folder, files in PLAN.items():
    for f in files:
        print(f"\n{'=' * 70}\n{folder}/{f}\n{'=' * 70}", flush=True)
        subprocess.run([sys.executable, f], cwd=ROOT / folder)
