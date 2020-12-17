import xlrd

    #1.安装与导入xlrd模块（读取excel）
#1. 打开工作簿并获取句柄
data = xlrd.open_workbook("C:\\Python\\a.xlsx")

#2.从工作簿里选中选项卡
sheet = data.sheet_by_name("用户管理表")

# 3.
print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")
rows = sheet.nrows #获取所有行数
cols = sheet.ncols #获取所有列数
# f = open("用户管理表.txt","w",encoding="utf-8") #打开一个文件用于写入数据
# a = []

# 4.遍历所有数据
for i in range(rows):
    for j in range(cols):
        print(str(sheet.cell_value(i,j)).replace(".0",""),"\t",end="")
    print()
for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(str(sheet.cell_value(i,j)).replace(".0",""))
    string = ",".join(a)
    f.write(string + "\n")


