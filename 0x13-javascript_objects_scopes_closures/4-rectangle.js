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
        console.log('X'.repeat(this.width));
      }
    }
  }

  // method to rotate the Rectangle's position //
  rotate () {
    if (this.width && this.height) {
      const tmp = this.width;
      this.width = this.height;
      this.height = tmp;
    }
  }

  // method to double the rectangle size //
  double () {
    if (this.width && this.height) {
      this.width = 2 * this.width;
      this.height = 2 * this.height;
    }
  }
}

module.exports = Rectangle;
