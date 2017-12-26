# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from xinhuanet.dbhelper import DBHelper
# 写入json文件类
class XinhuanetPipeline(object):
    def __init__(self):
        print '**************** WRITE FILE ******************'
        self.file = codecs.open('data/NEWS.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
