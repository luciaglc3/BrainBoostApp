
<!DOCTYPE html>
<html>
<head>
    <title>Englisch Quiz</title>
</head>
<body>

<h1>Englisch Quiz</h1>

<form action="/auswertung" method="post">

% for i, frage in enumerate(fragen):
    <h3>{{i+1}}. {{frage["frage"]}}</h3>

    % for antwort in frage["antworten"]:
        <label>
            <input type="radio" name="frage{{i}}" value="{{antwort}}">
            {{antwort}}
        </label><br>
    % end
% end

<br>
<button type="submit">Test abgeben</button>

</form>

</body>
</html>