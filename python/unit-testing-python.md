# Unit testing in Python

## `unittest`

Testing in Python can be done using the `unittest` module.

`unittest` provides a base class, `TestCase`, which may be used to
create new test cases. The example below show a simple function called
`mulitply` and a test which runs multiply with the arguments 2 and 3 and
compares the results to the expected results of 6.

``` python
import unittest

def multiply(arg1, arg2):
    return(arg1*arg2)

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)
```

Tests can be run for a single file like this.

``` bash
python -m unittest multiply_test.py
```

    ## .
    ## ----------------------------------------------------------------------
    ## Ran 1 test in 0.000s
    ## 
    ## OK

This will run all methods starting with `test`. A test uses `assert*()`
methods from
[`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase)
class to check the behaviour of functions. In the example above, we
assert that the return value of `multiply(2,3)` is equal to 6. If the
two are not equal, `unittest` will report that the test failed.

Usually we are testing a module or functions in a script, so the
functions definitions and tests will be in different files.

For example, if the following function is in a module named
`list_func.py`

``` python
import re

def filter_list(items):
    filtered_list = []
    for x in items:
        if re.search('cat', x) is not None:
            filtered_list.append(x)
    return(filtered_list)
```

You could have a test file `test_list_func.py` like this. In the test
file, you need to import the module that you are testing.

``` python
import list_func
import unittest

class TestFilterList(unittest.TestCase):

    def test_filter_list(self):
        test_list = ['patch', 'category', 'practice', 'concatenate']
        self.assertEqual(list_func.filter_list(test_list), 
                          ['category', 'concatenate'])
    
    def test_filter_list_empty(self):
        self.assertEqual(list_func.filter_list([]), [])
```

Then run the tests like this

``` bash
python -m unittest test_list_func.py
```

    ## ..
    ## ----------------------------------------------------------------------
    ## Ran 2 tests in 0.000s
    ## 
    ## OK
