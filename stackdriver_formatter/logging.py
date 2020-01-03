"""app.logging

Module that contains the default application logger configuration.
"""
import logging
import sys
import os

from .exceptions import CouldNotSetLogLevel, CouldNotSetStreamHandler
from .formatters import StackDriverJsonFormatter

# in order to make it equal to python default loggin
# pylint: disable=C0103
def getLogger(name):
    """Retrieves a logger configured for the application."""

    logger = logging.getLogger(name)
    try:
        logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))
    except Exception as error:
        raise CouldNotSetLogLevel(error)
    try:
        stream_handler = logging.StreamHandler(sys.stdout)
        formatter = StackDriverJsonFormatter()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    except Exception as error:
        raise CouldNotSetStreamHandler(error)
    return logger
