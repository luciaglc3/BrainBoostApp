import json
import os
from datetime import datetime


def ergebnis_speichern(name, kategorie, punkte, max_punkte, prozent):
    """Speichert Quiz-Ergebnisse in einer JSON-Datei."""

    dateipfad = "ergebnisse.json"

    neuer_eintrag = {
        "datum": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "name": name,
        "kategorie": kategorie,
        "punkte": punkte,
        "max_punkte": max_punkte,
        "prozent": prozent
    }

def ergebnisse_laden():
    """Lädt alle gespeicherten Ergebnisse."""

    dateipfad = "ergebnisse.json"

    if os.path.exists(dateipfad):

        with open(dateipfad, "r", encoding="utf-8") as datei:
            return json.load(datei)

    return []


    if os.path.exists(dateipfad):
        with open(dateipfad, "r", encoding="utf-8") as datei:
            daten = json.load(datei)
    else:
        daten = []

    daten.append(neuer_eintrag)

    with open(dateipfad, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=4, ensure_ascii=False)