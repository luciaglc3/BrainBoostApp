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

    for i in range(5):
        antwort = request.forms.get(f'frage{i}')
        
        if antwort:
            if antwort == "RICHTIGE_ANTWORT":  # kommt gleich besser
                punkte += 2

    return f"<h1>Du hast {punkte} Punkte!</h1>"


run(host='localhost', port=8080, debug=True, reloader=True)

