#!/usr/bin/node
// Prints a custom message depending of the number of arguments passed
if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
