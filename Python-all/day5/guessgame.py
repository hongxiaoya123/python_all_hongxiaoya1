import random

num= int(random.random()*1500)
count=0
while True:
    guess=int(input("请输入您要猜的数字："))
    count=count+1
    if num >guess:
        print("小了！")
    elif num<guess:
        print("大了！")
    else:
        print("恭喜你，猜中了，您猜的数字为：",num ,"您猜了",count,"次了！")
        break

