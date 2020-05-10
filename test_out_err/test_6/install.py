#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.common import get_logger

logger1 = get_logger('install1')
print(logger1)
print(id(logger1))
print(logger1.handlers)
logger1.debug('install logger1')

logger2 = get_logger('install1')
print(logger2)
print(id(logger2))
print(logger2.handlers)
logger2.debug('install logger2')

logger3 = get_logger('install2')
print(logger3)
print(id(logger3))
print(logger3.handlers)
logger3.debug('install logger3')

"""
% python install.py
<logging.Logger object at 0x10fbf89d0>
4559178192
[<logging.handlers.TimedRotatingFileHandler object at 0x10fbf8a50>]
<logging.Logger object at 0x10fbf89d0>
4559178192
[<logging.handlers.TimedRotatingFileHandler object at 0x10fbf8a50>]
<logging.Logger object at 0x10fbf8b10>
4559178512
[<logging.handlers.TimedRotatingFileHandler object at 0x10fbf8b50>]

% ll logs
total 16
drwxr-xr-x  4 huzhi  staff  128  5 10 19:27 ./
drwxr-xr-x  6 huzhi  staff  192  5 10 19:27 ../
-rw-r--r--  1 huzhi  staff  152  5 10 19:27 install1.log
-rw-r--r--  1 huzhi  staff   76  5 10 19:27 install2.log
% cat logs/install1.log
2020-05-10 19:27:05,125 install.py 10 install1     DEBUG    install logger1
2020-05-10 19:27:05,125 install.py 16 install1     DEBUG    install logger2
% cat logs/install2.log
2020-05-10 19:27:05,125 install.py 22 install2     DEBUG    install logger3
%
"""
