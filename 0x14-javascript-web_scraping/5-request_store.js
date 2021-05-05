#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  fs.writeFileSync(process.argv[3], response.body);
});
