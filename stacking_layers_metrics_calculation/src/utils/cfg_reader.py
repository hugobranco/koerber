import os
import logging


class CfgReader():

    APPLICATION_BASIC_LOG_LEVEL = os.environ.get('APPLICATION_BASIC_LOG_LEVEL') \
        if 'APPLICATION_BASIC_LOG_LEVEL' in os.environ else logging.DEBUG

    CHECK_APP_HEATH_TIME_SCHEDULER_SECONDS = os.environ.get('CHECK_APP_HEATH_TIME_SCHEDULER_SECONDS') \
        if 'CHECK_APP_HEATH_TIME_SCHEDULER_SECONDS' in os.environ else 6

    DATABASE_HOST_URL = os.environ.get('DATABASE_HOST_URL') if 'DATABASE_HOST_URL' in os.environ else 'localhost:3307'
    DATABASE_USER = os.environ.get('DATABASE_USER') if 'DATABASE_USER' in os.environ else 'user'
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') if 'DATABASE_PASSWORD' in os.environ else 'password'
    DATABASE_NAME = os.environ.get('DATABASE_NAME') if 'DATABASE_NAME' in os.environ else 'db'

