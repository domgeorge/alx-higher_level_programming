#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    // If 'c' is not defined, set it to 'X'
    if (c === undefined) {
      c = 'X';
    }

    // Print the square using the character 'c'
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
