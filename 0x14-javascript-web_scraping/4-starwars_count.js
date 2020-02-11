#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], (err, req, body) => {
  if (err) { console.log(err); }
  const countList = [];
  const films = JSON.parse(body).results;

  for (const film of films) {
    const characters = film.characters;
    for (const character of characters) {
      if (character.includes('18')) {
        countList.push(character);
      }
    }
  }
  console.log(countList.length);
});
