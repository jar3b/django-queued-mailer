# coding: utf-8
from django.core.mail.backends.base import BaseEmailBackend
from django.utils.encoding import force_text

from .logger import logger
from .tasks import send_message
from .utils import get_email_connection


def _get_message_recipients(email_message):
    message_recipients = getattr(email_message, 'to', None)
    if not isinstance(message_recipients, list):
        return 'unknown'
    return ', '.join(map(force_text, message_recipients))


class EmailBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super(EmailBackend, self).__init__(fail_silently, **kwargs)

    def send_messages(self, email_messages):
        num_sent = 0
        connection = get_email_connection()

        for email in email_messages:
            try:
                send_message.apply_async([email, connection])
                num_sent += 1
            except Exception as e:
                logger.error("cannot send message %s: %r" % (_get_message_recipients(email), e))

        return num_sent
