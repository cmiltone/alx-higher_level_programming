$('document').ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.ajax({ url }).done((res) => {
    $('div#hello').html(res.hello);
  })
})