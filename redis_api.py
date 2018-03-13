# -*- coding:utf-8 -*- 
from __future__ import absolute_import,unicode_literals
import json
import redis

from misc import unicode2str_r

class RedisApi(object):

    def __init__(self, user = 'xudi', ip = '127.0.0.1', password = None, port = 6379, db_number = 10):
        redis_url = 'redis://{0}:{1}@{2}:{3}/{4}'.format(user,password,ip,port,db_number)
        self.iredis = redis.Redis.from_url(redis_url)
        self.prefix = 'celery-task-meta'
        
    def exists(self, key):
        return self.iredis.exists(key)
    
    def list_keys(self,pattern = '*'):
        return self.iredis.keys(pattern)
    
    def get_key(self, id):
        key = '-'.join((self.prefix,id))
        return key
    
    def get_value_by_id(self,id):
        return self.get_value_by_key(self.get_key(id))
    
    def get_value_by_key(self, key):
        if self.iredis.exists(key):
            value = self.iredis.get(key)
        else:
            return None
        pydict = json.loads(value)
        return unicode2str_r(pydict)

if __name__ == '__main__':
    from config import Local,Remote
    proxy = Local()
    print proxy.db_user,proxy.db_ip,proxy.db_password,proxy.db_port,proxy.db_number
    db = RedisApi(proxy.db_user,proxy.db_ip,proxy.db_password,proxy.db_port,proxy.db_number)
    keys =  db.list_keys()
    if len(keys) > 0:
        print db.get_value_by_key(keys[-1])
    else:
        print 'no key'
    
    