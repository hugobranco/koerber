from datetime import timedelta, datetime
from sqlalchemy import func

from libs.database.database_connection import DatabaseConnection
from utils.base_exception_handler import BaseExceptionHandler
from utils.date_utils import DateUtils
from models.machine_input import MachineInput



class MachineInputDao():

    def __init__(self):
        try:
            self.model = MachineInput
            self.database_session = DatabaseConnection.create_session()
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    def get_all(self) -> list:
        """
            get all registers from machine_inputs table

            :return:
                return a list of MachineInput instances objects
        """
        try:
            return self.database_session.query(self.model).all() or []
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    def save_machine_input(self, machine_input: dict) -> MachineInput:
        """
            save machine input data in machine_inputs database table
        """
        try:
            machine_input_obj = MachineInput(
                seqnum=machine_input['seqnum'],
                machine_id=machine_input['machineId'],
                picked_layers=machine_input['pickedLayers'],
                timestamp=machine_input['timestamp']
            )

            # save machine_input_obj in database
            self.database_session.add(machine_input_obj)
            self.database_session.commit()
            self.database_session.expunge_all()
            self.database_session.close()

            return machine_input_obj
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))


    def sum_picked_layers_last_minute(self, timestamp: int) -> int:
        """
            sum the picked layers in the last minute

            :param timestamp:
                remove 1 min to this timestamp and get the layers between this values

            :return:
                return the number of picked layers un tha last minute
        """
        try:
            # cast timestamp to datetime instance
            timestamp_datetime = datetime.fromtimestamp(timestamp)

            # remove 1 minute to the timestamp
            ini_timestamp_datetime = timestamp_datetime - timedelta(minutes=1)

            # cast to timestamp the ini_timestamp_datetime
            ini_timestamp = datetime.timestamp(ini_timestamp_datetime)

            # get the last minute picked layers
            picked_layers = self.database_session.query(func.sum(self.model.picked_layers)).\
                filter(self.model.timestamp >= ini_timestamp, self.model.timestamp <= timestamp).first()

            return int(picked_layers[0])
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))
