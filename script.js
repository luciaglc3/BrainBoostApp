document.addEventListener("DOMContentLoaded", function () {

    function updateProgress() {
        let answered = document.querySelectorAll('input[type="radio"]:checked').length;
        let total = 20;
        let percent = Math.round((answered / total) * 100);

        document.getElementById("progress-fill").style.width = percent + "%";
        document.getElementById("progress-text").innerText = answered + " / " + total;
        document.getElementById("progress-percent").innerText = percent + "%";
    }

    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.addEventListener("change", updateProgress);
    });

    updateProgress();

    let timeLeft = 8 * 60;

    function updateTimer() {
        let timer = document.getElementById("timer");

        let minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;

        timer.innerText =
            String(minutes).padStart(2, "0") + ":" + String(seconds).padStart(2, "0");

        if (timeLeft <= 0) {
            let form = document.querySelector("form");
            if (form) {
                form.submit();
            }
            return;
        }

        timeLeft--;
    }

    updateTimer();
    setInterval(updateTimer, 1000);

});
