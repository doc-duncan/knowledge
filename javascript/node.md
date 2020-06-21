### node.js

#### Overview

node.js is a runtime, but is commonly mistaken for its own language. In reality it is a runtime that packages Chrome's v8 engine to execute javascript code. It provides additional modules to interact with the os and file system that it is running on. The motivation for creating node comes from the desire to have javascript powering both the frontend and backend of an application.

#### Foundational Knowledge
1. every file in node is a module
    - to get metadata about current module:
    ```javascript
    console.log(module);
    ```
2. all vars and functions are private and scoped to the module they are defined in
    - to use outside of the module these vars and functions must be explicitly exported:
    ```javascript
    function logger(msg){
        console.log(msg);
    }
    module.exports.log=logger;
    // OR
    exports.log=logger;
    ```
    - the exports object can then be set to a constant in a different module:
    ```javascript
    const logger = require('/logger');
    ```
    - the logger function could then be called:
    ```javascript
    logger.log('Hello World!');
    ```