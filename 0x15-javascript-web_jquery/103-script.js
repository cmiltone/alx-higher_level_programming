$('document').ready(function () {
  function get () {
    const lang = $('input#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
    $.ajax({ url }).done((res) => {
      $('div#hello').html(res.hello);
    });
  }

  $('input#btn_translate').on('click', get);

  $('inpu#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        get();
      }
    });
  });
});
