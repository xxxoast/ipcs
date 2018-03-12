#encoding : utf-8

class Remote(object):
    def __init__(self):
        self.broker_protcol = 'pyamqp'
        self.broker_user = 'xudi'
        self.broker_password = 'xudi.1989319'
        self.broker_ip = '120.24.189.82'
        self.broker_port = '5672'
        self.broker_vhost = 'myvhost'
        
        self.db_protcol = 'redis'
        self.db_user = 'xudi'
        self.db_password = 'xudi.1989319'
        self.db_ip = '120.24.189.82'
        self.db_port = '6379'
        self.db_number = 10
        
class Local(object):
    def __init__(self):
        self.broker_protcol = 'pyamqp'
        self.broker_user = 'xudi'
        self.broker_password = '1989319'
        self.broker_ip = '127.0.0.1'
        self.broker_port = '5672'
        self.broker_vhost = 'myvhost'
        
        self.db_protcol = 'redis'
        self.db_user = 'xudi'
        self.db_password = ''
        self.db_ip = '127.0.0.1'
        self.db_port = '6379'
        self.db_number = 10
        