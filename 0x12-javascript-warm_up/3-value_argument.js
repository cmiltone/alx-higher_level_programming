#!/usr/bin/node
const { argv } = process;
const args = argv.filter((_, i) => i > 1);

if (!args[0]) {
  console.log('No argument');
} else if (args[0]) {
  console.log(args[0]);
}
