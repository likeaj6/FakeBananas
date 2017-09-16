/**
 * @file ToInteger converts 'argument' to an integral numeric value.
 * @see {@link http://www.ecma-international.org/ecma-262/6.0/#sec-tointeger|7.1.4 ToInteger ( argument )}
 * @version 2.1.0
 * @author Xotic750 <Xotic750@gmail.com>
 * @copyright  Xotic750
 * @license {@link <https://opensource.org/licenses/MIT> MIT}
 * @module to-integer-x
 */

'use strict';

var toNumber = require('to-number-x');
var numberIsNaN = require('is-nan-x');
var numberIsFinite = require('is-finite-x');
var mathSign = require('math-sign-x');

/**
 * Converts `value` to an integer.
 *
 * @param {*} value - The value to convert.
 * @returns {number} Returns the converted integer.
 *
 * @example
 * var toInteger = require('to-integer-x');
 * toInteger(3); // 3
 * toInteger(Number.MIN_VALUE); // 0
 * toInteger(Infinity); // 1.7976931348623157e+308
 * toInteger('3'); // 3
 */
module.exports = function toInteger(value) {
  var number = toNumber(value);
  if (numberIsNaN(number)) {
    return 0;
  }

  if (number === 0 || numberIsFinite(number) === false) {
    return number;
  }

  return mathSign(number) * Math.floor(Math.abs(number));
};
