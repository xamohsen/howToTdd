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

    def testPlusReturnSum(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        self.assertEqual(five, sum.aged)
        self.assertEqual(five, sum.addend)

    def testReduceSum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(7), result)

    def testSimpleAdd(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        self.assertEqual(five, sum.aged)
        self.assertEqual(five, sum.addend)

    def testReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def testReduceMoneyDifferentCurrency(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def testIdentityRate(self):
        self.assertEqual(1, Bank().rate("USD", "USD"))
