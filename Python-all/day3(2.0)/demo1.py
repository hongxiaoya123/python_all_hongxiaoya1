
for i in range (1,10):
    for j in range (1,i+1):
        print(j,"x",i,"=",(j*i),"\t",end="")
    print()

'''
a=int(input("输入第一条边:"))
b=int(input("输入第二条边:"))
c=int(input("输入第三条边："))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("构成等边三角形")
    elif( a==b or a==c or b==c):
        print("构成等腰三角形")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("构成直角三角形")
    else:
        print("构成三角形！")
else:
    print("不构成三角形！")
'''
'''
num=int(input("请输入一个数："))
while num != 0:
    print(num % 10)
    num = num // 10
'''
'''
num=54321
w=num//10000
q=num//1000%10
b=num//100%10
s=num//10%10
g=num%10
print(w,q,b,s,g)
r=pow(w,3)+pow(q,3)+pow(b,3)+pow(s,3)+pow(g,3)
print(r)
'''
'''
A=78
B=56
B= A + B
A= B - A
B= B - A
print(A,B)
'''
'''
password="1234"
for i in range(3):
    p=input("请输入密码:")
    if p == password :
        print("登录成功!")
        break
    else:
        print("密码错误！")
        if i ==2:
            print("三次密码输入错误!")
            break
'''

for i in range(9,0,-1):
    for h in range(1,i+1):
        print(h, "x", i, "=", (h * i), "\t",end="")
    print()

'''
a=1
n=3
for i in range(n,n+1):
    a=a*i
    print(a)
'''
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
'''
'''
sum = 0
for i in range(1,21):
    sum1 = 1
    for i in range(1,i+1):
        sum1 = sum1 * i
    sum = sum1 + sum
print(sum)
'''
'''
max = 0
sum = 0
for i in range(10):
    num = int(input("请输入数据:"))
    if num > max:
        max = num
    sum = sum + num
print("最大值为：",max,"和为：",sum,"平均数为：",sum//10)
'''
'''
sum = 0
a = [1,5,21,30,15,9,30,24]
for i in range(0,len(a)):
    if a[i]% 5==0:
        sum =sum +a[i]
print(sum)

a = [1,5,21,30,15,9,30,24]
print(sorted(a))
'''






































