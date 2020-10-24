# Package.json

*disclaimer: info. for this page was sourced from [here](https://stackabuse.com/caret-vs-tilde-in-package-json/) and [here](https://michaelsoolee.com/npm-package-tilde-caret/)

### `dependencies`
package.json dependencies follow the [semver specification](https://github.com/doc-duncan/knowledge/blob/master/standards/semver.md)

by using special characters you can set specifications on what dependency versions are acceptable

- `^` the 'caret' character is used to install the most recent **minor** and **patch** versions. ex: `^3.4.2` will install up to `3.*.*` < `4.0.0`
- `~` the 'tilde' character is used to install the most recent **patch** versions. ex `~3.4.2` will install up to `3.4.*` < `3.5.0`