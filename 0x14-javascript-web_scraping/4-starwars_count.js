#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const episodes = JSON.parse(body).results;
  let total = 0;
  for (const element of episodes) {
    const episodeChars = element.characters;
    for (const char of episodeChars) {
      if (Number(char.split('/')[5]) === 18) {
        total += 1;
      }
    }
  }
  console.log(total);
});
