#!/usr/bin/node
// print C is fun any times in argv
const process = require('process');

const argv = process.argv;
const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
