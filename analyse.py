def analyse_erstellen(kategorie, prozent):

    if kategorie == "englisch":

        if prozent >= 80:
            return {
                "fach": "Englisch",
                "titel": "Sehr starke Leistung im Englisch-Quiz!",
                "text": "Du hast gezeigt, dass du Grammatik, Wortschatz und Satzstrukturen gut beherrschst.",
                "tipps": [
                    "Bleib dran und erweitere deinen Wortschatz regelmäßig.",
                    "Schaue Serien oder Videos auf Englisch.",
                    "Übe weiterhin Grammatik und Satzbau."
                ]
            }

        elif prozent >= 50:
            return {
                "fach": "Englisch",
                "titel": "Solide Leistung mit Verbesserungspotenzial.",
                "text": "Die Grundlagen sitzen teilweise schon gut.",
                "tipps": [
                    "Lerne regelmäßig Vokabeln.",
                    "Wiederhole englische Zeiten.",
                    "Lies kurze englische Texte."
                ]
            }

        else:
            return {
                "fach": "Englisch",
                "titel": "Hier solltest du nochmal gezielt üben.",
                "text": "Die Grundlagen sollten nochmal wiederholt werden.",
                "tipps": [
                    "Nutze Karteikarten.",
                    "Übe einfache Satzbildung.",
                    "Schaue Lernvideos."
                ]
            }

    elif kategorie == "mathe":

        if prozent >= 80:
            return {
                "fach": "Mathe",
                "titel": "Sehr gutes Ergebnis im Mathe-Quiz!",
                "text": "Du rechnest sicher und strukturiert.",
                "tipps": [
                    "Übe schwierigere Aufgaben.",
                    "Achte auf saubere Rechenwege.",
                    "Teste dich regelmäßig."
                ]
            }

        elif prozent >= 50:
            return {
                "fach": "Mathe",
                "titel": "Gute Grundlagen vorhanden.",
                "text": "Einige Themen brauchen noch Wiederholung.",
                "tipps": [
                    "Übe Prozentrechnung und Brüche.",
                    "Nutze Lernvideos.",
                    "Rechne Schritt für Schritt."
                ]
            }

        else:
            return {
                "fach": "Mathe",
                "titel": "Hier braucht es noch mehr Übung.",
                "text": "Vor allem die Grundlagen sollten trainiert werden.",
                "tipps": [
                    "Beginne mit einfachen Aufgaben.",
                    "Übe regelmäßig.",
                    "Nutze Beispielaufgaben."
                ]
            }

    else:

        if prozent >= 80:
            return {
                "fach": "Allgemeinwissen",
                "titel": "Sehr starkes Allgemeinwissen!",
                "text": "Du kennst dich in vielen Bereichen gut aus.",
                "tipps": [
                    "Bleib neugierig.",
                    "Lies Nachrichten und Artikel.",
                    "Teste dich weiter mit Quizfragen."
                ]
            }

        elif prozent >= 50:
            return {
                "fach": "Allgemeinwissen",
                "titel": "Gutes Grundwissen.",
                "text": "Du kennst viele Basics.",
                "tipps": [
                    "Schau Wissensvideos.",
                    "Lies kurze Sachtexte.",
                    "Wiederhole Fakten regelmäßig."
                ]
            }

        else:
            return {
                "fach": "Allgemeinwissen",
                "titel": "Hier kannst du dich noch verbessern.",
                "text": "Die Grundlagen können noch erweitert werden.",
                "tipps": [
                    "Lerne täglich neue Fakten.",
                    "Schau Dokumentationen.",
                    "Wiederhole falsche Fragen."
                ]
            }