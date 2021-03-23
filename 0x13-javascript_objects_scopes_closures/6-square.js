#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // Method to change the char to render the square //
  charPrint (c) {
    if (this.width && this.height) {
      if (c) {
        for (let i = 0; i < this.height; i++) {
          console.log(c.repeat(this.width));
        }
      } else {
        this.print()
      }
    }
  }
}

module.exports = Square;
