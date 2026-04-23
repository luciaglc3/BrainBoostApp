 <!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kategorien - BrainBoost</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e293b, #334155);
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container {
            max-width: 900px;
            width: 90%;
            text-align: center;
        }

        h1 {
            font-size: 42px;
            margin-bottom: 10px;
        }

        p {
            font-size: 18px;
            color: #cbd5e1;
            margin-bottom: 40px;
        }

        .cards {
            display: flex;
            justify-content: center;
            gap: 25px;
            flex-wrap: wrap;
        }

        .card {
            background: rgba(255, 255, 255, 0.08);
            width: 220px;
            padding: 30px 20px;
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.25);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
            background: rgba(255, 255, 255, 0.14);
        }

        .icon {
            font-size: 50px;
            margin-bottom: 15px;
        }

        .title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .text {
            font-size: 16px;
            color: #e2e8f0;
        }

        .back-link {
            display: inline-block;
            margin-top: 40px;
            text-decoration: none;
            color: #facc15;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Wähle eine Kategorie</h1>
        <p>Entscheide dich für ein Themengebiet und starte dein Quiz.</p>

        <div class="cards">
            <div class="card">
                <div class="icon">➗</div>
                <div class="title">Mathematik</div>
                <div class="text">Teste dein Wissen in Zahlen, Rechnen und Logik.</div>
            </div>


<a href="/quiz/allgemein" style="text-decoration: none; color: white;">
    <div class="card">
        <div class="icon">🌍</div>
        <div class="title">Allgemeinwissen</div>
        <div class="text">Fragen zu Ländern, Natur, Geschichte und mehr.</div>
    </div>
</a>


            
            <div class="card">
                <div class="icon">🇬🇧</div>
                <div class="title">Englisch</div>
                <div class="text">Trainiere Vokabeln, Grammatik und Sprachverständnis.</div>
            </div>
        </div>

        <a class="back-link" href="/">← Zurück zur Startseite</a>
    </div>
</body>
</html>