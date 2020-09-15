#!/usr/bin/node

function add (a, b) {
  return a + b;
}
if (process.argv.length === 4) {
  console.log(add(parseInt(process.argv[2], 10), parseInt(process.argv[3], 10)));
} else {
  console.log('NaN');
}
