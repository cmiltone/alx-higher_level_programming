const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.ajax({ url }).done((res) => {
  console.log(res)
  $('div#hello').html(res.hello);
})