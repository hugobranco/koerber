from controllers.master_controller import MasterController
from controllers.status_controller import StatusController
from controllers.metrics_controller import MetricsController

from utils.custom_logger import CustomLogger
from utils.cfg_reader import CfgReader
from utils.base_exception_handler import BaseExceptionHandler
from libs.global_objects import GlobalObjects
from libs.database.database_creation import DatabaseCreation

from utils.web_server import WebServer
from utils.app_scheduler import AppScheduler



class Main():

    def __init__(self):
        self.logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)
        self.logger.info(message='### APPLICATION START ###')

        # debug all environment variables
        self.logger.info(
            message=f"APPLICATION_BASIC_LOG_LEVEL = {CfgReader.APPLICATION_BASIC_LOG_LEVEL}"
        )
        self.logger.info(
            message=f"CHECK_APP_HEATH_TIME_SCHEDULER_SECONDS = {CfgReader.CHECK_APP_HEATH_TIME_SCHEDULER_SECONDS}"
        )
        self.logger.info(message=f"DATABASE_HOST_URL = {CfgReader.DATABASE_HOST_URL}")
        self.logger.info(message=f"DATABASE_USER = {CfgReader.DATABASE_USER}")
        self.logger.info(message=f"DATABASE_PASSWORD = {CfgReader.DATABASE_PASSWORD}")
        self.logger.info(message=f"DATABASE_NAME = {CfgReader.DATABASE_NAME}")

        # Start GlobalObjects
        GlobalObjects.init_global_objects()



    def init_database(self):
        """
            create database and database tables
        """
        try:
            DatabaseCreation.create_database()
        except BaseExceptionHandler as base_exception_handler:
            self.logger.error(message=base_exception_handler.error_message)



    def start_app_scheduler(self):
        """
            start app Scheduler
        """
        try:
            self.logger.info(message='Add jobs to scheduler')
            AppScheduler.add_jobs()
            self.logger.info(message='Scheduler just started... tic tac, tic tac ....')
            AppScheduler.start_scheduler()
        except BaseExceptionHandler as base_exception_handler:
            self.logger.error(message=base_exception_handler.error_message)



    def start_web_server(self):
        """
            start FastApi web server
        """
        try:
            WebServer.start_web_server()
        except BaseExceptionHandler as base_exception_handler:
            self.logger.error(message=base_exception_handler.error_message)



if __name__ == '__main__':
    main = Main()
    main.init_database()
    main.start_app_scheduler()
    main.start_web_server()

