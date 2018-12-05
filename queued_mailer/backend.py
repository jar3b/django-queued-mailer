from django.core.mail.backends.base import BaseEmailBackend
from django.utils.module_loading import import_string

from . import logger
from .settings import EMAIL_SEND_TASK


class EmailBackend(BaseEmailBackend):
    task = None

    def __init__(self, fail_silently=False, **kwargs):
        super(EmailBackend, self).__init__(fail_silently, **kwargs)
        self.task = import_string(EMAIL_SEND_TASK)

    def send_messages(self, email_messages):
        num_sent = 0
        for email in email_messages:
            logger.info(email)
            logger.info(self.task)
            num_sent += 1
        return num_sent
