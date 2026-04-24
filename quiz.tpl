<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{{titel}}</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #071a33;
            color: white;
        }

        .navbar {
            height: 80px;
            background: #08244a;
            display: flex;
            align-items: center;
            padding: 0 45px;
            border-bottom: 2px solid #173b70;
        }

        .logo {
            font-size: 26px;
            font-weight: bold;
            color: white;
            margin-right: 60px;
        }

        .logo span {
            color: #ffc400;
        }

        .navlinks a {
            color: white;
            text-decoration: none;
            margin: 0 20px;
            font-weight: bold;
        }

        .navlinks a:hover {
            color: #ffc400;
        }

        .result-btn {
            margin-left: auto;
            background: #ffc400;
            color: #071a33 !important;
            padding: 15px 22px;
            border-radius: 10px;
            font-weight: bold;
        }

        .hero {
            padding: 70px 60px;
            background: linear-gradient(135deg, #071a33, #0b3266);
            border-bottom: 4px solid #ffc400;
        }

        .hero h1 {
            font-size: 55px;
            margin: 0;
        }

        .hero h1 span {
            color: #ffc400;
        }

        .hero p {
            font-size: 22px;
            color: #c9d6e8;
        }

        .quiz-container {
            width: 85%;
            margin: 50px auto;
        }

        .info-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 25px;
            font-size: 20px;
            font-weight: bold;
        }

        .frage-box {
            background: #0d2b57;
            border: 2px solid #1d5fc2;
            border-radius: 18px;
            padding: 35px;
            margin-bottom: 35px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.25);
        }

        .frage-title {
            display: flex;
            align-items: center;
            gap: 20px;
            font-size: 24px;
            margin-bottom: 30px;
        }

        .nummer {
            background: #ffc400;
            color: #071a33;
            width: 58px;
            height: 58px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 24px;
            flex-shrink: 0;
        }

        .antwort {
            display: block;
            background: #153866;
            border: 2px solid #254b80;
            border-radius: 14px;
            padding: 18px 22px;
            margin: 14px 0;
            font-size: 19px;
            cursor: pointer;
            transition: 0.2s;
        }

        .antwort:hover {
            border-color: #ffc400;
            background: #1b477f;
        }

        input[type="radio"] {
            margin-right: 15px;
            accent-color: #ffc400;
            transform: scale(1.3);
        }

        .submit-btn {
            background: #ffc400;
            color: #071a33;
            border: none;
            padding: 18px 35px;
            border-radius: 12px;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
            float: right;
            margin-bottom: 50px;
        }

        .submit-btn:hover {
            background: #ffdd33;
        }

        .tipp {
            clear: both;
            background: #0b2447;
            border: 1px solid #254b80;
            border-radius: 15px;
            padding: 22px;
            color: #d8e3f0;
            font-size: 18px;
            margin-bottom: 40px;
        }

        @media (max-width: 700px) {
            .navbar {
                height: auto;
                flex-direction: column;
                align-items: flex-start;
                padding: 25px;
            }

            .navlinks a {
                display: block;
                margin: 12px 0;
            }

            .result-btn {
                margin-left: 0;
                margin-top: 12px;
            }

            .hero {
                padding: 40px 25px;
            }

            .hero h1 {
                font-size: 38px;
            }

            .quiz-container {
                width: 92%;
            }
        }
    </style>
</head>

<body>

    <div class="navbar">
        <div class="logo">Brain<span>Boost</span></div>

        <div class="navlinks">
            <a href="/">Startseite</a>
            <a href="/mathe">Mathe Quiz</a>
            <a href="/englisch">Englisch Quiz</a>
            <a href="/allgemeinwissen">Allgemeinwissen</a>
        </div>

        <a class="result-btn" href="/ergebnisse">Ergebnisse</a>
    </div>

    <div class="hero">
        <h1>Englisch <span>Quiz</span></h1>
        <p>Teste dein Englisch und verbessere deine Kenntnisse.</p>
    </div>

    <div class="quiz-container">

        <div class="info-row">
            <div>Fragen: {{len(fragen)}}</div>
            <div>Viel Erfolg!</div>
        </div>

        <form action="/auswertung" method="post">

            % for i, frage in enumerate(fragen):
            <div class="frage-box">
                <div class="frage-title">
                    <div class="nummer">{{i+1}}</div>
                    <strong>{{frage["frage"]}}</strong>
                </div>

                % for antwort in frage["antworten"]:
                <label class="antwort">
                    <input type="radio" name="antwort{{i}}" value="{{antwort}}" required>
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

</body>
</html>
