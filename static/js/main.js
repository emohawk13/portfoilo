$(document).ready(function () {
  // Show the modal when the contact button is clicked
  $('.contact-button').click(function () {
      $('#contactModal').modal('show');
  });
});

// JavaScript for the navbar visibility on scroll
window.addEventListener("scroll", function() {
  var navbar = document.getElementById("navbar");
  var parallaxContainer = document.querySelector(".parallax-container");
  var parallaxContainerHeight = parallaxContainer.offsetHeight;

  if (window.pageYOffset > parallaxContainerHeight) {
      navbar.classList.add("visible");
  } else {
      navbar.classList.remove("visible");
  }
});