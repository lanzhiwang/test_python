"""
https://www.cnblogs.com/alexkn/p/6980400.html
"""

import click
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

"""
(venv3) [root@lanzhiwang-centos7 test_click]# python 03.py --count=3
Your name: lanzhiwang
Hello lanzhiwang!
Hello lanzhiwang!
Hello lanzhiwang!
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 03.py --count=3 --name=lanzhiwang
Hello lanzhiwang!
Hello lanzhiwang!
Hello lanzhiwang!
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 03.py --help
Usage: 03.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.
(venv3) [root@lanzhiwang-centos7 test_click]#
"""