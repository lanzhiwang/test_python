#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

saved_std_out = sys.stdout
out_file = open('logs/out.log', 'w')
sys.stdout = out_file

saved_std_err = sys.stderr
err_file = open('logs/err.log', 'w')
sys.stderr = err_file

##########
import install
from views import index

##########

sys.stdout = saved_std_out
out_file.close()

sys.stderr = saved_std_err
err_file.close()

"""
% python init.py
% cat logs/out.log
log_file_name: install1
log_file_list: ['', 'install1']
logger: 4414904848
logger.handlers: []
log_file_path: /Users/huzhi/work/code/test_python/test_out_err/test_6/logs/install1.log
True
True
logger.handlers: [<logging.handlers.TimedRotatingFileHandler object at 0x107261a90>]
<logging.Logger object at 0x107261a10>
4414904848
[<logging.handlers.TimedRotatingFileHandler object at 0x107261a90>]
log_file_name: install1
log_file_list: ['', 'install1']
logger: 4414904848
logger.handlers: [<logging.handlers.TimedRotatingFileHandler object at 0x107261a90>]
<logging.Logger object at 0x107261a10>
4414904848
[<logging.handlers.TimedRotatingFileHandler object at 0x107261a90>]
log_file_name: install2
log_file_list: ['', 'install2']
logger: 4414905168
logger.handlers: []
log_file_path: /Users/huzhi/work/code/test_python/test_out_err/test_6/logs/install2.log
True
True
logger.handlers: [<logging.handlers.TimedRotatingFileHandler object at 0x107261b90>]
<logging.Logger object at 0x107261b50>
4414905168
[<logging.handlers.TimedRotatingFileHandler object at 0x107261b90>]

% cat logs/err.log
Traceback (most recent call last):
  File "init.py", line 16, in <module>
    from views import index
ImportError: No module named views
%
"""