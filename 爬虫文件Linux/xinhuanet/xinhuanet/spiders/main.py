﻿# -*- coding: utf-8 -*-
# 定时任务
# create by W_H_J 2017/9/22
import time
import subprocess
import schedule
import time
def crawl_work():
    # cmdline.execute('scrapy crawl my_spider'.split()) # 不要用自带的cmdline
    print "*********************************************************"
    print "******************* start work! *************************"
    print "*********************************************************"
    # 爬虫名字
    subprocess.Popen('scrapy crawl xinhuanet_All -o data/xinhuanet_All.csv')

if __name__=='__main__':
    # 多久后开始执行
    # schedule.every(1).minutes.do(crawl_work)
    print "%%%%%%%%%%%% Open successfully once every four hours %%%%%%%%%%"
    print "################# starts Four hours later #####################"
    # 提前启动一次
    i = 0
    while i < 1000:
        i = i+1
    if i == 1000:
        # 延迟10分钟
        time.sleep(10*60)
        schedule.every(30).seconds.do(crawl_work).run()
        schedule.clear()
        i = 1001
    # 按照计划任务爬取 4小时
    schedule.every(4).hours.do(crawl_work)
    while True:
        # 开始启动一次
        schedule.run_pending()
        # 每隔多久执行一次
        time.sleep(1)
