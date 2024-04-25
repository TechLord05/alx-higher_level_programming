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
    // Check if the object is empty
    if (Object.keys(this).length === 0) {
      return;
    }

    // Print the rectangle using 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
