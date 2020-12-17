from DBUtils import MYsqlUtils
from ExcelUtils import ExcelUtils
import os
class dataread:
    list=None
    def __init__(self,mode,filename="",sheetname="0",host="locahost",database="",user="",password="",tablename=""):
        if mode == "excel":
            if filename=="":
                raise Exception("文件名不能为空!")
            elif not os.path.isfile(filename):
                raise Exception("文件不存在！")
            else:
                dataread.list=ExcelUtils.read(filename,sheetname)
        elif mode =="database":
            dataread.list=MYsqlUtils.read(host=host,database=database,user=user,password=password,tablename=tablename)
        else:
            raise Exception("对不起，无法识别您的操作！")
