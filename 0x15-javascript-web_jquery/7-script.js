$('document').ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.ajax(url).done((res) => {
    $('div#character').html(res.name);
  });
});
