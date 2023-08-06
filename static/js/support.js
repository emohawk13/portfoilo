// support.js
function redirectToHome() {
    var homeUrl = "/goHome" ;
    setTimeout(function () {
        window.location.href = homeUrl;
    }, 5000); // 5 seconds (5000 milliseconds)
}

// Call redirectToHome function when the page is fully loaded
window.onload = function () {
    redirectToHome();
};