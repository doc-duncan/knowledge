# React Deep Dive

## What is React?
At a high level, React is a JavaScript library that assists developers with building user interfaces. Developers use React to build components that are then compilied into elements on an HTML page.

## Why React?
From my own research, there are a few main points that give React its popularity: 

1. **Component based development yields multiple benefits**. By developing in a component based environment you can achieve efficient **code reuse**. Instead of having duplicate code scattered across multiple applications you can manage a single contained component that can be reused all over and enforces a single point of control over change methodology. Secondly, the components and their state allow for a shift away from explicitly changing DOM nodes via JS or jQuery and instead declaring state attributes that then control the view. 

2. **React is consistently quick**. What I mean by this is its use of the **virtual DOM** allows efficient diffing and reconciliation to determine the minimum number of changes for the actual DOM. What initially tripped me up was that I thought that this speed could not be achieved by using raw JavaScript or jQuery. However, the benefit more comes from React's consistenty to avoid speed pitfalls or full rerenders that you could accidentally do when performing your own raw development.

3. **React is maintained by Facebook, which should result in years of solid maintenance and development**.

## Setting Up Sample Project (Without `create-react-app`)
An easy way to initialize a new React project is with `create-react-app`, however, if you are new to React like me then you may want to initialize the project and its dependencies manually so it is not a black box. The fourth article in [sources](#sources) was extremely helpful in learning this process. 

### Dependency Management
There are four three main packages, listed below, that need to be configured properly to start your journey with React.

1. **webpack** - In a general sense, webpack is a code bundler that ingests, transforms and bundles target code and outputs it as a minified resource. Specifically to React, it ingests components and outputs bundled JS code that the majority of browsers can interpret. Webpack works off of a file named `webpack.config.js`, which specifies settings for building your application. For a detailed explanation of setting up webpack please reference the fifth article of [sources](#sources).

    **installation**

    `npm install webpack webpack-cli --save-dev`

    **configuration**
    1. Add the following to `package.json`
        ```javascript
        "scripts": {
            "build": "webpack --mode production"
        }
        ```
    2. Add the following webpack configuration to `webpack.config.js` in the root directory. This configuration states, "For every file with a js or jsx extension Webpack pipes the code through babel-loader."
        ```javascript
        module.exports = {
            module: {
                rules: [
                {
                    test: /\.(js|jsx)$/,
                    exclude: /node_modules/,
                    use: {
                    loader: "babel-loader"
                    }
                }
                ]
            }
        };
        ```

2. **babel** - Babel is a transpiler, which takes current JS code and syntax and transforms it to be compatible with older browsers. Webpack relies on Babel for this transformation to produce its output.

    **installation**

    `npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev`
    - @babel/core is the main package
    - babel-loader is needed by webpack to interface with babel
    - @babel/preset-env is needed by babel for compiling modern JS to ES5
    - @babel/preset-react is needed by babel for compiling React and more specifically, JSX, to JS

    **configuration**

    1. Create a new file named `.babelrc` at the project root (this is babel configuration)
        ```javascript
        {
            "presets": ["@babel/preset-env", "@babel/preset-react"]
        }
        ```

3. **react and react-dom** - `react` is the main package for React, while `react-dom` allows for React specific DOM interaction.

    **installation**
    `npm install react react-dom`

### Sources
**Disclaimer: info. for this page has been sourced from the following:**

1. [React Tutorial](https://www.youtube.com/watch?v=DLX62G4lc44)
2. [React Speed Justification (Or Not?)](https://stackoverflow.com/questions/33355125/what-really-makes-reactjs-as-fast-as-it-claims-to-be)
3. [JSX](https://reactjs.org/docs/introducing-jsx.html)
4. [Set Up React Project From Scratch](https://www.valentinog.com/blog/babel/)
5. [What Is webpack?](https://dev.to/vish448/webpack-for-react-intro-3n01)
