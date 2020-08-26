*Please read [my react page](https://github.com/doc-duncan/knowledge/blob/master/javascript/react/react.md) prior to this because it will give you a greater understanding of what is needed for React to function properly without CRA*

# Create-React-App

Many developers use `create-react-app` (CRA) to quickly get off the ground with thier React applications. But, afterwards, many devs are left in the dark as to what CRA actually does.

At a high level, CRA handles all of the Babel, webpack, etc. configuration and includes special scripts (`react-scripts`). These scripts are preloaded into `package.json` and use the predefined configuration to start, test and build your application. 

By default, CRA creates the following directory structure

```
my-app
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
    └── setupTests.js
```

As you can see above, `react-scripts` will be looking for `index.js` (the entrypoint JS module) under `src/` and for `index.html` (the template HTML page) under `public/`

`App.js` is a sample component that is brought in by `index.js`

## Project Setup

To spin up a new env with CRA: `npx create-react-app <app-name>`

**What is `npx`?**

`npx` is similar to `npm`, but it runs scripts found in the `./node_modules/.bin` directory. By using `npx` you actually don't have to install the package globally either. For example, you can utilize `create-react-app` without having to manage the entire package and outdated versions.

By running `create-react-app` a new git repo is initialized and an initial commit is made

## Sources
*Disclaimer: info. for this page was sourced from the following*
1. [What Does CRA Actually Do?](https://levelup.gitconnected.com/what-does-create-react-app-actually-do-73c899443d61)*
2. [create-react-app](https://github.com/facebook/create-react-app)