from utils.base_exception_handler import BaseExceptionHandler
from libs.database.database import Database

from models.machine_input_metrics import MachineInputMetrics
from models.machine_input import MachineInput
from utils.cfg_reader import CfgReader
from utils.custom_logger import CustomLogger


class DatabaseCreation(Database):

    logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)


    @classmethod
    def create_database(cls):
        """
            Create database amd database tables in database if not exists
        """
        try:
            cls.logger.info('Create database')
            Database.base.metadata.create_all(cls.engine, checkfirst=True)
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    @classmethod
    def create_tables(cls):
        """
            Create database tables
        """
        try:
            cls.logger.info('Create tables')
            MachineInput.__table__.create(bind=Database.engine, checkfirst=True)
            MachineInputMetrics.__table__.create(bind=Database.engine, checkfirst=True)
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))

