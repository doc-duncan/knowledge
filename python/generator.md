## Generators

### Overview
The purpose of generators is to avoid having to store large data structures in memory and instead assist in iterations by just `yielding` the necessary values

### Code

Suppose we want to do some processing on n values

```python
def gen(stop):
    current = 0
    while current < stop:
        yield current
        current += 1
```