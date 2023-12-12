#!/usr/bin/node

const fs = require('fs');
let c = '';

c = c.concat(fs.readFileSync(process.argv[2]));
c = c.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], c);
