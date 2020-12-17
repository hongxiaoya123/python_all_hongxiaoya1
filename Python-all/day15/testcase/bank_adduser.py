import unittest
from day14.bank2 import bank_addUser
'''
    1.搞清楚哪些是要测的业务逻辑部分
    2.写核心部分
    3.业务：
        用户满了：3
        已经存在：2
        开户成功：1
        username,password,country,province,street,door,money
'''

class TestBankAddUser(unittest.TestCase):

    def testAddUser(self):
        username ="刘"
        password = "123123"
        country ="中国"
        province = "河南省"
        street = "新福大街"
        door = "189"
        money = 700

        status = 1 #期望结果

        # 实际结果
        s = bank_addUser(username,password,country,province,street,door,money)

        # 断言
        self.assertEqual(status,s)

    def testAddUser1(self):
        password = "123"
        country = "中国"
        province = "湖南省"
        street = "新大街"
        door = "19"
        money = 560
        status =3

        # 先添加100位用户
        for i in range(100):
            username = "张三" + str(i)

            bank_addUser(username, password, country, province, street, door, money)

        s = bank_addUser("李四",password,country,province,street,door,money)

        self.assertEqual(status, s)















