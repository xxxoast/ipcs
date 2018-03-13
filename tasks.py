# -*- coding:utf-8 -*- 

import sys
if ".." not in sys.path:
    sys.path.append("..")
from inspect_toolkit.algorithm import search
from iapp import capp

@capp.task
def add(x, y):
    return x + y

@capp.task
def non_certify(corpration,inspect_item):
    search(corpration,inspect_item)
