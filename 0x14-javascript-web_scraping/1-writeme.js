#!/usr/bin/node
// script to write content to file
const fs = require('fs');

const filename = process.argv[2];

const content = process.argv[3];

fs.writeFileSync(filename, content, 'utf8');
