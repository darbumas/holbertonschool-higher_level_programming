#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  for (const i of list) {
    tsil.unshift(i);
  }
  return tsil;
};
