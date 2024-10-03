function showProgress() {
    document.getElementById("progressBar").style.display = "block";
    var progress = document.getElementById("progress");
    var percent = 0;
    var interval = setInterval(function() {
        percent += Math.random() * 10;
        if (percent > 100) {
            percent = 100;
            clearInterval(interval);
        }
        progress.style.width = percent + "%";
        progress.innerHTML = Math.round(percent) + "%";
    }, 500);
}
