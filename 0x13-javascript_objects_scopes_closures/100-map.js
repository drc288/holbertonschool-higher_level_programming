#!/usr/bin/node
const data = require('./100-data').list;

console.log(data);
const up = data.map((x, index) => x * index);
console.log(up);
