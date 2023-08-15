#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
Object.keys(dict).map((key) => {
  if (!newDict[dict[key]]) newDict[dict[key]] = [];
  newDict[dict[key]].push(key);
  return key;
});
console.log(newDict);
