#!/usr/bin/node
exports.converter = function (base) {
  return function myConverter (i) {
    return i.toString(base);
  };
};
