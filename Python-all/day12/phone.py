
import time
class OldPhone:
    __phoneNumber = None
    __brand = None


    def __init__(self,phoneNumber,brand):
        self.__phoneNumber =phoneNumber
        self.__brand =brand

    def setphoneNumber(self,phoneNumber):
        self.__phoneNumber = phoneNumber
    def getphoneNumber(self):
        return self.__phoneNumber

    def setBrand(self,brand):
        self.__brand =brand
    def getBrand(self):
        return self.__brand

class NewPhone(OldPhone):
    def __init(self,phoneNumber,brand):
        super().__init__(phoneNumber,brand)

    def call(self,number):
        for i in range(1):
            print("语音拨号中......",end="\n")
            time.sleep(2)
        print(self.getBrand(),"在用",self.getphoneNumber(),"正在给",number,"打电话")

phone = NewPhone("iphone","憨憨:13546278946")
phone.call("刘日成:18708987324")

'''
class cook:
    __name = None
    __age = None
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
'''

class person:
    __name = None
    __age = None
    __sex = None












