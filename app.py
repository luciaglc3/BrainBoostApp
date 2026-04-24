from bottle import route, run, template, request
import random
from fragen import fragen_englisch

@route('/')
def startseite():
    return template('start')

@route('/kategorien')
def kategorien():
    return template('kategorien')

@route('/quiz/allgemein')
def quiz_allgemeinwissen():
    return template('allgemein')

@route('/englisch')
def englisch_test():
	ausgewaehlte_fragen = random.sample(fragen_englisch, 10)
	return template('quiz', titel="Englisch Quiz", fragen=ausgewaehlte_fragen)

@route('/auswertung', method='POST')
def auswertung():
    punkte = 0
    gesamt = 0

    for key in request.forms:
        if key.startswith("antwort"):
            nummer = key.replace("antwort", "")

            gegebene_antwort = request.forms.get("antwort" + nummer)
            richtige_antwort = request.forms.get("richtig" + nummer)

            gesamt += 1

            if gegebene_antwort == richtige_antwort:
                punkte += 2

    max_punkte = gesamt * 2

    return f"""
<h1>Ergebnis</h1>
<p>Du hast {punkte} von {max_punkte} Punkten erreicht.</p>
<a href="/englisch">Zurück zum Englisch Quiz</a>
"""





run(host='localhost', port=8080, debug=True, reloader=True)
