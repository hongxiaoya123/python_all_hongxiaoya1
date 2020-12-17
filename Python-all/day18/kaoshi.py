'''
import copy
# 浅拷贝  无法拷贝列表中的子列表
list = [1,2,3,[4,5,6]]
list1 = copy.copy(list)
list1[3][0] = 8
print(list[3][0])

# 深拷贝  完全拷贝
list = [1,2,3,[4,5,6]]
list1 = copy.deepcopy(list)
list1[3][2] =7
print(list[3][2])
print(list1[3][2])
'''

'''# 去重
list= [1,3,4,5,2,6,1]
print(set(list))
'''

'''# 转换列表
a = (1,2,5)
print(list(a))
'''

''' #选择排序
a = [1,6,3,2,5,7,8,9]
for i in range(len(a)):
    for j in range(i + 1,len(a)):1
        if a[j] > a[i]:
            # c =a[j]
            # a[j] = a[i]
            # a[i] =c
            a[i],a[j] = a[j],a[i]
print(a)
'''

'''# 冒泡排序 
a = [1,6,3,2,5,7,8,9]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    print("第",(i+1),"轮的数据是：",a)
'''

'''#列表翻转 
list=[1,2,3,4,5,6]
for i in range(0,len(list)):
    for j in range(len(list)-1):
        if list[j]<list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)
'''

'''
#字符串字符的统计
a = "this is a  dog,that is a monkey!"
for index,i in enumerate(a):
    if i in a[:index]:
        continue
    print(i,"出现了",a.count(i))
'''

'''#字典求出现次数
a =[1,3,2,1,2,3,1]
d ={}
for i in a:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i]=1
print(d)
'''

'''# 0~100质数
list =[]
for i in range(2,100):
    for j in range(2,int(i/2)+1):
        if not i%j:
            break
    else:
        list.append(i)
print(list)
'''

'''#时间读写
import time
while True:
    f = open("a.log","r+")
    w = open("b.txt","w+")
    data = f.read()
    w.write(data)
    print(w.read)
    time.sleep(60)
'''

'''#面向对象描述水杯
class cup:
    rl= None
    brand = None
    money= None

c=cup()
c.rl = "100ml"
c.brand = "格里呐"
c.money = 10
print("这个水杯",c.rl,"容量,品牌是",c.brand,"价格是",c.money)
'''

'''#遍历列表
list = [lambda : i for i in range(10)]
f = list[0]()
print(f)
'''

'''#删除两边的空格
s="    hello world   "
print(s.strip())
'''


