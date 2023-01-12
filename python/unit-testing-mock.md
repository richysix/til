## Using Mock objects

From [here](https://realpython.com/python-mock-library/)

Creating Mock objects in tests is useful if you want to test code that
uses a particular object without actually using that object. For
example, if your code queries an API, you might want to test the logic
of the code without actually querying the API.

### Creating Mock objects

``` python
from unittest.mock import Mock

def get_status(base_url, header_dict, payload):
    omim_status = requests.get(base_url, headers=header_dict, 
        params = payload)
    return(omim_status)

requests = Mock()
requests.get.return_value.status_code = 200

omim_status = get_status('https://api.omim.org/api/status', {}, {})
assert omim_status.status_code == 200
```

The code above, creates a Mock object that takes the place of the
requests module. Attributes and methods of Mock objects are created when
they are accessed. `requests.get.return_value.status_code = 200` creates
a new Mock object that can be accessed with `requests.get()` that has an
attribute named `status_code` which has the value 200. When
`requests.get()` is called in the `get_status` function, the return
value is the Mock object with the status_code attribute. Calling
`omim_status.status_code` on line 13 returns the value 200.

### Side Effects

At the moment, when `requests.get()` is called, it’s called with 3
arguments. These are ignored by the Mock `get` object, but we can also
add a function to run when the object is called using the `side_effect`
method. For example, we could print out the arguments supplied to
`requests.get()`. In this case, the return value from `requests.get()`
is whatever is returned from the side_effect function, so to keep the
`assert` statement working we could return a new `Mock` object with a
`status_code` attribute.

``` python
from unittest.mock import Mock

def get_status(base_url, header_dict, payload):
    omim_status = requests.get(base_url, headers=header_dict, 
        params = payload)
    return(omim_status)

def print_args(base_url, headers, params):
    print(base_url, headers, params)
    return(Mock(status_code = 200))

requests = Mock()
requests.get.side_effect = print_args

omim_status = get_status('https://api.omim.org/api/status', {}, {})
assert omim_status.status_code == 200
```

Now, when `requests.get` is called within `get_status`, the base_url,
headers and params arguments are printed. A Mock object with a
`status_code` attribute is returned and stored in the `omim_status`
variable.

The other thing you can do with side_effect is supply an iterable like a
list. In that case, each time the mocked method is called, it will
return the next value.

``` python
from unittest.mock import Mock

def get_status(base_url, header_dict, payload):
    omim_status = requests.get(base_url, headers=header_dict, 
        params = payload)
    return(omim_status)

requests = Mock()
requests.get.side_effect = [Mock(status_code = 200), Mock(status_code = 500)]

omim_status = get_status('https://api.omim.org/api/status', {}, {})
assert omim_status.status_code == 200

omim_status = get_status("https://api.omim.org/api/status", {}, {})
assert omim_status.status_code == 500
```

In this case, we supplied a list of two Mock object with different
`status_code` attributes. The first time `get_status` is called, it
returns a mock object with a `status_code` attribute with value 200. The
second time, a different mock object is returned, this time with a
`status_code` attribute with value 500.
