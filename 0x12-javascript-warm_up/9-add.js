#!/usr/bin/node
const process = require('process');

const argv = process.argv;

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return 'NaN';
  } else {
    return `${a + b}`;
  }
}

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
console.log(add(a, b));
