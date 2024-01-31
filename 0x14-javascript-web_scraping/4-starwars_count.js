#!/usr/bin/node

const req = require('request');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    const r = JSON.parse(body).results;
    console.log(r.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
