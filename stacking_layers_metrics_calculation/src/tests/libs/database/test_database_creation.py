import unittest

from libs.database.database_creation import DatabaseCreation
from utils.base_exception_handler import BaseExceptionHandler


class TestDatabaseCreation(unittest.TestCase):

    def test_create_database(self):
        try:
            DatabaseCreation.create_database()
        except BaseExceptionHandler:
            self.fail("DatabaseCreation.create_database() raised BaseExceptionHandler unexpectedly!")



    def test_create_models_tables(self):
        try:
            DatabaseCreation.create_models_tables()
        except BaseExceptionHandler:
            self.fail("DatabaseCreation.create_models_tables() raised BaseExceptionHandler unexpectedly!")
