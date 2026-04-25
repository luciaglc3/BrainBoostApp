<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>BrainBoost</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            min-height: 100vh;
            background: linear-gradient(135deg, #07182f, #123c69, #1b75bc);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .page {
            width: 90%;
            max-width: 1100px;
            display: flex;
            gap: 40px;
            align-items: center;
        }

        .left {
            flex: 1;
        }

        .badge {
            background: rgba(255,255,255,0.15);
            padding: 8px 14px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 20px;
            font-size: 14px;
        }

        h1 {
            font-size: 58px;
            margin: 0 0 15px 0;
        }

        h2 {
            font-size: 24px;
            margin-bottom: 20px;
            color: #ffd84d;
        }

        p {
            font-size: 18px;
            line-height: 1.6;
            color: #e6e6e6;
        }

        .features {
            margin-top: 25px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .feature {
            background: rgba(255,255,255,0.12);
            padding: 15px;
            border-radius: 14px;
        }

        .right {
            width: 360px;
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            border-radius: 25px;
            padding: 35px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.35);
            text-align: center;
        }

        .brain {
            font-size: 70px;
            margin-bottom: 15px;
        }

        .button {
            display: inline-block;
            margin-top: 25px;
            padding: 15px 30px;
            background: #ffd000;
            color: #1b1b1b;
            text-decoration: none;
            border-radius: 12px;
            font-weight: bold;
            font-size: 17px;
            transition: 0.2s;
        }

        .button:hover {
            background: #ffea70;
            transform: scale(1.05);
        }
    </style>
</head>

<body>

<div class="page">

    <div class="left">
        <div class="badge">Interaktive Lern-App für Schüler</div>

        <h1>BrainBoost</h1>
        <h2>Trainiere dein Wissen. Teste dich selbst. Verbessere dein Ergebnis.</h2>

        <p>
            BrainBoost ist eine digitale Lern-App für Schülerinnen und Schüler der Klassenstufen 8 bis 10.
            Die App hilft dabei, Wissen in verschiedenen Bereichen wie Englisch, Mathematik und Allgemeinwissen
            spielerisch zu überprüfen.
        </p>

        <p>
            Bei jedem Test werden zufällige Fragen aus einem größeren Fragenpool ausgewählt.
            Dadurch ist jeder Durchgang etwas anders und die Nutzer können ihr Wissen mehrfach testen,
            ohne immer dieselben Aufgaben zu bekommen.
        </p>

        <div class="features">
            <div class="feature">✅ Zufällige Fragen</div>
            <div class="feature">✅ Punktesystem</div>
            <div class="feature">✅ Mehrere Kategorien</div>
            <div class="feature">✅ Direktes Ergebnis</div>
        </div>
    </div>

    <div class="right">
        <div class="brain">🧠</div>
        <h2>Bereit für den Test?</h2>
        <p>
            Starte jetzt und finde heraus, wie gut dein Wissen wirklich ist.
        </p>

        <a href="/kategorien" class="button">Test starten</a>
    </div>

</div>

</body>
</html>
