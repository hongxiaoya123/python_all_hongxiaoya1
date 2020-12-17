import  unittest
from day14.calc import Calc

class TestCalc1(unittest.TestCase):

    def testSubs(self):
        a = 1
        b = 2
        sum = -1
        c = Calc()
        s = c.subs(a,b)

        self.assertEqual(sum,s)
        