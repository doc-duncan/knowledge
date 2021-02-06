# The Three Laws of TDD
* [Source](https://web.archive.org/web/20201128042346/http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)

1. You are not allowed to write any production code unless it is to make a failing unit test pass.
2. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.
 
## Description
You have to start with the test (By Law 2). The goal is to make the test fail with as little code as possible. Once the test fails, write as little code as possible to make the test pass (By Law 3). Write no other code.

If done correctly, you should be in almost a _**constant**_ state of executing the system. The full cycle should be a matter of minutes. 
> "Even 10 minutes is too long."

## Realization
If this system of TDD is followed, **than at any given moment, the code base was passing all tests a minute ago.**

## Benefits
1. You probably wont use a debugger that much anymore.
    1. How much time/money you save?
2. You become fearless when refactoring. No more breaking changes.
    1. Software becomes _**soft**_ and malleable.
2. You have documentation that is _**always**_ up to date with production behavior.
3. You will write modular code, because testable code is modular by definition.
