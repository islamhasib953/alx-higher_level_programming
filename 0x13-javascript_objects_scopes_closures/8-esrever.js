#!/usr/bin/node

exports.esrever = function (list) {
  const list2 = [];
  for (let i = 0; i < list.length; i++) {
    list2[i] = list[list.length - i - 1];
  }
  return (list2);
};
