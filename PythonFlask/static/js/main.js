(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var navLinks = document.querySelector(".nav-links");

  if (toggle && navLinks) {
    toggle.addEventListener("click", function () {
      navLinks.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", navLinks.classList.contains("is-open"));
    });
  }
})();
