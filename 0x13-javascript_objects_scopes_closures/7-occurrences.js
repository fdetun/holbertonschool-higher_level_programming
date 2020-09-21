#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let occur = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      occur += 1;
    }
    i++;
  }
  return occur;
};
