#!/usr/bin/node
const { argv } = process;
const num = parseInt(argv[2]);

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(num));
