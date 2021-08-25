from utils.cfg_reader import CfgReader
from utils.custom_logger import CustomLogger
from libs.enums.machine_input_status import MachineInputStatus



class GlobalObjects():

    logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)
    machine_input_messages_health: bool     # indicate if app is receiving machine inputs


    @classmethod
    def init_global_objects(cls):
        """
            create the application global class instances.
        """
        cls.machine_input_messages_health = MachineInputStatus.Red.value
