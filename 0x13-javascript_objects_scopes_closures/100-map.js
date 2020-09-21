#!/usr/bin/node
const i = require('./100-data').list;
const j = [];
i.map(x => j.push(i.indexOf(x) * x));
console.log(i);
console.log(j);
