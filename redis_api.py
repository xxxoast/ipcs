# -*- coding:utf-8 -*- 
#from __future__ import absolute_import,unicode_literals
import json
import redis

from misc import unicode2str_r

class RedisApi(object):

    def __init__(self, user = 'xudi', ip = '127.0.0.1', password = None, port = 6379, db_number = 10):
        if password is not None:
            redis_url = 'redis://{0}:{1}@{2}:{3}/{4}'.format(user,password,ip,port,db_number)
        else:
            redis_url = 'redis://{0}@{1}:{2}/{3}'.format(user,ip,port,db_number)
        print redis_url
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

def get_handler_from_proxy(proxy):
    print proxy.db_user,proxy.db_ip,proxy.db_password,proxy.db_port,proxy.db_number
    return proxy.db_user,proxy.db_ip,proxy.db_password,proxy.db_port,proxy.db_number
    
def get_local_handler():
    from config import Local
    proxy = Local()
    return RedisApi(*get_handler_from_proxy(proxy))

def get_remote_handler():
    from config import Remote
    proxy = Remote()
    return RedisApi(*get_handler_from_proxy(proxy))
    
if __name__ == '__main__':
    db = get_local_handler()
    keys =  db.list_keys()
    if len(keys) > 0:
        print db.get_value_by_key(keys[-1])
    else:
        print 'no key'
    
    