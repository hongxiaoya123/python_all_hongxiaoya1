import unittest
from day14.oridemo import TestCalc
from day14.subsdemo import TestCalc1
from HTMLTestRunner import HTMLTestRunner
#创建测试集
sutie = unittest.TestSuite()

# 将你要的测试用例加载进测试集
sutie.addTest(TestCalc("testAdd"))
sutie.addTest(TestCalc1("testSubs"))

#创建测试运行器（专门运行测试用例）
# TextTestRunner文本运行器的缺点：只能在控制台上看有没有通过
#runner = unittest.TextTestRunner()
# HTMLTestRtunner:界面版的运行器
f = open("计算器.html","w+",encoding="utf-8")
htmlrunner =HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title ="计算器的测试报告",
    description ="这是一个计算器的测试",
    verbosity=1, #粗细粒度
)
#运行器运行测试集
htmlrunner.run(sutie)






