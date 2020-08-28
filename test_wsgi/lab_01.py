import sys
import os
import subprocess
import tempfile
from time import sleep

from wsgiref.simple_server import make_server


def hot_deploy_with_flag(reloader=False, interval=5):
    pid = os.getpid()
    loop_flag = os.environ.get('BOTTLE_CHILD')
    print('loop_flag: %s of %s' % (loop_flag, pid))
    if reloader and not loop_flag:
        try:
            fd, lock_file = tempfile.mkstemp(prefix='six_web.', suffix='.lock')
            os.close(fd)
            while os.path.exists(lock_file):
                env = os.environ.copy()
                env['BOTTLE_CHILD'] = 'true'
                env['LOCK_FILE'] = lock_file
                args = [sys.executable] + sys.argv
                print('Creating another process, current pid: %s' % os.getpid())
                p = subprocess.Popen(args, env=env)
                print('new process pid: %s' % p.pid)
                sleep(interval)
                while p.poll() is None:
                    sleep(interval)
                    print('Updating lock_file time %s' % os.getpid())
        except KeyboardInterrupt:
            print('Process terminated. pid: %s' % os.getpid())
        finally:
            if os.path.exists(lock_file):
                os.remove(lock_file)
    try:
        i = 0
        while i < 5:
            print('another process pid: %s' % os.getpid())
            sleep(interval)
            i += 1
    except KeyboardInterrupt:
        print('exit. pid: %s' % os.getpid())


hot_deploy_with_flag(reloader=True, interval=5)
"""
[root@lanzhiwang-centos7 test_wsgi]# python3 lab_01.py
loop_flag: None of 27824
Creating another process, current pid: 27824
new process pid: 27825
loop_flag: true of 27825
another process pid: 27825
another process pid: 27825
Updating lock_file time 27824
another process pid: 27825
Updating lock_file time 27824
another process pid: 27825
Updating lock_file time 27824
another process pid: 27825
Updating lock_file time 27824
Updating lock_file time 27824
Creating another process, current pid: 27824
new process pid: 27837
loop_flag: true of 27837
another process pid: 27837
another process pid: 27837
Updating lock_file time 27824
another process pid: 27837
Updating lock_file time 27824
another process pid: 27837
Updating lock_file time 27824
another process pid: 27837
Updating lock_file time 27824
Updating lock_file time 27824
Creating another process, current pid: 27824
new process pid: 27844
loop_flag: true of 27844
another process pid: 27844
another process pid: 27844
Updating lock_file time 27824
another process pid: 27844
Updating lock_file time 27824
another process pid: 27844
Updating lock_file time 27824
another process pid: 27844
^CProcess terminated. pid: 27824
another process pid: 27824
exit. pid: 27844
^Cexit. pid: 27824
[root@lanzhiwang-centos7 test_wsgi]#
"""
