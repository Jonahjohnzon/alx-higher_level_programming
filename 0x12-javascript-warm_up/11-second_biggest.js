#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const i = [];
  for (let x = 2; x < size; x++) {
    i[x - 2] = parseInt(process.argv[x]);
  }
  ints.sort(function (a, b) { return b - a; });
  console.log(i[1]);
}
