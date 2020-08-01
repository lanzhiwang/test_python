"""
https://www.jianshu.com/p/572251c91dd0
"""

import click

@click.group()
def first():
    print("hello world")

@click.command()
@click.option("--name", help="the name")
def second(name):
    print("this is second: {}".format(name))

@click.command()
def third():
    print("this is third")

first.add_command(second)
first.add_command(third)

if __name__ == '__main__':
    first()

"""
(venv3) [root@lanzhiwang-centos7 test_click]# python 02.py
Usage: 02.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  second
  third
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 02.py second
hello world
this is second: None
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 02.py third
hello world
this is third
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 02.py second --name hh
hello world
this is second: hh
(venv3) [root@lanzhiwang-centos7 test_click]#
"""
