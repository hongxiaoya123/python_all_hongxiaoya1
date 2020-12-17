import unittest
import os
from day15.testcase.bank_takemoney import TestBankTakeMoney
from day15.testcase.bank_savemoney import TestBankSaveMoney
from HTMLTestRunner import HTMLTestRunner

# 1.创建测试集
sutie = unittest.TestSuite()

# 2.用测试集加载测试用例
# sutie.addTest(TestBanktakemoney("testTakeMoney"))
# sutie.addTest(TestBankSaveMoney("testSaveMoney"))
# 2.1 借助测试加载器

# 2.2 获取加载器
loader =unittest.defaultTestLoader

# 2.3 寻找匹配的用例
case = loader.discover(os.getcwd(), pattern="bank*.py")

# 2.4 添加到测试集里
sutie.addTest(case)

# 3. 创建HTML
f = open("银行取钱.html", "w+", encoding="utf-8")
htmlrunner =HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title ="银行取钱的测试报告",
    description ="这是一个银行取钱的测试",
    verbosity=1, #粗细粒度
)
#4.运行器运行测试集
htmlrunner.run(sutie)
