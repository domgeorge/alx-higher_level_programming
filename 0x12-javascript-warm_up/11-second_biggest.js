#!/usr/bin/node

// Check if there are less than or equal to 3 cmd line arguments
if (process.argv.length <= 3) {
  console.log('0');
} else {
  // Extract numeric values from cmd line arg
  const arf = process.argv.slice(2).map(Number);
  // Sort the arr of num in descending order and retrieve the next largest num
  const next = arf.sort(function (a, b) { return b - a; })[1];
  console.log(next);
}
