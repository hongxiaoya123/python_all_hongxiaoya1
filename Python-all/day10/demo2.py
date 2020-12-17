import pymysql
import xlrd

data = xlrd.open_workbook("C:\\Python\\b.xlsx")

sheet = data.sheet_by_name("用户管理表")

print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")
rows = sheet.nrows
cols = sheet.ncols
f = open("用户管理表.txt","w",encoding="utf-8")
a = []

for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(str(sheet.cell_value(i,j)).replace(".0",""))
    string = "\t\t".join(a)
    f.write(string + "\n")
    print(string)

con = pymysql.connect(host="localhost",user="root",password="",database="day10",charset="utf8")

cursor =con.cursor()

sql = "select * from person"

s = cursor.execute(sql)
print(s)

one = cursor.fetchall()
print(list(one))

con.commit()

cursor.close()
con.close()


