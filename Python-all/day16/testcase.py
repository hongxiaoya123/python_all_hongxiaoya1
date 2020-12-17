import unittest
from bank import bank_saveMoney
from ddt import ddt
from ddt import data
from ddt import unpack
from dataread import dataread


data1 =dataread("database",database="bank",tablename="savemoney",user="root",password="",host="localhost").list
@ddt
class TestBanksaveMoney(unittest.TestCase):

    @data(*data1)
    @unpack

    def testSaveMoney(self,ac,money):
        s =False
        b = bank_saveMoney(ac,money)



        self.assertEqual(s,b)
