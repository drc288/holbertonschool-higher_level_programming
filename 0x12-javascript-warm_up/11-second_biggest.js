#!/usr/bin/node
const process = require('process');

const argv = process.argv;
const argc = argv.length;
let newArray = [];

if (argc === 2) {
  console.log(0);
} else if (argc === 3) {
  console.log(0);
} else {
  for (let i = 2; i < argc; i++) {
    newArray.push(argv[i]);
  }
  const unique = new Set(newArray);
  newArray = [...unique].sort();
  const lenArray = newArray.length;
  console.log(newArray[lenArray - 2]);
}
