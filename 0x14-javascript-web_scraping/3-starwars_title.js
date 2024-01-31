#!/usr/bin/node

const req = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

req(API_URL + episodeNum, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
