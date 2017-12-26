# -*- coding: utf-8 -*-
# en_people.cn网爬取内容
# create 2017/9/14 W_H_J

import scrapy
from News.items import en_people_news
from News.dbhelper import DBHelper

class en_people_cnSpider(scrapy.Spider):
    name = "en_people"
    start_urls = ["http://en.people.cn"]

    # 新闻首页链接
    def parse(self, response):  # | //div[5]/div[1]/div[1]/div/ul/ul/li/a/@href
        # 主页面抓取规则
        # 1 //div[4]/div/div/div/ul/li/a/@href
        # 2.//div[4]/div/div/b/a/@href
        # 3.//div[5]/div[1]/div/div/ul/ul/li/a/@href
        # 4.//div[5]/div[1]/div/div/ul/div/a[2]/@href
        # 5.News of CPC //div[5]/div[2]/ul/li/a/@href

        for href in response.xpath('//div[4]/div/div/div/ul/li/a/@href | //div[4]/div/div/b/a/@href | //div[5]/div[1]/div/div/ul/ul/li/a/@href | //div[5]/div[1]/div/div/ul/div/a[2]/@href | //div[5]/div[2]/ul/li/a/@href'):
            full_url = response.urljoin(href.extract())
            # full_url="http://en.people.cn/n3/2017/0919/c90000-9271084.html"
            yield scrapy.Request(full_url, callback=self.parse_question)
    # 子页获取值
    def parse_question(self, response) :
                item = en_people_news()
                # 启用数据库助手
                data_seltct = DBHelper()
                sql_message = "select NEWS_id from en_people_message"  # 单独查询编辑
                str_data = data_seltct.select(sql_message)  # 执行sql语句
            # 内容ID
            #     str_id1 = response.xpath('head/meta[@name="publishdate"]/@content').extract()[0].encode("utf-8")
            #     str_id1 = str_id1.replace('-', '')
            #     str_id2 = response.xpath('head/meta[@name="catalogs"]/@content').extract()[0].encode("utf-8")
            #     str_id2 = str_id2.replace('F_', '')
            #     str_id3 = response.xpath('head/meta[@name="contentid"]/@content').extract()[0].encode("utf-8")
            #     str_id3 = str_id3.replace('F_', '')
            #     str_ID = str_id1+str_id2+str_id3
            #     取得当前的url
                str_id = str(response)
                str_index = str_id.index("n3")
                str_ID = str_id[str_index + 2:-6].replace('/', '').replace('-', '').replace('c', '')
                item['NEW_ID'] = str_ID
            # 新闻标题
                str_title = response.xpath('head/title/text()').extract()[0].encode("utf-8")
                # 此处用于去除- People's Daily Online 但有些标题特殊，因此暂不处理
                if str_title.find("- People's Daily Online") == -1:
                    str_Title = str_title
                else:
                    str_Title = str_title[:-24]
                item['NEW_TITLE'] = str_Title
            # 新闻发布时间
                item['NEW_TIME'] = response.xpath('head/meta[@name="publishdate"]/@content').extract()[0].encode("utf-8")
            # 新闻图片
            #     str_img = " | http://en.people.cn"  /html/body/div[6]/p[1]/a/img
                list_img = []
                img_Num = response.xpath("//div[@class='wb_12 clear']/p[@align='center']//img/@src | //div[@class='page_pic']/div[@class='pic']//a/img/@src | //div[@class='wb_12 clear']/p[@style]//img/@src | //div[@id='p_content']/p[@style]//img/@src").extract()
                if len(img_Num) > 0:
                    for i in img_Num:
                        if "http://" in i:
                            list_img.append("|"+i)
                        else:
                            list_img.append(" | http://en.people.cn" + i)
                else:
                    list_img.append("")
                # 追加链接开头
                str_img = ""
                for img in list_img:
                    str_img += img
                item['NEW_IMG'] = str_img
            # 新闻图片标题
                list_title = []
                str_img_title = response.xpath('//div[@class="wb_12 clear"]/p/em/text() | //div[@id="p_content"]/p[@style]/em/text() | //div[@id="p_content"]/p[@style]/text()').extract()
                if len(str_img_title):
                        for str_title_img in str_img_title:
                            # 此处判断用于过滤包含style样式的p标签，目前按空元素过滤，
                            # 日后若出现图片图注顺序不对应，在此处查看是否会产生bug
                            if len(str.strip(str_title_img.encode('utf-8'))) != 0:
                                list_title.append(str_title_img)
                else:
                   list_title.append("")
                str_img_title1 = ""
                for img_title in list_title:
                    str_img_title1 += img_title
                item['NEW_IMG_TITLE'] = str_img_title1
            # 新闻内容
                str_body = ""
                list_body = response.xpath('//div[@id="p_content"]/p[not(@style)]/text() | //div[@class="wb_12 clear"]//p[not(@style)]//text()').extract()
                if len(list_body):
                    for body in list_body:
                        str_body += body
                    item['NEW_BODY'] = str_body.replace('\r', '').replace('\n', '').replace('\t', '').encode('utf-8')
                else:
                    item['NEW_BODY'] = ""
                yield item
                if item["NEW_ID"] in str_data:
                    print "##### Already existing, not inserted #####"
                else:
                    print "-----------------################## insert ################-----------------"
                    sql = "insert into en_people_message(NEWS_ID,NEWS_TITLE,NEWS_TIME,NEWS_IMG,NEWS_IMG_TITLE,NEWS_BODY) values (%s,%s,%s,%s,%s,%s)"
                    params = (item["NEW_ID"], item["NEW_TITLE"], item["NEW_TIME"], item['NEW_IMG'], item['NEW_IMG_TITLE'], item["NEW_BODY"])
                    data_seltct.insert(sql, *params)
                # 产生回溯模拟用户Next一直到结束
                # print '************************************'  div[6]/center[2]/table/tbody/tr/td/a/img
                str_next = response.xpath("//div[@class='wb_12 clear']/center[2]/table//a/img/@src").extract()
                if len(str_next) == 1:
                    str_next = response.xpath("//div[@class='wb_12 clear']/center[2]/table//a/img/@src").extract()[0]
                    str_Next = str_next[-8:-4]
                    if str_Next == "Next":
                        url = response.xpath("//div[@class='wb_12 clear']//center[2]//a/@href").extract()[0]
                        # print url
                        yield scrapy.Request("http://en.people.cn" + url, callback=self.parse_question)
                elif len(str_next) == 2:
                    str_next = response.xpath("//div[@class='wb_12 clear']/center[2]/table//a/img/@src").extract()[1]
                    str_Next = str_next[-8:-4]
                    # print str_Next
                    if str_Next == "Next":
                        url = response.xpath("//div[@class='wb_12 clear']//center[2]//a/@href").extract()[1]
                        if "http://" in url:
                            url = url
                        else:
                            url = "http://en.people.cn"+url
                        yield scrapy.Request(url, callback=self.parse_question)

