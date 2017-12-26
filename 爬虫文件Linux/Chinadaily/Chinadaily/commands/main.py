# -*- coding: utf-8 -*-
# 定时任务
# create by W_H_J 2017/9/22
import time
import subprocess
import schedule
import time
def crawl_work():
    # cmdline.execute('scrapy crawl my_spider'.split()) # 不要用自带的cmdline
    print "**************************************************"
    print "****************** start work! *******************"
    print "**************************************************"
    # 爬虫名字
    subprocess.Popen('scrapy crawlall')

if __name__=='__main__':
    # 多久后开始执行
    # schedule.every(1).minutes.do(crawl_work)
    print "%%%%%%% Open successfully once every two hours %%%%%%%"
    print "############# starts Two hours later #################"
    # 提前启动一次
    i = 0
    while i < 1000:
        i = i+1
    if i == 1000:
        # 延迟5分钟
        time.sleep(5*60)
        schedule.every(30).seconds.do(crawl_work).run()
        schedule.clear()
        i = 1001
    # 按照计划任务爬取 设置为2小时运行一次
    schedule.every(2).hours.do(crawl_work)
    while True:
        # 开始启动一次
        schedule.run_pending()
        # 每隔多久执行一次
        time.sleep(1)
