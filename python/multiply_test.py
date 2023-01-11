import unittest

def multiply(arg1, arg2):
    return(arg1*arg2)

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)

