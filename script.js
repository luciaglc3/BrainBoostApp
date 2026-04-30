

function updateProgress() {
    let answered = document.querySelectorAll('input[type="radio"]:checked').length;
    let total = 20;

    let percent = Math.round((answered / total) * 100);

    document.getElementById("progress-fill").style.width = percent + "%";
    document.getElementById("progress-text").innerText = answered + " / " + total;
    document.getElementById("progress-percent").innerText = percent + "%";
}

document.querySelectorAll('input[type="radio"]').forEach(input => {
    input.addEventListener('change', updateProgress);
});