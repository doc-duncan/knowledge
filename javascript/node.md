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
Single and double quotes are equal, *but when converted to JSON everything is double*.

CLI node args are available via `process.argv`. The first two elements are boiler plate so be sure to skip these.

`__filename` and `__dirname` are available in the module.

Sample template string:
```
var test = 'World'
console.log(`Hello ${test}`)
```

#### JavaScript Promises

Prior to Promises there was exclusively callbacks. With callbacks you would make a request to an API, let's say, and when the API would return there would be a callback function that would be called. With this structure you could easily get caught in a chain of nested callbacks. 

Then along came promises, which are actually JS objects. *Promises have states*: pending, fulfilled and rejected. There are two main methods used to react to a change in promise state:

`promise.then()` - runs perscribed code when the corresponding promise is *fulfilled*.

`promise.catch()` - runs perscribed code whtn the corresponding promise is *rejected*.

It is worth noting that when chaining promises together, *only one catch method is needed and it will catch any rejection in the chain*.

#### JavaScript Objects

