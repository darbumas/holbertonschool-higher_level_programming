const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (json) {
  json.results.forEach(function (movie) {
    $('#list_movies').append('<Li>' + movie.title + '</Li>');
  });
});
