from bottle import route, run, template, request, static_file
import random
import copy

from fragen import fragen_englisch, fragen_allgemein, fragen_mathe
from analyse import analyse_erstellen


def quiz_fragen_vorbereiten(fragen_liste):
    fragen = copy.deepcopy(random.sample(fragen_liste, 20))

    for frage in fragen:
        random.shuffle(frage["antworten"])

    return fragen


# STARTSEITE
@route('/')
def startseite():
    return template('start')


# KATEGORIEN
@route('/kategorien')
def kategorien():
    return template('kategorien')


# STATIC DATEIEN
@route('/static/<filename>')
def static_files(filename):
    return static_file(filename, root='./static')


# ALLGEMEINWISSEN QUIZ
@route('/allgemeinwissen')
def allgemein():
    fragen = quiz_fragen_vorbereiten(fragen_allgemein)

    return template(
        'quiz',
        titel="Allgemeinwissen Quiz",
        kategorie="allgemein",
        fragen=fragen
    )


# MATHE QUIZ
@route('/mathe')
def mathe():
    fragen = quiz_fragen_vorbereiten(fragen_mathe)

    return template(
        'quiz',
        titel="Mathe Quiz",
        kategorie="mathe",
        fragen=fragen
    )


# ENGLISCH QUIZ
@route('/englisch')
def englisch():
    fragen = quiz_fragen_vorbereiten(fragen_englisch)

    return template(
        'quiz',
        titel="Englisch Quiz",
        kategorie="englisch",
        fragen=fragen
    )


# AUSWERTUNG
@route('/auswertung', method='POST')
def auswertung():

    punkte = 0
    gesamt_fragen = 20
    max_punkte = gesamt_fragen * 2

    kategorie = request.forms.get("kategorie")

    for i in range(gesamt_fragen):

        antwort = request.forms.get("antwort" + str(i))
        richtig = request.forms.get("richtig" + str(i))

        if antwort == richtig:
            punkte += 2

    prozent = int((punkte / max_punkte) * 100)

    analyse = analyse_erstellen(kategorie, prozent)

    return template(
        'ergebnis',
        punkte=punkte,
        max_punkte=max_punkte,
        prozent=prozent,
        analyse=analyse
    )


# SERVER STARTEN
run(
    host='localhost',
    port=8080,
    debug=True,
    reloader=True
)
