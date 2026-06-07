<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Ergebnis</title>
    <link rel="stylesheet" href="/static/style.css">
</head>

<body class="ergebnis-page">

    <div class="ergebnis-card">

        <h1>Dein Ergebnis</h1>

        <div class="score-circle">
            <span>{{prozent}}%</span>
        </div>

        <h2>{{punkte}} / {{max_punkte}} Punkte</h2>

        <div class="analyse-box">
            <h3>{{analyse["titel"]}}</h3>
            <p>{{analyse["text"]}}</p>

            <h3>Tipps</h3>

            % for tipp in analyse["tipps"]:
                <p>💡 {{tipp}}</p>
            % end
        </div>

        <div class="analyse-box">
            <h3>Gespeicherte Ergebnisse</h3>

            % for eintrag in ergebnisse:

                % name = eintrag["name"] if "name" in eintrag else "Unbekannt"

                <p>
                    <strong>{{name}}</strong><br>
                    Kategorie: {{eintrag["kategorie"]}}<br>
                    Punkte: {{eintrag["punkte"]}} / {{eintrag["max_punkte"]}}<br>
                    Prozent: {{eintrag["prozent"]}}%<br>
                    Datum: {{eintrag["datum"]}}
                </p>

                <hr>

            % end
        </div>

        <div class="result-actions">
            <a href="/start" class="result-button">Neues Quiz starten</a>
            <a href="/kategorien" class="result-button secondary">Andere Kategorie</a>
        </div>

    </div>

</body>
</html>
