#!/usr/bin/node
const a = require('./5-square');

module.exports = class Square extends a {
  constructor (f) {
    super(f);
    this.fde = f;
  }

  charPrint (a) {
    if (a === undefined) {
      this.print();
    } else {
      let i = 0;
      while (i < this.fde) {
        console.log(a.repeat(this.fde));
        i++;
      }
    }
  }
};
