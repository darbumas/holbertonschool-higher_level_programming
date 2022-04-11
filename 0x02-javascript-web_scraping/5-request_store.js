#!/usr/bin/node

const req = require('request');
const fs = require('fs');

req(process.argv[2], function (err, response, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
    if (err) throw err;
  });
});
