"""
https://www.cnblogs.com/alexkn/p/6980400.html
"""

import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for _ in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

"""
(venv3) [root@lanzhiwang-centos7 test_click]# python 06.py --help
Usage: 06.py [OPTIONS] NAME

Options:
  --count INTEGER  number of greetings
  --help           Show this message and exit.
(venv3) [root@lanzhiwang-centos7 test_click]# python 06.py lanzhiwang --count 2
Hello lanzhiwang!
Hello lanzhiwang!
(venv3) [root@lanzhiwang-centos7 test_click]#
"""