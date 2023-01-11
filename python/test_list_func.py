import list_func
import unittest

class TestFilterList(unittest.TestCase):

    def test_filter_list(self):
        test_list = ['patch', 'category', 'practice', 'concatenate']
        self.assertEqual(list_func.filter_list(test_list), 
                          ['category', 'concatenate'])
    
    def test_filter_list_empty(self):
        self.assertEqual(list_func.filter_list([]), [])

