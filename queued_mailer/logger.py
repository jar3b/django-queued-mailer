# coding: utf-8

import logging
import sys

logger = logging.getLogger(__name__)
hdlr = logging.StreamHandler(sys.stderr)
formatter = logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
