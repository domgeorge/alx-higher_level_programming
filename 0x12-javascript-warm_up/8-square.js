#!/usr/bin/node

// Check if 1st cmd line argument is undefined or not a num
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
	// if arg is a valid num
	const j = Number(process.argv[2]);

	// loop through each row of the square
	for (let i = 0; i < j; i++) {
		console.log('X'.repeat(j));
	}
}
