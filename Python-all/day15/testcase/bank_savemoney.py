import unittest
from day14.bank2 import bank_saveMoney

class TestBankSaveMoney(unittest.TestCase):

    def testSaveMoney(self):
        '''
            转入的数据：账号，存钱
            返回的数据：
                存钱失败！Ture
                失败：False
        ：return：
        '''
        #1.准备
        ac = "132133"
        money = 1000
        status =False

        #2. 调用被测方法
        s = bank_saveMoney(ac,money)
        self.assertEqual(status,s)
