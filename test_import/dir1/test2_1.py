#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath

print('test2_1')
print(sys.path)
print('test2_1')


PROJECT_DIR = dirname(abspath(__file__))
print(PROJECT_DIR)
sys.path.insert(0, PROJECT_DIR)

print('test2_1')
print(sys.path)
print('test2_1')


def test2_1():
    return 'test2_1'
