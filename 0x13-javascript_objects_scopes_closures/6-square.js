#!/usr/bin/node

const PrevSquare = require('./5-square');

module.exports = class Square extends PrevSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
