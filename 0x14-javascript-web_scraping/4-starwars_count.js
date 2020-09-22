#!/usr/bin/node
const request = require('request');
var sum = 0;
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
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
