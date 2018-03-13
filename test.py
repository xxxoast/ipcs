from __future__ import absolute_import,unicode_literals
from task import add
from ipcs.task import add,non_certify
from misc import unicode2str_r,unicode2utf8_r,unicode2cp936_r
import json

if __name__ == '__main__':
    result = non_certify.delay('pingan', 'merchant')
    print result.ready()
    re = json.loads(result.get())['result']
    for i in unicode2utf8_r(re):
        for j in i:
            print j,
        print ''
    print result.ready()