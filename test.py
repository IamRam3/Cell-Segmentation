from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys

logging.info("Welcome to the custom log and Exception")

try:
    a = 4/"1"

except Exception as e:
    raise AppException(e, sys)