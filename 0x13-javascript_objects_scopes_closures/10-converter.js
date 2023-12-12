#!/usr/bin/node

exports.converter = function (base) {
  function myConverter (no) {
    return no.toString(base);
  }

  return myConverter;
};
