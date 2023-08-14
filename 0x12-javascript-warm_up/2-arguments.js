#!/bin/node
const { argv } = process;
const args = argv.splice(0, 2);

if (args.length) {
  console.log(args.join(''));
} else {
  console.log('No argument');
}
