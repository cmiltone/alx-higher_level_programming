#!/usr/bin/node
const fs = require('fs');
const { argv } = process;
const file1 = argv[2];
const file2 = argv[3];
const file3 = argv[4];

let contents = '';

contents += fs.readFileSync(file1);
contents += '\n';
contents += fs.readFileSync(file2);

fs.writeFileSync(file3, contents);
