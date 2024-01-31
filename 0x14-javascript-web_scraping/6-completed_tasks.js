#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const complete = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (complete[task.userId] === undefined) {
          complete[task.userId] = 1;
        } else {
          complete[task.userId]++;
        }
      }
    }
    console.log(complete);
  } else {
    console.log('An error occured. Status code: ' + res.statusCode);
  }
});
