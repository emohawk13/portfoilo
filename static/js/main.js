document.addEventListener('DOMContentLoaded', function () {
  const hamburgerIcon = document.querySelector('.hamburger-icon');
  const menu = document.querySelector('.menu');

  function handleMenuToggle() {
    menu.classList.toggle('show-menu');
  }

  hamburgerIcon.addEventListener('click', handleMenuToggle);

  // Adjust menu display based on screen size
  const mediaQuery = window.matchMedia('(max-width: 1038px) and (max-height: 799px)');
  const nav = document.querySelector('nav');
  const socialBar = document.querySelector('.social');

  function handleMenuDisplay(mediaQuery) {
    if (mediaQuery.matches) {
      menu.style.display = 'block';
      nav.style.display = 'none';
      socialBar.style.display = 'none';;
    } else {
      menu.style.display = 'none';
      nav.style.display = 'block';
      socialBar.style.display = 'block';
    }
  }

  handleMenuDisplay(mediaQuery);

  // Add event listener for media query changes
  mediaQuery.addEventListener('change', function (event) {
    handleMenuDisplay(event.target);
  });

  // Close the menu when a menu item is clicked
  const menuItems = document.querySelectorAll('.menu li a');

  menuItems.forEach(function (menuItem) {
    menuItem.addEventListener('click', function () {
      menu.classList.remove('show-menu');
    });
  });
});


/*menu.style.display = 'block';
          nav.style.display = 'none';
          socialBar.style.display = 'none';*/

/*menu.style.display = 'none';
nav.style.display = 'block';
socialBar.style.display = 'block';*/