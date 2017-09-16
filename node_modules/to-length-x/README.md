<a href="https://travis-ci.org/Xotic750/to-length-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/to-length-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/to-length-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/to-length-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/to-length-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/to-length-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/to-length-x" title="npm version">
<img src="https://badge.fury.io/js/to-length-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_to-length-x"></a>

## to-length-x
ES6-compliant shim for ToLength.

**See**: [7.1.15 ToLength ( argument )](http://www.ecma-international.org/ecma-262/6.0/#sec-tolength)  
**Version**: 2.1.0  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  
<a name="exp_module_to-length-x--module.exports"></a>

### `module.exports(value)` ⇒ <code>number</code> ⏏
Converts `value` to an integer suitable for use as the length of an
array-like object.

**Kind**: Exported function  
**Returns**: <code>number</code> - Returns the converted integer.  

| Param | Type | Description |
| --- | --- | --- |
| value | <code>\*</code> | The value to convert. |

**Example**  
```js
var toLength = require('to-length-x');
toLength(3); // 3
toLength(Number.MIN_VALUE); // 0
toLength(Infinity); // Number.MAX_SAFE_INTEGER
toLength('3'); // 3
```
