#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
req(url, function (err, response, body) {
  if (err) throw err;
  let num = 0;
  for (const movie of JSON.parse(body).results) {
    for (const character of movie.characters) {
      if (character.endsWith('/18/')) {
        num++;
      }
    }
  }
  console.log(num);
});
