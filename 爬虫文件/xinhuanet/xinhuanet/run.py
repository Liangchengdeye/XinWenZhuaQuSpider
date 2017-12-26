# -*- coding: utf-8 -*-
# '''此页面为单独运行每一个爬虫'''
from scrapy import cmdline
    # 1.China子页面
# cmdline.execute("scrapy crawl xinhuanet_China -o csv/xinhuanet_China.csv".split())
    # 2.world子页面
# cmdline.execute("scrapy crawl xinhuanet_World -o csv/xinhuanet_World.csv".split())
    # 2.所有页面
# cmdline.execute("scrapy crawl xinhuanet_All -o csv/xinhuanet_All.csv".split())