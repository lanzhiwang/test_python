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
        _monitor_file_change()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.join()
        print('Mock Thread is exciting!')
        return exc_type

    def __enter__(self):
        self.start()


def _monitor_file_change():
    file_history = dict()
    for module in list(sys.modules.values()):
        path = getattr(module, '__file__', '')
        if path and os.path.exists(path):
            file_history[path] = os.stat(path).st_mtime
    status = None
    while not status:
        for path, last_modify_time in list(file_history.items()):
            if not os.path.exists(path) or os.stat(path).st_mtime > float(last_modify_time):
                status = 'reload'
                _thread.interrupt_main()
                break


try:
    print('current pid: %s' % os.getpid())
    bg = MockThreadInterruptted()
    with bg:
        for i in range(1, 5):
            sleep(i)
            print('with %s' % i)
except KeyboardInterrupt:
    print('Process terminated. pid: %s' % os.getpid())