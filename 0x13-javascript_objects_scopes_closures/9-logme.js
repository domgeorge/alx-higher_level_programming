#!/usr/bin/node

let num = 0;

exports.logMe = function (item) {
  // Print the number of arguments or new argument value
  console.log(num + ': ' + item);

  num++;
};
