$(document).ready(() => {
  // setting owl carousel

  let navText = ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-left'></i>"];

  $('#hero-carousel').owlCarousel({
    items: 1,
    dots: false,
    loop: true,
    nav: true,
    navText: navText,
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
      0: {
        items: 1
      },
      850: {
        items: 1
      }
    }
  });

  $('#favorites-films').owlCarousel({
    items: 2,
    dots: false,
    loop: true,
    nav: true,
    navText: navText,
    responsive: {
      0: {
        items: 1
      },
      850: {
        items: 2
      }
    }
  });

  $('#buys-films').owlCarousel({
    items: 2,
    dots: false,
    loop: true,
    nav: true,
    navText: navText,
    responsive: {
      0: {
        items: 1
      },
      850: {
        items: 2
      }
    }
  });
});

