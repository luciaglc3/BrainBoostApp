from bottle import route, run, template

@route('/')
def startseite():
    return template('start')

@route('/kategorien')
def kategorien():
    return template('kategorien')

run(host='localhost', port=8080, debug=True, reloader=True)

@route('/quiz/allgemein')
def quiz_allgemeinwissen():
    return template('allgemein')