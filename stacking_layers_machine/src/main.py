from utils.base_exception_handler import BaseExceptionHandler

from utils.cfg_reader import CfgReader
from utils.custom_logger import CustomLogger
from utils.app_scheduler import AppScheduler
from libs.database.database_creation import DatabaseCreation



class Main():

    def __init__(self):
        self.logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)
        self.logger.info(message='### APPLICATION START ###')

        # debug all environment variables
        self.logger.info(
            message=f"APPLICATION_BASIC_LOG_LEVEL = {CfgReader.APPLICATION_BASIC_LOG_LEVEL}"
        )
        self.logger.info(
            message=f"STACKING_LAYERS_METRICS_SERVICE_URL = {CfgReader.STACKING_LAYERS_METRICS_SERVICE_URL}"
        )
        self.logger.info(message=f"DATABASE_HOST_URL = {CfgReader.DATABASE_HOST_URL}")
        self.logger.info(message=f"DATABASE_USER = {CfgReader.DATABASE_USER}")
        self.logger.info(message=f"DATABASE_PASSWORD = {CfgReader.DATABASE_PASSWORD}")
        self.logger.info(message=f"DATABASE_NAME = {CfgReader.DATABASE_NAME}")



    def init_database(self):
        """
            create database and tables in mysql
        """
        try:
            DatabaseCreation.create_database()
        except BaseExceptionHandler as base_exception_handler:
            self.logger.error(message=base_exception_handler.error_message)



    def start_app_scheduler(self):
        """
            start app scheduler
        """
        try:
            self.logger.info(message='Add jobs to scheduler')
            AppScheduler.add_jobs()
            self.logger.info(message='Scheduler just started... tic tac, tic tac ....')
            AppScheduler.start_scheduler()
        except BaseExceptionHandler as base_exception_handler:
            self.logger.error(message=base_exception_handler.error_message)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main = Main()
    main.init_database()
    main.start_app_scheduler()

