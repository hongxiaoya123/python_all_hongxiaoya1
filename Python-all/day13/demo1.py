'''
def devide(a,b):
    if a == 0:
        raise IndexError("被除数不能为0！")
    else:
        print(a/b)

try:
    devide(9,0)
except ZeroDivisionError as d:
    print("我处理了第一个!")
except IndexError as d:
    print("让我处理了第二个")
except Exception as d:
    print("甭管了，我处理了！")
'''
'''
def start():
    print("计算器已经启动")
def devision(a,b):
    print(a/b)

def end():
    print("AC键关闭，电池扣了！")


try:
    start()
    devision(9,0)

except ZeroDivisionError as e:
    print("捕捉到了被除数不能为0异常！",e)
except Exception as e:
    print("我都能捕捉！",e)
finally: # finally代码块肯定会执行
    end()  # 重要资源关闭的代码
'''
'''
def devision(a,b):
    try:
        print(a/b)
        return"除法正常处理"
    except IndexError as e:
        print("角标异常！")
        return 1
    except ZeroDivisionError as e:
        print("被除数不能为0!")
        return 2
    finally:
        print("执行最终代码块！")
        return 3

s = devision(3,0)
print(s)
'''










'''
自定义异常：
    1.继承异常体系中的父类
    2.重写__init__方法，传入msg异常信息
'''
'''
class UserNotExistException(Exception):
    def __init__(self,msg):
        self.msg = msg
raise UserNotExistException("用户信息不匹配！")
'''
















