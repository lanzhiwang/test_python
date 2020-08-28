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

start_wsgi()

"""
[root@lanzhiwang-centos7 test_wsgi]# python3 simple_server.py
Serving HTTP on 0.0.0.0 port 8000 ...
127.0.0.1 - - [27/Aug/2020 20:37:14] "GET / HTTP/1.1" 200 3034


[root@lanzhiwang-centos7 ~]# curl http://localhost:8000
Hello world!

CONTENT_LENGTH = ''
CONTENT_TYPE = 'text/plain'
GATEWAY_INTERFACE = 'CGI/1.1'
HISTCONTROL = 'ignoredups'
HISTSIZE = '1000'
HOME = '/root'
HOSTNAME = 'lanzhiwang-centos7'
HTTP_ACCEPT = '*/*'
HTTP_HOST = 'localhost:8000'
HTTP_USER_AGENT = 'curl/7.29.0'
LANG = 'zh_CN.UTF-8'
LESSOPEN = '||/usr/bin/lesspipe.sh %s'
LOGNAME = 'root'
LS_COLORS = 'rs=0:di=38;5;27:ln=38;5;51:mh=44;38;5;15:pi=40;38;5;11:so=38;5;13:do=38;5;5:bd=48;5;232;38;5;11:cd=48;5;232;38;5;3:or=48;5;232;38;5;9:mi=05;48;5;232;38;5;15:su=48;5;196;38;5;15:sg=48;5;11;38;5;16:ca=48;5;196;38;5;226:tw=48;5;10;38;5;16:ow=48;5;10;38;5;21:st=48;5;21;38;5;15:ex=38;5;34:*.tar=38;5;9:*.tgz=38;5;9:*.arc=38;5;9:*.arj=38;5;9:*.taz=38;5;9:*.lha=38;5;9:*.lz4=38;5;9:*.lzh=38;5;9:*.lzma=38;5;9:*.tlz=38;5;9:*.txz=38;5;9:*.tzo=38;5;9:*.t7z=38;5;9:*.zip=38;5;9:*.z=38;5;9:*.Z=38;5;9:*.dz=38;5;9:*.gz=38;5;9:*.lrz=38;5;9:*.lz=38;5;9:*.lzo=38;5;9:*.xz=38;5;9:*.bz2=38;5;9:*.bz=38;5;9:*.tbz=38;5;9:*.tbz2=38;5;9:*.tz=38;5;9:*.deb=38;5;9:*.rpm=38;5;9:*.jar=38;5;9:*.war=38;5;9:*.ear=38;5;9:*.sar=38;5;9:*.rar=38;5;9:*.alz=38;5;9:*.ace=38;5;9:*.zoo=38;5;9:*.cpio=38;5;9:*.7z=38;5;9:*.rz=38;5;9:*.cab=38;5;9:*.jpg=38;5;13:*.jpeg=38;5;13:*.gif=38;5;13:*.bmp=38;5;13:*.pbm=38;5;13:*.pgm=38;5;13:*.ppm=38;5;13:*.tga=38;5;13:*.xbm=38;5;13:*.xpm=38;5;13:*.tif=38;5;13:*.tiff=38;5;13:*.png=38;5;13:*.svg=38;5;13:*.svgz=38;5;13:*.mng=38;5;13:*.pcx=38;5;13:*.mov=38;5;13:*.mpg=38;5;13:*.mpeg=38;5;13:*.m2v=38;5;13:*.mkv=38;5;13:*.webm=38;5;13:*.ogm=38;5;13:*.mp4=38;5;13:*.m4v=38;5;13:*.mp4v=38;5;13:*.vob=38;5;13:*.qt=38;5;13:*.nuv=38;5;13:*.wmv=38;5;13:*.asf=38;5;13:*.rm=38;5;13:*.rmvb=38;5;13:*.flc=38;5;13:*.avi=38;5;13:*.fli=38;5;13:*.flv=38;5;13:*.gl=38;5;13:*.dl=38;5;13:*.xcf=38;5;13:*.xwd=38;5;13:*.yuv=38;5;13:*.cgm=38;5;13:*.emf=38;5;13:*.axv=38;5;13:*.anx=38;5;13:*.ogv=38;5;13:*.ogx=38;5;13:*.aac=38;5;45:*.au=38;5;45:*.flac=38;5;45:*.mid=38;5;45:*.midi=38;5;45:*.mka=38;5;45:*.mp3=38;5;45:*.mpc=38;5;45:*.ogg=38;5;45:*.ra=38;5;45:*.wav=38;5;45:*.axa=38;5;45:*.oga=38;5;45:*.spx=38;5;45:*.xspf=38;5;45:'
MAIL = '/var/spool/mail/root'
OLDPWD = '/root/work/code'
PATH = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin'
PATH_INFO = '/'
PWD = '/root/work/code/test_python/test_wsgi'
QUERY_STRING = ''
REMOTE_ADDR = '127.0.0.1'
REMOTE_HOST = ''
REQUEST_METHOD = 'GET'
SCRIPT_NAME = ''
SERVER_NAME = 'lanzhiwang-centos7'
SERVER_PORT = '8000'
SERVER_PROTOCOL = 'HTTP/1.1'
SERVER_SOFTWARE = 'WSGIServer/0.2'
SHELL = '/bin/bash'
SHLVL = '1'
SSH_CLIENT = '122.189.36.128 51818 22'
SSH_CONNECTION = '122.189.36.128 51818 172.29.146.40 22'
SSH_TTY = '/dev/pts/0'
TERM = 'xterm-256color'
USER = 'root'
XDG_RUNTIME_DIR = '/run/user/0'
XDG_SESSION_ID = '8728'
_ = '/usr/bin/python3'
wsgi.errors = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>
wsgi.file_wrapper = <class 'wsgiref.util.FileWrapper'>
wsgi.input = <_io.BufferedReader name=5>
wsgi.multiprocess = False
wsgi.multithread = True
wsgi.run_once = False
wsgi.url_scheme = 'http'
wsgi.version = (1, 0)
[root@lanzhiwang-centos7 ~]#
"""

# try:
#     start_wsgi()
# except KeyboardInterrupt:
#     print('exit')

"""
[root@lanzhiwang-centos7 test_wsgi]# python3 lab_06.py
Serving HTTP on 0.0.0.0 port 8000 ...
^Cexit
[root@lanzhiwang-centos7 test_wsgi]#

[root@lanzhiwang-centos7 ~]# ps -ef | grep python
root     27814 27504  1 14:27 pts/3    00:00:00 python3 simple_server.py
[root@lanzhiwang-centos7 ~]# ps -T -p 27814
  PID  SPID TTY          TIME CMD
27814 27814 pts/3    00:00:00 python3
[root@lanzhiwang-centos7 ~]#
"""
