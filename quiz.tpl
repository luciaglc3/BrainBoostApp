<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{{titel}}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>

    <div class="navbar">
        <div class="logo">Brain<span>Boost</span></div>

        <div class="navlinks">
            <a href="/">Startseite</a>
            <a href="/mathe">Mathe</a>
            <a href="/englisch">Englisch</a>
            <a href="/allgemeinwissen">Allgemeinwissen</a>
        </div>

        <a class="result-btn" href="/ergebnisse">Ergebnisse</a>
    </div>

    <div class="sticky-progress">
        <div class="progress-top">
            <span>Fortschritt: <span id="progress-text">0 / 20</span></span>
            <span id="progress-percent">0%</span>
        </div>

        <div class="progress-bar">
            <div id="progress-fill"></div>
        </div>
    </div>

    <div class="hero">
        <h1>{{titel}}</h1>
        <p>Teste dein Wissen und verbessere deine Kenntnisse.</p>
    </div>

    <div class="quiz-container">

        <div class="info-row">
            <div>Fragen: {{len(fragen)}}</div>
            <div>Viel Erfolg!</div>
        </div>

        <form action="/auswertung" method="post">
            <input type="hidden" name="kategorie" value="{{kategorie}}">

            % for i, frage in enumerate(fragen):
            <div class="frage-box">
                <div class="frage-title">
                    <div class="nummer">{{i+1}}</div>
                    <strong>{{frage["frage"]}}</strong>
                </div>

                % for antwort in frage["antworten"]:
                <label class="antwort">
                    <input type="radio" name="antwort{{i}}" value="{{antwort}}">
                    {{antwort}}
                </label>
                % end

                <input type="hidden" name="richtig{{i}}" value="{{frage['richtig']}}">
            </div>
            % end

            <button class="submit-btn" type="submit">Quiz abgeben →</button>
        </form>

        <div class="tipp">
            💡 Tipp: Lies jede Frage genau und wähle erst dann deine Antwort aus.
        </div>

    </div>

    <script src="/static/script.js"></script>

</body>
</html>
