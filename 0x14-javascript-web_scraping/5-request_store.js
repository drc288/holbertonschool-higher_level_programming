#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');

request(process.argv[2], (err, res, body) => {
  if (err) { console.log(err); }
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) { console.log(err); }
  });
});
