#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const ab = Number(process.argv[2]);
  let x = 0;
  while (x < ab) {
    console.log('X'.repeat(ab));
    x++;
  }
}
