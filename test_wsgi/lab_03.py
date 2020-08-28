import sys
import os
import subprocess
import tempfile
from time import sleep
import _thread
import threading

from wsgiref.simple_server import make_server


class MockThreadInterruptted(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('End process, pid is %s' % os.getpid())
        _thread.interrupt_main()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.join()
        print('Mock Thread is exciting!')
        return exc_type

    def __enter__(self):
        self.start()


# try:
#     print('current pid: %s' % os.getpid())
#     bg = MockThreadInterruptted()
#     bg.start()
#     bg.join()
# except KeyboardInterrupt:
#     print('Process terminated. pid: %s' % os.getpid())

"""
[root@lanzhiwang-centos7 test_wsgi]# python3 lab_03.py
current pid: 27953
End process, pid is 27953
Process terminated. pid: 27953
[root@lanzhiwang-centos7 test_wsgi]#
"""

try:
    print('current pid: %s' % os.getpid())
    bg = MockThreadInterruptted()
    with bg:
        for i in range(1, 2):
            sleep(i)
            print('with %s' % i)
except KeyboardInterrupt:
    print('Process terminated. pid: %s' % os.getpid())

"""
[root@lanzhiwang-centos7 test_wsgi]# python3 lab_03.py
current pid: 28001
End process, pid is 28001
Process terminated. pid: 28001
[root@lanzhiwang-centos7 test_wsgi]#
"""
