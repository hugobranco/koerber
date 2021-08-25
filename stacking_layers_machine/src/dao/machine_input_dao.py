from libs.database.database import Database
from libs.database.database_creation import DatabaseCreation
from utils.base_exception_handler import BaseExceptionHandler
from models.machine_input import MachineInput
from sqlalchemy import func



class MachineInputDao():

    def __init__(self):
        try:
            self.model = MachineInput
            self.database_session = Database.create_session()
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



    def get_one_record(self) -> MachineInput:
        """
            get only one record just to check database connection

            :return:
                return a MachineInput class instance
        """
        try:
            return self.database_session.query(self.model).first() or MachineInput()
        except Exception as ex:
            Database.create_connection()
            DatabaseCreation.create_database()
            self.database_session.rollback()
            return None



    def get_max_seq_number_value(self) -> int:
        """
            get max seqnumber value present in machine_inputs database table

            :return:
                return the max seqnumber value
        """
        try:
            seqnumber = self.database_session.query(func.max(self.model.seqnum)).first()

            return seqnumber[0] if(seqnumber[0]) else 0
        except Exception as ex:
            Database.create_connection()
            DatabaseCreation.create_database()
            raise BaseExceptionHandler(error_msg=str(ex))



    def is_duplicate_record(self, seqnum: int, machine_id: int, picked_layers: int, timestamp: int) -> bool:
        """
            check if exists any record with this values. Return True if exists and False if not exists

            :param seqnum:
                seqnum attribute value to check
            :param machine_id:
                machine_id attribute value to check
            :param picked_layers:
                 picked_layers attribute value to check
            :param timestamp:
                timestamp attribute value to check

            :return:
                if record exists it means is duplicated so return True and if not exists return False
        """
        try:
            machine_input = self.database_session.query(self.model).\
                                filter(self.model.seqnum == seqnum,
                                       self.model.machine_id == machine_id,
                                       self.model.picked_layers == picked_layers,
                                       self.model.timestamp == timestamp).first() or None

            return False if not machine_input else True
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))

