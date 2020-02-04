#!/usr/bin/node
const process = require('process');

const argv = process.argv;
function factorial (num = 0) {
  if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

const number = argv[2];
console.log(factorial(number));
