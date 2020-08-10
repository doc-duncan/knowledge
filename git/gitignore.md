# Gitignore Patterns

### Special Characters
1. Comment: `#`
2. Negation: `!`
3. Directory Separator: `/`
4. Wildcard: `*` (matches all but `/`)
5. Single Wildcard: `?` (matches any single character but `/`)
6. Double Wildcard: `**` (matches multiple layers above or below)

### Matching Rules
1. "If there is a separator at the beginning or middle (or both) of the pattern, then the pattern is relative to the directory level of the particular `.gitignore` file itself. Otherwise the pattern may also match at any level below the `.gitignore` level."
2. "If there is a separator at the end of the pattern then the pattern will only match directories, otherwise the pattern can match both files and directories."

### Examples
1. `docs` -> matches all files and directories at any level named 'docs'
2. `docs/` -> matches all directories at any level named 'docs'
3. `docs/file` -> matches only files named 'file' in the docs dir at the same level as the `.gitignore`
