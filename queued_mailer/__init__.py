import logging
import sys

from django.utils.module_loading import import_string

logger = logging.getLogger(__name__)
hdlr = logging.StreamHandler(sys.stderr)
formatter = logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

# celery app
celery_app = import_string('project.celery_app.app')
