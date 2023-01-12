## Using `patch`

From [here](https://realpython.com/python-mock-library/)

`unittest.mock` provides a `patch` function which looks up up an object
in a given module and replaces that object with a Mock. It is usually
used as either a function decorator or a context manager.

### `patch` as a decorator

To mock an object for the duration of a test function, use `patch` as a
decorator.

`get_status.py`

``` python
import requests

def get_status(base_url, header_dict, payload):
    omim_status = requests.get(base_url, headers=header_dict, 
        params = payload)
    if omim_status.status_code != 200:
        raise ConnectionError(f'Request returned a status other than 200: {omim_status.status_code}')
    else:
        return(omim_status)
```

`test_patch.py`

``` python
import unittest
from unittest.mock import Mock, patch
import get_status

class TestSubmitRequest(unittest.TestCase):
    @patch('get_status.requests.get')
    def test_submit_request_connection_refused_error(self, mock_obj):
        mock_obj.return_value.status_code = 429
        # check error
        with self.assertRaises(ConnectionError) as exception_context:
            get_status.get_status('', {}, {})
        self.assertEqual(
            str(exception_context.exception),
            'Request returned a status other than 200: 429'
        )
```

    ## .
    ## ----------------------------------------------------------------------
    ## Ran 1 test in 0.001s
    ## 
    ## OK

``` bash
python -m unittest test_patch.py
```

The `patch` decorator takes a string that represents the object to mock.
The string you use depends on where you want to mock. In this case, we
want to mock the `requests.get` method where it is called in the
`get_status.py` module. So the string to `patch` is
‘get_status.requests.get’. `patch` creates a Mock object and this is
passed into the test function, so the test function now has an extra
parameter (`mock_obj`). We set the return value of the mock object to
429 and this means that `get_status` raises a `ConnectionError`
exception.

### `patch` as a context manager

To only `patch` an object for a subset of the test scope, you can use
`patch` as a context manager.

`test_patch_2.py`

``` python
import unittest
from unittest.mock import Mock, patch
import get_status

class TestSubmitRequest(unittest.TestCase):
    def test_submit_request_connection_refused_error(self):
        with patch('get_status.requests.get') as mock_obj:
            mock_obj.return_value.status_code = 429
            # check error
            with self.assertRaises(ConnectionError) as exception_context:
                get_status.get_status('', {}, {})
                self.assertEqual(
                    str(exception_context.exception),
                    'Request returned a status other than 200: 429'
                )
```

    ## .
    ## ----------------------------------------------------------------------
    ## Ran 1 test in 0.001s
    ## 
    ## OK

``` bash
python -m unittest test_patch_2.py
```

In this situation, `with patch('get_status.requests.get') as mock_obj:`
patches the `requests.get` method with a Mock object(`mock_obj`). Once,
the test exits the scope of the `with` statement, the original method is
restored.
