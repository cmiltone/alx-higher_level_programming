#!/usr/bin/node
// script to print file contents
const fs = require('fs');

const filename = process.argv[2];

const content = fs.readFileSync(filename, 'utf8');

console.log(content);
