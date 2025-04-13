from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO")  # Console logging
logger.add("logs/api.log", rotation="500 KB", level="DEBUG")  # File logging
