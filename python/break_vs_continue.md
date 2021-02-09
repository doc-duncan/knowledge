### `break` vs `continue`

#### Purpose
Both `break` and `continue` are used to alter the default logic flow of both `for` and `while`
loops.

#### `break`
Use `break` if you want to stop execution of the loop and proceed to the next line outside of the
loop.

```python
for char in 'coding':
    if char == 'n':
        break
    print(char)

### prints:
# c
# o
# d
# i
```

#### `continue`
Use `continue` if you want to immediately move on to the next iteration of the loop, without
finishing the logic of the current iteration.

```python
for char in 'coding':
    if char == 'n':
        continue
    print(char)
### prints:
# c
# o
# d
# i
# g
```
