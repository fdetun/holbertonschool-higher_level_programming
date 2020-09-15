#!/usr/bin/node
function fac (x) {
  if (x === 1) {
    return x;
  } else {
    return x * fac(x - 1);
  }
}
if (process.argv[2]) {
  console.log(fac(process.argv[2]));
} else {
  console.log(1);
}
