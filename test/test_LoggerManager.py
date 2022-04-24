import os
import os.path as path
import sys
import unittest
import uuid

script_dir = path.dirname(path.realpath(__file__))

sys.path.append(path.join(script_dir,".."))
from src.utils import LoggerManager


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        env = os.environ
        filename = uuid.uuid4().hex + ".log"
        self.logfile = path.join( (env['TEMP'] if sys.platform == "win32" else "/tmp" ), filename)
        self.logger = LoggerManager.getlogger(name="test", logfile=self.logfile)
        self.logger2 = LoggerManager.getlogger(name="junk")

    def test_logfile_creation(self):
        self.assertTrue(path.exists(self.logfile))

    def test_singleton_logger(self):
        self.assertEqual(self.logger, self.logger2)  # add assertion here

    def test_singleton_logger_by_id(self):
        self.assertEqual(id(self.logger), id(self.logger2))  # add assertion here

    def test_logname(self):
        self.assertEqual("test", self.logger.get_name())

if __name__ == '__main__':
    unittest.main()
