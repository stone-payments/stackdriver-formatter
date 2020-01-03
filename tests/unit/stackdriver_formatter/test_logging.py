import os
import sys
import unittest
from unittest import TestCase

from stackdriver_formatter import logging as custom_logging
from stackdriver_formatter import exceptions

class TestStackDriverJsonFormat(TestCase):
    def test_get_logger_with_critical_log_level(self):
        os.environ['LOG_LEVEL'] = "CRITICAL"
        try:
            LOGGER = custom_logging.getLogger(__name__)
        except exceptions.CouldNotSetLogLevel:
            assert False, "exceptions.CouldNotSetLogLevel()"
        except exceptions.CouldNotSetStreamHandler:
            assert False, "exceptions.CouldNotSetStreamHandler()"

        self.assertEqual(LOGGER.level, custom_logging.logging.CRITICAL)
        LOGGER.critical("CRITICAL MESSAGE")


    def test_get_logger_with_error_log_level(self):
        os.environ['LOG_LEVEL'] = "ERROR"
        try:
            LOGGER = custom_logging.getLogger(__name__)
        except exceptions.CouldNotSetLogLevel:
            assert False, "exceptions.CouldNotSetLogLevel()"
        except exceptions.CouldNotSetStreamHandler:
            assert False, "exceptions.CouldNotSetStreamHandler()"

        self.assertEqual(LOGGER.level, custom_logging.logging.ERROR)


    def test_get_logger_with_warning_log_level(self):
        os.environ['LOG_LEVEL'] = "WARNING"
        try:
            LOGGER = custom_logging.getLogger(__name__)
        except exceptions.CouldNotSetLogLevel:
            assert False, "exceptions.CouldNotSetLogLevel()"
        except exceptions.CouldNotSetStreamHandler:
            assert False, "exceptions.CouldNotSetStreamHandler()"

        self.assertEqual(LOGGER.level, custom_logging.logging.WARNING)

    def test_get_logger_with_info_log_level(self):
        os.environ['LOG_LEVEL'] = "INFO"
        try:
            LOGGER = custom_logging.getLogger(__name__)
        except exceptions.CouldNotSetLogLevel:
            assert False, "exceptions.CouldNotSetLogLevel()"
        except exceptions.CouldNotSetStreamHandler:
            assert False, "exceptions.CouldNotSetStreamHandler()"

        self.assertEqual(LOGGER.level, custom_logging.logging.INFO)

    def test_get_logger_with_debug_log_level(self):
        os.environ['LOG_LEVEL'] = "DEBUG"
        try:
            LOGGER = custom_logging.getLogger(__name__)
        except exceptions.CouldNotSetLogLevel:
            assert False, "exceptions.CouldNotSetLogLevel()"
        except exceptions.CouldNotSetStreamHandler:
            assert False, "exceptions.CouldNotSetStreamHandler()"

        self.assertEqual(LOGGER.level, custom_logging.logging.DEBUG)

if __name__ == '__main__':
    unittest.main()