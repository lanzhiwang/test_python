import logging
from logging.handlers import TimedRotatingFileHandler
import os


APP_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# /Users/huzhi/work/code/test_python/test_logging/test_3


def get_logger(log_file_name):
    """
    log_file_name = 'install'
    log_file_name = 'bin/start'
    log_file_name = 'views/index'
    log_file_name = 'lib/data/pg'

    log_file_list = ['', 'install']
    log_file_list = ['bin', 'start']
    log_file_list = ['view', 'index']
    log_file_list = ['lib/data', 'pg']

    """
    # print('log_file_name: %s' % log_file_name)

    log_file_name = log_file_name.strip('/')
    pos = log_file_name.rfind('/')
    log_file_list = [None, None]
    if pos == -1:
        log_file_list[0] = ''
        log_file_list[1] = log_file_name
    else:
        log_file_list[0] = log_file_name[:pos]
        log_file_list[1] = log_file_name[pos+1:]
    # print('log_file_list: %s' % log_file_list)

    logger = logging.getLogger(log_file_name)
    # print('logger: %s' % id(logger))

    # print('logger.handlers: %s' % logger.handlers)
    if not logger.handlers:
        log_file_path = os.path.join(APP_ROOT_PATH, 'logs', log_file_list[0], '%s.log' % log_file_list[1])
        # print('log_file_path: %s' % log_file_path)

        # print(os.path.exists(os.path.dirname(log_file_path)))
        if not os.path.exists(os.path.dirname(log_file_path)):
            os.makedirs(os.path.dirname(log_file_path))
        # print(os.path.exists(os.path.dirname(log_file_path)))

        log_handler = TimedRotatingFileHandler(log_file_path, 'midnight')
        log_handler.suffix = "%Y-%m-%d"
        formatter = logging.Formatter('%(asctime)s %(filename)s %(lineno)d %(name)-12s %(levelname)-8s %(message)s')
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)
        logger.setLevel(logging.DEBUG)
        # print('logger.handlers: %s' % logger.handlers)
    return logger


if __name__ == '__main__':
    get_logger('views/index')
