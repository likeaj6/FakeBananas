<a href="https://travis-ci.org/Xotic750/trim-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/trim-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/trim-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/trim-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/trim-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/trim-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/trim-x" title="npm version">
<img src="https://badge.fury.io/js/trim-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_trim-x"></a>

## trim-x
This method removes whitespace from the left and right end of a string.

**Version**: 1.0.3  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  
<a name="exp_module_trim-x--module.exports"></a>

### `module.exports(string)` ⇒ <code>undefined</code> \| <code>string</code> ⏏
This method removes whitespace from the left and right end of a string.

**Kind**: Exported function  
**Returns**: <code>undefined</code> \| <code>string</code> - The trimmed string.  

| Param | Type | Description |
| --- | --- | --- |
| string | <code>string</code> | The string to trim the whitespace from. |

**Example**  
```js
var trim = require('trim-x');

trim(' \t\na \t\n') === 'a'; // true
```
