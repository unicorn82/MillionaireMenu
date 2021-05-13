import logging
import logging.config
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from os import path

class logHelper:
    def __init__(self, module):
        log_file_path = path.join(path.dirname(path.abspath(__file__)), '../conf/logging.conf')
        logging.config.fileConfig(log_file_path)

        timeRotateHandle = TimedRotatingFileHandler("logs/scarpy.log", when='d', interval=1, backupCount=5)
        self.timeRotateLogger = logging.getLogger(module)
        self.timeRotateLogger.setLevel(logging.INFO)
        self.timeRotateLogger.addHandler(timeRotateHandle)

    def info(self, msg):
        print("logger info ", msg)
        self.timeRotateLogger.info(msg)



    def debug(self, msg):
        self.timeRotateLogger.debug(msg)

    def error(self, msg):
        self.timeRotateLogger.error(msg)



