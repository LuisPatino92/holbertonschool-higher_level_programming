#!/usr/bin/node

if (process.argv.length < 4) console.log(`${0}`);
else console.log(`${Math.max.apply(Math, process.argv.slice(2))}`);
