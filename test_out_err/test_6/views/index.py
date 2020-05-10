#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(ROOT_PATH)  # /Users/huzhi/work/code/test_python/test_logging/test_3

sys.path.insert(0, ROOT_PATH)

from utils.common import get_logger

logger1 = get_logger('view/index')
print(logger1)
print(id(logger1))
print(logger1.handlers)
logger1.debug('install logger1')

logger2 = get_logger('view/index')
print(logger2)
print(id(logger2))
print(logger2.handlers)
logger2.debug('install logger2')

"""
% python install.py
<logging.Logger object at 0x1083049d0>
4432349648
[<logging.handlers.TimedRotatingFileHandler object at 0x108304a50>]
<logging.Logger object at 0x1083049d0>
4432349648
[<logging.handlers.TimedRotatingFileHandler object at 0x108304a50>]
% cat logs/install.log
2020-05-10 19:19:32,265 install.py 10 install      DEBUG    install logger1
2020-05-10 19:19:32,265 install.py 16 install      DEBUG    install logger2
%
"""
