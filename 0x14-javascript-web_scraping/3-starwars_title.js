#!/usr/bin/node

const request = require('request');

const elements = ['https://swapi-api.hbtn.io/api/films/', process.argv[2]];

const url = elements.join('');

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
