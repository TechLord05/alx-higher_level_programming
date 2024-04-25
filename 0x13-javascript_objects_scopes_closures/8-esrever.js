#!/usr/bin/node

exports.esrever = function (list) {
  // Check if the list is not empty or undefined
  if (!list || list.length === 0) {
    return [];
  }
  // Create a new array to store the reversed elements
  const reversedList = [];

  // Loop through the original list in reverse order using recursion
  function reverseElements (index) {
    if (index < 0) {
      return;
    }
    // Add each element to the new array
    reversedList.push(list[index]);
    // Recursive call for the next index
    reverseElements(index - 1);
  }
  // Start the recursion from the last index
  reverseElements(list.length - 1);
  // Return the reversed list
  return reversedList;
};
