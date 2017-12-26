# -*- coding: utf-8 -*-
# xinhuanet_All网爬取内容
# create 2017/9/28 W_H_J

import scrapy
import json
from xinhuanet.items import xinhuanet_all
from xinhuanet.dbhelper import DBHelper
# 新闻页面所有json文件内容获取
class xinhuanet_All(scrapy.Spider):
    name = "xinhuanet_All"

    # 需要拼接的url
    baseURL1 = "http://qc.wa.news.cn/nodeart/list?nid="
    baseURL2 = "&cnt=50&pgnum="
    # 偏移起始位
    offset = 1
    # English版起始页
    nid = 11143391  # 地址范围[11143391,11143499]
    # 启示地址
    start_urls = [baseURL1 + str(nid) + baseURL2 + str(offset)]

    def parse(self, response):
        # 启用数据库助手
        data_news = DBHelper()
        sql_news = "select news_id from news"  # 单独查询编辑
        str_data = data_news.select(sql_news)  # 执行sql语句
        # 判断是否有数据存在
        data_bool = json.loads(response.body.replace('(', '').replace(')', ''))['status']
        if data_bool == 0:
            data_find = True
            data_list = json.loads(response.body.replace('(', '').replace(')', ''))['data']['list']
            for data in data_list:
                item = xinhuanet_all()
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

                item["news_id"] = str_id
                item["news_title"] = str_title
                item["news_url"] = str_url
                item["news_author"] = str_author
                item["news_pubtime"] = str_pubtime
                item["news_img_arr"] = str_img_arr
                item["news_keyword"] = str_keyword
                yield item
                # 判断如果本次数据库中已存在本次查询id则不插入，否则插入
                # 插入数据
                if item["news_id"] in str_data:
                    print "################## Already existing, not inserted ##################"
                else:
                    print "##########################  insert data ############################"
                    sql = "insert into news (news_id,news_title,news_url,news_author,news_pubtime,news_img_arr,news_keyword,flag) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    params = (
                    item['news_id'], item['news_title'], item['news_url'], item['news_author'], item['news_pubtime'],
                    item['news_img_arr'], item['news_keyword'], '3')
                    data_news.insert(sql, *params)
        else:
            # 偏移地址结束
            data_find = False
            print "************************* this url end ****************************"
        if data_find:
            # 在nid不增加的前提下，偏移地址增加直到查询结束
            self.offset += 1
            baseURL1 = "http://qc.wa.news.cn/nodeart/list?nid="
            baseURL2 = "&cnt=50&pgnum="
            # print self.offset
            # print self.nid
            print baseURL1 + str(self.nid)+baseURL2+str(self.offset)
            yield scrapy.Request(baseURL1 + str(self.nid)+baseURL2+str(self.offset), callback=self.parse)
        if data_find == False:
            # 如果查询结束表示本次nid范围内，偏移地址遍历结束，则开始增加nid一次
            if self.nid < 11143499:  # English网站最大地址范围11143499
                self.offset = 1
                self.nid += 1
                baseURL1 = "http://qc.wa.news.cn/nodeart/list?nid="
                baseURL2 = "&cnt=50&pgnum="
                # print self.offset
                # print self.nid
                print baseURL1 + str(self.nid) + baseURL2 + str(self.offset)
                yield scrapy.Request(baseURL1 + str(self.nid) + baseURL2 + str(self.offset), callback=self.parse)
            else:
                # 所有新闻链接遍历结束
                print "***************************** OVER ********************************"
                return