#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  if (!error) {
    const char = JSON.parse(body).characters;
    printCharacter(char, 0);
  }
});

function printCharacter (characters, index) {
  req(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacter(characters, index + 1);
      }
    }
  });
}
