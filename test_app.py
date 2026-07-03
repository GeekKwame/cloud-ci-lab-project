import subprocess
import sys


def test_app_runs():
    """Runs app.py as a subprocess and checks it exits cleanly with expected output."""
    result = subprocess.run(
        [sys.executable, "app.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "app.py did not exit successfully"
    assert "Cloud CI Pipeline Running" in result.stdout, "Expected output not found"
    print("Test passed: app.py runs and prints expected output")


if __name__ == "__main__":
    test_app_runs()
