#!/usr/bin/node

const repeats = Number(process.argv[2]);

if (isNaN(repeats)) {
  console.log('Missing number of occurrences');
} else if (repeats > 0) {
  for (let i = 0; i < repeats; i++) {
    console.log('X'.repeat(repeats));
  }
}
