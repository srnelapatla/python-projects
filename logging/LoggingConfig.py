# this is copied from internet
import logging.config

"""
MY_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default_formatter': {
            'format': '[%(levelname)s:%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
    },
    'loggers': {
        'mylogger': {
            'handlers': ['stream_handler'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

logging.config.dictConfig(MY_LOGGING_CONFIG)
logger = logging.getLogger('C:\\000_Development\\pythonFiles\\myPythonlogger')
logger.info('info log')

"""

# Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="C:\\000_Development\\pythonFiles\\myPythonlogger.log",
                    filemode="w",
                    format=Log_Format,
                    level=logging.ERROR)

logger = logging.getLogger()

# Testing our Logger

#logger.error("Our First Log Message")
