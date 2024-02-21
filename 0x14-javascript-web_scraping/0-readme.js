#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 3) {
  console.log('Pass in a file argument');
  process.exit(1);
}

fs.readFile(process.argv[2], 'utf-8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
