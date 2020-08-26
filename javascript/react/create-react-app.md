*Disclaimer: Info. for this page was sourced from [here](https://levelup.gitconnected.com/what-does-create-react-app-actually-do-73c899443d61)*

# Create-React-App

Many developers use `create-react-app` (CRA) to quickly get off the ground with thier React applications. But, afterwards, many devs are left in the dark as to what CRA actually does.

To spin up a new env with CRA: `npx create-react-app <app-name>`

**What is `npx`?**

`npx` is similar to `npm`, but it runs scripts found in the `./node_modules/.bin` directory. By using `npx` you actually don't have to install the package globally either. For example, you can utilize `create-react-app` without having to manage the entire package and outdated versions.

## `init.js`
`init.js` is kicked off first via the CRA command. The first step done is dependency installations. A `package.json` file is made and CRA decides whether `npm` or `yarn` should be used as a package manager (`yarn` is given priority). In particular, `react`, `react-dom` and `react-scripts` are installed. `package.json` is then modified to include the `start`, `build`, `test` and `eject` scripts and the `defaultBrowsers` and `eslinstConfig` config. This finalizes the creation of `package.json` for CRA. After this, the `public`, `src`, `README.md` and `.gitignore` directories and files are copied over to the working directory. Lastly, `git init` is ran automatically and initializes the current working directory as a repo with its first commit.

Because of these installations, there are many new packages inside `node_modules`. The majority of these packages come from the extensive dependency list of `react-scripts`. We will go over a few key ones now...

#### Babel
Babel and its many dependencies is responsible for transforming your code to work with the browsers.

#### ESLint
"ESlint is a linter meaning that scans your code against a set of rules. If you violate one of these rules it warns you"

#### Jest
"Jest is a testing library for JavaScript. It is also made by Facebook like CRA and React."

#### Webpack
"A highly modifiable tool that bundles JS files. Webpack is what runs Babel, ESLint and PostCSS. **The majority of what react-scripts does for you is related to setting up and running Webpack. Almost every dependency plugs into Webpack or plugs into something that plugs into Webpack**"

## `react-scripts.js`
So we know that react-scripts brings many dependencies together, but what exactly does it do?

Well, if you remember, our `package.json` has multiple scripts that map to `react-scripts` calls. For example, the `npm start` command is used to run `react-scripts start`. When a script is called like this, `react-scripts` first makes sure that the argument is acceptable (`start`, `test`, `build`...). If the arg. passes inspection, then control is passed to the script with the following format: `/scripts/<arg>.js` (here it would be `scripts/start.js`). The `start.js` script then interfaces with Webpack to spin up a dev server on the specified port.

This is a short overview and encompasses a high level of the source article. I will potentially expand on this in the future to dive deeper into the scripts and Webpack.

## defaults

By default, react-scripts looks at the `public` directory for index.html and the final build will be in the `build` directory.