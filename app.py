from bottle import route, run, template, request
import random
from fragen import fragen_englisch, fragen_allgemein, fragen_mathe

@route('/')
def startseite():
    return template('start')

@route('/kategorien')
def kategorien():
    return template('kategorien')

@route('/allgemeinwissen')
def allgemein():
    fragen = random.sample(fragen_allgemein, 10)
    return template('quiz', titel="Allgemeinwissen Quiz", fragen=fragen)

@route('/mathe')
def mathe():
	fragen = random.sample(fragen_mathe, 10)
	return template('quiz', titel="Mathe Quiz", fragen=fragen)


@route('/englisch')
def englisch_test():
	ausgewaehlte_fragen = random.sample(fragen_englisch, 10)
	return template('quiz', titel="Englisch Quiz", fragen=ausgewaehlte_fragen)

@route('/test')
def test():
	fragen= { 
	    "allgemein": random.sample(fragen_allgemein, 10),
	    "mathe": random.sample(fragen_mathe, 10),
	    "englisch": random.sample(fragen_englisch, 10)}

	return template('test', fragen=fragen)



@route('/auswertung', method='POST')
def auswertung():
    punkte = 0
    gesamt = 0

    for key in request.forms:
        if key.startswith("antwort_"):
            nummer = key.replace("antwort_", "")

            gegebene_antwort = request.forms.get("antwort_" + nummer)
            richtige_antwort = request.forms.get("richtig_" + nummer)

            gesamt += 1

            if gegebene_antwort == richtige_antwort:
                punkte += 2

    max_punkte = 60

    return f"""
    <h1>Ergebnis</h1>
    <p>Du hast {punkte} von {max_punkte} Punkten erreicht.</p>
    <p>Beantwortete Fragen: {gesamt} von 30</p>
    <a href="/test">Test nochmal starten</a>
    """
	
	run(host='localhost', port=8080, debug=True, reloader=True)
