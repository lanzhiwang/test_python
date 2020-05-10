#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

print('test4_1')
print(sys.path)
print('test4_1')
"""
test4_1
[
    '/Users/huzhi/work/code/import-learn',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg',
    '/Users/huzhi/work/code/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
]
test4_1
"""

from dir1.dir2.test3_1 import test3_1
from test2_1 import test2_1


logger.debug('debug test4_1')


def test4_1():
    return '%s : %s : test4_1' % (test2_1(), test3_1())


if __name__ == '__main__':
    print(test4_1())
    print(dir_test_2.test3_1.test3_1())


    print(dir_test_1.test2_1.test2_1())
    

