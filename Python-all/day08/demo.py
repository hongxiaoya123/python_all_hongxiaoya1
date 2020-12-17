'''
    1.写入到文件：a.txt
    2.写入的数据："万能的测试开发"
    文件操作模式：
        w：写
        r：读
        +：可读可写
        a:只能写（可以在原来的基础上附加数据）
        b：字节读写
        wb（写入字节：写入一个图片，mp3，mp4）
    读取：
        read()读取所有数据，弊端：直接加载所有数据，若数据太大，机器太卡
        readlines():读取所有行，并将每一行放入到列表
        readline():单独读取一行

'''
# 1.打开文件，并获取文件句柄（把柄）
# f = open("a.txt","w+",encoding="UTF—8")
#
# # 2.写入数据
# f.write("万能的测试开发!!!!!\n")   #用到c语言底层资源

# f.writelines("\t\t静夜思(李白)\n")
# f.writelines("床前明月光，疑似地上霜。\n")
# f.writelines("举头望明月，低头思故乡！\n")

#3.关闭资源（）
# f.close()

f = open("lian.jpg","rb") # 读取
w = open("表情包.jpg","wb") # 写入

# 读取一个图片
data = f.read()

# 将读取数据写入到另一个文件中
w.write(data)

# 关闭读取和写入资源
f.close()
w.close()

# 输出
print(data)

# 从当前盘复制到另一个盘里
f = open("../景甜.jpg","rb")
w = open("D:/旺财.jpg","wb")

data =  f.read()
w.write(data)

f.close()

w.close()