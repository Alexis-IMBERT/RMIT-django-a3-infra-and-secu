$(document).ready(function() {
    var input = document.querySelector("#phone");
    var iti = window.intlTelInput(input, {
      initialCountry: "auto",
      separateDialCode: true,
      formatOnDisplay: true,
      nationalMode: false,
      preferredCountries: ["us", "gb"],  // Optional: Specify preferred countries
      utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js"
    });
  });

