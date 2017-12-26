# -*- coding: utf-8 -*-
# Latest 最新新闻页面
# Create by W_H_J 2017/10/10
import scrapy
from Chinadaily.items import china_latest
from Chinadaily.dbhelper import DBHelper
class china_News2(scrapy.Spider):

    name = "china_Latest"
    base_url = "http://www.chinadaily.com.cn/china/node_53007329.htm"
    start_urls = [base_url]

    # 新闻home链接
    def parse(self, response):
        # 启用数据库助手
        data_seltct = DBHelper()
        sql_home = "select news_id from news"  # 单独查询编辑
        item = china_latest()
        node_list = response.xpath('//body')
        # 循环读取到每条新闻Title并获取链接
        for node in node_list:
            # 规则一爬取 上边栏 /div[6]/div[1]/div[1]/span/h4/a
            for i in range(len(node.xpath('//div[@class="main_art"]//span/h4/a/@href').extract())):
                str_bool = node.xpath('//div[@class="main_art"]//span/h4/a/@href').extract()[i]
                if '/content_' in str_bool:
                    # 新闻链接
                    str_url1 = node.xpath('//div[@class="main_art"]//span/h4/a/@href').extract()[i]
                    if "http://" in str_url1:
                        item['latest_url'] = str_url1
                    else:
                        str_URL = "http://www.chinadaily.com.cn/china/" + str_url1
                        # print str_URL
                        item['latest_url'] = str_URL
                    # 新闻标题
                    str_title = node.xpath('//div[@class="main_art"]//span/h4/a/text()').extract()[i]
                    # print str_title
                    item['latest_title'] = str_title
                    # 新闻ID
                    str_url = node.xpath('//div[@class="main_art"]//span/h4/a/@href').extract()[i]
                    str_time_url = node.xpath('//div[@class="main_art"]//span/b/text()').extract()[i]
                    str_time_url1 = str_time_url[0:10].replace('-', '')
                    str_id1 = str_url.index('/content_')
                    str_id2 = str_url[str_id1 + 9:-4]
                    str_ID = str_time_url1 + str_id2
                    item['latest_id'] = str_ID
                    # 新闻发布时间
                    str_time = node.xpath('//div[@class="main_art"]//span/b/text()').extract()[i]
                    # print str_time
                    item['latest_pubtime'] = str_time
                    yield item

                    # 插入数据
                    str_data = data_seltct.select(sql_home)  # 执行sql语句
                    if item["latest_id"] in str_data:
                        print "###------------------ Already existing, not inserted --------------------###"
                    else:
                        print "-----------------################## insert ################-----------------"
                        sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                        params = (item["latest_id"], item['latest_title'], item['latest_url'], item['latest_pubtime'], '2')
                        data_seltct.insert(sql, *params)
        # 产生回溯模拟用户Next一直到结束
        if len(response.xpath('//div[@id="div_currpage"]/a[9]/text()')):
            if response.xpath('//div[@id="div_currpage"]/a[9]/text()').extract()[0] == "Next":
                url = response.xpath('//div[@id="div_currpage"]/a[9]/@href').extract()[0]
                yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse)
            elif response.xpath('//div[@id="div_currpage"]/a[10]/text()').extract()[0] == "Next":
                url = response.xpath('//div[@id="div_currpage"]/a[10]/@href').extract()[0]
                yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse)
            elif response.xpath('//div[@id="div_currpage"]/a[11]/text()').extract()[0] == "Next":
                url = response.xpath('//div[@id="div_currpage"]/a[11]/@href').extract()[0]
                yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse)
            elif len(response.xpath('//div[@id="div_currpage"]/a[12]/text()')):
                if response.xpath('//div[@id="div_currpage"]/a[12]/text()').extract()[0] == "Next":
                    url = response.xpath('//div[@id="div_currpage"]/a[12]/@href').extract()[0]
                    yield scrapy.Request("http://www.chinadaily.com.cn/china/" + url, callback=self.parse)


