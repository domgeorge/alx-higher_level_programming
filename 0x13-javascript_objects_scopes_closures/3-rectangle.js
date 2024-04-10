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

  print () {
    // Loop through each row
    for (let i = 0; i < this.height; i++) {
      // Print 'X' char to create row
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
