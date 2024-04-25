#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const sourceFilePathA = process.argv[2];
const sourceFilePathB = process.argv[3];
const destinationFilePath = process.argv[4];

try {
  const dataA = fs.readFileSync(sourceFilePathA, 'utf-8');
  const dataB = fs.readFileSync(sourceFilePathB, 'utf-8');

  const concatenatedData = dataA + dataB;

  fs.writeFileSync(destinationFilePath, concatenatedData);
  console.log('Concatenation successful!');
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
