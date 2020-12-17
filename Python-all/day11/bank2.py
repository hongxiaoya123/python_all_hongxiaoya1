import random
import datetime
from tools import tools
bank = {}
bank_name ="中国工商银行昌平支行"
bank_choice ={"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}

myinfo = '''
\033[0;32;40m
------------账户信息-------------
账户：{account}
姓名：{username}
密码：{password}
地址：
    国家：{country}
    省份：{province}
    街道：{street}
    门牌号：{door}
账户余额：{money}
注册银行名：{bank_name}
---------------------------------
\033[0m
'''

#欢迎模块
welcome = '''
************************************
*       中国工商银行账户管理系统        *
************************************
*                选项               *
'''
welcome_item ='''*              {0}.{1}               *'''
def print_welcome():
    print(welcome,end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))
    print("************************************")


#输入帮助方法
def inputHelp(chose,datatype = "str"):
    while True:
        print("请输入",chose,":")
        i = input(">>>>>:")
        if len(i) ==0:
            print("该选项不能为空，请重新输入！")
        if datatype != "str":
            return int(i)
        else:
            return i

# 判断是否存在该银行选项
def isExists(chose,data):
    if chose in data:
        return True
    return False

# 获取随机
def getRandom(self):
    li ="0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    string = ""
    for i in range(8):
        string = string +li[int(random.random()*len(li))]
    return string

# 通过账号获取账户信息
def findByAccount(account):
    for i in bank.keys():
        if bank[i]["account"] == account:
            return i
        return None


class User:
    __account = None
    __username =None
    __password =None
    __address =None
    __money =None
    __reg_date =None
    __bankname =None

    def __init__(self,username,password,address,money):
        self.__username = username
        self.__password = password
        self.__address = address
        self.__money = money
        self.__account = tools().getRandom()
        self.__bankname = "中国工商银行昌平支行"
        self.__reg_date = datetime()

    def getAccount(self):
        return self.__account
    def setUsername(self,username):
        self.__username = username
    def setPassword(self,password):
        self.__password = password
    def setAddress(self,address):
        self.__address = address
    def setMoney(self,money):
        self.__money = money
    def getReg_date(self):
        return self.__reg_date
    def getBankname(self):
        return self.__bankname

class Address:
    __country = None
    __province = None
    __street = None
    __door =None

    def __init__(self,country,province,street,door):
        self.__country = country
        self.__province =province
        self.__street = street
        self.__door = door

    def setCountry(self,country):
        self.__country = country
    def setProvince(self,province):
        self.__province = province
    def setStreet(self,street):
        self.__street = street
    def setDoor(self,door):
        self.__door =door




while True:
    print_welcome()
    chose = inputHelp("请输入选项:")
    if isExists(chose,bank_choice):
        if chose == "1":
            pass
        elif chose == "2":
            pass
        elif chose == "3":
            pass
        elif chose == "4":
            pass
        elif chose == "5":
            pass
        elif chose == "6":
            print("Bye bye~~")
            break
    else:
        print("不存在该选项！")









