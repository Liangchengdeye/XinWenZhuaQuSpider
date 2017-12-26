# -*- coding: utf-8 -*-
# '''此页面为单独运行每一个爬虫'''
from scrapy import cmdline
    # 1.China子页面
# cmdline.execute("scrapy crawl china_Photos -o csv/china_Photos.csv".split())
    # 2.规则一页面News Society Innovation HK/Taiwan/Macao
# cmdline.execute("scrapy crawl china_News1 -o csv/china_News1.csv".split())
    # 3.规则二页面
# cmdline.execute("scrapy crawl china_News2 -o csv/china_News2.csv".split())
    # 4.首页页面
# cmdline.execute("scrapy crawl china_Home -o csv/china_Home.csv".split())
    # 5.最新页面
# cmdline.execute("scrapy crawl china_Latest -o csv/china_Latest.csv".split())
