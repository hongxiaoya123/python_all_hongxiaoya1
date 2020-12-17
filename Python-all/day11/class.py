'''
    1.类：（类名首字母必须大写，方法第二个单词开始首字母大写）
        属性
        行为（功能：方法、函数）
    2.对象
        c = Car
        句柄 = 类名（）
    3.封装：
        3.1 将属性进行私有化
            将属性前面加上__
        3.2 提供方法间接赋值
    类对象：
        1.属性封装
        2.提供set xxx/get xxx方法，用户进行属性的间接赋值
        3.提供有参构造函数
'''
'''
class Person:
    __username = ""
    __age = None
    def setUsername(self,u):
        self.__username =u 

    def setAge(self,a):
        if a ==None:
            print("输入年龄有误！")
        elif a >115 or a < 0:
            print("输入年龄有误！")
        else:
            self.__age = a
    def show(self):
        print("他叫",self.__username,"他的年龄是:",self.__age)

c = person()

c.setUsername("憨憨")
c.setAge(88)
c.show()
'''

class Dog:
    __color = None
    __speed = None
    __belong = None
    def __init__(self,a,b,s):
        self.__color = a
        self.__speed = b
        self.__belong =s

    def setColor(self,a):
        self.__color = a
    def getColor(self):
        return self.__color
    def setSpeed(self,b):
        self.__speed = b
    def getSpeed(self):
        return self.__speed
    def setBelong(self,s):
        self.__belong = s
    def getBelong(self):
        return self.__belong

d = Dog("蓝色","犬科","30km/h")

print(d.getColor(),d.getSpeed(),d.getBelong())





