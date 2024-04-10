#!/usr/bin/node

exports.esrever = function (list) {
  // Initialize an array
  const reversedList = [];

  // Loop in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the reversed list
    reversedList.push(list[i]);
  }

  return reversedList;
};
