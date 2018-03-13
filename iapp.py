# -*- coding:utf-8 -*- 
#from __future__ import absolute_import,unicode_literals
import os,sys
pkg_path = os.path.sep.join(
    (os.path.abspath(os.curdir).split(os.path.sep)[:-1]))
if pkg_path not in sys.path:
    sys.path.append(pkg_path)
    
from celery import Celery
from ipcs.config import Remote,Local

proxy = Remote()
broker_protcol,broker_user,broker_password,broker_ip,broker_port,broker_vhost = proxy.broker_protcol,proxy.broker_user,proxy.broker_password,\
                                        proxy.broker_ip,proxy.broker_port,proxy.broker_vhost
db_protcol,db_user,db_password,db_ip,db_port,db_number = proxy.db_protcol,proxy.db_user,proxy.db_password,\
                                        proxy.db_ip,proxy.db_port,proxy.db_number


s_broker = '{0}://{1}:{2}@{3}:{4}/{5}'.format(broker_protcol,broker_user,broker_password,broker_ip,broker_port,broker_vhost)
s_backend = '{0}://{1}:{2}@{3}:{4}/{5}'.format(db_protcol,db_user,db_password,db_ip,db_port,db_number)

capp = Celery('ipcs', backend = s_backend, broker= s_broker, include = ['ipcs.task'])

if __name__ == '__main__':
    capp.start()