#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if conditions are not met
      return {};
    }
  }

  // Instance method to print the rectangle
  print () {
    if (Object.keys(this).length === 0) {
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Instance method to rotate the rectangle
  rotate () {
    if (Object.keys(this).length === 0) {
      return;
    }

    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Instance method to double the rectangle's dimensions
  double () {
    if (Object.keys(this).length === 0) {
      return;
    }

    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
