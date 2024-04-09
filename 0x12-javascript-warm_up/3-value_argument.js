#!/usr/bin/node

// Retrieve the first cmd line arg
const arg = process.argv[2];

// Check if argument is defined
console.log(arg !== undefined ? arg : 'No argument');
