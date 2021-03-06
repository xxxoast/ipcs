# -*- coding:utf-8 -*- 
#from __future__ import absolute_import,unicode_literals

import os,sys
pkg_path = os.path.sep.join(
    (os.path.abspath(os.curdir).split(os.path.sep)[:-1]))
if pkg_path not in sys.path:
    sys.path.append(pkg_path)

from ipcs.iapp import capp
from ipcs.misc import unicode2str_r
from celery.utils.log import get_task_logger

from inspect_toolkit.algorithm import search

logger = get_task_logger(__name__)

@capp.task
def add(x, y):
    return x + y

@capp.task
def non_certify(corpration,inspect_item):
    logger.info('params {} {}'.format(corpration,inspect_item))
    return search(unicode2str_r(corpration),unicode2str_r(inspect_item))

