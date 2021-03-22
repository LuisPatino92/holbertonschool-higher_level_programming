#!/usr/bin/node

let repeats = Number(process.argv[2]);

if (isNaN(repeats)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < repeats; i++) {
    console.log('C is fun');
  }
}
