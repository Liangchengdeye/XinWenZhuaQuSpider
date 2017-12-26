# -*- coding: utf-8 -*-
# xinhuanet_World网爬取内容
# create 2017/9/28 W_H_J

import scrapy
from xinhuanet.items import xinhuanet_world
import json
from xinhuanet.dbhelper import DBHelper

class xinhuanet_China(scrapy.Spider):
    name = "xinhuanet_World"
    pgnum = 1
    start_urls = ["http://www.xinhuanet.com/english/world/index.htm"]

    # 新闻home链接
    def parse(self, response):

        for href in response.xpath('//div[@class="title"]/h3/a/@href').extract():
            # print href
            yield scrapy.Request(href, callback=self.parse_question)
    def parse_question(self,response):
        # 对获取到的链接类型进行判断，即就是标题头部
        str_url = str(response)
        str_index = str_url.index("/world")
        str_Id = str_url[str_index + 6:-5].replace('/', '').replace('-', '')
        # print str_Id
        pgnum = 1
        if str_Id == 'politics':
            base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143391&cnt=50&pgnum="
            yield scrapy.Request(base_url + str(pgnum), callback=self.parse_ask)
        elif str_Id == 'chinaworld':
            base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143392&cnt=50&pgnum="
            yield scrapy.Request(base_url + str(pgnum), callback=self.parse_ask)
        elif str_Id == 'business':
            base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143393&cnt=50&pgnum="
            yield scrapy.Request(base_url + str(pgnum), callback=self.parse_ask)
        elif str_Id == 'science':
            base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143395&cnt=50&pgnum="
            yield scrapy.Request(base_url + str(pgnum), callback=self.parse_ask)
        elif str_Id == 'society':
            base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143398&cnt=50&pgnum="
            yield scrapy.Request(base_url + str(pgnum), callback=self.parse_ask)
        elif str_Id == 'sport':
            base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143396&cnt=50&pgnum="
            yield scrapy.Request(base_url + str(pgnum), callback=self.parse_ask)
        elif str_Id == 'HKMacaoTaiwan':
            base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143397&cnt=50&pgnum="
            yield scrapy.Request(base_url + str(pgnum), callback=self.parse_ask)
        elif str_Id == 'cultureedu':
            base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143394&cnt=50&pgnum="
            yield scrapy.Request(base_url + str(pgnum), callback=self.parse_ask)

    def parse_ask(self, response):
        # data_china = DBHelper()
        # sql_health = "select china_id from xinhuanet_china"  # 单独查询编辑
        # str_data = data_china.select(sql_health)  # 执行sql语句
        # 判断是否有数据存在
        data_bool = json.loads(response.body.replace('(', '').replace(')', ''))['status']
        if data_bool == 0:
            data_find = True
            data_list = json.loads(response.body.replace('(', '').replace(')', ''))['data']['list']
            for data in data_list:
                item = xinhuanet_world()
                # 新闻ID
                str_id = data["DocID"]
                # 新闻标题
                str_title = data["Title"]
                # 新闻链接
                str_url = data["LinkUrl"]
                # 作者
                str_author = data["Author"]
                # 发布时间
                str_pubtime = data["PubTime"]
                # 包含图片
                str_img_arr = data["imgarray"]
                # 关键字
                str_keyword = data["keyword"]

                item["world_id"] = str_id
                item["world_title"] = str_title
                item["world_url"] = str_url
                item["world_author"] = str_author
                item["world_pubtime"] = str_pubtime
                item["world_img_arr"] = str_img_arr
                item["world_keyword"] = str_keyword
                yield item
                # # 插入数据
                # if item["china_id"] in str_data:
                #     print "################## Already existing, not inserted ##################"
                # else:
                #     print "##########################  insert data ############################"
                #     sql = "insert into xinhuanet_china (china_id,china_title,china_url,china_author,china_pubtime,china_img_arr,china_keyword) values(%s,%s,%s,%s,%s,%s,%s)"
                #     params = (item['china_id'], item['china_title'], item['china_url'], item['china_author'], item['china_pubtime'], item['china_img_arr'], item['china_keyword'])
                #     data_china.insert(sql, *params)

        else:
            data_find = False
            print "************************** All Find **************************"
        # # 回溯爬取
        # if data_find:  # 此处if判断有问题，如果一个为假则整个回溯全部停止
        #     # 回溯判断
        #     str_url = str(response)
        #     str_index = str_url.index("nid=")
        #     str_index2 = len(str_url)-str_url.index("cnt")
        #     # 对返回链接关键字提取
        #     str_find_index = str_url[str_index + 4:-str_index2-1]
        #     if str_find_index == '11143391':
        #         self.pgnum += 1
        #         base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143391&cnt=50&pgnum="
        #         yield scrapy.Request(base_url+str(self.pgnum), callback=self.parse_ask)
        #     elif str_find_index == '11143392':
        #         self.pgnum += 1
        #         base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143392&cnt=50&pgnum="
        #         yield scrapy.Request(base_url + str(self.pgnum), callback=self.parse_ask)
        #     elif str_find_index == '11143393':
        #         self.pgnum += 1
        #         base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143393&cnt=50&pgnum="
        #         yield scrapy.Request(base_url + str(self.pgnum), callback=self.parse_ask)
        #     elif str_find_index == '11143394':
        #         self.pgnum += 1
        #         base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143394&cnt=50&pgnum="
        #         yield scrapy.Request(base_url + str(self.pgnum), callback=self.parse_ask)
        #     elif str_find_index == '11143395':
        #         self.pgnum += 1
        #         base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143395&cnt=50&pgnum="
        #         yield scrapy.Request(base_url + str(self.pgnum), callback=self.parse_ask)
        #     elif str_find_index == '11143396':
        #         self.pgnum += 1
        #         base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143396&cnt=50&pgnum="
        #         yield scrapy.Request(base_url + str(self.pgnum), callback=self.parse_ask)
        #     elif str_find_index == '11143397':
        #         self.pgnum += 1
        #         base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143397&cnt=50&pgnum="
        #         yield scrapy.Request(base_url + str(self.pgnum), callback=self.parse_ask)
        #     elif str_find_index == '11143398':
        #         self.pgnum += 1
        #         base_url = "http://qc.wa.news.cn/nodeart/list?nid=11143398&cnt=50&pgnum="
        #         yield scrapy.Request(base_url + str(self.pgnum), callback=self.parse_ask)
        #     else:
        #         print "nothing to show!"

