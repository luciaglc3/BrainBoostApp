from bottle import route, run, template, request, static_file
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


@route('/static/<filename>')
def static_files(filename):
	return static_file(filename, root='./static')





@route('/englisch')
def englisch_test():
	ausgewaehlte_fragen = random.sample(fragen_englisch, 20)
	return template('quiz', titel="Englisch Quiz",kategorie="englisch", fragen=ausgewaehlte_fragen)

@route('/auswertung', method='POST')
def auswertung():
    punkte = 0
    gesamt = 0
    kategorie = request.forms.get("kategorie")

    for key in request.forms:
        if key.startswith("antwort"):
            nummer = key.replace("antwort", "")

            antwort = request.forms.get("antwort" + nummer)
            richtig = request.forms.get("richtig" + nummer)

            gesamt += 1

            if antwort == richtig:
                punkte += 2

    max_punkte = gesamt * 2

    if max_punkte > 0:
        prozent = int((punkte / max_punkte) * 100)
    else:
        prozent = 0

    if kategorie == "englisch":
        if prozent >= 80:
            analyse = """
            <p><strong>Sehr starke Leistung im Englisch-Quiz!</strong></p>
            <p>Du hast gezeigt, dass du Grammatik, Wortschatz und einfache Satzstrukturen gut beherrschst.</p>
            <ul>
                <li>Bleib dran und erweitere deinen Wortschatz regelmäßig.</li>
                <li>Schaue Serien oder kurze Videos auf Englisch mit Untertiteln.</li>
                <li>Übe weiterhin unregelmäßige Verben und Satzbau.</li>
            </ul>
            """
        elif prozent >= 50:
            analyse = """
            <p><strong>Solide Leistung, aber da ist noch Luft nach oben.</strong></p>
            <p>Du verstehst viele Grundlagen, solltest aber besonders Wortschatz und Grammatik weiter festigen.</p>
            <ul>
                <li>Lerne täglich 5–10 neue Vokabeln.</li>
                <li>Wiederhole Zeiten wie Simple Past, Present Perfect und Present Simple.</li>
                <li>Lies kurze englische Texte und markiere unbekannte Wörter.</li>
            </ul>
            """
        else:
            analyse = """
            <p><strong>Hier solltest du nochmal gezielt üben.</strong></p>
            <p>Vor allem Grundlagen wie Vokabeln, Artikel, Verben und einfache Sätze sollten wiederholt werden.</p>
            <ul>
                <li>Starte mit Basisvokabeln aus Alltag, Schule und Freizeit.</li>
                <li>Übe regelmäßig mit Karteikarten.</li>
                <li>Schau kurze Lernvideos zu englischer Grammatik.</li>
            </ul>
            """

    elif kategorie == "mathe":
        if prozent >= 80:
            analyse = """
            <p><strong>Sehr gutes Ergebnis im Mathe-Quiz!</strong></p>
            <p>Du rechnest sicher und hast ein gutes Verständnis für mathematische Grundlagen.</p>
            <ul>
                <li>Übe weiter mit schwierigeren Aufgaben.</li>
                <li>Achte darauf, Rechenwege sauber aufzuschreiben.</li>
                <li>Teste dich regelmäßig mit gemischten Aufgaben.</li>
            </ul>
            """
        elif prozent >= 50:
            analyse = """
            <p><strong>Solide Grundlage, aber du solltest weiter üben.</strong></p>
            <p>Einige Rechenarten sitzen schon, andere Themen brauchen noch Wiederholung.</p>
            <ul>
                <li>Übe täglich 15–20 Minuten Grundrechenarten, Brüche und Prozentrechnung.</li>
                <li>Schau Lernvideos zu den Themen, bei denen du unsicher bist.</li>
                <li>Rechne Aufgaben schriftlich Schritt für Schritt nach.</li>
            </ul>
            """
        else:
            analyse = """
            <p><strong>Mathe braucht hier noch deutlich mehr Training.</strong></p>
            <p>Das ist kein Problem, aber du solltest systematisch bei den Grundlagen anfangen.</p>
            <ul>
                <li>Wiederhole zuerst Multiplikation, Division, Brüche und Prozentrechnung.</li>
                <li>Rechne lieber viele leichte Aufgaben sauber als wenige schwere.</li>
                <li>Nutze Erklärvideos und schreibe dir Beispielaufgaben ab.</li>
            </ul>
            """

    else:
        if prozent >= 80:
            analyse = """
            <p><strong>Sehr starkes Allgemeinwissen!</strong></p>
            <p>Du hast ein breites Wissen aus verschiedenen Bereichen gezeigt.</p>
            <ul>
                <li>Bleib neugierig und informiere dich regelmäßig über neue Themen.</li>
                <li>Lies Nachrichten, Sachtexte oder Wissensartikel.</li>
                <li>Teste dich weiter mit Quizfragen aus verschiedenen Bereichen.</li>
            </ul>
            """
        elif prozent >= 50:
            analyse = """
            <p><strong>Gutes Grundwissen, aber noch ausbaufähig.</strong></p>
            <p>Du kennst viele Basics, kannst dein Wissen aber noch breiter aufstellen.</p>
            <ul>
                <li>Lies kurze Artikel zu Geschichte, Geografie, Naturwissenschaften und Politik.</li>
                <li>Schau Wissensformate oder Dokumentationen.</li>
                <li>Wiederhole regelmäßig Fakten mit Quizfragen.</li>
            </ul>
            """
        else:
            analyse = """
            <p><strong>Hier kannst du dein Allgemeinwissen noch deutlich verbessern.</strong></p>
            <p>Fang mit Grundthemen wie Länder, Geschichte, Naturwissenschaften und Alltagwissen an.</p>
            <ul>
                <li>Schau kurze Wissensvideos oder Dokumentationen.</li>
                <li>Lerne jeden Tag 3–5 neue Fakten.</li>
                <li>Wiederhole Fragen, die du falsch beantwortet hast.</li>
            </ul>
            """

    return f"""
    <h1>Ergebnis</h1>
    <p>Du hast {punkte} von {max_punkte} Punkten erreicht.</p>
    <p>Das entspricht {prozent}%.</p>
    {analyse}
    <a href="/">Zurück zur Startseite</a>
    """
   

	



	run(host='localhost', port=8080, debug=True, reloader=True)
