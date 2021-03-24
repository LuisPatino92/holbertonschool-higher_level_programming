#!/usr/bin/node

const list = require('./100-data').list;
let i = -1;

const list2 = list.map(function (x) {
  i++;
  return (x * i);
});

console.log(list);
console.log(list2);
