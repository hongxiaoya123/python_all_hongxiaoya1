import unittest
from day14.bank2 import bank_takeMoney

class TestBankTakeMoney(unittest.TestCase):

    def testTakeMoney(self):

        account = "qaz1"
        password = 123456
        money = 6000
        status = 0

        s =bank_takeMoney(account,password,money)
        print(s)

        self.assertEqual(status,s)

















