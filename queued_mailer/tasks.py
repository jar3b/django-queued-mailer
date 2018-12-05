from time import sleep

import celery
from celery.utils.log import get_task_logger

from .settings import TASK_QUEUE_NAME

logger = get_task_logger(__name__)


@celery.task(bind=True, queue=TASK_QUEUE_NAME, acks_late=True, default_retry_delay=30)
def send_message(self, email):
    logger.info('task started')
    try:
        sleep(5)
        logger.info('task success')
    except Exception as e:
        logger.info('task error')
        raise self.retry(exc=e)
