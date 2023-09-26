#!/usr/bin/node
// script to print file contents
const req = require('request');

const url = process.argv[2];

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const todos = JSON.parse(body);

  const dict = {};

  for (let i = 0; i < todos.length; i++) {
    const todo = todos[i];

    if (todo.completed) {
      if (dict[todo.userId]) {
        dict[todo.userId] += 1;
      } else {
        dict[todo.userId] = 1;
      }
    }
  }

  console.log(dict);
});
