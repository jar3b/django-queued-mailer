from celery.task import task

from .logger import logger
from .settings import EMAIL_BACKEND


@task
def send_message(email):
    logger.info('TASK CALLED')
    logger.info(EMAIL_BACKEND)
    logger.info(email)
