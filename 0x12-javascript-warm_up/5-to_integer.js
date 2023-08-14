#!/usr/bin/node
const { argv } = process;
let num = Math.floor(new Number(argv[2]));
if (num != NaN) {
  console.log(`My number is: ${num}`);
} else {
  console.log("Not a number")
}
