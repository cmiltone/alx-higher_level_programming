#!/usr/bin/node
// script to print file contents
const req = require('request');

const url = process.argv[2];

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;

  let count = 0;

  for (let i = 0; i < films.length; i++) {
    const film = films[i];

    for (let j = 0; j < film.characters.length; j++) {
      const character = film.characters[j];

      const parts = character.split('/');

      if (parts.includes('18')) {
        count += 1;
      }
    }
  }

  console.log(count);
});
