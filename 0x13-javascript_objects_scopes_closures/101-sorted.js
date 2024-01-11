#!/usr/bin/node

const dict = require('./101-data').dict;

const invertedDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (invertedDict[occurrences] === undefined) {
    invertedDict[occurrences] = [userId];
  } else {
    invertedDict[occurrences].push(userId);
  }
}
console.log(invertedDict);
