import json
col_dict = json.load(open('col_dict.json'))

neu_dict01 = {
  "WOHNNACH": "Wohnumfeld nach Entlassung (01 = eigener Haushalt, 02 = betreutes Wohnen, 03 = Dauerpflegeeinrichtung, 98 = sonstige, 99 = nicht bekannt)",
  "BERUF": "Berufstätigkeit nach Ereignis (01 = ja, 02 = nein – nach Rea berufsunfähig, 03 = nein – bereits vor Rea nicht berufstätig, 99 = nicht bekannt)",
  "FREIGABEZEITPUNKT_A": "Zeitstempel der endgültigen Datensatz-Freigabe im Register (Datum + Uhrzeit) – kennzeichnet den Abschluss der Dokumentation",
  "LAND_B": "**Bundesland-Schlüssel des Zielkrankenhauses bzw. des Folge-Datensatzes (00 = nicht dokumentiert, 01 = BW … 16 = TH, 99 = unbekannt)**",
  "WV_TYP": "**Typ des Weiterversorgungs-Moduls: 01 = Basis, 02 = Max, 03 = Pädiatrie, 04 = Cardiac Arrest Center**",
  "filter_$": "**Technisches Flag, ob der Datensatz aktuell von einem Analyse-/Filter-Skript berücksichtigt wird (1 = ja, 0 = nein)**",
  "CPR_TOD": "**Todesfeststellung während laufender Reanimation (01 = ja – Pat. verstarb unter CPR, 02 = nein)**",
  "Hypoxie_grab": "**Schweregrad der hypoxischen Schädigung (0 = keine, 1 = mild, 2 = moderat, 3 = schwer)**",
  "Azidose_grab": "**Schweregrad der metabolischen Azidose auf Klinikaufnahme (0 = keine, 1 = mild, 2 = moderat, 3 = schwer)**",
  "MaschCPR": "**Angabe, ob während der Reanimation eine mechanische CPR-Hilfe eingesetzt wurde (01 = manuell, 02 = mechanisch/Feedback-System)**",
  "Azidose_grad": "**Alternative Schreibweise für Azidose_grab (gleiches Codierschema; wird in Altdaten verwendet)**"

}

col_dict.update(neu_dict01)

# JSON in eine Datei schreiben
with open('col_dict.json', 'w', encoding='utf-8') as f:
    json.dump(col_dict, f, ensure_ascii=False, indent=4)
