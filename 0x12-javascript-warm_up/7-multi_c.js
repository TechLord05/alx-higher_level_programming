#!/usr/bin/node

const numOccu = parseInt(process.argv[2]);

if (isNaN(numOccu)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOccu; i++) {
    console.log('C is fun');
  }
}
