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
