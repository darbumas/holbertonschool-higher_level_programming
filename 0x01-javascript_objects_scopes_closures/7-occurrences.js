#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (const i of list) {
    if (i === searchElement) {
      n++;
    }
  }
  return n;
};
