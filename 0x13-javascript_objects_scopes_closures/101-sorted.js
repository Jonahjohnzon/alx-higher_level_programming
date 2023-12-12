#!/usr/bin/node

const dict = require('./101-data').dict;
const newD = {};

Object.keys(dict).map(function (key) {
  if (!Array.isArray(newD[dict[key]])) {
    newD[dict[key]] = [];
  }
  newD[dict[key]].push(key);
});

console.log(newD);
