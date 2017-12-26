# -*- coding: utf-8 -*-
# en_people.Home网爬取内容
# create 2017/9/20 W_H_J

import scrapy
from News.items import en_people_home
import re
from News.dbhelper import DBHelper
class en_people_cnSpider(scrapy.Spider):
    name = "en_people_Home"
    start_urls = ["http://en.people.cn"]

    # 新闻首页链接
    def parse(self, response):  # | //div[5]/div[1]/div[1]/div/ul/ul/li/a/@href
        # 启用数据库助手
        data_seltct = DBHelper()
        sql_home = "select news_id from news"  # 单独查询编辑

        item = en_people_home()
        # 主页面抓取规则
        # 1 //div[4]/div/div/div/ul/li/a/@href
        # 2.//div[4]/div/div/b/a/@href
        # 3.//div[5]/div[1]/div/div/ul/ul/li/a/@href
        # 4.//div[5]/div[1]/div/div/ul/div/a[2]/@href
        # 5.News of CPC //div[5]/div[2]/ul/li/a/@href
        # om.nn320170919900009271033 http: // english.people.com.cn / n3 / 2017 / 0919 / c90000 - 9271033.html
        for href in range(len(response.xpath('//div[4]/div/div/div/ul/li/a/@href | //div[4]/div/div/b/a/@href | //div[5]/div[1]/div/div/ul/ul/li/a/@href | //div[5]/div[1]/div/div/ul/div/a[2]/@href | //div[5]/div[2]/ul/li/a/@href'))):
            full_url = response.urljoin(response.xpath('//div[4]/div/div/div/ul/li/a/@href | //div[4]/div/div/b/a/@href | //div[5]/div[1]/div/div/ul/ul/li/a/@href | //div[5]/div[1]/div/div/ul/div/a[2]/@href | //div[5]/div[2]/ul/li/a/@href').extract()[href]).encode('utf-8')
            str_index = full_url.index("n3")
            str_Id = full_url[str_index+2:-5].replace('/', '').replace('-', '').replace('c', '')
            # 发布时间
            str_pubtime1 = str_Id[:4]
            str_pubtime2 = str_Id[4:6]
            str_pubtime3 = str_Id[6:8]
            str_pubtime = str_pubtime1+"-"+str_pubtime2+"-"+str_pubtime3
            # print str_pubtime
            item['home_title'] = response.xpath('//div[4]/div/div/div/ul/li/a/text() | //div[4]/div/div/b/a/text() | //div[5]/div[1]/div/div/ul/ul/li/a/text() | //div[5]/div[1]/div/div/ul/div/a[2]/text() | //div[5]/div[2]/ul/li/a/text()').extract()[href]
            item['home_url'] = full_url
            item['home_id'] = str_Id
            item['home_time'] = str_pubtime
            yield item
            # 插入数据
            str_data = data_seltct.select(sql_home)  # 执行sql语句
            if item["home_id"] in str_data:
                print "##### Already existing, not inserted #####"
            else:
                print "-----------------################## insert ################-----------------"
                sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                params = (item["home_id"], item['home_title'], item['home_url'], item['home_time'], '1')
                data_seltct.insert(sql, *params)


