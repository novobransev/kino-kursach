$(document).ready(() => {
  // setting owl carousel

  let navText = ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-right'></i>"]

  $('#hero-carousel').owlCarousel({
      items: 1,
      dots: false,
      loop: true,
      nav:true,
      navText: navText,
      autoplay: true,
      autoplayHoverPause: true
  });

  $('#favorites-films').owlCarousel({
    items: 2,
    dots: false,
    loop: true,
    nav:true,
    navText: navText,
  });

  $('#buys-films').owlCarousel({
    items: 2,
    dots: false,
    loop: true,
    nav:true,
    navText: navText,
  });
});

