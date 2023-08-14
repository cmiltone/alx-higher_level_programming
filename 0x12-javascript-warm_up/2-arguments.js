#!/bin/node
const { argv } = process;
const args = argv.filter((arg, i) => i > 1);

if (args.length) {
  console.log(args.join(""))
} else {
  console.log('No argument')
}