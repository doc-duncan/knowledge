## Git Hooks

*Disclaimer: info. for this page was sourced from [here](https://www.youtube.com/watch?v=fMYv6-SZsSo)*

Git hooks allow us to run custom scripts at the time of certain life cycle events like committing, merging, pushing etc.

### structure
Hooks are stored in `.git/hooks`. There are many sample templates available in this directory after `git init` is executed. To enable one of these sample scripts all you need to do is remove the `sample` extension. Git is targeting specific file names to execute at the corresponding life cycle event.

### rules
1. If a script exists with a `0` exit code then the script succeeded and the process moves on. **To stop execution at the hook then an exit code of anything other than `0` must be returned from the script.**
2. **Hooks are not checked into source control, therefore if you delete your local directory then they will be gone.**
3. The `--no-verify` flag can bypass all hooks easily.
