#!/usr/bin/node

// Check if the first and second arguments are provided
if (process.argv[2] === undefined) {
  process.argv[2] = 'undefined';
}
if (process.argv[3] === undefined) {
  process.argv[3] = 'undefined';
}

// Print the concatenated string
console.log(process.argv[2] + ' is ' + process.argv[3]);
