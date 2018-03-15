# encoding : utf-8
#from __future__ import absolute_import,unicode_literals

import os,sys
import socket

pkg_path = os.path.sep.join(
    (os.path.abspath(os.curdir).split(os.path.sep)[:-1]))
if pkg_path not in sys.path:
    sys.path.append(pkg_path)
    
from inspect_toolkit.utils import unicode2cp936,unicode2utf8,unicode2cp936_r,unicode2utf8_r,unicode2str_r

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip    