import unittest
from Dollar import *


class DollarTest(unittest.TestCase):

    def test_multiplication(self):
        d = Dollar(5)
        self.assertEqual(d.times(2), 10)
