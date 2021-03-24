#!/usr/bin/node

const originalDict = require('./101-data').dict;

const newObj = {};

for (const element in originalDict) {
  if (newObj[originalDict[element]] === undefined) {
    newObj[originalDict[element]] = [];
  }
  newObj[originalDict[element]].push(element);
}

console.log(newObj);
