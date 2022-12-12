import redis
import string
import requests
redis_conf = redis.ConnectionPool(host='1.116.151.240', port=6379, password='pass1234', db=0, decode_responses=True)
redis_cli = redis.StrictRedis(connection_pool=redis_conf)

if __name__ == '__main__':
    redis_cli.lpush('zhihu_user', 'mei-ri-jing-ji-xin-wen')

