import unittest
import os
from HTMLTestRunner import HTMLTestRunner

sutie = unittest.TestSuite()

loader =unittest.defaultTestLoader

case = loader.discover(os.getcwd(), pattern="calc*.py")

sutie.addTest(case)

f = open("计算器.html", "w+", encoding="utf-8")
htmlrunner =HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title ="计算器钱的测试报告",
    description ="这是一个计算器的测试",
    verbosity=1,
)

htmlrunner.run(sutie)
