#!/usr/bin/node

function factorial (x) {
  const num = parseInt(x);
  if (!num || num === 0) {
    return 1;
  } else {
    return num * factorial(x - 1);
  }
}
console.log(factorial(process.argv[2]));
