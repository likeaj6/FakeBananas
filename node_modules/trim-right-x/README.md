<a href="https://travis-ci.org/Xotic750/trim-right-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/trim-right-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/trim-right-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/trim-right-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/trim-right-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/trim-right-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/trim-right-x" title="npm version">
<img src="https://badge.fury.io/js/trim-right-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_trim-right-x"></a>

## trim-right-x
This method removes whitespace from the right end of a string.

**Version**: 1.3.3  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  
<a name="exp_module_trim-right-x--module.exports"></a>

### `module.exports(string)` ⇒ <code>undefined</code> \| <code>string</code> ⏏
This method removes whitespace from the right end of a string.

**Kind**: Exported function  
**Returns**: <code>undefined</code> \| <code>string</code> - The right trimmed string.  

| Param | Type | Description |
| --- | --- | --- |
| string | <code>string</code> | The string to trim the right end whitespace from. |

**Example**  
```js
var trimRight = require('trim-right-x');

trimRight(' \t\na \t\n') === ' \t\na'; // true
```
