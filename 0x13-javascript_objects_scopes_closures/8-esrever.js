#!/usr/bin/node

exports.esrever = function (list) {
  let totalArray = list.length - 1;
  const newList = [];
  for (totalArray; totalArray >= 0; totalArray--) {
    newList.push(list[totalArray]);
  }
  return newList;
};
