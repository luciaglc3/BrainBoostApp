<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Kategorien</title>

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

        .container {
            text-align: center;
        }

        h1 {
            font-size: 48px;
            margin-bottom: 10px;
        }

        .untertitel {
            font-size: 20px;
            margin-bottom: 40px;
        }

        .karten-container {
            display: flex;
            gap: 30px;
            justify-content: center;
        }

        .karte {
            width: 260px;
            height: 200px;
            background: rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 25px;
            text-decoration: none;
            color: white;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            transition: 0.2s;
        }

        .karte:hover {
            transform: translateY(-5px);
            background: rgba(255,255,255,0.25);
        }

        .icon {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .zurueck {
            display: inline-block;
            margin-top: 30px;
            color: #ffd000;
            text-decoration: none;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>Wähle eine Kategorie</h1>
    <p class="untertitel">Entscheide dich für ein Themengebiet und starte dein Quiz.</p>

    <div class="karten-container">

        <a href="/mathe" class="karte">
            <div class="icon">➗</div>
            <h2>Mathematik</h2>
            <p>Teste dein Wissen in Zahlen, Rechnen und Logik.</p>
        </a>

        <a href="/allgemeinwissen" class="karte">
            <div class="icon">🌍</div>
            <h2>Allgemeinwissen</h2>
            <p>Fragen zu Ländern, Natur, Geschichte und mehr.</p>
        </a>

        <a href="/englisch" class="karte">
            <div class="icon">🇬🇧</div>
            <h2>Englisch</h2>
            <p>Trainiere Vokabeln, Grammatik und Sprachverständnis.</p>
        </a>

    </div>

    <a href="/" class="zurueck">← Zurück zur Startseite</a>

</div>

</body>
</html>
