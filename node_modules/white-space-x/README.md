<a href="https://travis-ci.org/Xotic750/white-space-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/white-space-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/white-space-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/white-space-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/white-space-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/white-space-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/white-space-x" title="npm version">
<img src="https://badge.fury.io/js/white-space-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_white-space-x"></a>

## white-space-x
List of ECMAScript5 white space characters.

**Version**: 2.0.3  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  

* [white-space-x](#module_white-space-x)
    * [`~list`](#module_white-space-x..list) : <code>Array.&lt;Object&gt;</code>
    * [`~string`](#module_white-space-x..string) : <code>string</code>

<a name="module_white-space-x..list"></a>

### `white-space-x~list` : <code>Array.&lt;Object&gt;</code>
An array of the ES5 whitespace char codes, string, and their descriptions.

**Kind**: inner property of [<code>white-space-x</code>](#module_white-space-x)  
**Example**  
```js
var whiteSpace = require('white-space-x');
whiteSpaces.list.foreach(function (item) {
  console.log(lib.description, item.code, item.string);
});
```
<a name="module_white-space-x..string"></a>

### `white-space-x~string` : <code>string</code>
A string of the ES5 whitespace characters.

**Kind**: inner property of [<code>white-space-x</code>](#module_white-space-x)  
**Example**  
```js
var whiteSpace = require('white-space-x');
var characters = [
  '\u0009',
  '\u000a',
  '\u000b',
  '\u000c',
  '\u000d',
  '\u0020',
  '\u00a0',
  '\u1680',
  '\u180e',
  '\u2000',
  '\u2001',
  '\u2002',
  '\u2003',
  '\u2004',
  '\u2005',
  '\u2006',
  '\u2007',
  '\u2008',
  '\u2009',
  '\u200a',
  '\u2028',
  '\u2029',
  '\u202f',
  '\u205f',
  '\u3000',
  '\ufeff'
];
var ws = characters.join('');
var re1 = new RegExp('^[' + whiteSpace.string + ']+$)');
re1.test(ws); // true
```
