# Python Docstrings

### Purpose
Docstrings describe the functionality of your classes, modules, functions or methods. They are generally meant to be kept as high level
descriptions of purpose. They differ from comments, which should explain how you are doing things. **Docstrings should be looked at as
documentation for consumers of your code.**

### Access
Docstring documentation can be acessed via two different ways:
1. the `__doc__` attribute
  * `print(my_object.__doc__)`
2. the `help` function
  * `help(my_object)`

### Syntax
* Triple quotes are used to designate Docstrings. Either single or double quotes may be used, but the standard convention is to use double quotes.
* Start with a capital letter and end with a period `(.)`.

```python
def my_func(arg):
  """Takes in arg and returns 2 times arg."""
  code goes here...
```

### One-Line Docstring
One-Line Docstrings should start and end on the same line (including the triple quotes). They should have a short description of the target.

### Multi-Line Docstring
Multi-Line Docstrings should have a short description on the first line of the documentation, which is then followed by a blank line. After the
blank line a more informative description may be written, followed by arguments, return values and exceptions.

```python
def my_func(arg):
  """Takes in arg and returns 2 times arg.

  :param arg: value to double
  :type arg: int
  :return: Double arg
  :rtype: int	
  """
  code goes here...



