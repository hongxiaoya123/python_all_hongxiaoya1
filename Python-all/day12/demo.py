'''
class OldPhone:
    phoneNumber = None
    vioce = None

    def call(self,number):
        print(self.phoneNumber,"正在给",number,"打电话......")


class NewPhone(OldPhone):
    place =None
    picture =None
    ps =None

    def call(self,number):
        super().call(number)
        print("归属地",self.place,"图片",self.picture,"备注",self.ps)

phone = NewPhone()
phone.phoneNumber ="13425637892"
phone.vioce = "月亮之上"

phone.place ="河北"
phone.picture ="佩奇"
phone.ps ="旺财"
phone.call("15654638728")
'''
'''
import time

class Animal(object):
    __color = None
    __weight =None
    __age = None

    def __init__(self,color,weight,age):
        self.__color = color
        self.__weight = weight
        self.__age =age

    def setColor(self,color):
        self.__color =color
    def getColor(self):
        return self.__color
    def setWeight(self,weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight
    def setAge(self,age):
        self.__age =age
    def getAge(self):
        return self.__age

class Dog(Animal):
    __brand = None

    def __init__(self,color,weight,age,brand):
        super().__init__(color,weight,age)
        self.__brand =brand

    def setBrand(self,brand):
        self.brand = brand
    def getBrand(self):
        return self.__brand


    def show(self):
        for i in range(3):
            print("汪..呜..",end="")
            time.sleep(1)
        print("我是",self.getColor(),
              "的狗,我有",self.getWeight(),"斤,"
              "我能活",self.getAge(),"年,我是",self.getBrand())

d = Dog("蓝色",15,15,"中华田园犬")
d.show()
'''