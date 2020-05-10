#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

saved_std_out = sys.stdout  # 保存标准输出流
with open('out.txt', 'w+') as file:
    sys.stdout = file  # 标准输出重定向至文件
    print('This message is for file!')

sys.stdout = saved_std_out  # 恢复标准输出流
print('This message is for screen!')

"""
% python test_1.py
This message is for screen!
% cat out.txt
This message is for file!
%
"""