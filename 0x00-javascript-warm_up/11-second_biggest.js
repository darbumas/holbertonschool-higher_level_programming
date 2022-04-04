#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let biggest, secondBig;
  if (parseInt(process.argv[2]) >= parseInt(process.argv[3])) {
    biggest = parseInt(process.argv[2]);
    secondBig = parseInt(process.argv[3]);
  } else {
    biggest = parseInt(process.argv[3]);
    secondBig = parseInt(process.argv[2]);
  }

  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > biggest) {
      secondBig = biggest;
      biggest = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > secondBig) {
      secondBig = parseInt(process.argv[i]);
    }
  }
  console.log(secondBig);
}
