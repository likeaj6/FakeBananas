(function(f){if(typeof exports==="object"&&typeof module!=="undefined"){module.exports=f()}else if(typeof define==="function"&&define.amd){define([],f)}else{var g;if(typeof window!=="undefined"){g=window}else if(typeof global!=="undefined"){g=global}else if(typeof self!=="undefined"){g=self}else{g=this}g.returnExports = f()}})(function(){var define,module,exports;return (function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(_dereq_,module,exports){
/**
 * @file Tests if a value is a string with the boxed bug; splits to an array.
 * @version 1.0.0
 * @author Xotic750 <Xotic750@gmail.com>
 * @copyright  Xotic750
 * @license {@link <https://opensource.org/licenses/MIT> MIT}
 * @module split-if-boxed-bug-x
 */

'use strict';

var splitString = _dereq_('has-boxed-string-x') === false;
var strSplit;
var isString;
if (splitString) {
  strSplit = String.prototype.split;
  isString = _dereq_('is-string');
}

/**
 * This method tests if a value is a string with the boxed bug; splits to an
 * array for iteration; otherwise returns the original value.
 *
 * @param {*} value - The value to be tested.
 * @returns {*} An array or characters if value was a string with the boxed bug;
 *  otherwise the value.
 * @example
 * var splitIfBoxedBug = require('split-if-boxed-bug-x');
 *
 * // No boxed bug
 * splitIfBoxedBug('abc'); // 'abc'
 *
 * // Boxed bug
 * splitIfBoxedBug('abc'); // ['a', 'b', 'c']
 */
module.exports = function splitIfBoxedBug(value) {
  return splitString && isString(value) ? strSplit.call(value, '') : value;
};


},{"has-boxed-string-x":2,"is-string":3}],2:[function(_dereq_,module,exports){
/**
 * @file Check support of by-index access of string characters.
 * @version 1.0.1
 * @author Xotic750 <Xotic750@gmail.com>
 * @copyright  Xotic750
 * @license {@link <https://opensource.org/licenses/MIT> MIT}
 * @module has-boxed-string-x
 */

'use strict';

var boxedString = Object('a');

/**
 * Check failure of by-index access of string characters (IE < 9)
 * and failure of `0 in boxedString` (Rhino).
 *
 * `true` if no failure; otherwise `false`.
 *
 * @type boolean
 */
module.exports = boxedString[0] === 'a' && (0 in boxedString);

},{}],3:[function(_dereq_,module,exports){
'use strict';

var strValue = String.prototype.valueOf;
var tryStringObject = function tryStringObject(value) {
	try {
		strValue.call(value);
		return true;
	} catch (e) {
		return false;
	}
};
var toStr = Object.prototype.toString;
var strClass = '[object String]';
var hasToStringTag = typeof Symbol === 'function' && typeof Symbol.toStringTag === 'symbol';

module.exports = function isString(value) {
	if (typeof value === 'string') { return true; }
	if (typeof value !== 'object') { return false; }
	return hasToStringTag ? tryStringObject(value) : toStr.call(value) === strClass;
};

},{}]},{},[1])(1)
});