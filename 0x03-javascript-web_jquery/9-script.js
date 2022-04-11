const url = 'https://fourtonfish.com/hellosalut/?lang=fr'
$.getJSON(url, function (data) {
  $('#hello').text(data.hello);
});
