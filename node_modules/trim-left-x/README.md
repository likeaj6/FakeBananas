<a href="https://travis-ci.org/Xotic750/trim-left-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/trim-left-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/trim-left-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/trim-left-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/trim-left-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/trim-left-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/trim-left-x" title="npm version">
<img src="https://badge.fury.io/js/trim-left-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_trim-left-x"></a>

## trim-left-x
This method removes whitespace from the left end of a string.

**Version**: 1.3.5  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  
<a name="exp_module_trim-left-x--module.exports"></a>

### `module.exports(string)` ⇒ <code>undefined</code> \| <code>string</code> ⏏
This method removes whitespace from the left end of a string.

**Kind**: Exported function  
**Returns**: <code>undefined</code> \| <code>string</code> - The left trimmed string.  

| Param | Type | Description |
| --- | --- | --- |
| string | <code>string</code> | The string to trim the left end whitespace from. |

**Example**  
```js
var trimLeft = require('trim-left-x');

trimLeft(' \t\na \t\n') === 'a \t\n'; // true
```
