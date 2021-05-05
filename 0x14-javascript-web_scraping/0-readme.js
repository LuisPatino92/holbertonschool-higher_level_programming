#!/usr/bin/node

const fs = require('fs');

const content = fs.readFileSync('cisfun', 'utf-8');

console.log(content);
