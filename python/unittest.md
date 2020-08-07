### Python Unittest

#### Start
1. Create a test class that inherits from unittest.TestCase
```python
import unittest

class TestCalc(unittest.TestCase):
    ...
```
2. Define a test method **(must start with test_ or else the test will not be run)**
*Use self.assert methods to assert expected outcomes*
```python
import unittest
import fake_math_object

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = fake_math_object.add(10, 5)
        self.assertEqual(result, 15)
```

#### Run
1. Assume the above class (TestCalc) is in a module named test_calc.py
2. As it is written above, the module **cannot** just be run using: `python test_calc.py`
3. Instead the class needs to be passed into unittest: `python -m unittest test_calc.py`
4. The following could be added to the module to allow it to be run directly:
```python
...
if __name__ == '__main__':
    unittest.main()
```

#### setUp, tearDown, setUpClass and tearDownClass
1. Use the setUp method to run code **prior to each test method**
```python
def setUp(self):
    """ran before each test method"""
    ...
```
2. Use tearDown to run code **after each test method**
```python
def tearDown(self):
    """ran after each test method"""
    ...
```
3. Use the setUpClass class method to run code **once before running all test methods**
```python
@classmethod
def setUpClass(cls):
    """ran once before running all test methods"""
```
4. Use the tearDownClass class method to run code **once after running all test methods**
```python
@classmethod
def tearDownClass(cls):
    """ran once after running all test methods"""
```

#### Mock and patch
1. Mock and patch allow objects to be substituted for another object
2. This comes in handy if you want to isolate your test from other functions or external APIs
3. **The Mock object (and not patch) should be used when it is needed as an argument**
4. **Patch should be used to patch objects and builtins that are not passed in as arguments**

##### Mock Example
1. Suppose a method needs tested, but it relies upon an external API
2. Mock can be used to create a dummy API so the actual API does not have to be called

api.py
```python
def api_call(api):
    sample_data = 'hello world!'
    api.get_data(sample_data)
```
test.py
```python
import api
import unittest
from unittest.mock import Mock

class TestMock(unittest.TestCase):
    def test_mock(self):
        # the following creates a Mock object that can then be used in place of the API
        mock_api = unittest.mock.Mock()
        api.api_call(mock_api)
        # ensure api.get_data was called with 'hello world!'
        mock_api.get_data.assert_called_with('hello world!')
```

##### Patch Example
1. If something needs to be mocked that isn't passed into the call, then use patch
2. You can use the function decorator to scope the patch to the test method

api.py
```python
import requests

def api_call():
    response = requests.get('https://someurl.com')
    if response.ok:
        return response.Text
    else:
        return 'Bad Response'
```
test.py
```python
import api
import unittest
from unittest.mock import patch

class TestMock(unittest.TestCase):
    # the following overrides api.requests.get in the api module
    @patch('api.requests.get')
    def test_mock(self, mock_get):
        mock_get.ok = True
        mock_get.text = 'Success'
        response = api.api_call()
        mock_get.assert_called_with('https://someurl.com')
        self.assertEqual(response, 'Success')
```

For more info: https://www.youtube.com/watch?v=ww1UsGZV8fQ
