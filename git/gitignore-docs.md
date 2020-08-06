# Gitignore Patterns

### Special Characters
Comment: `#`
Negation: `!`
Directory Separator: `/`
Wildcard: `*` (matches all but `/`)
Single Wildcard: `?` (matches any single character but `/`)
Double Wildcard: `**` (matches multiple layers above or below)

### Matching Rules
1. "If there is a separator at the beginning or middle (or both) of the pattern, then the pattern is relative to the directory level of the particular `.gitignore` file itself. Otherwise the pattern may also match at any level below the `.gitignore` level."

2. "If there is a separator at the end of the pattern then the pattern will only match directories, otherwise the pattern can match both files and directories."

### Examples
`docs` -> matches all files and directories at any level named 'docs'
`docs/` -> matches all directories at any level named 'docs'
`docs/file` -> matches only files named 'file' in the docs dir at the same level as the `.gitignore`
