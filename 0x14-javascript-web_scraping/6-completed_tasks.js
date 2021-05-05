#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const toDos = JSON.parse(body);
  const result = {};
  for (const task of toDos) {
    result[task.userId] = 0;
  }
  for (const task of toDos) {
    if (task.completed === true) {
      result[task.userId] += 1;
    }
  }
  const newDict = {};
  for (const element of Object.keys(result)) {
    if (result[element] !== 0) {
      newDict[element] = result[element];
    }
  }
  console.log(newDict);
});
