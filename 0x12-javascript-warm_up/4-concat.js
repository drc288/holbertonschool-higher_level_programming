#!/usr/bin/node
// concatenate argv[2] argv[3]
const process = require('process');

const argv = process.argv;
let ar1, ar2;
if (argv[2] == null) {
  ar1 = 'undefined';
} else {
  ar1 = argv[2];
}
if (argv[3] == null) {
  ar2 = 'undefined';
} else {
  ar2 = argv[3];
}
console.log(`${ar1} is ${ar2}`);
