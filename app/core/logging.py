import logging
import os
from logging.handlers import RotatingFileHandler
from app.core.config import settings

LOG_DIR = settings.LOG_DIR
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "logs.log")

LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s]  %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

file_handler = RotatingFileHandler(
    LOG_FILE_PATH, maxBytes=10_000_000, backupCount=5, encoding="utf-8"
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.info(f"Logging initialized. Writing logs to: {LOG_FILE_PATH}")
