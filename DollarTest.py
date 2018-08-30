import unittest
from Dollar import *


class DollarTest(unittest.TestCase):

    def test_multiplication(self):
        d = Dollar(5)
        self.assertEqual(10, d.times(2).amount)
        self.assertEqual(15, d.times(3).amount)