$('document').ready(function () {
  $('div#toggle_header').on('click', () => {
    $('header').toggleClass('red');
    $('header').toggleClass('green');
  });
});
