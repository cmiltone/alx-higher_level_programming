#!/usr/bin/node
// script to print file contents
const req = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
