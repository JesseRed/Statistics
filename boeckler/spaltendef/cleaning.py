import ast
import astunparse

# Pfad zur coldict.py
INPUT_FILE = 'coldict.py'
OUTPUT_FILE = 'coldict_clean.py'

# AST der Quelldatei parsen
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    source = f.read()
module = ast.parse(source)

# Suche nach der Zuweisung an coldict
for node in module.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == 'coldict':
                dict_node = node.value
                break
        else:
            continue
        break
else:
    raise ValueError("Kein coldict-Dictionary in {INPUT_FILE} gefunden")

# Werte aus dict literal extrahieren
entries = []  # Liste von (key, value_node)
for key_node, val_node in zip(dict_node.keys, dict_node.values):
    if isinstance(key_node, ast.Constant) and isinstance(key_node.value, str):
        key = key_node.value
        if isinstance(val_node, ast.Constant) and isinstance(val_node.value, str):
            val = val_node.value
        else:
            # Falls komplexer Ausdruck, über astunparse zurück in Quelle
            val = astunparse.unparse(val_node).strip()
        entries.append((key, val_node, val))
    else:
        # Schlüssel nicht string literal überspringen
        continue

# Duplikate finden und kürzeren Wert entfernen
valid = {}
for key, val_node, val_str in entries:
    if key not in valid:
        valid[key] = (val_node, val_str)
    else:
        # existierender Eintrag
        _, existing_str = valid[key]
        # längeren Wert behalten
        if len(val_str) > len(existing_str):
            valid[key] = (val_node, val_str)

# Neue Dict-Literal-Knoten zusammenbauen
new_keys = []
new_vals = []
for key, (val_node, _) in valid.items():
    new_keys.append(ast.Constant(value=key))
    new_vals.append(val_node)

new_dict = ast.Dict(keys=new_keys, values=new_vals)
# Zuweisungs-Knoten ersetzen
for node in module.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == 'coldict':
                node.value = new_dict
                break

# Modifiziertes AST zurück in Quellcode
new_source = astunparse.unparse(module)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(new_source)

print(f"Bereinigt und geschrieben nach {OUTPUT_FILE}")
