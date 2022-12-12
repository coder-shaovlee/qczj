import string

import redis
from lxml import etree
import scrapy
import sys
import os
from scrapy_redis.spiders import RedisSpider


class QcSpider(RedisSpider):
    name = 'qc'
    redis_batch_size = 1
    redis_key = 'test'
    custom_settings = {
        "REDIS_PARAMS": {
            "host": '1.116.151.240',
            "port": 6379,
            "password": "pass1234",
            "db": 0
        }
    }

    def make_request_from_data(self, data):
        data = data.decode()
        print(data)
        url = data
        headers = {
            "authority": "www.autohome.com.cn",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://www.autohome.com.cn/car/",
            "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        print(data)
        return scrapy.Request(url=url, headers=headers, dont_filter=True, callback=self.parse)


    def parse(self, response, *args):
        HTML = etree.HTML(response.text)
        car_List = HTML.xpath("//dl/dd/ul//li")
        for car in car_List:
            item = dict()
            item['name'] = ''.join(car.xpath("./h4/a/text()"))
            item['price'] = ''.join(car.xpath("./text()")).strip()
            if not item['name']: continue
            else:
                pass
                yield item


if __name__ == '__main__':
    redis_conf = redis.ConnectionPool(host='1.116.151.240', port=6379, password='pass1234', db=0, decode_responses=True)
    redis_cli = redis.StrictRedis(connection_pool=redis_conf)
    redis_cli.lpush('test', 'https://www.autohome.com.cn/grade/carhtml/B.html')
    # os.system('python3 -m scrapy crawl qc')
