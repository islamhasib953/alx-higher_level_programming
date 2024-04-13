#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = {};
for (const key in dict) {
  const val = dict[key];
  if (!newDict[val]) newDict[val] = [];
  newDict[val].push(key);
}
console.log(newDict);
