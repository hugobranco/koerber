import os
import logging


class CfgReader():

    APPLICATION_BASIC_LOG_LEVEL = os.environ.get('APPLICATION_BASIC_LOG_LEVEL') \
        if 'APPLICATION_BASIC_LOG_LEVEL' in os.environ else logging.DEBUG

    STACKING_LAYERS_METRICS_SERVICE_URL = os.environ.get('STACKING_LAYERS_METRICS_SERVICE_URL') \
        if 'STACKING_LAYERS_METRICS_SERVICE_URL' in os.environ else 'http://localhost:8000/machines_metrics/input/save'

    MACHINE_DATA_TIME_SCHEDULER_SECONDS = os.environ.get('MACHINE_DATA_TIME_SCHEDULER_SECONDS') \
        if 'MACHINE_DATA_TIME_SCHEDULER_SECONDS' in os.environ else 5

    DATABASE_HOST_URL = os.environ.get('DATABASE_HOST_URL') if 'DATABASE_HOST_URL' in os.environ else 'localhost:3307'
    DATABASE_USER = os.environ.get('DATABASE_USER') if 'DATABASE_USER' in os.environ else 'user'
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') if 'DATABASE_PASSWORD' in os.environ else 'password'
    DATABASE_NAME = os.environ.get('DATABASE_NAME') if 'DATABASE_NAME' in os.environ else 'db'
