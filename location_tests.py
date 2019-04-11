import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
        loc1 = Location("Sacramento", 100, 210)
        self.assertEqual(repr(loc1), "Location('Sacramento', 100, 210)")
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")
        self.assertNotEqual(repr(loc), repr(loc1))
    
    # Add more tests!

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc, loc1)
        loc2 = Location("Sacramento", 100, 210)
        self.assertNotEqual(loc1, loc2)


if __name__ == "__main__":
        unittest.main()
