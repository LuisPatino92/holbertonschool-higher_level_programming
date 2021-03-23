#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!isNaN(Number(w)) && !isNaN(Number(h)) && Number(w) > 0 && Number(h) > 0) {
      this.width = Number(w);
      this.height = Number(h);
    }
  }
}

module.exports = Rectangle;
