# -*- coding: utf-8 -*-
# News Society Innovation HK/Taiwan/Macao页面
# Create by W_H_J 2017/9/30
import scrapy
from Chinadaily.items import china_news1
from Chinadaily.dbhelper import DBHelper
class china_News1(scrapy.Spider):

    name = "china_News1"
    base_url = "http://www.chinadaily.com.cn/china/"
    pgnum = 1
    start_urls = [base_url]

    # 新闻home链接
    def parse(self, response):
        str_node = response.xpath('//div[@class="topNav2_art"]/ul/li/a/text()').extract()
        for str_node1 in str_node:
            if str_node1 == 'News':
                url_1 = response.xpath('//div[@class="topNav2_art"]/ul/li/a/@href').extract()[0]
                yield scrapy.Request(url_1, callback=self.parse_ask)
            elif str_node1 == 'Society':
                url_2 = response.xpath('//div[@class="topNav2_art"]/ul/li/a/@href').extract()[1]
                yield scrapy.Request(url_2, callback=self.parse_ask)
            elif str_node1 == 'Innovation':
                url_3 = response.xpath('//div[@class="topNav2_art"]/ul/li/a/@href').extract()[2]
                yield scrapy.Request(url_3, callback=self.parse_ask)
            elif str_node1 == 'HK/Taiwan/Macao':
                url_4 = response.xpath('//div[@class="topNav2_art"]/ul/li/a/@href').extract()[3]
                yield scrapy.Request(url_4, callback=self.parse_ask)
    def parse_ask(self, response):

        # 启用数据库助手
        data_seltct = DBHelper()
        sql_home = "select news_id from news"  # 单独查询编辑
        item = china_news1()
        node_list = response.xpath('//body')
        # 循环读取到每条新闻Title并获取链接
        for node in node_list:
            # 规则一爬取 上边栏
            for i in range(len(node.xpath('//div[@class="tw2"]//a/@href').extract())-1):
                str_bool = node.xpath('//div[@class="tw2"]//a/@href').extract()[i+1]
                if '/content' in str_bool:
                    # 新闻链接
                    str_url1 = node.xpath('//div[@class="tw2"]//a/@href').extract()[i+1]
                    if "http://" in str_url1:
                        item['news1_url'] = str_url1
                    else:
                        str_URL = "http://www.chinadaily.com.cn/china/" + str_url1
                        # print str_URL
                        item['news1_url'] = str_URL
                    # 新闻标题
                    str_title = node.xpath('//div[@class="tw2"]//a/text()').extract()[i]
                    # print str_title
                    item['news1_title'] = str_title
                    # 新闻ID
                    str_url = node.xpath('//div[@class="tw2"]//a/@href').extract()[i+1]
                    str_id3 = str_url.index('/content_')
                    str_time_url1 = str_url[str_id3-10:10].replace('-', '').replace('/', '')
                    str_id1 = str_url.index('/content_')
                    str_id2 = str_url[str_id1 + 9:-4]
                    str_ID = str_time_url1 + str_id2
                    # print str_ID
                    item['news1_id'] = str_ID
                    # 新闻发布时间
                    str_time = node.xpath('//div[@class="tw2"]//a/@href').extract()[i+1]
                    str_time4 = str_time[::-1]
                    str_time1 = str_time4[21:24].replace('/', '').replace('-', '')
                    str_time2 = str_time4[24:27].replace('/', '').replace('-', '')
                    str_time3 = str_time4[27:31].replace('/', '').replace('-', '')
                    str_Time1 = str_time1 + "-" + str_time2 + "-" + str_time3
                    str_Time = str_Time1[::-1]
                    # print str_Time[::-1]
                    item['news1_pubtime'] = str_Time
                    yield item

                    # 插入数据
                    str_data = data_seltct.select(sql_home)  # 执行sql语句
                    if item["news1_id"] in str_data:
                        print "###------------------ Already existing, not inserted --------------------###"
                    else:
                        print "-----------------################## insert ################-----------------"
                        sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                        params = (item["news1_id"], item['news1_title'], item['news1_url'], item['news1_pubtime'], '2')
                        data_seltct.insert(sql, *params)
            # 规则二爬取
            for i in range(len(node.xpath('//div[@class="mb10 tw3_01_2"]/span/h4/a/@href').extract())-1):
                str_bool = node.xpath('//div[@class="mb10 tw3_01_2"]/span/h4/a/@href').extract()[i]
                if '/content_' in str_bool:
                    # 新闻链接
                    str_url1 = node.xpath('//div[@class="mb10 tw3_01_2"]/span/h4/a/@href').extract()[i]
                    if "http://" in str_url1:
                        item['news1_url'] = str_url1
                    else:
                        str_URL = "http://www.chinadaily.com.cn/china/" + str_url1
                        # print str_URL
                        item['news1_url'] = str_URL
                    # 新闻标题 /html/body/div[6]/div[1]/div[7]/span/h4/a
                    str_title = node.xpath('//div[@class="mb10 tw3_01_2"]/span/h4/a/text()').extract()[i]
                    # print str_title
                    item['news1_title'] = str_title
                    # 新闻ID
                    str_url = node.xpath('//div[@class="mb10 tw3_01_2"]/span/h4/a/@href').extract()[i]
                    str_time_url = node.xpath('//div[@class="mb10 tw3_01_2"]/span/b//text()').extract()[i]
                    str_time_url1 = str_time_url[0:10].replace('-', '')
                    str_id1 = str_url.index('/content_')
                    str_id2 = str_url[str_id1 + 9:-4]
                    str_ID = str_time_url1 + str_id2
                    item['news1_id'] = str_ID
                    # 新闻发布时间
                    str_time = node.xpath('//div[@class="mb10 tw3_01_2"]/span/b//text()').extract()[i]
                    item['news1_pubtime'] = str_time
                    yield item

                    # 插入数据
                    str_data = data_seltct.select(sql_home)  # 执行sql语句
                    if item["news1_id"] in str_data:
                        print "###------------------ Already existing, not inserted --------------------###"
                    else:
                        print "-----------------################## insert ################-----------------"
                        sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                        params = (item["news1_id"], item['news1_title'], item['news1_url'], item['news1_pubtime'], '2')
                        data_seltct.insert(sql, *params)

        # 产生回溯模拟用户Next一直到结束   //*[@id="div_currpage"]/a[11] //*[@id="div_currpage"]/a[11]
        if len(response.xpath('//div[@id="div_currpage"]/a[10]/text()')):
            if response.xpath('//div[@id="div_currpage"]/a[10]/text()').extract()[0] == "Next":
                url = response.xpath('//div[@id="div_currpage"]/a[10]/@href').extract()[0]
                yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse_ask)
            elif response.xpath('//div[@id="div_currpage"]/a[11]/text()').extract()[0] == "Next":
                url = response.xpath('//div[@id="div_currpage"]/a[11]/@href').extract()[0]
                yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse_ask)
            elif len(response.xpath('//div[@id="div_currpage"]/a[12]/text()')):
                if response.xpath('//div[@id="div_currpage"]/a[12]/text()').extract()[0] == "Next":
                   url = response.xpath('//div[@id="div_currpage"]/a[12]/@href').extract()[0]
                   yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse_ask)
        elif len(response.xpath('//div[@id="div_currpage"]/a[8]/text()')):
            if response.xpath('//div[@id="div_currpage"]/a[8]/text()').extract()[0] == "Next":
               url = response.xpath('//div[@id="div_currpage"]/a[8]/@href').extract()[0]
               yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse_ask)