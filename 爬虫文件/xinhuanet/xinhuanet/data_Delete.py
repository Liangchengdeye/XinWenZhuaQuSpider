# -*- coding: utf-8 -*-
# 过期新闻删除
# '''请谨慎操作'''
# create by W_H_J 2017/9/29
import time
import datetime
from dbhelper import DBHelper
if __name__ == '__main__':
    while 1:
         try:
            print "The deletion will be performed, please choice (Y/N), Y: ok, N: cancel:"
            str = raw_input('Choice:')
            if str == 'y' or str == 'Y':
                print "---- Confirm delete ----"
                a = raw_input('Please enter a date,format: yyyy-mm-dd:\n\r')
                t = time.strptime(a, "%Y-%m-%d")
                y, m, d = t[0:3]
                str_time = datetime.datetime(y, m, d)
                # 时间类型转字符串
                str3 = str_time.strftime('%Y-%m-%d')
                # print type(str3)
                # 执行删除数据库任务
                data_delete = DBHelper()
                sql = "delete from news where news_pubtime <= %s"
                params = [str3]
                data_delete.delete(sql, *params)
                # if str4:
                #     print "删除成功！"
                # else:
                #     print "删除失败，请查看数据库！"
                # print str_time
            elif str == 'N' or str == 'n':
                print "------------------------- Cancel operation --------------------------------"
            break
         except:
             print "#### The input format is error！####"

    raw_input("Press any key to end !")