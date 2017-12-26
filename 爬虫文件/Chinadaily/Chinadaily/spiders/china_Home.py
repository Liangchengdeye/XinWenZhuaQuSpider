# -*- coding: utf-8 -*-
# 首页
# Create by W_H_J 2017/10/9
import scrapy
from Chinadaily.items import china_home
from Chinadaily.dbhelper import DBHelper
class china_Home(scrapy.Spider):

    name = "china_Home"
    base_url = "http://www.chinadaily.com.cn/china/"
    start_urls = [base_url]
    # 首页规则提取
    # //div[@id="D1pic1"]/div/div/h3/a
    # //div[5]/div[1]/div[1]/div[1]/div/a/@href
    # // div[5]/div[1]/div[1]/div[2]/div/div/span/a
    # //div[5]/div[1]/div[3]/div[1]/div/div/a
    # //div[@class="tw3"]/div/div/span[2]/a
    # //div[@class="tw3"]/div/span[2]/a
    # //div[@class="tBox3"]/a
    # //div[@class="tBox2"]/a
    # //div[@class="tw2"]/div/span/a
    # //ul[@class="lisBox"]/li/a
    # //span[@class="tw6_t"]/a
    # //div[@class="tw4_t"]/a

    # 新闻home链接
    def parse(self, response):
        # 启用数据库助手
        data_seltct = DBHelper()
        sql_home = "select news_id from news"  # 单独查询编辑
        item = china_home()
        for href in range(len(response.xpath('//div[@class="tw4_t"]/a/@href | //div[@id="D1pic1"]/div/div/h3/a/@href | //div[5]/div[1]/div[1]/div[1]/div/a/@href | // div[5]/div[1]/div[1]/div[2]/div/div/span/a/@href | //div[5]/div[1]/div[3]/div[1]/div/div/a/@href | //div[@class="tw3"]/div/div/span[2]/a/@href | //div[@class="tw3"]/div/span[2]/a/@href | //div[@class="tBox3"]/a/@href | //div[@class="tBox2"]/a/@href | //div[@class="tw2"]/div/span/a/@href | //ul[@class="lisBox"]/li/a/@href | //span[@class="tw6_t"]/a/@href'))):
            # 新闻链接
            full_url = response.urljoin(response.xpath('//div[@class="tw4_t"]/a/@href | //div[@id="D1pic1"]/div/div/h3/a/@href | //div[5]/div[1]/div[1]/div[1]/div/a/@href | // div[5]/div[1]/div[1]/div[2]/div/div/span/a/@href | //div[5]/div[1]/div[3]/div[1]/div/div/a/@href | //div[@class="tw3"]/div/div/span[2]/a/@href | //div[@class="tw3"]/div/span[2]/a/@href | //div[@class="tBox3"]/a/@href | //div[@class="tBox2"]/a/@href | //div[@class="tw2"]/div/span/a/@href | //ul[@class="lisBox"]/li/a/@href | //span[@class="tw6_t"]/a/@href').extract()[href]).encode('utf-8')
            if '/content_' in full_url:
                # 新闻ID
                str_id3 = full_url.index('/content_')
                str_time_url1 = full_url[str_id3-10:-20].replace('-', '').replace('/', '')
                # print str_time_url1
                str_id1 = full_url.index('/content_')
                str_id2 = full_url[str_id1 + 9:-4]
                str_ID = str_time_url1 + str_id2
                # 新闻标题
                str_title = response.xpath('//div[@class="tw4_t"]/a/text() | //div[@id="D1pic1"]/div/div/h3/a/text() | //div[5]/div[1]/div[1]/div[1]/div/a/text() | // div[5]/div[1]/div[1]/div[2]/div/div/span/a/text() | //div[5]/div[1]/div[3]/div[1]/div/div/a/text() | //div[@class="tw3"]/div/div/span[2]/a/text() | //div[@class="tw3"]/div/span[2]/a/text()  | //div[@class="tBox3"]/a/text() | //div[@class="tBox2"]/a/text() | //div[@class="tw2"]/div/span/a/text() | //ul[@class="lisBox"]/li/a/text() | //span[@class="tw6_t"]/a/text()').extract()[href]
                # 发布时间
                str_pubtime1 = str_time_url1[0:4]
                str_pubtime2 = str_time_url1[4:6]
                str_pubtime3 = str_time_url1[6:8]
                str_Pubtime = str_pubtime1+"-"+str_pubtime2+"-"+str_pubtime3
                # 列表集
                item['china_title'] = str_title
                item['china_url'] = full_url
                item['china_id'] = str_ID
                item['china_pubtime'] = str_Pubtime
                yield item
            # 插入数据
            str_data = data_seltct.select(sql_home)  # 执行sql语句
            if item["china_id"] in str_data:
                print "###------------------ Already existing, not inserted --------------------###"
            else:
                print "-----------------################## insert ################-----------------"
                sql = "insert into news (news_id,news_title,news_url,news_pubtime,flag) values(%s,%s,%s,%s,%s)"
                params = (item["china_id"], item['china_title'], item['china_url'], item['china_pubtime'],'2')
                data_seltct.insert(sql, *params)
