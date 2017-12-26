# -*- coding: utf-8 -*-
# China_Photos页面
# Create by W_H_J 2017/9/30
import scrapy
from Chinadaily.items import china_photos
from Chinadaily.dbhelper import DBHelper
class china_Photos(scrapy.Spider):
    name = "china_Photos"
    base_url ="http://www.chinadaily.com.cn/china/2011flash.html"
    pgnum = 1
    start_urls = [base_url]
    # 新闻home链接
    def parse(self, response):
        item = china_photos()
        # 启用数据库助手
        data_seltct = DBHelper()
        sql_home = "select news_id from news"  # 单独查询编辑
        node_list = response.xpath('//body')
        # 循环读取到每条新闻Title并获取链接
        for node in node_list:
            # 规则一爬取
            for i in range(len(node.xpath('//ul[@id="SwitchNav"]/li/a/@href').extract())):
                # 过滤规则删选
                str_bool = node.xpath('//ul[@id="SwitchNav"]/li/a/@href').extract()[i]
                if '/content' in str_bool:
                    # 新闻链接
                    str_url1 = node.xpath('//ul[@id="SwitchNav"]/li/a/@href').extract()[i]
                    if "http://" in str_url1:
                        item['photos_url'] = str_url1
                    else:
                        str_URL = "http://www.chinadaily.com.cn/china/"+str_url1
                        # print str_URL
                        item['photos_url'] = str_URL
                    # 新闻标题
                    str_title = node.xpath('//ul[@id="SwitchNav"]/li/a/text()').extract()[i]
                    # print str_title
                    item['photos_title'] = str_title
                    # 新闻ID
                    str_url = node.xpath('//ul[@id="SwitchNav"]/li/a/@href').extract()[i]
                    str_id3 = str_url.index('/content_')
                    str_time_url1 = str_url[str_id3 - 10:10].replace('-', '').replace('/', '')
                    str_id1 = str_url.index('/content_')
                    str_id2 = str_url[str_id1 + 9:-4]
                    str_ID = str_time_url1 + str_id2
                    # print str_ID
                    # str_id1 = str_url[::-1]  # 字符串反转
                    # str_id2 = str_id1[4:12].replace('/', '').replace('-', '')
                    # str_id3 = str_id1[21:31].replace('/', '').replace('-', '')
                    # str_ID1 = str_id2+str_id3
                    # str_ID = str_ID1[::-1]
                    item['photos_id'] = str_ID
                    # 新闻发布时间    对于有部分链接无法提取新闻ID与发布时间，因为并不符合正常格式，不是普通新闻页面
                    str_time = node.xpath('//ul[@id="SwitchNav"]/li/a/@href').extract()[i]
                    str_time4 = str_time[::-1]
                    str_time1 = str_time4[21:24].replace('/', '').replace('-', '')
                    str_time2 = str_time4[24:27].replace('/', '').replace('-', '')
                    str_time3 = str_time4[27:31].replace('/', '').replace('-', '')
                    str_Time1 = str_time1+"-"+str_time2+"-"+str_time3
                    str_Time = str_Time1[::-1]
                    # print str_Time[::-1]
                    item['photos_pubtime'] = str_Time
                    yield item

                    # 插入数据
                    str_data = data_seltct.select(sql_home)  # 执行sql语句
                    if item["photos_id"] in str_data:
                        print "###------------------ Already existing, not inserted --------------------###"
                    else:
                        print "-----------------################## insert ################-----------------"
                        sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                        params = (item["photos_id"], item['photos_title'], item['photos_url'], item['photos_pubtime'], '2')
                        data_seltct.insert(sql, *params)
            # 规则二爬取
            for i in range(len(node.xpath('//div[@class="tw_photo_Box2"]/div[2]/a/@href').extract())):
                str_bool = node.xpath('//div[@class="tw_photo_Box2"]/div[2]/a/@href').extract()[i]
                if '/content' in str_bool:
                    # 新闻链接
                    str_url1 = node.xpath('//div[@class="tw_photo_Box2"]/div[2]/a/@href').extract()[i]
                    if "http://" in str_url1:
                        item['photos_url'] = str_url1
                    else:
                        str_URL = "http://www.chinadaily.com.cn/china/"+str_url1
                        # print str_URL
                        item['photos_url'] = str_URL
                    # 新闻标题
                    str_title = node.xpath('//div[@class="tw_photo_Box2"]/div[2]/a/text()').extract()[i]
                    # print str_title
                    item['photos_title'] = str_title
                    # 新闻ID
                    str_url = node.xpath('//div[@class="tw_photo_Box2"]/div[2]/a/@href').extract()[i]
                    str_id3 = str_url.index('/content_')
                    str_time_url1 = str_url[str_id3 - 10:10].replace('-', '').replace('/', '')
                    str_id1 = str_url.index('/content_')
                    str_id2 = str_url[str_id1 + 9:-4]
                    str_ID = str_time_url1 + str_id2
                    # print str_ID
                    # str_id1 = str_url[::-1]  # 字符串反转
                    # str_id2 = str_id1[4:12].replace('/', '').replace('-', '')
                    # str_id3 = str_id1[21:31].replace('/', '').replace('-', '')
                    # str_ID1 = str_id2 + str_id3
                    # str_ID = str_ID1[::-1]
                    item['photos_id'] = str_ID
                    # 新闻发布时间
                    str_time = node.xpath('//div[@class="tw_photo_Box2"]/div[2]/a/@href').extract()[i]
                    str_time4 = str_time[::-1]
                    str_time1 = str_time4[21:24].replace('/', '').replace('-', '')
                    str_time2 = str_time4[24:27].replace('/', '').replace('-', '')
                    str_time3 = str_time4[27:31].replace('/', '').replace('-', '')
                    str_Time1 = str_time1 + "-" + str_time2 + "-" + str_time3
                    str_Time = str_Time1[::-1]
                    # print str_Time[::-1]
                    item['photos_pubtime'] = str_Time
                    yield item

                    # 插入数据
                    str_data = data_seltct.select(sql_home)  # 执行sql语句
                    if item["photos_id"] in str_data:
                        print "###------------------ Already existing, not inserted --------------------###"
                    else:
                        print "-----------------################## insert ################-----------------"
                        sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                        params = (item["photos_id"], item['photos_title'], item['photos_url'], item['photos_pubtime'], '2')
                        data_seltct.insert(sql, *params)


        # 产生回溯模拟用户Next一直到结束   //*[@id="div_currpage"]/a[11]
        if response.xpath('//div[@id="div_currpage"]/a[10]/text()').extract()[0] == "Next":
            url = response.xpath('//div[@id="div_currpage"]/a[10]/@href').extract()[0]
            yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse)
        elif response.xpath('//div[@id="div_currpage"]/a[11]/text()').extract()[0] == "Next":
            url = response.xpath('//div[@id="div_currpage"]/a[11]/@href').extract()[0]
            yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse)
        elif len(response.xpath('//div[@id="div_currpage"]/a[12]/text()')):
            if response.xpath('//div[@id="div_currpage"]/a[12]/text()').extract()[0] == "Next":
               url = response.xpath('//div[@id="div_currpage"]/a[12]/@href').extract()[0]
               yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse)