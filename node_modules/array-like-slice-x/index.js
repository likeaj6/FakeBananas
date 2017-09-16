/**
 * @file Cross-browser array-like slicer.
 * @version 1.1.0
 * @author Xotic750 <Xotic750@gmail.com>
 * @copyright  Xotic750
 * @license {@link <https://opensource.org/licenses/MIT> MIT}
 * @module array-like-slice-x
 */

'use strict';

var toObject = require('to-object-x');
var toInteger = require('to-integer-x');
var toLength = require('to-length-x');
var isUndefined = require('validate.io-undefined');
var splitIfBoxedBug = require('split-if-boxed-bug-x');

var setRelative = function _setRelative(value, length) {
  return value < 0 ? Math.max(length + value, 0) : Math.min(value, length);
};

/**
 * The slice() method returns a shallow copy of a portion of an array into a new
 * array object selected from begin to end (end not included). The original
 * array will not be modified.
 *
 * @param {!Object} argsObject - The `arguments` to slice.
 * @param {number} [start] - Zero-based index at which to begin extraction.
 *  A negative index can be used, indicating an offset from the end of the
 *  sequence. slice(-2) extracts the last two elements in the sequence.
 *  If begin is undefined, slice begins from index 0.
 * @param {number} [end] - Zero-based index before which to end extraction.
 *  Slice extracts up to but not including end. For example, slice([0,1,2,3,4],1,4)
 *  extracts the second element through the fourth element (elements indexed
 *  1, 2, and 3).
 *  A negative index can be used, indicating an offset from the end of the
 *  sequence. slice(2,-1) extracts the third element through the second-to-last
 *  element in the sequence.
 *  If end is omitted, slice extracts through the end of the sequence (arr.length).
 *  If end is greater than the length of the sequence, slice extracts through
 *  the end of the sequence (arr.length).
 * @returns {Array} A new array containing the extracted elements.
 * @example
 * var arrayLikeSlice = require('array-like-slice-x');
 * var args = (function () {
    return arguments;
 * }('Banana', 'Orange', 'Lemon', 'Apple', 'Mango'));
 *
 * var citrus = arrayLikeSlice(args, 1, 3);
 *
 * // args contains ['Banana', 'Orange', 'Lemon', 'Apple', 'Mango']
 * // citrus contains ['Orange','Lemon']
 */
module.exports = function slice(arrayLike, start, end) {
  var iterable = splitIfBoxedBug(toObject(arrayLike));
  var length = toLength(iterable.length);
  var k = setRelative(toInteger(start), length);
  var relativeEnd = isUndefined(end) ? length : toInteger(end);
  var finalEnd = setRelative(relativeEnd, length);
  var val = [];
  val.length = Math.max(finalEnd - k, 0);
  var next = 0;
  while (k < finalEnd) {
    if (k in iterable) {
      val[next] = iterable[k];
    }

    next += 1;
    k += 1;
  }

  return val;
};
