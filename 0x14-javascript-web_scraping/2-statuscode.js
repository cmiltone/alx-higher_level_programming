#!/usr/bin/node
// script to print file contents
const req = require('request');

const url = process.argv[2];

req(url, function (error, response) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', response?.statusCode);
});
