#!/usr/bin/node

let session = 0;
exports.logMe = function (item) {
  console.log(`${session++}: ${item}`);
};
