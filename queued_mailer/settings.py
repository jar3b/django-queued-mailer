from django.conf import settings

EMAIL_BACKEND = getattr(
    settings,
    "QMAILER_EMAIL_BACKEND",
    "django.core.mail.backends.smtp.EmailBackend"
)

EMAIL_SEND_TASK = getattr(
    settings,
    "QMAILER_SEND_TASK",
    "queued_mailer.tasks.send_message"
)
