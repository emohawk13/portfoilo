// stuff for the sideMenu bar
const sideMenuTab = document.getElementById("sideMenuTab");
const sideMenu = document.getElementById("sideMenu");
const contents = document.querySelectorAll(".content.container");

sideMenuTab.addEventListener("click", () => {
    sideMenu.classList.toggle("expanded");
    contents.forEach(content => {
        content.classList.toggle("expanded");
        animateMenuItems();
    });
});

$(document).ready(function () {
    $('#contactButton').click(function () {
        $('#contactModal').modal('show');
    });
});

document.getElementById("testButton").addEventListener("click", function () {
    window.location.href = "/test";
});

function animateMenuItems() {
    const menuItems = document.querySelectorAll('.side-menu li');
    menuItems.forEach((item, index) => {
        item.style.transitionDelay = `${index * 0.1}s`; // Delay for staggered effect
    });
}