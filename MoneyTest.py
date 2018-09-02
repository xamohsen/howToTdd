import unittest


from Dollar import *
from Franc import *


class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        d = Dollar(5)
        f = Franc(5)
        # test dollar multiplication
        self.assertEqual(Dollar(10), d.times(2))
        self.assertEqual(Dollar(15), d.times(3))
        # test franc multiplication
        self.assertEqual(Franc(15), f.times(3))
        self.assertEqual(Franc(10), f.times(2))

    def test_equality(self):
        # test dollar equality
        self.assertTrue(Dollar(5).__eq__(Dollar(5)))
        self.assertFalse(Dollar(5).__eq__(Dollar(15)))
        # test franc equality
        self.assertTrue(Franc(5).__eq__(Franc(5)))
        self.assertFalse(Franc(5).__eq__(Franc(15)))
        # test money equality
        self.assertFalse(Franc(5).__eq__(Dollar(15)))

    def testCurrency(self):
        self.assertEqual("USD", Dollar(1).currency())
        self.assertEqual("CHF", Franc(1).currency())
