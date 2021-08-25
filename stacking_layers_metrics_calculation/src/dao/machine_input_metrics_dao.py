from libs.database.database_connection import DatabaseConnection
from models.machine_input import MachineInput
from models.machine_input_metrics import MachineInputMetrics
from utils.base_exception_handler import BaseExceptionHandler
from dao.machine_input_dao import MachineInputDao


class MachineInputMetricsDao():

    def __init__(self):
        try:
            self.model = MachineInputMetrics
            self.database_session = DatabaseConnection.create_session()
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    def calculate_metrics_and_save(self, machine_input: MachineInput):
        """
            calculate machine input speed and rate per minute and save in database

            :param machine_input:
                MachineInput class instance with machine input data to calculate speed and rate per minute
        """
        try:
            # first calculate machine speed stacking per minute. This is the instantaneous speed
            speed_layers_stacking_minute = machine_input.picked_layers * 12

            # sum picked layers in the last minute to calculate the rate
            machine_input_dao = MachineInputDao()
            sum_layers_last_minute = machine_input_dao.sum_picked_layers_last_minute(machine_input.timestamp)

            rate_layers_stacking_minute = sum_layers_last_minute * 100 / speed_layers_stacking_minute

            machine_input_metrics = MachineInputMetrics(
                machine_id=machine_input.machine_id,
                picked_layers=machine_input.picked_layers,
                speed_layers_stacking_minute=speed_layers_stacking_minute,
                sum_layers_last_minute=sum_layers_last_minute,
                rate_layers_stacking_minute=rate_layers_stacking_minute,
                timestamp=machine_input.timestamp
            )

            # save machine_input_obj in database
            self.database_session.add(machine_input_metrics)
            self.database_session.commit()
            self.database_session.expunge_all()
            self.database_session.close()
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    def get_metrics_by_date(self, ini_timestamp: int, end_timestamp: int) -> list:
        """
            get the metrics between dates

            :param ini_timestamp:
                get metrics with timestamp >= to this param
            :param end_timestamp:
                get metrics with timestamp <= to this param

            :return:
                return list with metrics to all machines between ini_timestamp and end_timestamp
        """
        try:
            # get all registers between ini_timestamp and end_timestamp
            return self.database_session.query(self.model).\
                filter(self.model.timestamp >= ini_timestamp,
                       self.model.timestamp <= end_timestamp).\
                order_by(self.model.timestamp.asc()).all()
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))
