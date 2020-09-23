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
  for (const cn of JSON.parse(body).characters) {
    let nl = {
      url: cn + '?format=json',
      method: 'GET'
    };
    request(nl, (err, reponse, ok) => {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(ok).name);
    });
  }
});
