"""module containing the logger"""
import logging
from datetime import datetime

logger = logging.getLogger("to_do_list_logger")
logger.setLevel(logging.DEBUG)

now = datetime.now()
formatted_time = now.strftime("%Y_%m_%d_%H_%M_%S_%f")
log_file_path = f"logs/{formatted_time}.log"

file_handler = logging.FileHandler(log_file_path)
file_formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_formatter = logging.Formatter("%(message)s")
stream_handler.setFormatter(stream_formatter)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)
