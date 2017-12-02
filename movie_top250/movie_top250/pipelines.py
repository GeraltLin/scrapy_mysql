# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
class MovieTop250Pipeline(object):
    def __init__(self):

        self.dbpool = adbapi.ConnectionPool('pymysql',
                                            host='127.0.0.1',
                                            db='doubanmovie',
                                            user='root',
                                            passwd='123456',
                                            cursorclass=pymysql.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=False)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    def _conditional_insert(self, tx, item):
        # print item['name']
        sql = "insert into movie(moviename,rating) values(%s,%s)"
        params = (item["moviename"], item["rating"])
        #执行sql语句
        tx.execute(sql, params)

    def _handle_error(self, failure, item, spider):
        print('--------------database operation exception!!-----------------')
        print('-------------------------------------------------------------')
        print(failure)
