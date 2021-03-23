#!/usr/bin/node

const SquareMod = require('./5-square');

class Square extends SquareMod {
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
