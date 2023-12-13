#!/usr/bin/node
let pr = parseInt(process.argv[2]);
if (isNaN(pr) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (pr > 0) {
    console.log('C is fun');
    pr--;
  }
}
