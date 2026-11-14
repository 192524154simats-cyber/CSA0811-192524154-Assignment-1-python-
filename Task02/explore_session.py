"""Task 2 - replays an interactive Python session (>>> prompts) so it can be
screenshotted. You can ALSO type the same lines yourself in `python` (REPL)."""
import code

lines = [
    "type(10)", "type(10.0)", 'type("10")', "type(True)", "type([10, 8.5])",
    "7/2", "7//2", "7%2", "-7//2", "-7%2",
    "0.1 + 0.2", "0.1 + 0.2 == 0.3",
    "round(0.1 + 0.2, 2) == 0.3",
    "from decimal import Decimal",
    'Decimal("0.1") + Decimal("0.2") == Decimal("0.3")',
    "Decimal(0.1)",
    "isinstance(True, int)", "True + True",
    "sum([0.1] * 10)", "sum([0.1] * 10) == 1.0",
]
console = code.InteractiveConsole()
for line in lines:
    print(">>>", line)
    console.push(line)
