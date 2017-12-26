# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from News.dbhelper import DBHelper
import json
import codecs
'''写入json文件类'''
class NewsPipeline(object):
    def __init__(self):
        print '**************** WRITE FILE ******************'
        self.file = codecs.open('json/ALL.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


''' 数据库操作类'''
class NEWScrapyPipeline(object):
        ''' 保存到数据库中对应的class
           1、在settings.py文件中配置
           2、在自己实现的爬虫类中yield item,会自动执行'''
        # # 启用数据库助手
        # data_seltct = DBHelper()
        # sql_opinions = "select opinions_id from en_people_opinions"  # 单独查询编辑
        # str_data = data_seltct.select(sql_opinions)  # 执行sql语句
        #
        # sql_business = "select business_id from en_people_business"
        # str_data1 = data_seltct.select(sql_business)

        def __init__(self, dbpool):
            self.dbpool = dbpool
            ''' 这里注释中采用写死在代码中的方式连接线程池，可以从settings配置文件中读取，更加灵活
                self.dbpool=adbapi.ConnectionPool('MySQL',
                                              host='127.0.0.1',
                                              db='crawlpicturesdb',
                                              user='root',
                                              passwd='root',
                                              cursorclass=pymysql.cursors.DictCursor,
                                              charset='utf8',
                                              use_unicode=False)'''

        @classmethod
        def from_settings(cls, settings):
            # 连接数据库引擎
            dbparams = dict(
                host=settings['MYSQL_HOST'],  # 读取settings中的配置
                db=settings['MYSQL_DBNAME'],
                user=settings['MYSQL_USER'],
                passwd=settings['MYSQL_PASSWD'],
                charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
                cursorclass=MySQLdb.cursors.DictCursor,
                use_unicode=False,
            )
            dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy
            return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

        # pipeline默认调用
        def process_item(self, item, spider):
            # print "我是插入"
            #
            # print item["opinions_id"]
            # print self.str_data
            query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
            # query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
            return item

        # 写入数据库中
        def _conditional_insert(self, tx, item):
            print item["opinions_id"]
            print item["business_id"]
            # 判断如果本次数据库中已存在本次查询id则不插入，否则插入
            # if len(item["opinions_id"]):
            #     if item["opinions_id"] in self.str_data:
            #         print "已存在不插入"
            #     else:
            #         print "插入数据"
            #         sql = "insert into en_people_opinions(opinions_id,opinions_title,opinions_url) values(%s,%s,%s)"
            #         params = (item["opinions_id"], item["opinions_title"], item["opinions_url"])
            #         tx.execute(sql, params)
            # if item["business_id"] in self.str_data1:
            #     print "yicunzia"
            # else:
            #     sql = "insert into en_people_business(business_id,business_title,business_url) values(%s,%s,%s)"
            #     params = (item["business_id"], item["business_title"], item["business_url"])
            #     tx.execute(sql, params)

        # 错误处理方法
        def _handle_error(self, failue, item, spider):
            print '--------------database operation exception!!-----------------'
            print '-------------------------------------------------------------'
            print failue