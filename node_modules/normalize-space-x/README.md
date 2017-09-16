<a href="https://travis-ci.org/Xotic750/normalize-space-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/normalize-space-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/normalize-space-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/normalize-space-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/normalize-space-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/normalize-space-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/normalize-space-x" title="npm version">
<img src="https://badge.fury.io/js/normalize-space-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_normalize-space-x"></a>

## normalize-space-x
Trims and replaces sequences of whitespace characters by a single space.

**Version**: 1.3.3  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  
<a name="exp_module_normalize-space-x--module.exports"></a>

### `module.exports(string)` ⇒ <code>string</code> ⏏
This method strips leading and trailing white-space from a string,
replaces sequences of whitespace characters by a single space,
and returns the resulting string.

**Kind**: Exported function  
**Returns**: <code>string</code> - The normalized string.  

| Param | Type | Description |
| --- | --- | --- |
| string | <code>string</code> | The string to be normalized. |

**Example**  
```js
var normalizeSpace = require('normalize-space-x');

normalizeSpace(' \t\na \t\nb \t\n') === 'a b'; // true
```
