#!/usr/bin/node
const request = require('request');

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/?format=json',
  method: 'GET'
};

request(options, (err, reponse, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
