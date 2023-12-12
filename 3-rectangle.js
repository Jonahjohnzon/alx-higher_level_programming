#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((h > 0) && (w > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let b = 0; b < this.height; b++) {
      let s = '';
      for (let ca = 0; ca < this.width; ca++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
