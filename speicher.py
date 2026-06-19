import json
import os
from datetime import datetime


DATEIPFAD = "ergebnisse.json"


def ergebnisse_laden():
    """Laedt alle gespeicherten Ergebnisse aus der JSON-Datei."""
    if not os.path.exists(DATEIPFAD):
        return []

    try:
        with open(DATEIPFAD, "r", encoding="utf-8") as datei:
            daten = json.load(datei)
            if isinstance(daten, list):
                return daten
            return []
    except (json.JSONDecodeError, OSError):
        return []


def ergebnis_speichern(name, kategorie, punkte, max_punkte, prozent):
    """Speichert ein neues Quiz-Ergebnis dauerhaft in ergebnisse.json."""
    neuer_eintrag = {
        "datum": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "name": name,
        "kategorie": kategorie,
        "punkte": punkte,
        "max_punkte": max_punkte,
        "prozent": prozent,
    }

    daten = ergebnisse_laden()
    daten.append(neuer_eintrag)

    with open(DATEIPFAD, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=4, ensure_ascii=False)
