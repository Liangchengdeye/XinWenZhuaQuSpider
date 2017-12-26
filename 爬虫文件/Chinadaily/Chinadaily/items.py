# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# Latest最新新闻页面
class china_latest(scrapy.Item):
    latest_id = scrapy.Field()
    latest_title = scrapy.Field()
    latest_url = scrapy.Field()
    latest_pubtime = scrapy.Field()
# Photos页面
class china_photos(scrapy.Item):
    photos_id = scrapy.Field()
    photos_title = scrapy.Field()
    photos_url = scrapy.Field()
    photos_pubtime = scrapy.Field()
# china 首页
class china_home(scrapy.Item):
    china_id = scrapy.Field()
    china_title = scrapy.Field()
    china_url = scrapy.Field()
    china_pubtime = scrapy.Field()
# 规则一类item
class china_news1(scrapy.Item):
    news1_id = scrapy.Field()
    news1_title = scrapy.Field()
    news1_url = scrapy.Field()
    news1_pubtime = scrapy.Field()
# 规则二类item
class china_news2(scrapy.Item):
    news2_id = scrapy.Field()
    news2_title = scrapy.Field()
    news2_url = scrapy.Field()
    news2_pubtime = scrapy.Field()
