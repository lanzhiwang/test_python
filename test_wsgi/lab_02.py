#!/usr/bin/env python3
# encoding: utf-8

import threading
import _thread
import os


def worker():
    """thread worker function"""
    print('Worker')
    print('thread pid: %s' % os.getpid())
    _thread.interrupt_main()
    """
    thread.interrupt_main():在主线程中引发一个 KeyboardInterrupt（通常是Ctrl+C或者是delete）异常，
    子线程可以通过这个函数中断主线程。
    """


try:
    print('current pid: %s' % os.getpid())
    t = threading.Thread(target=worker)
    t.start()
except KeyboardInterrupt:
    print('Process terminated. pid: %s' % os.getpid())

"""
[root@lanzhiwang-centos7 test_wsgi]# python3 lab_03.py
current pid: 27895
Worker
thread pid: 27895
Process terminated. pid: 27895
[root@lanzhiwang-centos7 test_wsgi]#
"""
