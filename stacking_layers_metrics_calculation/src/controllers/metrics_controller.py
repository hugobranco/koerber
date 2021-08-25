from typing import Optional
from fastapi import Response, status
from datetime import datetime

from controllers.master_controller import MasterController
from libs.enums.machine_input_status import MachineInputStatus
from libs.enums.metrics_types import MetricsTypes
from libs.global_objects import GlobalObjects
from utils.app_scheduler import AppScheduler

from utils.date_utils import DateUtils
from utils.base_exception_handler import BaseExceptionHandler

from dao.machine_input_metrics_dao import MachineInputMetricsDao
from dao.machine_input_dao import MachineInputDao
from libs.metrics.build_metrics import BuildMetrics




class MetricsController(MasterController):

    @staticmethod
    @MasterController.web_server.get(f"/machines_metrics/stacking/data",
                                     name="Return Machines Stacking Metrics Data /minute",
                                     description="Return machines stacking metrics, per minute. Machines speed and rate")
    def data(response: Response, date_ini: str, date_end: str, provided_metrics: Optional[str] = MetricsTypes.All.name):
        """
            return speed and rate machines metrics data between date_ini and date_end. Return a json with metrics data.

            :param response:
                http response object
            :param date_ini:
                start date to query metrics data
            :param date_end:
                end date to query metrics data
            :param provided_metrics:
                type of metrics desired

            :return:
                return json with metrics data
        """
        try:
            # validate params
            # validate date_ini and date_end params
            datetime_ini = DateUtils.datetime_string_to_datetime_obj(
                datetime_string=date_ini, datetime_format='%Y-%m-%dT%H:%M:%S'
            )
            datetime_end = DateUtils.datetime_string_to_datetime_obj(
                datetime_string=date_end, datetime_format='%Y-%m-%dT%H:%M:%S'
            )

            # validate provided_metrics param
            if(provided_metrics not in [obj.value for obj in MetricsTypes]):
                return MetricsController.return_request_error(
                    error_message=f"Param 'provided_metrics' must have one of this values: "
                                  f"{', '.join([obj.value for obj in MetricsTypes])}",
                    http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    response=response
                )

            method_to_call = getattr(BuildMetrics, f"build_{provided_metrics.lower()}_metrics_by_dates")
            return method_to_call(
                ini_timestamp=int(datetime.timestamp(datetime_ini)),
                end_timestamp=int(datetime.timestamp(datetime_end))
            )
        except BaseExceptionHandler as ex:
            MetricsController.logger.error(message=ex.error_message)
            return MetricsController.return_request_error(
                error_message=ex.error_message, http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                response=response
            )
        except Exception as ex:
            MetricsController.logger.error(message=str(ex))
            return MetricsController.return_request_error(
                error_message=str(ex), http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,response=response
            )



    @staticmethod
    @MasterController.web_server.post(f"/machines_metrics/input/save", name="Save Machine Data Input",
                                      description="Save in database machine input data")
    def save(response: Response, machine_input: dict):
        """
            receive machine data to save in database

            :param response:
                http response object
            :param machine_input:
                dictionary with machine data
        """
        try:
            # restart schedule job to update App heath. The machine data was received so have to restart schedule job
            AppScheduler.remove_jobs()
            AppScheduler.add_jobs()

            # update global variable machine_input_messages_health to Green
            GlobalObjects.machine_input_messages_health = MachineInputStatus.Green.value

            # validate machine input. Machine input must have this structure:
            #   {“seqnum”: 1, "machineId": 1,"timestamp": 1615215673,"pickedLayers": 4}
            if(not all(key in machine_input for key in ("seqnum", "machineId", "timestamp", "pickedLayers"))):
                return MetricsController.return_request_error(
                    error_message="Machine input must have this values: 'seqnum', 'machineId', 'timestamp', "
                                  "'pickedLayers'",
                    http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    response=response
                )

            # save machine input in database
            machine_input_dao = MachineInputDao()
            machine_input_obj = machine_input_dao.save_machine_input(machine_input=machine_input)

            # calculate metrics and save them in database
            machine_input_metrics_dao = MachineInputMetricsDao()
            machine_input_metrics_dao.calculate_metrics_and_save(machine_input=machine_input_obj)

            return {'machines_input_status': 'Green'}
        except BaseExceptionHandler as ex:
            MetricsController.logger.error(message=ex.error_message)
            return MetricsController.return_request_error(
                error_message=ex.error_message, http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                response=response
            )
        except Exception as ex:
            MetricsController.logger.error(message=str(ex))
            return MetricsController.return_request_error(
                error_message=str(ex), http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,response=response
            )
