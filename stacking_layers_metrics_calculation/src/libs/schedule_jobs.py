from utils.custom_logger import CustomLogger
from utils.cfg_reader import CfgReader
from libs.global_objects import GlobalObjects
from libs.enums.machine_input_status import MachineInputStatus


class ScheduleJobs():

    logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)


    @staticmethod
    def update_app_heath():
        """
            schedule function to update app health to offline. If this schedule job run it means the machine data in
            not arriving, so the app health is RED
        """
        ScheduleJobs.logger.debug(message="Run schedule job!!")

        # set machine_input_messages_health global object to RED
        GlobalObjects.machine_input_messages_health = MachineInputStatus.Red.value
