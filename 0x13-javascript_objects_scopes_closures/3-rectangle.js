#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!isNaN(Number(w)) && !isNaN(Number(h)) && Number(w) > 0 && Number(h) > 0) {
      this.width = Number(w);
      this.height = Number(h);
    }
  }

  // method to print a representation of the rectangle //
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log("X".repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
