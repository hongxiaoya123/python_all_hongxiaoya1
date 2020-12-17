'''
li = [1,2,3,4,5,6,7,8,9]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[j] > li[i]:
            li[j],li[i] = li[i],li[j]
print(li)
'''
'''
a = [1,4,7,5,82,1,3,4,5,9,7,6,1,10]
for i in range(0,len(a)):
    count = 0
    flag =True
    for k in range(0,i):
        if a[k] == a[i]:
            flag = False
            break
    if flag ==False:
        continue
    for j in range(0,len(a)):
        if a[i] == a[j]:
            count +=1
    print(a[i],"出现了",count,"次!")
'''
'''
names = [
    ["何登勇","56","男","106","IBM", 500 ,"50"],
    ["曹东雪","19","女","230","微软", 501 ,"60"],
    ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
    ["李汉聪", "45", "男", "230", "Tencent", 700 , "10"]
]
names.append(["张佳伟,45,男,220,alibaba,500,30"])
print(names)
'''
'''
#求出现的次数  字典    key：
a = [1,4,7,5,82,1,3,4,5,9,7,6,1,10]
d = {}
for i in a:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
'''









































