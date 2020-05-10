#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/33500220/how-to-redirect-stderr-to-a-file-in-python

import sys

original_stderr = sys.stderr
file_err = open('err.txt', 'w')
sys.stderr = file_err
print(os.getcwd())
sys.stderr = original_stderr
print(os.getcwd())
file_err.close()

print(os.getcwd())

"""
% python test_3.py
% cat err.txt
Traceback (most recent call last):
  File "test_3.py", line 9, in <module>
    print(os.getcwd())
NameError: name 'os' is not defined
%
"""
