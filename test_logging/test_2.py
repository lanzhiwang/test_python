#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

applog_hand = logging.FileHandler("app.log")
formatter = logging.Formatter('%(asctime)s %(filename)s %(lineno)d %(name)-12s %(levelname)-8s %(message)s')
applog_hand.setFormatter(formatter)

logger = logging.getLogger('name1')
logger.addHandler(applog_hand)
logger.setLevel(logging.DEBUG)

print('id(logger): %s' % id(logger))
print('logger.handlers: %s' % logger.handlers)
logger.debug('debug logger')
logger.debug('id(logger): %s' % id(logger))
