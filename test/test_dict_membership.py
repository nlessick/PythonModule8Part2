import unittest
from more_fun_with_collections.dict_membership import in_dict


class test_dict_one(unittest.TestCase):
    def test_in_dict_true(self):
        test_dict = {'A':1,'G':7,'K':11}
        test_true = in_dict(test_dict)
        self.assertEqual(test_true, ('Does the dictionary contain A? ',True))

class test_dict_two(unittest.TestCase):
    def test_in_dict_false(self):
        test_dict = {'B':2,'G':7,'K':11}
        test_false = in_dict(test_dict)
        self.assertEqual(test_false, ('Does the dictionary contain A? ',False))


if __name__ == '__main__':
    unittest.main()
