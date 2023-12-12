#!/usr/bin/node
const dict = require('./101-data').dict;
const newd = {};

Object.keys(dict).map(function (key) {
  if (!Array.isArray(newd[dict[key]])) {
    newd[dict[key]] = [];
  }
  newd[dict[key]].push(key);
});

console.log(newd);
