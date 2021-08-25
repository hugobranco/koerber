from libs.database.database_connection import DatabaseConnection
from models.machine_input import MachineInput
from models.machine_input_metrics import MachineInputMetrics
from utils.base_exception_handler import BaseExceptionHandler



class DatabaseCreation():

    @classmethod
    def create_database(cls):
        """
            Create database
        """
        try:
            DatabaseConnection.base.metadata.create_all(
                DatabaseConnection.engine,
                checkfirst=True
            )
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    @classmethod
    def create_models_tables(cls):
        """
            create tables in database
        """
        try:
            MachineInput.__table__.create(bind=DatabaseConnection.engine, checkfirst=True)
            MachineInputMetrics.__table__.create(bind=DatabaseConnection.engine, checkfirst=True)
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))
