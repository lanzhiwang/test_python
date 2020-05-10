#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

saved_std_out = sys.stderr
with open('err.txt', 'w') as file:
    sys.stderr = file
    print(os.getcwd())

sys.stdout = saved_std_out
print(os.getcwd())

"""
% python test_4.py
% cat err.txt
%
"""