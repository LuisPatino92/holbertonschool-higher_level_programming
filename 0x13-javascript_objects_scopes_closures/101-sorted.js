#!/usr/bin/node

const originalDict = require('./101-data').dict;

const newObj = {};

for (let element in originalDict) {
  if (newObj[originalDict[element]] === undefined) {
    newObj[originalDict[element]] = [];
  }
  newObj[originalDict[element]].push(element);
}

console.log(originalDict);
console.log(newObj);