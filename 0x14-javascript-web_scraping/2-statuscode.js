#!/usr/bin/node
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, reponse) => {
  if (err) {
    return console.log(err);
  }
  console.log('code: ' + reponse.statusCode);
});
