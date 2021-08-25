import requests

from utils.custom_logger import CustomLogger
from utils.cfg_reader import CfgReader

from utils.base_exception_handler import BaseExceptionHandler
from libs.machine_data import MachineData


class ScheduleJobs():

    logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)


    @staticmethod
    def send_machine_data():
        """
            send dictionary with machine data to service that save and calculate machine metrics
        """
        try:
            ScheduleJobs.logger.debug(message="Run schedule job!!")

            # get machine data from function generate random machine data
            machine_data = MachineData.get_random_machine_data()

            # send machine data dictionary to machine metrics service. Only send machine data if not None
            if(machine_data):
                ScheduleJobs.logger.debug(message=str(machine_data))
                requests.post(CfgReader.STACKING_LAYERS_METRICS_SERVICE_URL,
                              json=machine_data,
                              headers={'Content-Type': 'application/json'})
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))
