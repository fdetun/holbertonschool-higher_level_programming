#!/usr/bin/node
const request = require('request');
let sum = 0;
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, reponse, body) => {
  if (err) {
    return console.log(err);
  }
  for (const i of JSON.parse(body).results) {
    for (const j of i.characters) {
      if (j.search('api/people/18/') > 0) {
        sum += 1;
      }
    }
  }
  console.log(sum);
});
