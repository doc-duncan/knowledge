## *args and **kwargs
`*args` and `**kwargs` are both used to handle an undetermined amount of optional arguments passed into a function

you do not have to use the words 'args' and/or 'kwargs' - **the important parts are `*` and `**`**

#### `*args`
the single asterisk args is used to capture "non-keyworded" arguments
```python
def my_function(*args):
  for arg in args:
    print(args)

my_function(1, 'two', 3.0)

### output
# 1
# two
# 3.0
### end output
```

#### `**kwargs`
the double asterisk kwargs is used to capture "keyworded" arguments
```python
def my_function(**kwargs):
  print(kwargs)

my_function(one=1, two='two', three=3.0)

### output
# {'one': 1, 'two': 'two', 'three': 3.0}
### end output
```
