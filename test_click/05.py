"""
https://www.cnblogs.com/alexkn/p/6980400.html
"""

import click


@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()

"""
(venv3) [root@lanzhiwang-centos7 test_click]# python 05.py
Usage: 05.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  dropdb
  initdb
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 05.py initdb
Initialized the database
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 05.py dropdb
Dropped the database
(venv3) [root@lanzhiwang-centos7 test_click]#
"""