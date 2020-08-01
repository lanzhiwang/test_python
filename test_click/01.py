"""
https://www.jianshu.com/p/572251c91dd0
"""

import click

@click.command()
@click.option("--name", default="li", help="your name")
@click.option("--age", default=26, help="your age")
def hello_world(name, age):
    click.echo(name)
    print(age)

if __name__ == '__main__':
    hello_world()


"""
(venv3) [root@lanzhiwang-centos7 test_click]# python 01.py
li
26
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 01.py --name ll --age 27
ll
27
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 01.py --help
Usage: 01.py [OPTIONS]

Options:
  --name TEXT    your name
  --age INTEGER  your age
  --help         Show this message and exit.
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 01.py -h
Usage: 01.py [OPTIONS]
Try '01.py --help' for help.

Error: no such option: -h
(venv3) [root@lanzhiwang-centos7 test_click]#
"""