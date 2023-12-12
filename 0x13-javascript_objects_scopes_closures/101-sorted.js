#!/usr/bin/node
const dic = require('./101-data').dict;
const newd = {};

Object.keys(dic).map(function (key) {
  if (!Array.isArray(newd[dic[key]])) {
    newd[dic[key]] = [];
  }
  newd[dic[key]].push(key);
});

console.log(newd);
