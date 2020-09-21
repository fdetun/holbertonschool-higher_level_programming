#!/usr/bin/node
const i = require('./100-data').list;
let j = []
j = i.map(x => i.indexOf(x) * x)
console.log(i);
console.log(j);
