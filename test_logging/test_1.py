#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import test_2

applog_hand = logging.FileHandler("app.log")
formatter = logging.Formatter('%(asctime)s %(filename)s %(lineno)d %(name)-12s %(levelname)-8s %(message)s')
applog_hand.setFormatter(formatter)

logger1 = logging.getLogger('name1')
logger1.addHandler(applog_hand)
logger1.setLevel(logging.DEBUG)

print('id(logger1): %s' % id(logger1))
print('logger1.handlers: %s' % logger1.handlers)
logger1.debug('debug logger1')
logger1.debug('id(logger): %s' % id(logger1))


logger2 = logging.getLogger('name1')
print('id(logger2): %s' % id(logger2))
print('logger2.handlers: %s' % logger2.handlers)
# applog_hand = logging.FileHandler("app.log")
# formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
# applog_hand.setFormatter(formatter)
# logger2.addHandler(applog_hand)
# logger2.setLevel(logging.DEBUG)

logger2.debug('debug logger2')
logger2.debug('id(logger): %s' % id(logger2))


logger3 = logging.getLogger('name2')
print('id(logger3): %s' % id(logger3))
print('logger3.handlers: %s' % logger3.handlers)
# applog_hand = logging.FileHandler("app.log")
# formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
# applog_hand.setFormatter(formatter)
logger3.addHandler(applog_hand)
logger3.setLevel(logging.DEBUG)
print('logger3.handlers: %s' % logger3.handlers)

logger3.debug('debug logger3')
logger3.debug('id(logger): %s' % id(logger3))

"""
% python test_1.py
id(logger): 4437671824
logger.handlers: [<logging.FileHandler object at 0x108786210>]
id(logger1): 4437671824
logger1.handlers: [<logging.FileHandler object at 0x108786210>, <logging.FileHandler object at 0x108817fd0>]
id(logger2): 4437671824
logger2.handlers: [<logging.FileHandler object at 0x108786210>, <logging.FileHandler object at 0x108817fd0>]
id(logger3): 4437778512
logger3.handlers: []
logger3.handlers: [<logging.FileHandler object at 0x108817fd0>]
huzhi@huzhideMacBook-Pro test_logging % cat app.log
2020-05-10 18:51:15,354 test_2.py 15 name1        DEBUG    debug logger
2020-05-10 18:51:15,354 test_2.py 16 name1        DEBUG    id(logger): 4437671824
2020-05-10 18:51:15,355 test_1.py 16 name1        DEBUG    debug logger1
2020-05-10 18:51:15,355 test_1.py 16 name1        DEBUG    debug logger1
2020-05-10 18:51:15,355 test_1.py 17 name1        DEBUG    id(logger): 4437671824
2020-05-10 18:51:15,355 test_1.py 17 name1        DEBUG    id(logger): 4437671824
2020-05-10 18:51:15,355 test_1.py 29 name1        DEBUG    debug logger2
2020-05-10 18:51:15,355 test_1.py 29 name1        DEBUG    debug logger2
2020-05-10 18:51:15,355 test_1.py 30 name1        DEBUG    id(logger): 4437671824
2020-05-10 18:51:15,355 test_1.py 30 name1        DEBUG    id(logger): 4437671824
2020-05-10 18:51:15,355 test_1.py 43 name2        DEBUG    debug logger3
2020-05-10 18:51:15,355 test_1.py 44 name2        DEBUG    id(logger): 4437778512
%
"""
