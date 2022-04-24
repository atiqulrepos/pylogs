import logging
import os.path
import os.path as path

# sys.path.append(path.abspath(__file__))

from src.utils import LoggerManager, LoggerError, log as lg
from src.classes import Employee

# https://stackoverflow.com/questions/61141419/in-python-i-can-write-a-log-to-console-but-its-not-getting-written-into-file
# print(str(logger.handlers).split(","))
script_path = path.join(path.dirname(path.abspath(__file__)))
logdir = path.join(script_path, "..", "logs")

if not os.path.exists(logdir):
    os.makedirs(logdir)
logfile = path.join(logdir, "test.log")
if path.exists(logfile):
    os.remove(logfile)
log2 = LoggerManager.getlogger(name="junk", logfile=logfile, file_level=logging.INFO, stream_level=logging.INFO)
log2.critical("critical")
log2.error("error")
log2.warning("warning")
log2.info("info")
log2.debug("debug")

e = Employee(fname="atiqul", lname="islam")
e.print_email()


log3 = LoggerManager.getlogger(name="junk", logfile=logfile, file_level=logging.INFO, stream_level=logging.INFO)
log3.critical("log3-critical")
log3.error("log3-error")
log3.warning("log3-warning")
log3.info("log3-info")
log3.debug("log3-debug")

try:
    lg().error('in try block')
except LoggerError as ex:
    print(ex)
