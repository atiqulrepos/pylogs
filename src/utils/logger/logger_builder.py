import logging


class LoggerBuilder(logging.Logger):
    def __init__(self, name=None, logfile=None, file_level=logging.INFO, stream_level=logging.WARNING):
        super(LoggerBuilder, self).__init__(name)
        # super().__init__(self, name)
        self.levels = {
            'file_level': file_level,
            'stream_level': stream_level
        }
        self.add_stream()
        if logfile:
            self.logfile = logfile
            self.add_file()

    def get_logfile(self):
        return self.logfile

    def get_name(self):
        return self.name

    def add_stream(self):
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter('[%(asctime)s-%(name)s-%(filename)s-%(levelname)s]: %(message)s',
                                          datefmt="%Y%m%d %H:%M:%S"))
        sh.setLevel(self.levels['stream_level'])
        logging.Logger.addHandler(self, sh)

    def add_file(self):
        fh = logging.FileHandler(self.logfile)
        fh.setLevel(self.levels['file_level'])
        fh.setFormatter(logging.Formatter('[%(asctime)s-%(name)s-%(filename)s-%(funcName)s-%(levelname)s]: %(message)s',
                                          datefmt="%Y%m%d %H:%M:%S"))
        logging.Logger.addHandler(self, fh)
