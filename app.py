from bottle import route, run, template, static_file, request
import random
import copy
import json
import os
from datetime import datetime
from speicher import ergebnis_speichern, ergebnisse_laden

from fragen import fragen_englisch, fragen_allgemein, fragen_mathe
from analyse import analyse_erstellen


def quiz_fragen_vorbereiten(fragen_liste):
    """Wählt 20 zufällige Fragen aus und mischt die Antworten."""
    fragen = copy.deepcopy(random.sample(fragen_liste, min(20, len(fragen_liste))))
    
    for frage in fragen:
        random.shuffle(frage["antworten"])
    
    return fragen


# --- Statische Dateien ---

@route('/static/<filepath:path>')
def static_files(filepath):
    """Liefert statische Dateien (CSS, JS, Bilder)."""
    return static_file(filepath, root='./static')


# --- Seiten ---

@route('/')
def about():
    """Einleitungsseite."""
    return template('about')
    
@route('/about')
def about_page()
    return template('about')

@route('/start')
def startseite():
    """Startseite."""
    return template('start')


@route('/kategorien')
def kategorien():
    """Kategorienauswahl."""
    return template('kategorien')


# --- Quiz-Routen ---

@route('/allgemeinwissen')
def allgemein():
    """Allgemeinwissen-Quiz starten."""
    fragen = quiz_fragen_vorbereiten(fragen_allgemein)
    return template('quiz', titel="Allgemeinwissen Quiz", kategorie="allgemein", fragen=fragen)


@route('/mathe')
def mathe():
    """Mathe-Quiz starten."""
    fragen = quiz_fragen_vorbereiten(fragen_mathe)
    return template('quiz', titel="Mathe Quiz", kategorie="mathe", fragen=fragen)


@route('/englisch')
def englisch():
    """Englisch-Quiz starten."""
    fragen = quiz_fragen_vorbereiten(fragen_englisch)
    return template('quiz', titel="Englisch Quiz", kategorie="englisch", fragen=fragen)


# --- Auswertung ---
@route('/auswertung', method='POST')
def auswertung():
    """Wertet das Quiz aus und zeigt das Ergebnis."""

    gesamt_fragen = 20
    max_punkte = gesamt_fragen * 2
    punkte = 0

    kategorie = request.forms.get("kategorie", "")
    name = request.forms.get("name", "Unbekannt")

    for i in range(gesamt_fragen):

        antwort = request.forms.get(f"antwort{i}")
        richtig = request.forms.get(f"richtig{i}")

        if antwort and richtig and antwort == richtig:
            punkte += 2

    prozent = int((punkte / max_punkte) * 100)

    analyse = analyse_erstellen(kategorie, prozent)

    ergebnis_speichern(
        name,
        kategorie,
        punkte,
        max_punkte,
        prozent
    )

    alle_ergebnisse = ergebnisse_laden()

    return template(
        'ergebnis',
        punkte=punkte,
        max_punkte=max_punkte,
        prozent=prozent,
        analyse=analyse,
        ergebnisse=alle_ergebnisse
    ) 
# --- Server starten ---

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
