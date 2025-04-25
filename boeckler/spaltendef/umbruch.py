import ast

INPUT_FILE = 'coldict.py'
OUTPUT_FILE = 'coldict_clean2.py'

# Einlesen und Parsen
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    source = f.read()
module = ast.parse(source)

# Zuweisung an coldict finden
for node in module.body:
    if isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id == 'coldict':
                dict_node = node.value
                break
        else:
            continue
        break
else:
    raise ValueError("Kein coldict-Dictionary gefunden in " + INPUT_FILE)

# Schlüssel/Wert-Paare extrahieren
entries = []  # (key, string_value, value_node)
for k_node, v_node in zip(dict_node.keys, dict_node.values):
    if (isinstance(k_node, ast.Constant) and isinstance(k_node.value, str)
        and isinstance(v_node, ast.Constant) and isinstance(v_node.value, str)):
        entries.append((k_node.value, v_node.value))

# Duplikate entfernen (kürzeren String verwerfen)
valid = {}
for key, val in entries:
    if key not in valid or len(val) > len(valid[key]):
        valid[key] = val

# Bereinigtes Dictionary schreiben (je Eintrag eigene Zeile)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("coldict = {\n")
    for key, val in valid.items():
        f.write(f"    {repr(key)}: {repr(val)},\n")
    f.write("}\n")

print(f"Bereinigt und geschrieben nach {OUTPUT_FILE}")
