import logging
from logging.config import dictConfig
from log_config import log_config # this is your local file

dictConfig(log_config)
logger = logging.getLogger("my-project-logger") # should be this name unless you change it in log_config.py