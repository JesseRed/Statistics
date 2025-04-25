import pandas as pd
import pyreadstat
from pathlib import Path

# Pfad zur SPSS-Datei (unter WSL-Style Pfad)
sav_path = Path("/mnt/g/OneDrive/GhostWriter/2025_Boeckler/data/SPSSMaster.sav")
xlsx_path = sav_path.with_suffix(".xlsx")

# Einlesen
print(f"Lade Datei: {sav_path}")
df, meta = pyreadstat.read_sav(sav_path)

print(meta.column_names)  # oder meta.variable_value_labels, etc.

# Export nach Excel
# print(f"Exportiere nach: {xlsx_path}")
# df.to_excel(xlsx_path, index=False)


# Exportiere als CSV statt Excel
csv_path = sav_path.with_suffix(".csv")
print(f"Exportiere nach: {csv_path}")
df.to_csv(csv_path, index=False)
print("Fertig ✅")