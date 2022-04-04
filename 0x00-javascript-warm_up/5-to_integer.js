#!/usr/bin/node
// Prints My number: <first argument converted in integer>

const firstArg = process.argv[2];
if (parseInt(firstArg)) {
  console.log('My number: ' + parseInt(firstArg));
} else {
  console.log('Not a number');
}
