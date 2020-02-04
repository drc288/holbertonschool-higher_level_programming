#!/usr/bin/node
// verifi if exists the data an print
const process = require('process');

const argv = process.argv;
if (argv[2] == null) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
