#!/usr/bin/node

if (isNaN(Number(process.argv[2]))) console.log(0);
else console.log(`${Math.max.apply(Math, process.argv.slice(2))}`);
