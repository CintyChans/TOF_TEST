
import json
from datetime import datetime
import os
import logging

_logfile = "log"
_logger = "mylog"

class log_file:
    def __init__(self, file_tag="log"):
        os.makedirs(_logfile, exist_ok=True)
        self.logger = logging.getLogger(_logger)
        self.file_name = (
            f"{_logfile}/{file_tag}_{datetime.now().strftime('%Y%m%d')}.log"
        )
        self.file_handle = logging.FileHandler(self.file_name)
        self.formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
        self.file_handle.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handle)
        self.logger.setLevel(logging.DEBUG)

    def error(self, message):
        self.logger.error(message)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def close(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)


log = log_file()
# 读取配置文件
try:
    with open("default.json", "r") as file:
        # 加载 JSON 数据
        default_data = json.load(file)
except FileNotFoundError:
    log.error(f"File not found.")
except json.JSONDecodeError:
    log.error(f"Error decoding JSON in file '.")

_header = "57"
_frame_header = "57"
_data_length = 16 - 1
_function_mark = "00"
_baudrate = "921600"
_title = "TOF_TEST"
_padx = 5
_pady = 5
_width = 10
_sticky = "we"
