# bikespace_api/bikespace_api/tests/test_config.py

import os
import unittest

from flask import current_app
from flask_testing import TestCase

from bikespace_api import create_app

app = create_app()


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("bikespace_api.config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config["SECRET_KEY"] == "my_precious")
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("bikespace_api.config.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config["SECRET_KEY"] == "my_precious")
        self.assertTrue(app.config["TESTING"])
        self.assertFalse(app.config["PRESERVE_CONTEXT_ON_EXCEPTION"])
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_TEST_URL")
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object("bikespace_api.config.ProductionConfig")
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config["SECRET_KEY"] == "my_precious")
        self.assertFalse(app.config["TESTING"])


if __name__ == "__main__":
    unittest.main()
