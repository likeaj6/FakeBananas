<a href="https://travis-ci.org/Xotic750/math-sign-x"
   title="Travis status">
<img
   src="https://travis-ci.org/Xotic750/math-sign-x.svg?branch=master"
   alt="Travis status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/math-sign-x"
   title="Dependency status">
<img src="https://david-dm.org/Xotic750/math-sign-x.svg"
   alt="Dependency status" height="18"/>
</a>
<a href="https://david-dm.org/Xotic750/math-sign-x#info=devDependencies"
   title="devDependency status">
<img src="https://david-dm.org/Xotic750/math-sign-x/dev-status.svg"
   alt="devDependency status" height="18"/>
</a>
<a href="https://badge.fury.io/js/math-sign-x" title="npm version">
<img src="https://badge.fury.io/js/math-sign-x.svg"
   alt="npm version" height="18"/>
</a>
<a name="module_math-sign-x"></a>

## math-sign-x
ES6-compliant shim for Math.sign.

**See**: [20.2.2.29 Math.sign(x)](http://www.ecma-international.org/ecma-262/6.0/#sec-math.sign)  
**Version**: 2.1.0  
**Author**: Xotic750 <Xotic750@gmail.com>  
**License**: [MIT](&lt;https://opensource.org/licenses/MIT&gt;)  
**Copyright**: Xotic750  
<a name="exp_module_math-sign-x--module.exports"></a>

### `module.exports(x)` ⇒ <code>number</code> ⏏
This method returns the sign of a number, indicating whether the number is positive,
negative or zero.

**Kind**: Exported function  
**Returns**: <code>number</code> - A number representing the sign of the given argument. If the argument
is a positive number, negative number, positive zero or negative zero, the function will
return 1, -1, 0 or -0 respectively. Otherwise, NaN is returned.  

| Param | Type | Description |
| --- | --- | --- |
| x | <code>\*</code> | A number. |

**Example**  
```js
var mathSign = require('math-sign-x');

mathSign(3);     //  1
mathSign(-3);    // -1
mathSign('-3');  // -1
mathSign(0);     //  0
mathSign(-0);    // -0
mathSign(NaN);   // NaN
mathSign('foo'); // NaN
mathSign();      // NaN
```
