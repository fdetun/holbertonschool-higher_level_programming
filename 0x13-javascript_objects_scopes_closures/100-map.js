#!/usr/bin/node
const i = require('./100-data').list;
console.log(i);
console.log(i.map(x => i.indexOf(x) * x));
