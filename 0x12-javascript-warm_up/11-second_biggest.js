#!/usr/bin/node
const { argv } = process;

const nums = argv.filter((_, i) => i > 1).map((a) => parseInt(a));
if (nums.length <= 1) {
  console.log(0);
} else {
  console.log(nums.sort((a, b) => b - a)[1]);
}
