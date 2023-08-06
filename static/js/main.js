$(document).ready(function () {
  // Show the modal when the contact button is clicked
  $('.contact-button').click(function () {
      $('#contactModal').modal('show');
  });
});

  document.addEventListener("DOMContentLoaded", function () {
    const wrapper = document.getElementById("mainWrapper");
    const navMenu = document.querySelector(".navMenu");

    // Add scroll event listener to the wrapper
    wrapper.addEventListener("scroll", function () {
      // Adjust the scrollOffset value according to when you want to show the navbar
      const scrollOffset = 400;

      if (wrapper.scrollTop > scrollOffset) {
        navMenu.classList.remove("hidden-navbar");
      } else {
        navMenu.classList.add("hidden-navbar");
      }
    });
  });


