#!/usr/bin/node

// Convert the 1st cmd line arg to an int
const no = Number.parseInt(process.argv[2]);

// Check if converted value is NaN
console.log(Number.isNaN(no) ? 'Not a number' : 'My number: ' + no);
