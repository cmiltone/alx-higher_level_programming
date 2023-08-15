#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let max = 0;
  for (let i = 0; i < list.length; i++) {
    const element = list[i];
    if (element === searchElement) max += 1;
  }

  return max;
};
