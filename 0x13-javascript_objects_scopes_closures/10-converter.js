#!/usr/bin/node

exports.converter = function (base) {
  return (doom) => doom.toString(base);
};
