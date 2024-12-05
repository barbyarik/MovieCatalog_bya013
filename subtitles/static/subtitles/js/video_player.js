let player;
(function onYouTubeIframeAPIReady() {
    player = new YT.Player('youtube_video', {
        events: {
            'onReady': onPlayerReady
        }
    });
})();

function onPlayerReady(event) {
    player.playVideo();
    setInterval(updateSubtitle, 100);
}

function findCurrentSubtitleIndex(subtitles, currentTime) {
    let left = 0;
    let right = subtitles.length - 1;
    let mid;

    while (left <= right) {
        mid = Math.floor((left + right) / 2);
        if (subtitles[mid].start_time <= currentTime && subtitles[mid].end_time > currentTime) {
            return mid;
        } else if (subtitles[mid].start_time > currentTime) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}

function updateSubtitle() {
    const currentTime = player.getCurrentTime();
    const index = findCurrentSubtitleIndex(subtitles, currentTime);
    const subtitleElement = document.getElementById('subtitle');

    if (index !== -1) {
        let subtitleText = subtitles[index].text;
        if (subtitles[index].character) {
            subtitleElement.innerHTML = `<strong>${subtitles[index].character}</strong>: ${subtitleText}`;
        } else {
            subtitleElement.innerHTML = `<i>${subtitleText}</i>`;
        }
        subtitleElement.style.display = 'block';
    } else {
        subtitleElement.style.display = 'none';
    }
}