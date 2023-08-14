#!/usr/bin/node
const { argv } = process;
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let xes = '';
    for (let j = 0; j < num; j++) {
      xes += 'X';
    }
    console.log(xes);
  }
}
