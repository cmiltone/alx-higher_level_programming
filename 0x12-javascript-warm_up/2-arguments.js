#!/usr/bin/node
const { argv } = process;
const args = argv.filter((_, i) => i > 1);

if (args.length <= 0) {
  console.log('No argument');
} else if (args.length >= 2) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
