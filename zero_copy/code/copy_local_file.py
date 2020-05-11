import os

source_file = open(r'./480P_2000K_200329271.mp4', 'rb')
dist_file = open(r'./dist.mp4', 'w+')

ret = 0
offset = 0
while True:
    ret = os.sendfile(dist_file.fileno(), source_file.fileno(), offset, 65536)
    offset += ret
    if ret == 0:
        break

"""
% python3 copy_local_file.py
Traceback (most recent call last):
  File "copy_local_file.py", line 9, in <module>
    ret = os.sendfile(dist_file.fileno(), source_file.fileno(), offset, 65536)
OSError: [Errno 38] Socket operation on non-socket
%
"""
