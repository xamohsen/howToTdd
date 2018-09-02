import unittest

from Money import *


class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        d = Money.dollar(5)
        f = Money.franc(5)
        # test dollar multiplication
        self.assertEqual(Money(10, "USD"), d.times(2))
        self.assertEqual(Money(15, "USD"), d.times(3))
        # test franc multiplication
        self.assertEqual(Money(15, "CHF"), f.times(3))
        self.assertEqual(Money(10, "CHF"), f.times(2))

    def test_equality(self):
        # test money equality
        self.assertTrue(Money(5, "USD").__eq__(Money.dollar(5)))
        self.assertFalse(Money(5, "USD").__eq__(Money.dollar(15)))
        self.assertFalse(Money.franc(5).__eq__(Money.dollar(5)))

    def testCurrency(self):
        self.assertEqual("USD", Money(1, "USD").getCurrency())
        self.assertEqual("CHF", Money(1, "CHF").getCurrency())

    def testSimpleAdd(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        self.assertEqual(five, sum.aged)
        self.assertEqual(five, sum.addend)
