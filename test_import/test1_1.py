#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import test1_2
import dir1.test2_1
import dir1.dir2.test3_1
import dir1.dir2.dir3.test4_1



import os
import sys
from os.path import dirname, abspath

print('*****' * 20)
print(sys.path)
PROJECT_DIR = dirname(dirname(abspath(__file__)))
print(PROJECT_DIR)
sys.path.insert(0, PROJECT_DIR)
print(sys.path)
"""
[
    '/Users/huzhi/work/code/import-learn',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
]

/Users/huzhi/work/code

[
    '/Users/huzhi/work/code',
    '/Users/huzhi/work/code/import-learn',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
]

"""


print('*****' * 20)
CURR = os.path.abspath(os.path.dirname(__file__))
print(CURR)
ISOP_PARDIR = os.path.normpath(os.path.join(CURR, os.path.pardir))
print(ISOP_PARDIR)
sys.path.insert(0, ISOP_PARDIR)
print(sys.path)
"""
/Users/huzhi/work/code/import-learn
/Users/huzhi/work/code
[
    '/Users/huzhi/work/code',
    '/Users/huzhi/work/code',
    '/Users/huzhi/work/code/import-learn',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
]
"""


logger = logging.getLogger()
applog_hand = logging.FileHandler("app.log")
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
applog_hand.setFormatter(formatter)
logger.addHandler(applog_hand)
logger.setLevel(logging.DEBUG)

logger.debug('debug test1_1')


def test1_1():
    return 'test1_1 : %s' % dir1.dir2.dir3.test4_1.test4_1()


if __name__ == '__main__':
    print(test1_1())
    print(test1_2.test1_2())
    print(dir1.test2_1.test2_1())
    print(dir1.dir2.test3_1.test3_1())
    print(dir1.dir2.dir3.test4_1.test4_1())


"""
% python test1_1.py
test1_2
['/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
test1_2
test2_1
['/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
test2_1
/Users/huzhi/work/code/import-learn/dir1
test2_1
['/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
test2_1
test3_1
['/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
test3_1
test4_1
['/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
test4_1
test2_1
['/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
test2_1
/Users/huzhi/work/code/import-learn/dir1
test2_1
['/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
test2_1
****************************************************************************************************
['/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
/Users/huzhi/work/code
['/Users/huzhi/work/code', '/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
****************************************************************************************************
/Users/huzhi/work/code/import-learn
/Users/huzhi/work/code
['/Users/huzhi/work/code', '/Users/huzhi/work/code', '/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn/dir1', '/Users/huzhi/work/code/import-learn', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg', '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']
test1_1 : test2_1 : test3_1 : test4_1
test1_2
test2_1
test3_1
test2_1 : test3_1 : test4_1
%
"""