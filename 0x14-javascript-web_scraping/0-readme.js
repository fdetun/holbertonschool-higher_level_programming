#!/usr/bin/node

const fde = require('fs');

fde.readFile(process.argv[2], 'utf8', function (error, datas) {
  if (datas) {
    console.log(datas);
  } else {
    console.log(error);
  }
});
