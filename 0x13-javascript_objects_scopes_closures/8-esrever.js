#!/usr/bin/node

exports.esrever = function (list) {
  let aux;
  for (let i = 0; i < Math.floor(list.length / 2); i++) {
    aux = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = aux;
  }
  return (list)
};
