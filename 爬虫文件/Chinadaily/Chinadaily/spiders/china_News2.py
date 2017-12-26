# -*- coding: utf-8 -*-
# Cover story Environment Health Military页面
# Create by W_H_J 2017/10/9
import scrapy
from Chinadaily.items import china_news2
from Chinadaily.dbhelper import DBHelper
class china_News2(scrapy.Spider):

    name = "china_News2"
    base_url = "http://www.chinadaily.com.cn/china/"
    pgnum = 1
    start_urls = [base_url]

    # 新闻home链接
    def parse(self, response):
        str_node = response.xpath('//div[@class="topNav2_art"]/ul/li/a/text()').extract()
        for str_node1 in str_node:
            if str_node1 == 'Cover Story':
                url_1 = response.xpath('//div[@class="topNav2_art"]/ul/li/a/@href').extract()[4]
                # print url_1
                yield scrapy.Request(url_1, callback=self.parse_ask)
            elif str_node1 == 'Environment':
                url_2 = response.xpath('//div[@class="topNav2_art"]/ul/li/a/@href').extract()[6]
                yield scrapy.Request(url_2, callback=self.parse_ask)
            elif str_node1 == 'Health':
                url_3 = response.xpath('//div[@class="topNav2_art"]/ul/li/a/@href').extract()[7]
                yield scrapy.Request(url_3, callback=self.parse_ask)
            elif str_node1 == 'Military':
                url_4 = response.xpath('//div[@class="topNav2_art"]/ul/li/a/@href').extract()[8]
                yield scrapy.Request(url_4, callback=self.parse_ask)
    def parse_ask(self, response):

        # 启用数据库助手
        data_seltct = DBHelper()
        sql_home = "select news_id from news"  # 单独查询编辑
        item = china_news2()
        node_list = response.xpath('//body')
        # 循环读取到每条新闻Title并获取链接
        for node in node_list:
            # 规则一爬取 上边栏 /div[6]/div[1]/div[1]/span/h4/a
            for i in range(len(node.xpath('//div[@class="main_art"]//span/h4/a/@href').extract())):
                str_bool = node.xpath('//div[@class="main_art"]//span/h4/a/@href').extract()[i]
                if '/content' in str_bool:
                    # 新闻链接
                    str_url1 = node.xpath('//div[@class="main_art"]//span/h4/a/@href').extract()[i]
                    if "http://" in str_url1:
                        item['news2_url'] = str_url1
                    else:
                        str_URL = "http://www.chinadaily.com.cn/china/" + str_url1
                        # print str_URL
                        item['news2_url'] = str_URL
                    # 新闻标题
                    str_title = node.xpath('//div[@class="main_art"]//span/h4/a/text()').extract()[i]
                    # print str_title
                    item['news2_title'] = str_title
                    # 新闻ID
                    str_url = node.xpath('//div[@class="main_art"]//span/h4/a/@href').extract()[i]
                    str_time_url = node.xpath('//div[@class="main_art"]//span/b/text()').extract()[i]
                    str_time_url1 = str_time_url[0:10].replace('-', '')
                    str_id1 = str_url.index('/content_')
                    str_id2 = str_url[str_id1+9:-4]
                    str_ID =str_time_url1+str_id2
                    item['news2_id'] = str_ID
                    # 新闻发布时间
                    str_time = node.xpath('//div[@class="main_art"]//span/b/text()').extract()[i]
                    # print str_time
                    item['news2_pubtime'] = str_time
                    yield item

                    # 插入数据
                    str_data = data_seltct.select(sql_home)  # 执行sql语句
                    if item["news2_id"] in str_data:
                        print "###------------------ Already existing, not inserted --------------------###"
                    else:
                        print "-----------------################## insert ################-----------------"
                        sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                        params = (item["news2_id"], item['news2_title'], item['news2_url'], item['news2_pubtime'], '2')
                        data_seltct.insert(sql, *params)
        # 产生回溯模拟用户Next一直到结束
        if len(response.xpath('//div[@id="div_currpage"]/a[9]/text()')):
            if response.xpath('//div[@id="div_currpage"]/a[9]/text()').extract()[0] == "Next":
               url = response.xpath('//div[@id="div_currpage"]/a[9]/@href').extract()[0]
               yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse_ask)
            elif response.xpath('//div[@id="div_currpage"]/a[10]/text()').extract()[0] == "Next":
                url = response.xpath('//div[@id="div_currpage"]/a[10]/@href').extract()[0]
                yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse_ask)
            elif response.xpath('//div[@id="div_currpage"]/a[11]/text()').extract()[0] == "Next":
                url = response.xpath('//div[@id="div_currpage"]/a[11]/@href').extract()[0]
                yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse_ask)
            elif len(response.xpath('//div[@id="div_currpage"]/a[12]/text()')):
                if response.xpath('//div[@id="div_currpage"]/a[12]/text()').extract()[0] == "Next":
                    url = response.xpath('//div[@id="div_currpage"]/a[12]/@href').extract()[0]
                    yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse_ask)