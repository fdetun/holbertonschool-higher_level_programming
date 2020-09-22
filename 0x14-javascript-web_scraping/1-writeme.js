#!/usr/bin/node
const fs = require('fs');

const datas = process.argv[3];

fs.writeFile(process.argv[2], datas,
  {
    encoding: 'utf8',
    flag: 'w'
  },
  (err) => {
    if (err) { console.log(err); }
  });
