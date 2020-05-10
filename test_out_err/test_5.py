#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import redirect_stdout, redirect_stderr

out = open('out.txt', 'w')
err = open('err.txt', 'w')
with redirect_stdout(out), redirect_stderr(err):
    print(os.getcwd())
