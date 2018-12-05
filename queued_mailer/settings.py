# coding: utf-8

from django.conf import settings

EMAIL_BACKEND = getattr(
    settings,
    "QMAILER_EMAIL_BACKEND",
    "django.core.mail.backends.smtp.EmailBackend"
)

TASK_QUEUE_NAME = getattr(
    settings,
    "QMAILER_TASK_QUEUE_NAME",
    "default"
)
