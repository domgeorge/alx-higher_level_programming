#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check both width and height are greater than 0
    if (w > 0 && h > 0) {
      // If true, initialize the width and height attr
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
