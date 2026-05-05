let timeLeft = 480;

function updateTimer() {
    const timer = document.getElementById("timer");

    if (timer) {
        let minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;

        timer.innerText =
            "Zeit: " + minutes + ":" + (seconds < 10 ? "0" + seconds : seconds);

        if (timeLeft > 0) {
            timeLeft--;
        } else {
            const form = document.querySelector("form");
            if (form) form.submit();
        }
    }
}

function updateProgress() {
    const answered = document.querySelectorAll('input[type="radio"]:checked').length;
    const total = 20;
    const percent = Math.round((answered / total) * 100);

    const fill = document.getElementById("progress-fill");
    const text = document.getElementById("progress-text");
    const percentText = document.getElementById("progress-percent");

    if (fill) fill.style.width = percent + "%";
    if (text) text.innerText = answered + " / " + total;
    if (percentText) percentText.innerText = percent + "%";
}

document.querySelectorAll('input[type="radio"]').forEach(input => {
    input.addEventListener("change", updateProgress);
});

setInterval(updateTimer, 1000);
updateTimer();
updateProgress();
