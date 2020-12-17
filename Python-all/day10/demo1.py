class people:
    age = 0
    name = ""
    sex = ""
    height = ""
    weight = ""

    def walk(self):
        print("走过来，走过去！烦死人！！")

c = people()
c.age = 58
c.name = "刘日成"
c.sex = "女"
c.height = "160"
c.weight ="160"

c.walk()
print("ta叫",c.name,"年龄",c.age,"性别",c.sex,"身高",c.height,"体重",c.weight)
