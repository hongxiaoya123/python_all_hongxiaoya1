'''
f=[1,4,33,4,7]
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print("列表的长度:",len(f))
'''
'''
a = [2,3,1,4,5,3]
max = a[0]
index = -1
for i in range (0,len(a)):
    if a[i] >= max:
        max = a[i]
        index = i
print("a里最大值为:",max,"所对应的角标为：",index)
'''
'''
sum = 0
a = [1,5,21,30,15,9,30,24]
for i in range(0,len(a)):
    if a[i]% 5==0:
        sum =sum +a[i]
print(sum)
'''

shop =[
    ["小米 watch",500],
    ["老干妈",10],
    ["泡椒凤爪",13],
    ["lenovo pc",4500],
    ["辣条",2.5],
]
print("欢迎来到超市购物广场".center(70,"-"))
# 1.先初始化自己的金钱
while True:
    salary = input("请输入您的初始金钱：")
    if salary.isdigit():#判断输入的字符串是否能看成数字
        salary = int (salary)
        print("您的初始金钱为：",salary,"祝您本次购物愉快！")
        break
    else:
        print("请输入您的初始金额！")
# 展示所有商品
mycart =[]
while True:
   for index,value in enumerate (shop):
    print(index,"  ",value)
    choice = input("请输入您要买的商品编号：")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(shop):
            if salary >= shop[choice][1]:
                mycart.append(shop[choice])
                salary -= shop[choice][1]
                print("恭喜你，添加成功！您的余额还剩：", salary)
            else:
                print("对不起，您的余额不足，请充值！")
        else:
            print("对不起，您输入的商品不存在！")
    elif choice == "q" or choice == "Q":
        print("欢迎下次光临")
        break
    else:
        print("输入不合法，请重新输入")
    print("-----------------------")
    for i in mycart:
        print(i)
    print("您的余额为：", salary)











