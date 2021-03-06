# coding: utf-8
import smtplib
import ssl
import time
from socket import error as socket_error

import celery
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage

from queued_mailer.utils import get_email_connection
from .exceptions import EmailTransportException
from .settings import TASK_QUEUE_NAME

logger = get_task_logger(__name__)


class PersitentEmailConnectionTask(celery.Task):
    _connection = None

    @property
    def connection(self):
        if self._connection is None:
            self._connection = get_email_connection()

        return self._connection

    def clean_connection(self):
        self._connection = None


@celery.task(bind=True, base=PersitentEmailConnectionTask, queue=TASK_QUEUE_NAME, acks_late=True,
             default_retry_delay=20, autoretry_for=(EmailTransportException,), retry_kwargs={'max_retries': 5})
def send_message(self, email):
    logger.debug('task started')

    start_time = time.time()

    if not isinstance(email, EmailMessage):
        raise Exception('Invalid message class, only django.core.mail.EmailMessage is supported')

    try:
        email.connection = self.connection
        email.send()
    except (ssl.SSLError, smtplib.SMTPServerDisconnected) as e:
        # nullify connection
        self.clean_connection()
        raise self.retry(e, countdown=1)
    except (socket_error, smtplib.SMTPSenderRefused,
            smtplib.SMTPRecipientsRefused,
            smtplib.SMTPDataError,
            smtplib.SMTPAuthenticationError) as e:
        logger.warning('message transport failure: %r' % e)
        raise EmailTransportException(e)
    except Exception as e:
        logger.error('message send error: %r' % e)
        raise

    elapsed_time = time.time() - start_time
    logger.warning("message sent, elapsed time %s" % elapsed_time)
