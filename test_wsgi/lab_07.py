import sys
import os


def monitor_file_change():
    file_history = dict()
    print(sys.modules)
    print(list(sys.modules.values()))
    for module in list(sys.modules.values()):
        print(module)
        path = getattr(module, '__file__', '')
        print(path)
        print(os.path.exists(path))
        if path and os.path.exists(path):
            ## 将所有文件, 文件时间先存起来
            file_history[path] = os.stat(path).st_mtime
        print('+++++++++++')
    print(file_history)

monitor_file_change()

"""
{
    'builtins': <module 'builtins' (built-in)>,
    'sys': <module 'sys' (built-in)>,
    '_frozen_importlib': <module '_frozen_importlib' (frozen)>,
    '_imp': <module '_imp' (built-in)>,
    '_warnings': <module '_warnings' (built-in)>,
    '_thread': <module '_thread' (built-in)>,
    '_weakref': <module '_weakref' (built-in)>,
    '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>,
    '_io': <module 'io' (built-in)>,
    'marshal': <module 'marshal' (built-in)>,
    'posix': <module 'posix' (built-in)>,
    'zipimport': <module 'zipimport' (built-in)>,
    'encodings': <module 'encodings' from '/usr/lib64/python3.6/encodings/__init__.py'>,
    'codecs': <module 'codecs' from '/usr/lib64/python3.6/codecs.py'>,
    '_codecs': <module '_codecs' (built-in)>,
    'encodings.aliases': <module 'encodings.aliases' from '/usr/lib64/python3.6/encodings/aliases.py'>,
    'encodings.utf_8': <module 'encodings.utf_8' from '/usr/lib64/python3.6/encodings/utf_8.py'>,
    '_signal': <module '_signal' (built-in)>,
    '__main__': <module '__main__' from 'lab_05.py'>,
    'encodings.latin_1': <module 'encodings.latin_1' from '/usr/lib64/python3.6/encodings/latin_1.py'>,
    'io': <module 'io' from '/usr/lib64/python3.6/io.py'>,
    'abc': <module 'abc' from '/usr/lib64/python3.6/abc.py'>,
    '_weakrefset': <module '_weakrefset' from '/usr/lib64/python3.6/_weakrefset.py'>,
    'site': <module 'site' from '/usr/lib64/python3.6/site.py'>,
    'os': <module 'os' from '/usr/lib64/python3.6/os.py'>,
    'errno': <module 'errno' (built-in)>,
    'stat': <module 'stat' from '/usr/lib64/python3.6/stat.py'>,
    '_stat': <module '_stat' (built-in)>,
    'posixpath': <module 'posixpath' from '/usr/lib64/python3.6/posixpath.py'>,
    'genericpath': <module 'genericpath' from '/usr/lib64/python3.6/genericpath.py'>,
    'os.path': <module 'posixpath' from '/usr/lib64/python3.6/posixpath.py'>,
    '_collections_abc': <module '_collections_abc' from '/usr/lib64/python3.6/_collections_abc.py'>,
    '_sitebuiltins': <module '_sitebuiltins' from '/usr/lib64/python3.6/_sitebuiltins.py'>,
    'sysconfig': <module 'sysconfig' from '/usr/lib64/python3.6/sysconfig.py'>,
    '_sysconfigdata_m_linux_x86_64-linux-gnu': <module '_sysconfigdata_m_linux_x86_64-linux-gnu' from '/usr/lib64/python3.6/_sysconfigdata_m_linux_x86_64-linux-gnu.py'>
}

[
    <module 'builtins' (built-in)>,
    <module 'sys' (built-in)>,
    <module '_frozen_importlib' (frozen)>,
    <module '_imp' (built-in)>,
    <module '_warnings' (built-in)>,
    <module '_thread' (built-in)>,
    <module '_weakref' (built-in)>,
    <module '_frozen_importlib_external' (frozen)>,
    <module 'io' (built-in)>,
    <module 'marshal' (built-in)>,
    <module 'posix' (built-in)>,
    <module 'zipimport' (built-in)>,
    <module 'encodings' from '/usr/lib64/python3.6/encodings/__init__.py'>,
    <module 'codecs' from '/usr/lib64/python3.6/codecs.py'>,
    <module '_codecs' (built-in)>,
    <module 'encodings.aliases' from '/usr/lib64/python3.6/encodings/aliases.py'>,
    <module 'encodings.utf_8' from '/usr/lib64/python3.6/encodings/utf_8.py'>,
    <module '_signal' (built-in)>,
    <module '__main__' from 'lab_05.py'>,
    <module 'encodings.latin_1' from '/usr/lib64/python3.6/encodings/latin_1.py'>,
    <module 'io' from '/usr/lib64/python3.6/io.py'>,
    <module 'abc' from '/usr/lib64/python3.6/abc.py'>,
    <module '_weakrefset' from '/usr/lib64/python3.6/_weakrefset.py'>,
    <module 'site' from '/usr/lib64/python3.6/site.py'>,
    <module 'os' from '/usr/lib64/python3.6/os.py'>,
    <module 'errno' (built-in)>,
    <module 'stat' from '/usr/lib64/python3.6/stat.py'>,
    <module '_stat' (built-in)>,
    <module 'posixpath' from '/usr/lib64/python3.6/posixpath.py'>,
    <module 'genericpath' from '/usr/lib64/python3.6/genericpath.py'>,
    <module 'posixpath' from '/usr/lib64/python3.6/posixpath.py'>,
    <module '_collections_abc' from '/usr/lib64/python3.6/_collections_abc.py'>,
    <module '_sitebuiltins' from '/usr/lib64/python3.6/_sitebuiltins.py'>,
    <module 'sysconfig' from '/usr/lib64/python3.6/sysconfig.py'>,
    <module '_sysconfigdata_m_linux_x86_64-linux-gnu' from '/usr/lib64/python3.6/_sysconfigdata_m_linux_x86_64-linux-gnu.py'>
]


<module 'builtins' (built-in)>

False
+++++++++++
<module 'sys' (built-in)>

False
+++++++++++
<module '_frozen_importlib' (frozen)>

False
+++++++++++
<module '_imp' (built-in)>

False
+++++++++++
<module '_warnings' (built-in)>

False
+++++++++++
<module '_thread' (built-in)>

False
+++++++++++
<module '_weakref' (built-in)>

False
+++++++++++
<module '_frozen_importlib_external' (frozen)>

False
+++++++++++
<module 'io' (built-in)>

False
+++++++++++
<module 'marshal' (built-in)>

False
+++++++++++
<module 'posix' (built-in)>

False
+++++++++++
<module 'zipimport' (built-in)>

False
+++++++++++
<module 'encodings' from '/usr/lib64/python3.6/encodings/__init__.py'>
/usr/lib64/python3.6/encodings/__init__.py
True
+++++++++++
<module 'codecs' from '/usr/lib64/python3.6/codecs.py'>
/usr/lib64/python3.6/codecs.py
True
+++++++++++
<module '_codecs' (built-in)>

False
+++++++++++
<module 'encodings.aliases' from '/usr/lib64/python3.6/encodings/aliases.py'>
/usr/lib64/python3.6/encodings/aliases.py
True
+++++++++++
<module 'encodings.utf_8' from '/usr/lib64/python3.6/encodings/utf_8.py'>
/usr/lib64/python3.6/encodings/utf_8.py
True
+++++++++++
<module '_signal' (built-in)>

False
+++++++++++
<module '__main__' from 'lab_05.py'>
lab_05.py
True
+++++++++++
<module 'encodings.latin_1' from '/usr/lib64/python3.6/encodings/latin_1.py'>
/usr/lib64/python3.6/encodings/latin_1.py
True
+++++++++++
<module 'io' from '/usr/lib64/python3.6/io.py'>
/usr/lib64/python3.6/io.py
True
+++++++++++
<module 'abc' from '/usr/lib64/python3.6/abc.py'>
/usr/lib64/python3.6/abc.py
True
+++++++++++
<module '_weakrefset' from '/usr/lib64/python3.6/_weakrefset.py'>
/usr/lib64/python3.6/_weakrefset.py
True
+++++++++++
<module 'site' from '/usr/lib64/python3.6/site.py'>
/usr/lib64/python3.6/site.py
True
+++++++++++
<module 'os' from '/usr/lib64/python3.6/os.py'>
/usr/lib64/python3.6/os.py
True
+++++++++++
<module 'errno' (built-in)>

False
+++++++++++
<module 'stat' from '/usr/lib64/python3.6/stat.py'>
/usr/lib64/python3.6/stat.py
True
+++++++++++
<module '_stat' (built-in)>

False
+++++++++++
<module 'posixpath' from '/usr/lib64/python3.6/posixpath.py'>
/usr/lib64/python3.6/posixpath.py
True
+++++++++++
<module 'genericpath' from '/usr/lib64/python3.6/genericpath.py'>
/usr/lib64/python3.6/genericpath.py
True
+++++++++++
<module 'posixpath' from '/usr/lib64/python3.6/posixpath.py'>
/usr/lib64/python3.6/posixpath.py
True
+++++++++++
<module '_collections_abc' from '/usr/lib64/python3.6/_collections_abc.py'>
/usr/lib64/python3.6/_collections_abc.py
True
+++++++++++
<module '_sitebuiltins' from '/usr/lib64/python3.6/_sitebuiltins.py'>
/usr/lib64/python3.6/_sitebuiltins.py
True
+++++++++++
<module 'sysconfig' from '/usr/lib64/python3.6/sysconfig.py'>
/usr/lib64/python3.6/sysconfig.py
True
+++++++++++
<module '_sysconfigdata_m_linux_x86_64-linux-gnu' from '/usr/lib64/python3.6/_sysconfigdata_m_linux_x86_64-linux-gnu.py'>
/usr/lib64/python3.6/_sysconfigdata_m_linux_x86_64-linux-gnu.py
True
+++++++++++

{
    '/usr/lib64/python3.6/encodings/__init__.py': 1545601034.0,
    '/usr/lib64/python3.6/codecs.py': 1545601034.0,
    '/usr/lib64/python3.6/encodings/aliases.py': 1545601034.0,
    '/usr/lib64/python3.6/encodings/utf_8.py': 1545601034.0,
    'lab_05.py': 1598581708.0,
    '/usr/lib64/python3.6/encodings/latin_1.py': 1545601034.0,
    '/usr/lib64/python3.6/io.py': 1545601034.0,
    '/usr/lib64/python3.6/abc.py': 1545601034.0,
    '/usr/lib64/python3.6/_weakrefset.py': 1545601034.0,
    '/usr/lib64/python3.6/site.py': 1585833211.0,
    '/usr/lib64/python3.6/os.py': 1545601034.0,
    '/usr/lib64/python3.6/stat.py': 1545601034.0,
    '/usr/lib64/python3.6/posixpath.py': 1545601034.0,
    '/usr/lib64/python3.6/genericpath.py': 1545601034.0,
    '/usr/lib64/python3.6/_collections_abc.py': 1545601034.0,
    '/usr/lib64/python3.6/_sitebuiltins.py': 1545601034.0,
    '/usr/lib64/python3.6/sysconfig.py': 1585834594.0,
    '/usr/lib64/python3.6/_sysconfigdata_m_linux_x86_64-linux-gnu.py': 1585834496.0
}
[root@lanzhiwang-centos7 test_wsgi]#


"""
