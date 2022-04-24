# import sys
# import os.path as path
# file_path = path.dirname(path.abspath(__file__))
# sys.path.append(path.join(path.join(file_path, "..")))
# sys.path.append(path.join(path.join(file_path, "..","..")))
# sys.path.append(path.join(path.join(file_path, "..","..","..")))

from src.lib import Singleton
from .logger_builder import LoggerBuilder
from .logger_error import LoggerError
import logging


class LoggerManager(object):
    __metaclass__ = Singleton
    _logger = None

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def getlogger(name=None, logfile=None, file_level=logging.INFO, stream_level=logging.WARNING):

        if not name:
            raise ValueError("Must supply logger name")

        if isinstance(LoggerManager._logger, LoggerBuilder):
            return LoggerManager._logger

        LoggerManager._logger = LoggerBuilder(name=name, logfile=logfile, file_level=file_level, stream_level=stream_level)
        return LoggerManager._logger

def log():
    logger= LoggerManager._logger
    if not isinstance(logger, logging.Logger):
        raise LoggerError("Logger is not set yet")

    return logger

