# Characterization Testing
* [Source](https://michaelfeathers.silvrback.com/characterization-testing)

Characterization Testing is about testing _**behavior**_, not _**correctness**_. Without thinking about software specifications, you can just record behavior given certain input.

## Utility
When is it useful to test like this? 

- When we want to build knowledge about what the code actually does, how the application actually _**behaves**_. Characterization testing is great when performed prior to a **refactor** or **rewrite**.

What happens when a character test uncovers undocumented behavior? Is it a bug by default? 
- Not necessarily, that depends on the context. In fact, users may have become accustomed to this behavior and expect the feature to exist.
> "When a system goes into production, in a way, it becomes its own specification. We need to know when we are changing existing behavior regardless of whether we think it’s right or not."

It's best to leave the test and record this behavior so its no longer undocumented and future changes can be tested against this behavior.
