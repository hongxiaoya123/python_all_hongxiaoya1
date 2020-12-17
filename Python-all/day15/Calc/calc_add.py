import unittest
from day15.Calc.calcdemo import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [1,2,3],
    [2,3,5],
    [4,6,10]
]
@ddt
class TestCalcAdd(unittest.TestCase):
    @data(*data1)
    @unpack

    def testAdd(self,q,w,e):
        a = q
        b = w
        status = e

        c = Calc()
        s = c.add(a,b)

        self.assertEqual(status,s)


data2 = [
    [3,2,1],
    [5,3,2],
    [10,6,4]
]
@ddt
class TestCalcSubs(unittest.TestCase):
    @data(*data2)
    @unpack

    def testSubs(self,q,w,e):
        a = q
        b = w
        status = e

        c = Calc()
        s = c.subs(a,b)

        self.assertEqual(status,s)


data3 = [
    [3,2,6],
    [5,3,15],
    [10,6,60]
]
@ddt
class TestCalcMult(unittest.TestCase):
    @data(*data3)
    @unpack

    def testMult(self,q,w,e):
        a = q
        b = w
        status = e

        c = Calc()
        s = c.mult(a,b)

        self.assertEqual(status,s)

data4 = [
    [6,2,3],
    [15,3,5],
    [60,6,10]
]
@ddt
class TestCalcDivi(unittest.TestCase):
    @data(*data4)
    @unpack

    def testDivi(self,q,w,e):
        a = q
        b = w
        status = e

        c = Calc()
        s = c.divi(a,b)

        self.assertEqual(status,s)










