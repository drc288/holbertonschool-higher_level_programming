#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], (err, req, body) => {
  if (err) { console.log(err); }

  const films = JSON.parse(body).results;
  const characters = films[0].characters;
  let scope;

  for (const character of characters) {
    if (character.includes('18')) {
      scope = character;
    }
  }

  request(scope, (err, req, body) => {
    if (err) { console.log(err); }
    console.log(JSON.parse(body).films.length);
  });
});
