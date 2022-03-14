import logging
import LoggingConfig  # this will import the logger file setup to the current module

# Get the logger specified in the file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def add(a, b):
    logger.info("called add method")
    try:
        result = a + b
    except TypeError:
        logger.exception("TypeError occurred")
    else:
        return result


logging.warning('Watch out!, you are passing non-numberic to airthmetic operation')
c = add(10, 'Santosh')
