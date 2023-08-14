#!/usr/bin/node
const { argv } = process;
const num = Math.floor(Number(argv[2]));
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number is: ${num}`);
}
