import unittest
from lab1 import *

# A few test cases.  Add more!!!


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        ulist = []
        self.assertIsNone(max_list_iter(ulist))  # checks when list is empty
        vlist = [14, 35, 50, 19]
        self.assertEqual(max_list_iter(vlist), 50)  # checks test_max_list_iter on a valid list
        vlist = [21, 409, 54, 1, 2]
        self.assertEqual(max_list_iter(vlist), 409)  # checks test_max_list_iter on a valid list

    def test_reverse_rec(self):
        # following code will test all branches of reverse_rec
        alist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(alist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1, 3, 5, 7, 9]), [9, 7, 5, 3, 1])  # checks reverse_rec on a valid list

    def test_bin_search(self):
        alist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(3, 0, 0, alist)
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, low, high, list_val), 4)
        self.assertEqual(bin_search(10, low, high, list_val), 8)  # checks bin_search on a valid list
        self.assertEqual(bin_search(2, low, high, [1, 3, 5, 7, 9]), None)  # checks when the target is not found


if __name__ == "__main__":
        unittest.main()