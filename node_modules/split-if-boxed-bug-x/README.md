<a href="https://travis-ci.org/Xotic750/split-if-boxed-bug-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/split-if-boxed-bug-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/split-if-boxed-bug-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/split-if-boxed-bug-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/split-if-boxed-bug-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/split-if-boxed-bug-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/split-if-boxed-bug-x" title="npm version">
<img src="https://badge.fury.io/js/split-if-boxed-bug-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_split-if-boxed-bug-x"></a>

## split-if-boxed-bug-x
Tests if a value is a string with the boxed bug; splits to an array.

**Version**: 1.0.0  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  
<a name="exp_module_split-if-boxed-bug-x--module.exports"></a>

### `module.exports(value)` ⇒ <code>\*</code> ⏏
This method tests if a value is a string with the boxed bug; splits to an
array for iteration; otherwise returns the original value.

**Kind**: Exported function  
**Returns**: <code>\*</code> - An array or characters if value was a string with the boxed bug;
 otherwise the value.  

| Param | Type | Description |
| --- | --- | --- |
| value | <code>\*</code> | The value to be tested. |

**Example**  
```js
var splitIfBoxedBug = require('split-if-boxed-bug-x');

// No boxed bug
splitIfBoxedBug('abc'); // 'abc'

// Boxed bug
splitIfBoxedBug('abc'); // ['a', 'b', 'c']
```
