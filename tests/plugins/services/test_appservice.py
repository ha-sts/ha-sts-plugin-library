#!/usr/bin/env python3

# Disabling the "abstract-class-instantiated" as this specifically tests the abstract class
# pylint: disable=E0110

### IMPORTS ###
import logging
import unittest

from unittest.mock import patch

from hasts.plugins.services import AppService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestAppService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    @patch.multiple(AppService, __abstractmethods__ = set())
    def test_get_app(self):
        self.logger.debug("test_get_app")
        tmp_as = AppService()
        # This is for an "abstract" class, so this should raise a NotImplementedError
        with self.assertRaises(NotImplementedError):
            tmp_as.get_app()
