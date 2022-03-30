#!/usr/bin/env python3

# Disable some rules in pylint because they're not valid for this file:
#  - R0903 (too-few-public-methods)
# pylint: disable=R0903

### IMPORTS ###
import logging
import unittest

from hasts.plugins.services import FlaskAppService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class MockFlaskApp:
    pass

class TestFlaskAppService(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_get_app(self):
        self.logger.debug("test_get_app")
        tmp_as = FlaskAppService(MockFlaskApp())
        self.assertIsInstance(tmp_as.get_app(), MockFlaskApp)
