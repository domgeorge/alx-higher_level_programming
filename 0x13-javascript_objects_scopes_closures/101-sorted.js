#!/usr/bin/node

const dict = require('./101-data.js').dict;

const nDict = {};

// Loop over the keys (user ids) and values occurrence
Object.keys(dict).forEach(user => {
  const occurrence = dict[user];

  // If not a key, create a new key with array that contains userID
  if (!nDict[occurrence]) {
    nDict[occurrence] = [user];
  } else {
    // If already a key, push the user id to its array
    newDict[occurrence].push(user);
  }
});

console.log(nDict);
