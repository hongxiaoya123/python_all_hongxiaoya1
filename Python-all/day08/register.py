'''
# 读取
a = {}
f=open("a.txt","r+",encoding="utf-8")
data =f.readlines()
for i in data:
    line = i.split(":")
    a[line[0]] = line[1].replace("\n", "")
f.close()
# 开发
name = input("请输入用户名：")
password = input("请输入密码：")
if name in a:
    if password == a[name]:
        print("登陆成功！")
    else:
         print("密码错误！")
else:
    print("该用户不存在！")
'''
'''
list = open("scores.txt","r+",encoding="utf-8")
list1 = open("scores1.txt","w+",encoding="utf-8")
num={}
for i in list:
    num1=0
    for j in i.strip().split(" ")[1:]:
        num1=num1+int(j)
        num2=i.strip().split(" ")[0:1]
    list1.write("%s %s\n"%(i[0:3],num1))
list.close()
'''
'''
f = open("baidu_x_systm.log","r+",encoding="utf-8")
dic = {} # {ip:次数}
lines = f.readlines()

for line in lines:
    ip = line.split(" ")[0]
    if ip in dic:
        dic[ip] = dic[ip] +1
    else:
        dic[ip] = 1
print(dic)
'''

f = open("scores.txt","r+",encoding="utf-8")
dic = {} # 姓名：总分

lines = f.readlines() #["罗恩 23 35 44"]

for line in lines:
    li = line.replace("\n","").split(" ") # ["罗恩"，23,35,44]
    name = li[0] # "罗恩"
    scores = li[1:] # ["23","35","44"]
    dic[name] = sum([int(i) for i in scores]) # [23 35 44]  lambda

print(dic)

list = open("scores.txt","r+",encoding="utf-8")
list1 = open("scores1.txt","w+",encoding="utf-8")
num={}
for i in list:
    num1=0
    for j in i.strip().split(" ")[1:]:
        num1=num1+int(j)
        num2=i.strip().split(" ")[0:1]
    list1.write("%s %s\n"%(i[0:3],num1))
list.close()


f = open("baidu_x_systm.log","r+",encoding="utf-8")
dic = {} # {ip:次数}
lines = f.readlines()

for line in lines:
    ip = line.split(" ")[0]
    if ip in dic:
        dic[ip] = dic[ip] +1
    else:
        dic[ip] = 1
print(dic)





