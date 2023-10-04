$('document').ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.ajax(url).done((res) => {
    for (let i = 0; i < res.results.length; i++) {
      const el = res.results[i];
      $('ul#list_movies').append(`<li>${el.title}</li>`);
    }
  });
});
