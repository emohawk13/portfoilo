$('.contact-button').click(function (event) {
  event.preventDefault();  // Prevent the default action
  $('#contactModal').modal('show');
});

document.querySelector(".btn.btn-primary").addEventListener("click", function (event) {
  // Prevent the default form submission temporarily
  event.preventDefault();

  // AJAX request to Flask to record button press
  fetch('/button_pressed', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ button: "contact_button" })
  })
    .then(response => response.json())
    .then(data => {
      console.log(data.message);

      // After recording the button press, submit the form
      event.target.closest('form').submit();
    });
});

