#!/usr/bin/node

// Check if 1st cmd line argument is undefined or not a num
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  // If arg is a valid num
  const i = Number(process.argv[2]);
  let j = 0;

  // Loop while j is less than the specified number of occurrences
  while (j < i) {
    console.log('C is fun');
    j++;
  }
}
