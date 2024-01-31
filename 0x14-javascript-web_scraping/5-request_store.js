#!/usr/bin/node

const fs = require('fs');
const re = require('request');
req(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
