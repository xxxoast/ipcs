# -*- coding:utf-8 -*- 
import json
import redis

from misc import unicode2str_r

class RedisApi(object):

    def __init__(self, db_addr = '127.0.0.1', password = None, db_port = 6379, db_name = 10):
        self.iredis = redis.Redis(host = db_addr, password = None, port = db_port, db = db_name)
        self.prefix = 'celery-task-meta'
        
    def exists(self, key):
        return self.iredis.exists(key)
    
    def list_keys(self,pattern = '*'):
        return self.iredis.keys(pattern)
    
    def get_key(self, id):
        key = '-'.join((self.prefix,id))
        return key
        
    def get_value(self, id):
        key = self.get_key(id)
        if self.iredis.exists(key):
            value = self.iredis.get(key)
        else:
            return None
        pydict = json.loads(value)
        return unicode2str_r(pydict)

if __name__ == '__main__':
    from config import Local
    local = Local()
    db = RedisApi(local.db_ip,local.db_password,local.db_port,local.db_number)
    print db.list_keys()
    id = 'b7a3e446-c739-4623-ac09-317c195d6bed'
    print db.get_value(id)
    
    