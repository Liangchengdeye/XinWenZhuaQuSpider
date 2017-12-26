# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
class ChinadailyPipeline(object):
    # 存入到json文件便于查阅，仅供参考，每次刷新
    def __init__(self):
        print '**************** WRITE FILE ******************'
        self.file = codecs.open('json/NEWS.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


