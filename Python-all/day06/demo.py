'''
a = [3,4,1,2,6,7,5,0,9]
for i in range(len(a)-1):
    for j in range(i + 1,len(a)):
        if a[j] > a[i] :
            a[i],a[j] =a[j],a[i]
print(a)
'''
'''
string ="this is a  dog,that is a monkey!"
li = list(string)
for i in range(0,len(li)):
    count = 0 #计数器
    #排重
    flag = True #开关位置
    for k in range(0,i):
        if li[k] == li[i]:
            flag =False #一旦发现相同字符，开关位置关闭
            break
    if flag == False:
        continue
    for j in range(0,len(li)):
        if li[i] == li[j]:
            count +=1
    print(li[i],"出现了",count,"次！")
'''
'''
string ="this is a  dog,that is a monkey!"
for index,ch in enumerate(string):
    if ch in string[:index]:
        continue
    print(ch,"出现了",string.count(ch))
'''
'''
"好处：一本万利，写一次，多次使用"

def sum(a,b):#申明一个方法，能接受两个数，并对接受的数据进行求和，然后使用return进行返回
    print("已成功登录")
    c = a+b
    print("任务完成")
    return c
print("准备登陆.....")
s = sum(12,32) #调用sum方法，实现求和
print("退出登陆")
print(s)
'''
'''
# 写一个方法，打印任何传入的数据
def printStr(msg):
    print(msg)
printStr("hello!")
'''






























