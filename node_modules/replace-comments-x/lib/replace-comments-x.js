(function(f){if(typeof exports==="object"&&typeof module!=="undefined"){module.exports=f()}else if(typeof define==="function"&&define.amd){define([],f)}else{var g;if(typeof window!=="undefined"){g=window}else if(typeof global!=="undefined"){g=global}else if(typeof self!=="undefined"){g=self}else{g=this}g.returnExports = f()}})(function(){var define,module,exports;return (function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(_dereq_,module,exports){
/**
 * @file Replace the comments in a string.
 * @version 1.0.3
 * @author Xotic750 <Xotic750@gmail.com>
 * @copyright  Xotic750
 * @license {@link <https://opensource.org/licenses/MIT> MIT}
 * @module replace-comments-x
 */

'use strict';

var isString = _dereq_('is-string');
var STRIP_COMMENTS = /((\/\/.*$)|(\/\*[\s\S]*?\*\/))/mg;

/**
 * This method replaces comments in a string.
 *
 * @param {string} string - The string to be stripped.
 * @param {string} [replacement] - The string to be used as a replacement.
 * @returns {string} The new string with the comments replaced.
 * @example
 * var replaceComments = require('replace-comments-x');
 *
 * replaceComments(test;/* test * /, ''), // 'test;'
 * replaceComments(test; // test, ''), // 'test;'
 */
module.exports = function replaceComments(string) {
  var replacement = arguments.length > 1 && isString(arguments[1]) ? arguments[1] : '';
  return isString(string) ? string.replace(STRIP_COMMENTS, replacement) : '';
};

},{"is-string":2}],2:[function(_dereq_,module,exports){
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