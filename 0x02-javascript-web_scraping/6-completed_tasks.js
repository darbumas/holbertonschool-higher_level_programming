#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const usr = {};
    JSON.parse(body).forEach(function (task) {
      if (task.completed) {
        const id = task.userId;
        if (!(id in usr)) {
          usr[id] = 0;
        }
        usr[id] += 1;
      }
    });
    console.log(usr);
  }
});
