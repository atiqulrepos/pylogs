import logging
import os.path as path

# sys.path.append(path.abspath(__file__))

from utils import LoggerManager, LoggerError, log as lg
from classes import Employee

# https://stackoverflow.com/questions/61141419/in-python-i-can-write-a-log-to-console-but-its-not-getting-written-into-file
# print(str(logger.handlers).split(","))

log2 = LoggerManager.getLogger(name="junk", logfile=path.join(path.dirname(path.abspath(__file__)), "../test.log"), file_level=logging.INFO, stream_level=logging.INFO)
log2.critical("critical")
log2.error("error")
log2.warning("warning")
log2.info("info")
log2.debug("debug")

e = Employee(fname="atiqul", lname="islam")
e.print_email()

try:
    lg().error('in try block')
except LoggerError as ex:
    print(ex)
