
import pandas as pd
from pathlib import Path

# Datei-Pfade
file1 = Path("data_raw.csv")
file2 = Path("SPSSMaster.csv")

# Einlesen der Header
cols1 = pd.read_csv(file1, nrows=0).columns
cols2 = pd.read_csv(file2, nrows=0).columns

# Vergleiche
missing_in_file2 = [col for col in cols1 if col not in cols2]
missing_in_file1 = [col for col in cols2 if col not in cols1]

# Ausgabe
print("Spalten in data_raw.csv, aber NICHT in SPSSMaster.csv:")
for col in missing_in_file2:
    print(f"  - {col}")

print("\nSpalten in SPSSMaster.csv, aber NICHT in data_raw.csv:")
for col in missing_in_file1:
    print(f"  - {col}")
