#!/usr/bin/env python
# encoding: utf-8
# ENV: python 2.7, redis(pip install redis)
import redis

# Create redis connection_pool and connect to redis by using it
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.StrictRedis(connection_pool = pool)

# redis data will save in this dict 
domain_list = {}


with open('redis.txt', 'a') as f:
    # r.keys() will get all keys in redis
    all_keys = r.keys()
    
    for domain_name in all_keys:
        domain_list[domain_name] = long(r.get(domain_name))
        
    for domain_access_rate in sorted(domain_list.iteritems(), key=lambda x: x[1], reverse=True):
        f.write("%s : %d\n" % (domain_access_rate[0], domain_access_rate[1]))