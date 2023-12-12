#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];

  for (let ia = list.length - 1; ia >= 0; --ia) {
    rev.push(list[ia]);
  }

  return rev;
};
