#!/usr/bin/node
const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      let chars = '';
      for (let j = 0; j < this.height; j++) {
        chars += c;
      }
      console.log(chars);
    }
  }
}

module.exports = Square;
