# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# xinhuanet_china首页抓取
class xinhuanet_china(scrapy.Item):
    china_id = scrapy.Field()
    china_title = scrapy.Field()
    china_url = scrapy.Field()
    china_author = scrapy.Field()
    china_pubtime = scrapy.Field()
    china_img_arr = scrapy.Field()
    china_keyword = scrapy.Field()
# xinhuanet_world首页抓取
class xinhuanet_world(scrapy.Item):
    world_id = scrapy.Field()
    world_title = scrapy.Field()
    world_url = scrapy.Field()
    world_author = scrapy.Field()
    world_pubtime = scrapy.Field()
    world_img_arr =scrapy.Field()
    world_keyword = scrapy.Field()
# xinhuanet_ALL首页抓取
class xinhuanet_all(scrapy.Item):
    news_id = scrapy.Field()
    news_title = scrapy.Field()
    news_url = scrapy.Field()
    news_author = scrapy.Field()
    news_pubtime = scrapy.Field()
    news_img_arr =scrapy.Field()
    news_keyword = scrapy.Field()
