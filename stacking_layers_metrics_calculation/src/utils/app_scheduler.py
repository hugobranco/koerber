from apscheduler.schedulers.background import BackgroundScheduler

from libs.schedule_jobs import ScheduleJobs
from utils.cfg_reader import CfgReader
from utils.custom_logger import CustomLogger
from utils.base_exception_handler import BaseExceptionHandler


class AppScheduler():

    app_scheduler = BackgroundScheduler(daemon=True, timezone="Europe/Lisbon")
    logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)


    @classmethod
    def start_scheduler(cls):
        """
            starts app scheduler service
        """
        try:
            cls.logger.info(message="start app scheduler service")
            if (not cls.app_scheduler.state):
                cls.app_scheduler.start()
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    @classmethod
    def add_jobs(cls):
        """
            add functions to scheduler
        """
        cls.app_scheduler.add_job(
            ScheduleJobs.update_app_heath,
            'interval',
            seconds=int(CfgReader.CHECK_APP_HEATH_TIME_SCHEDULER_SECONDS),
            id='update_app_health'
        )



    @classmethod
    def remove_jobs(cls):
        """
            remove jobs functions from scheduler
        """
        cls.app_scheduler.remove_job(job_id='update_app_health')
