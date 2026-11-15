from pathlib import Path
import subprocess
import sys

NOTEBOOKS = [
    "01_data_collection.ipynb",
    "02_returns_diagnostics.ipynb",
    "03_market_regimes.ipynb",
    "04_wavelet_analysis.ipynb",
    "05_empirical_tail_dependence.ipynb",
    "06_copula_models.ipynb",
    "07_tail_risk_map.ipynb",
    "08_portfolio_risk.ipynb",
    "09_out_of_sample.ipynb",
    "10_backtesting.ipynb",
    "11_final_results.ipynb",
]

ROOT = Path(__file__).resolve().parent
NOTEBOOK_DIR = ROOT / "notebooks"

# Allow notebooks to sit in the project root if no /notebooks folder exists.
if not NOTEBOOK_DIR.exists():
    NOTEBOOK_DIR = ROOT

# Ensure expected output folders exist.
for folder in [
    ROOT / "data" / "raw",
    ROOT / "data" / "processed",
    ROOT / "outputs" / "tables",
    ROOT / "outputs" / "figures",
]:
    folder.mkdir(parents=True, exist_ok=True)

print("=" * 72)
print("SAIFA QUANT EDGE 1.0 — FULL REPRODUCTION")
print("=" * 72)
print(f"Project root: {ROOT}")
print(f"Notebook directory: {NOTEBOOK_DIR}")
print()

missing = [nb for nb in NOTEBOOKS if not (NOTEBOOK_DIR / nb).exists()]
if missing:
    print("ERROR: Missing notebook(s):")
    for nb in missing:
        print(f"  - {nb}")
    sys.exit(1)

for i, notebook in enumerate(NOTEBOOKS, start=1):
    path = NOTEBOOK_DIR / notebook

    print(f"[{i}/{len(NOTEBOOKS)}] Running {notebook} ...")

    command = [
    sys.executable,
    "-m",
    "nbconvert",
    "--to",
    "notebook",
    "--execute",
    "--inplace",
    "--ExecutePreprocessor.timeout=900",
    str(path),
]

    try:
        subprocess.run(
            command,
            cwd=ROOT,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        print()
        print("=" * 72)
        print(f"FAILED: {notebook}")
        print("=" * 72)
        print("Fix the notebook error shown above, then rerun:")
        print("    python run_all.py")
        sys.exit(exc.returncode)

    print(f"Completed: {notebook}")
    print()

print("=" * 72)
print("SUCCESS")
print("All notebooks executed successfully.")
print("Final outputs are available in:")
print("  outputs/tables/")
print("  outputs/figures/")
print("=" * 72)
