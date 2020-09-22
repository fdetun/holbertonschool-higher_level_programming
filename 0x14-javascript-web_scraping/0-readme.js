#!/usr/bin/node

const fde = require('fs');

fde.readFile(process.argv[2], 'utf8', function (error, datas) {
  if (error) {
    console.log(error);
  } else {
    console.log(datas);
  }
});
