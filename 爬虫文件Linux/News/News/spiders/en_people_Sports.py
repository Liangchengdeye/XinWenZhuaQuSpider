# -*- coding: utf-8 -*-
# en_people.Sports网爬取内容
# create 2017/9/18 W_H_J

import scrapy
from News.items import en_people_sports
from News.dbhelper import DBHelper
class en_people_Sports(scrapy.Spider):
        name = "en_people_Sports"
        # 爬虫爬取的数据范围
        allowed_domains = ['en.people.cn']
        # 需要拼接的url
        baseURL = "http://en.people.cn/90779/"
        offset = 1
        # 启示地址
        start_urls = [baseURL + "index"+str(offset)+".html"]
        # 新闻首页链接
        def parse(self, response):
            # 启用数据库助手
            data_seltct = DBHelper()
            sql_sport = "select news_id from news"  # 单独查询编辑
            str_data = data_seltct.select(sql_sport)  # 执行sql语句
            node_list=response.xpath("//div[@class='d2p3_left fl']")
            # 循环读取到每条新闻Title并获取链接
            for node in node_list:
                item = en_people_sports()
                for i in range(len(node.xpath("//h3/a/text()").extract())):
                    item['sports_title'] = node.xpath("//h3/a/text()").extract()[i]
                    str_url =  "http://en.people.cn"+node.xpath("//h3/a/@href").extract()[i]
                    item['sports_url'] =str_url
                    # 生成新闻ID
                    str_index = str_url.index("n3")
                    str_Id = str_url[str_index + 2:-5].replace('/', '').replace('-', '').replace('c', '')
                    item['sports_id'] = str_Id
                    # 发布时间
                    if "n3" in str_url:
                        str_index = str_url.index("n3")
                        str_Id = str_url[str_index + 2:-5].replace('/', '').replace('-', '').replace('c', '')
                        str1 = str_Id[:4]
                        str2 = str_Id[4:6]
                        str3 = str_Id[6:8]
                        str_time = str1 + "-" + str2 + "-" + str3
                        item['sports_time'] = str_time
                    elif "/n/" in str_url:
                        str_index = str_url.index("/n/")
                        str_Id = str_url[str_index + 2:-5].replace('/', '').replace('-', '').replace('c', '')
                        str1 = str_Id[:4]
                        str2 = str_Id[4:6]
                        str3 = str_Id[6:8]
                        str_time = str1 + "-" + str2 + "-" + str3
                        item['sports_time'] = str_time
                    yield item
                    # 插入数据
                    if item["sports_id"] in str_data:
                        print "##### Already existing, not inserted #####"
                    else:
                        print "-----------------################## insert ################-----------------"
                        sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                        params = (item["sports_id"], item["sports_title"], item["sports_url"], item["sports_time"], '1')
                        data_seltct.insert(sql, *params)
            # 产生回溯模拟用户Next一直到结束
            if response.xpath("//div[@class='d2_18 clear']/a/text()").extract()[-1] == "Next":
                if response.xpath("//a[@class='common_current_page']/text()").extract()[0] == "1":
                    url=response.xpath("//div[@class='d2_18 clear']/a[6]/@href").extract()[0]
                    yield scrapy.Request("http://en.people.cn/90779/" + url, callback=self.parse)
                else:
                    url=response.xpath("//div[@class='d2_18 clear']/a[7]/@href").extract()[0]
                    yield scrapy.Request("http://en.people.cn/90779/" + url, callback=self.parse)

