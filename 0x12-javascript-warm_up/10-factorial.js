#!/usr/bin/node

function fact (num) {
  if (isNaN(num) || num === 0) return (1);
  else return (fact(num - 1) * num);
}

console.log(`${fact(Number(process.argv[2]))}`)
