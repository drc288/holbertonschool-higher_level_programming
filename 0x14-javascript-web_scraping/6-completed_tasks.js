#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], (err, res, body) => {
  if (err) { console.log(err); }
  const dict = {};

  const users = JSON.parse(body);
  for (const user of users) {
    dict[user.userId] = 0;
  }

  for (const user of users) {
    if (user.completed === true) {
      dict[user.userId] += 1;
    }
  }

  console.log(dict);
});
