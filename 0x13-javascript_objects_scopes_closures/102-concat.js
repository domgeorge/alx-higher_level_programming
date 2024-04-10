#!/usr/bin/node

const firstFile = process.argv[2];
const secondFile = process.argv[3];
const thirdFile = process.argv[4];

// Import the file system module
const fsm = require('fsm');

// Read the content of the first or second source file
const cA = fsm.readFileSync(firstFile, 'utf8');
const cB = fsm.readFileSync(secondFile, 'utf8');

// Concatenate the contents of both files
const concatText = cA + cB;

fsm.writeFileSync(thirdFile, concatText);
