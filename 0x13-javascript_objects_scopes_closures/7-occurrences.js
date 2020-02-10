#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  for (const val of list) {
    if (val === searchElement) {
      cont += 1;
    }
  }
  return cont;
};
