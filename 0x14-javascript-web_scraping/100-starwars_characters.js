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
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    const charUrl = characters[i];

    req(charUrl, function (err, res, bdy) {
      if (err) {
        console.log(err);
        return;
      }

      const character = JSON.parse(bdy);
      console.log(character.name);
    });
  }
});
