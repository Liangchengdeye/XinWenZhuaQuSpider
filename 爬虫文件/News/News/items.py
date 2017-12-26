# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# en_people_news网爬取内容
class en_people_news(scrapy.Item):
    NEW_ID = scrapy.Field()
    NEW_TITLE = scrapy.Field()
    NEW_TIME = scrapy.Field()
    NEW_IMG = scrapy.Field()
    NEW_IMG_TITLE = scrapy.Field()
    NEW_BODY = scrapy.Field()
# en_people_news首页抓取
class en_people_news_Father(scrapy.Item):
    NEW_TITLE_id =scrapy.Field()
    NEW_TITLE_FATHER = scrapy.Field()
    NEW_URL_FATHER = scrapy.Field()
# en_people_Opinions子页面抓取链接
class en_people_opinions(scrapy.Item):
    opinions_id = scrapy.Field()
    opinions_title = scrapy.Field()
    opinions_url = scrapy.Field()
    opinions_time = scrapy.Field()
# en_people_Business子页面抓取链接
class en_people_business(scrapy.Item):
    business_id = scrapy.Field()
    business_title = scrapy.Field()
    business_url = scrapy.Field()
    business_time = scrapy.Field()
# en_people_Military子页面抓取链接
class en_people_militart(scrapy.Item):
    military_id = scrapy.Field()
    military_title = scrapy.Field()
    military_url = scrapy.Field()
    military_time = scrapy.Field()
# en_people_World子页面抓取链接
class en_people_world(scrapy.Item):
    world_id = scrapy.Field()
    world_title = scrapy.Field()
    world_url = scrapy.Field()
    world_time = scrapy.Field()
# en_people_Society子页面抓取链接
class en_people_society(scrapy.Item):
    society_id = scrapy.Field()
    society_title = scrapy.Field()
    society_url = scrapy.Field()
    society_time = scrapy.Field()
# en_people_Culture子页面抓取链接
class en_people_culture(scrapy.Item):
    culture_id = scrapy.Field()
    culture_title = scrapy.Field()
    culture_url = scrapy.Field()
    culture_time = scrapy.Field()
# en_people_Science子页面抓取链接
class en_people_science(scrapy.Item):
    science_id = scrapy.Field()
    science_title = scrapy.Field()
    science_url = scrapy.Field()
    science_time = scrapy.Field()
# en_people_Sports子页面抓取链接
class en_people_sports(scrapy.Item):
    sports_id = scrapy.Field()
    sports_title = scrapy.Field()
    sports_url = scrapy.Field()
    sports_time = scrapy.Field()
# en_people_Speical Coverage子页面抓取链接
class en_people_speical(scrapy.Item):
    special_id = scrapy.Field()
    special_title = scrapy.Field()
    special_url = scrapy.Field()
    special_time = scrapy.Field()
# en_people_Video子页面抓取链接
class en_people_video(scrapy.Item):
    video_id = scrapy.Field()
    video_title = scrapy.Field()
    video_url = scrapy.Field()
    video_time = scrapy.Field()
# en_people_Photo子页面抓取链接
class en_people_photo(scrapy.Item):
    photo_id = scrapy.Field()
    photo_title = scrapy.Field()
    photo_url = scrapy.Field()
    photo_time = scrapy.Field()
# en_people_Travel子页面抓取链接
class en_people_travel(scrapy.Item):
    travel_id = scrapy.Field()
    travel_title = scrapy.Field()
    travel_url = scrapy.Field()
    travel_time = scrapy.Field()
# en_people_Home首页标题及链接
class en_people_home(scrapy.Item):
    home_id = scrapy.Field()
    home_title = scrapy.Field()
    home_url = scrapy.Field()
    home_time = scrapy.Field()
# en_people_Latest_News1首页标题及链接
class en_people_latest(scrapy.Item):
    latest_id = scrapy.Field()
    latest_title = scrapy.Field()
    latest_url = scrapy.Field()
    latest_time = scrapy.Field()
# en_people_Latest_News2首页标题及链接
class en_people_latest2(scrapy.Item):
    latest2_id = scrapy.Field()
    latest2_title = scrapy.Field()
    latest2_url = scrapy.Field()
    latest2_time = scrapy.Field()
# en_people_Health标题及链接
class en_people_health(scrapy.Item):
    health_id = scrapy.Field()
    health_title = scrapy.Field()
    health_url = scrapy.Field()
    health_time = scrapy.Field()
# en_people_Stories标题及链接
class en_people_stories(scrapy.Item):
    stories_id = scrapy.Field()
    stories_title = scrapy.Field()
    stories_url = scrapy.Field()
    stories_time = scrapy.Field()
# en_people_Odds_culture标题及链接
class en_people_odds(scrapy.Item):
    odds_id = scrapy.Field()
    odds_title = scrapy.Field()
    odds_url = scrapy.Field()
    odds_time = scrapy.Field()

