#!/usr/bin/node

// Check if an argument is provided
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  // Print the first argument
  console.log(process.argv[2]);
}
