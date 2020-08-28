import sys
import os
import subprocess
import tempfile
from time import sleep
import _thread
import threading

from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    from io import StringIO
    stdout = StringIO()
    print("Hello world!", file=stdout)
    print(file=stdout)
    h = sorted(environ.items())
    for k, v in h:
        print(k, '=', repr(v), file=stdout)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return [stdout.getvalue().encode("utf-8")]


def start_wsgi():
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()


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
        print('current pid: %s' % os.getpid())
        bg = MockThreadInterruptted()
        with bg:
            start_wsgi()
    except KeyboardInterrupt:
        print('Process terminated. pid: %s' % os.getpid())


hot_deploy_with_flag(reloader=True, interval=5)

