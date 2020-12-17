name=input("请输入姓名：")
age=int(input("请输入年龄："))
sex=input("请输入性别：")
id=input("请输入身份证号：")
high=int(input("请输入身高："))
weight=input("请输入体重：")

info='''
--------------中国建设银行开户个人信息------------
姓名:{name}
年龄:{age}
性别:{sex}
身份证号:{id}
身高:{high}
体重:{weight}
----------------------------------------------
'''
print(info.format(name=name,age=age,sex=sex,id=id,high=high,weight=weight))




