from . import logger
from .settings import EMAIL_BACKEND


def send_message():
    logger.info(EMAIL_BACKEND)
    logger.info('sent')
