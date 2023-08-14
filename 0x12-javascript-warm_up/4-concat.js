#!/usr/bin/node
const { argv } = process;
const args = argv.filter((_, i) => i > 1);

console.log(`${args[0]} is ${args[1]}`);
