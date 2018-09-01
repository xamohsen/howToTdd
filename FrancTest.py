import unittest
from Franc import *


class FrancTest(unittest.TestCase):

    def test_multiplication(self):

        d = Franc(5)
        self.assertEqual(Franc(10), d.times(2))
        self.assertEqual(Franc(15), d.times(3))
