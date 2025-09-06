import sys
import subprocess
from pathlib import Path


CALC_SCRIPT = Path(__file__).resolve().parents[1] / "source" / "calculator_p.py"


def run_calc_with_input(s: str):
    proc = subprocess.run([sys.executable, str(CALC_SCRIPT)], input=s + "\n", text=True, capture_output=True)
    return proc


def last_output_value(stdout: str) -> str:
    # extract last token that can be parsed as int from the stdout
    tokens = []
    for line in stdout.splitlines():
        for part in line.strip().split():
            tokens.append(part)
    # find last token that is an integer
    for t in reversed(tokens):
        try:
            int(t)
            return t
        except Exception:
            continue
    return ""


def test_add_two_numbers():
    proc = run_calc_with_input("2 3")
    assert proc.returncode == 0, f"process failed: {proc.stderr}"
    assert last_output_value(proc.stdout) == "5"


def test_add_multiple_numbers():
    proc = run_calc_with_input("10 -4 1")
    assert proc.returncode == 0, f"process failed: {proc.stderr}"
    assert last_output_value(proc.stdout) == "7"


def test_non_numeric_input_fails():
    proc = run_calc_with_input("a 1")
    # map(int, ...) should raise ValueError -> non-zero exit
    assert proc.returncode != 0
