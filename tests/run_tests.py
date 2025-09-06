import importlib.util
import sys
from pathlib import Path

TEST_FILE = Path(__file__).resolve().parent / "test_calculator_addition.py"

spec = importlib.util.spec_from_file_location("test_module", str(TEST_FILE))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

tests = [
    "test_add_two_numbers",
    "test_add_multiple_numbers",
    "test_non_numeric_input_fails",
]

failed = 0
for name in tests:
    fn = getattr(mod, name)
    try:
        fn()
        print(f"PASS: {name}")
    except AssertionError as e:
        print(f"FAIL: {name} - AssertionError: {e}")
        failed += 1
    except Exception as e:
        print(f"ERROR: {name} - Exception: {e}")
        failed += 1

if failed:
    print(f"{failed} test(s) failed")
    sys.exit(1)
else:
    print("All tests passed")
    sys.exit(0)
