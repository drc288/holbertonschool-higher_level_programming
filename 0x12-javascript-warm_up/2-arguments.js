#!/usr/bin/node
// Detect the argv and print argument found
// or No argument if not find
const process = require('process');

const argv = process.argv;
if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length >= 4) {
  console.log('Arguments found');
}
