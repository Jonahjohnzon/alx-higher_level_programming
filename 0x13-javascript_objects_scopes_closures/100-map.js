#!/usr/bin/node

const lists = require('./100-data.js').list;
console.log(lists);
console.log(lists.map((items, i) => items * i));
