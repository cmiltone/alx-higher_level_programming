#!/usr/bin/node
// script to print file contents
const req = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFileSync(filename, body, 'utf8');
});
