from django.core.mail import get_connection

from .settings import EMAIL_BACKEND


def get_email_connection():
    return get_connection(backend=EMAIL_BACKEND)
