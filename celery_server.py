from celery import Celery
from config import Remote,Local

proxy = Remote()
broker_protcol,broker_user,broker_password,broker_ip,broker_port,broker_vhost = proxy.broker_protcol,proxy.broker_user,proxy.broker_password,\
                                        proxy.broker_ip,proxy.broker_port,proxy.broker_vhost
db_protcol,db_user,db_password,db_ip,db_port,db_number = proxy.db_protcol,proxy.db_user,proxy.db_password,\
                                        proxy.db_ip,proxy.db_port,proxy.db_number


s_broker = '{0}://{1}:{2}@{3}:{4}/{5}'.format(broker_protcol,broker_user,broker_password,broker_ip,broker_port,broker_vhost)
s_backend = '{0}://{1}:{2}@{3}:{4}/{5}'.format(db_protcol,db_user,db_password,db_ip,db_port,db_number)

app = Celery('celery_server', backend = s_backend, broker= s_broker)

@app.task
def add(x, y):
    return x + y


