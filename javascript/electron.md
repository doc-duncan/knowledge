# Electron

## What is Electron?
Electron is a framework that allows you to build cross-platform desktop applications using HTML, JS and CSS.

## Why Electron?
The beauty of Electron is that you get the system integration of traditional native applications and the versatility and consistency of web application development. This is made possible through two main components:

1. Electron applications include an embeded chrome browser. This means that you can use all of your favorite JS UI frameworks to build your application. This also means that every deployment of your application, regardless of the underlying OS, will be using the same browser version. This creates automatic consistency accross platforms.

2. Electron exposes the node API, which gives you system integration, such as interacting with the file system.

## Sample Application
The second [source](#sources) is a great resource for explaining the sample app and **how electron and node relate**. "Electron apps are developed in JavaScript using the same principles and methods found in Node.js development."
1. Initialize new npm project
    ```sh
    mkdir <my-project-dir>
    cd <my-project-dir>
    # initialize npm project with default package.json
    npm init -y 
    ```
    Be sure your `package.json` file has a `"main"` key pointing to the main JS file (if this is excluded Electron will look for `index.js`)

    ```javascript
    {
    "name": "electron",
    "version": "2.0.0",
    "main": "main.js",
    "license": "MIT"
    }
    ```

    Add Electron start script to `package.json`...by default `npm start` would run the main script with Node, so we need to overwrite this so it runs with `electron`

    ```javascript
    "scripts": {
        "start": "electron ."
    }
    ```

2. Initialize git
    
    `git init`

3. Add `.gitignore`
    ```sh
    # pushing and pulling all packages would be time consuming and overwhelming
    node_modules/
    # if mac
    .DS_Store
    ```

4. Install `electron`
    
    `npm install electron --save-dev`

5. Create `main.js`

    The `main.js` file starts the app and opens your web page in a new browser window.

    ```javascript
    const { app, BrowserWindow } = require('electron')

    function createWindow () {
        const win = new BrowserWindow({
            width: 800,
            height: 600,
            webPreferences: {
                nodeIntegration: true
            }
        })
        // sample web page
        win.loadFile('index.html')
    }
    app.whenReady().then(createWindow)
    ```

6. Create `index.html`

    This is the base page that will be rendered by `main.js`

    ```html
    <html>
        <head>
            <title>Hello World!</title>
            <body>
                <h1>Hello World!</h1>
            </body>
        </head>
    </html>
    ```

7. Run Application

    `npm start`

## Sources
*Disclaimer: Info. for this page was sourced from the following*
1. [What is Electron?](https://brainhub.eu/blog/what-is-electron-js/)
2. [Electron First App.](https://www.electronjs.org/docs/tutorial/first-app)
