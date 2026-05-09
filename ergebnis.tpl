<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Ergebnis</title>

    <link rel="stylesheet" href="/static/style.css">
</head>

<body class="ergebnis-page">

<div class="ergebnis-card">

    <div class="result-label">
        {{analyse["fach"]}} Quiz
    </div>

    <h1>Dein Ergebnis</h1>

    <div class="score-circle">
        <span>{{prozent}}%</span>
    </div>

    <h2>
        {{punkte}} von {{max_punkte}} Punkten erreicht
    </h2>

    <div class="analyse-box">

        <h3>{{analyse["titel"]}}</h3>

        <p>{{analyse["text"]}}</p>

        <h4>Tipps zur Verbesserung:</h4>

        <ul>
            % for tipp in analyse["tipps"]:
                <li>{{tipp}}</li>
            % end
        </ul>

    </div>

    <div class="result-actions">

        <a href="/kategorien" class="result-button">
            Neues Quiz starten
        </a>

        <a href="/" class="result-button secondary">
            Zur Startseite
        </a>

    </div>

</div>

</body>
</html>