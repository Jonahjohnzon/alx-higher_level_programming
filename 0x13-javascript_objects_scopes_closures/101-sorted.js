#!/usr/bin/node
const dic = require('./101-data').dict;

const total = Object.entries(dic);
const val = Object.values(dic);
const valUniq = [...new Set(val)];
const newDict = {};
for (const a in valUniq) {
  const list = [];
  for (const z in total) {
    if (total[z][1] === valUniq[a]) {
      list.unshift(total[z][0]);
    }
  }
  newDict[valUniq[a]] = list;
}
console.log(newDict);
