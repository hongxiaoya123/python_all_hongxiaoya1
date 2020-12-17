'''
import random
num=int(random.random()*100+50)#0~1
print(num)
'''

num=int(input("请输入您要的层数："))
i=1
while i <=num:
    print("第",i,"层",end="")
    b=1
    while b<=i:
        print(b,"x",i,"=",(b*i),"\t",end="")
        b=b+1
    print()
    i=i+1












