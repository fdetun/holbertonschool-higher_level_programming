#!/usr/bin/node
let i = 2;
const arr = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  while (i < process.argv.length) {
    arr[i - 2] = process.argv[i];
    i++;
  }
  arr.sort(function (a, b) { return a - b; });
  console.log(arr[process.argv.length - 4]);
}
