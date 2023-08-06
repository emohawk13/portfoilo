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


// Function to generate Lorem Ipsum paragraph
function generateLoremParagraph() {
  // Number of sentences in the paragraph (change as needed)
  const numSentences = 4;

  // Lorem Ipsum text generator
  function generateLoremText() {
      return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.";
  }

  let paragraph = "";
  for (let i = 0; i < numSentences; i++) {
      paragraph += generateLoremText() + " ";
  }

  return paragraph;
}

// Insert the generated Lorem Ipsum paragraph into the div with id "lorem-text"
document.getElementById("lorem-text").textContent = generateLoremParagraph();