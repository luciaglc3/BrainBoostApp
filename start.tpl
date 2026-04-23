<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>BrainBoost</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(270deg, #0f172a, #1e3a8a, #0f172a);
    background-size: 600% 600%;
    animation: gradientMove 10s ease infinite;
    color: white;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.bg-icon {
    position: absolute;
    font-size: 200px;
    opacity: 0.07;
    top: 20%;
    left: 20%;
    animation: float 6s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}

.container {
    background: rgba(255,255,255,0.1);
    padding: 40px;
    border-radius: 15px;
    text-align: center;
}

.start-button {
    display: inline-block;
    margin-top: 20px;
    padding: 15px 30px;
    background: #facc15;
    color: black;
    text-decoration: none;
    border-radius: 10px;
}
</style>
</head>

<body>

<div class="bg-icon">🧠</div>

<div class="container">
    <h1>BrainBoost</h1>
    <p>Teste dein Wissen und sammle Punkte</p>
    <p>Geeignet für die Klassenstufen 8 bis 10</p>

    <a class="start-button" href="/kategorien">Starte jetzt</a>
</div>

</body>
</html>
