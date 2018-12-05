from . import logger, celery_app as app
from .settings import EMAIL_BACKEND


@app.task()
def send_message(email):
    logger.info(EMAIL_BACKEND)
    logger.info(email)
