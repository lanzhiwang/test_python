"""
https://www.cnblogs.com/alexkn/p/6980400.html
"""

import click


@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()

"""
(venv3) [root@lanzhiwang-centos7 test_click]# python 04.py
Usage: 04.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  dropdb
  initdb
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 04.py initdb
Initialized the database
(venv3) [root@lanzhiwang-centos7 test_click]#
(venv3) [root@lanzhiwang-centos7 test_click]# python 04.py dropdb
Dropped the database
(venv3) [root@lanzhiwang-centos7 test_click]#
"""
