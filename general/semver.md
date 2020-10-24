## Semantic Versioning Specification

*Disclaimer: info. for this page was sourced from [here](https://semver.org/) and [here](https://docs.npmjs.com/misc/semver)*

Semantic Versioning or 'semver' was created to provide guidelines for versioning software releases. By following these rules it gives users the ability to more properly manage their dependencies with greater confidence.

### Rules

- versions must be of the format `MAJOR.MINOR.PATCH`
- 'PATCH' version is only incremented when **backwards compatible** bug fixes are introduced
- 'MINOR' version is only incremented when 
    - **new backwards compatible** functionality is introduced
    - anything in the public API is marked as deprecated
    - substantial functionality or improvements are introduced in the private code
- 'MAJOR' version is only incremented when **backwards incompatible** changes are introduced
- 'PATCH' must be reset to 0 with 'MINOR' version upgrade
- 'PATCH' and 'MINOR' versions must be reset to 0 with 'MAJOR' version upgrade
- 'MAJOR' version starting with 0 is for initial development and nothing should be considered stable
