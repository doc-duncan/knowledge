## node.js

#### Overview

node.js is a runtime, but is commonly mistaken for its own language. In reality it is a runtime that packages Chrome's v8 engine to execute javascript code. It provides additional modules to interact with the os and file system that it is running on. The motivation for creating node comes from the desire to have javascript powering both the frontend and backend of an application.

#### Foundational Knowledge
Every file in node is a module. To get metadata about the current module:
```javascript
console.log(module);
```
All vars and functions are private and scoped to the module they are defined in. To use outside of the module these vars and functions must be explicitly exported:
```javascript
function logger(msg){
    console.log(msg);
}
module.exports.log=logger;
// OR
exports.log=logger;
```
The exports object can then be set to a constant in another module:
```javascript
const logger = require('/logger');
```
The logger function could then be called:
```javascript
logger.log('Hello World!');
```