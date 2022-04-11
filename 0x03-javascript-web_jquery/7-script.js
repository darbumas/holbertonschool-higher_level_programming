const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(url, {
  tags: 'name'
}, function (json) {
  $('#character').text(json.name);
});
