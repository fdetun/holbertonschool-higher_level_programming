#!/usr/bin/node
console.log(require('./100-data').list.map(x => require('./100-data').list.indexOf(x) * x));
