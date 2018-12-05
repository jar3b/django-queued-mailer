import logging

from .settings import EMAIL_BACKEND


def send_message():
    logging.info(EMAIL_BACKEND)
    logging.info('sent')
