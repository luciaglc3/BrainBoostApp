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
    fragen = random.sample(fragen_allgemein, 20)
    return template('quiz', titel="Allgemeinwissen Quiz",kategorie="allgemein", fragen=fragen)

@route('/mathe')
def mathe():
	fragen = random.sample(fragen_mathe, 20)
	return template('quiz', titel="Mathe Quiz",kategorie="mathe", fragen=fragen)


@route('/englisch')
def englisch_test():
	ausgewaehlte_fragen = random.sample(fragen_englisch, 20)
	return template('quiz', titel="Englisch Quiz",kategorie="englisch", fragen=ausgewaehlte_fragen)



	



	run(host='localhost', port=8080, debug=True, reloader=True)
