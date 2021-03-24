#!/usr/bin/node

const sorted = new Float64Array(process.argv.slice(2)).sort();

if (process.argv.length < 4) console.log(0);
else console.log(`${Number(sorted[sorted.length - 2])}`);
