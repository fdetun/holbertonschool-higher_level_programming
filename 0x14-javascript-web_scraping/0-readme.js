#!/usr/bin/node

const fde = require('fs');

fde.readFile('cisfun', 'utf8', function (error, datas) {
  if (data) {
    console.log(datas);
  } else {
    console.log(error);
  }
});
