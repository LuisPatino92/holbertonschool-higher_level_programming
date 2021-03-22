#!/usr/bin/node

if (process.argv.length < 4) console.log(`${0}`);
else console.log(`${Number(process.argv.slice(2).sort()[process.argv.slice(2).length - 2])}`);
