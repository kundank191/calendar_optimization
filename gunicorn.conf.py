import logging
import multiprocessing
import os
from logging.handlers import TimedRotatingFileHandler

bind = ":8080"
timeout = 500
workers = multiprocessing.cpu_count()
threads = 2
errorlog = os.path.dirname(__file__) + "/logs/errorlog.log"
accesslog = os.path.dirname(__file__) + "/logs/accesslog.log"
errorlog_handler = TimedRotatingFileHandler(errorlog, when='D', interval=1, backupCount=7)

logging.basicConfig(handlers=[errorlog_handler])
logging.getLogger().setLevel(logging.INFO)
capture_output = True