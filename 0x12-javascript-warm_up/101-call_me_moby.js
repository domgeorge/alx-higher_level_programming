#!/usr/bin/node

// Define module that exports objects
module.exports = {
  // The method callMeMoby takes in two param
  callMeMoby: function (j, theFunction) {
    // Loop x times
    for (let i = 0; i < j; i++) {
      // Execute the given function
      theFunction();
    }
  }
};
