
// for path: app/templates/layouts/partials/_music_widget.html
function toggleMusic() {
    var audio = document.getElementById("bgm-player");
    var icon = document.getElementById("music-icon");
    if (audio.paused) {
        audio.play();
        icon.innerHTML = '<i class="fas fa-pause"></i>';
    } else {
        audio.pause();
        icon.innerHTML = '<i class="fas fa-play"></i>';
    }
}

// end | for path: app/templates/layouts/partials/_music_widget.html