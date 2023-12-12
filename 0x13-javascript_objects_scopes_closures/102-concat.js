#!/usr/bin/node

const f = require('fs');

const fA= f.readFileSync(process.argv[2]).toString();
const sA = f.readFileSync(process.argv[3]).toString();
f.writeFileSync(process.argv[4], fA + sA);
