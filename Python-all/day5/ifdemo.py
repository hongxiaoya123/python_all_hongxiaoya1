i = 0 # 输入三次分数并判断
while i<3:
 score=int(input("请输入您本次考试分数："))
 if score<=100 and score>95:
    print("优秀！excellent!")
 elif score<=95 and score>80:
    print("良好！good!")
 elif score<=80 and score>70:
    print("一般！just so so!")
 elif score<=70 and score>=60:
    print("及格啦~再努力！")
 elif score<60 and score>=0:
    print("您点的男女混合双打已经在等着您啦~")
 else:
    print("输入非法！")
 i = i+1


