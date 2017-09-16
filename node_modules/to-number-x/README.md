<a href="https://travis-ci.org/Xotic750/to-number-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/to-number-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/to-number-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/to-number-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/to-number-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/to-number-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/to-number-x" title="npm version">
<img src="https://badge.fury.io/js/to-number-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_to-number-x"></a>

## to-number-x
Converts argument to a value of type Number.

**Version**: 1.1.0  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  
<a name="exp_module_to-number-x--module.exports"></a>

### `module.exports` ⇒ <code>\*</code> ⏏
This method converts argument to a value of type Number.

**Kind**: Exported member  
**Returns**: <code>\*</code> - The argument converted to a number.  
**Throws**:

- <code>TypeError</code> If argument is a Symbol.


| Param | Type | Description |
| --- | --- | --- |
| argument | <code>\*</code> | The argument to convert to a number. |

**Example**  
```js
var toNumber = require('to-number-x');

toNumber('1'); // 1
toNumber(null); // 0
toNumber(true); // 1
```
