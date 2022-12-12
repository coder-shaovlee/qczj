# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

import redis
from itemadapter import ItemAdapter


class QczjPipeline:

    def __init__(self):
        self.redis_cli = redis.ConnectionPool(host=self.host, port=self.port, password=self.password, db=self.db)
        self.redis_con = redis.StrictRedis(connection_pool=self.redis_cli)

    def open_spider(self, spider):
        print('开始爬虫！')
        print(self.redis_con)
        print(self.port)

    @classmethod
    def from_crawler(cls, crawler):
        cls.host = crawler.settings.get('REDIS_PARAMS').get('host')
        cls.port = crawler.settings.get('REDIS_PARAMS').get('port')
        cls.password = crawler.settings.get('REDIS_PARAMS').get('password')
        cls.db = crawler.settings.get('REDIS_PARAMS').get('db')
        return cls()

    def process_item(self, item, spider):
        print(item)
        self.redis_con.lpush('car', str(item))
        return item
