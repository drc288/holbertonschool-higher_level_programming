#!/usr/bin/node
// Convert the number
const process = require('process');

const argv = process.argv;
let toNum;
if (argv.length === 2) {
  console.log('Not a number');
} else if (argv.length === 3) {
  toNum = parseInt(argv[2]);
  if (isNaN(toNum)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${toNum}`);
  }
}
