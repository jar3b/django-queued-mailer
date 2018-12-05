from django.core.mail.backends.base import BaseEmailBackend
from django.utils.encoding import force_text
from django.utils.module_loading import import_string

from .logger import logger
from .settings import EMAIL_SEND_TASK


def _get_message_recipients(email_message):
    message_recipients = getattr(email_message, 'to', None)
    if not isinstance(message_recipients, list):
        return 'unknown'
    return ', '.join(map(force_text, message_recipients))


class EmailBackend(BaseEmailBackend):
    task = None

    def __init__(self, fail_silently=False, **kwargs):
        super(EmailBackend, self).__init__(fail_silently, **kwargs)
        self.task = import_string(EMAIL_SEND_TASK)

    def send_messages(self, email_messages):
        num_sent = 0
        for email in email_messages:
            try:
                self.task.apply_async([email, ])
                num_sent += 1
            except Exception as e:
                logger.error("cannot send message %s: %r" % (_get_message_recipients(email), e))

        return num_sent
