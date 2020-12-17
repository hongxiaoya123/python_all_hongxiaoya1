
import datetime
from tools import tools
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
    def setAccount(self,username):
        self.__username = username

