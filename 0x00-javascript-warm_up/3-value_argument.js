#!/usr/bin/node
// Prints the first argument passed to it
const firstAv = process.argv[2];
if (firstAv) {
  console.log(firstAv);
} else {
  console.log('No argument');
}
