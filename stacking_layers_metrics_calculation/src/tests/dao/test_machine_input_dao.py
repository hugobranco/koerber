import unittest
from datetime import datetime

from dao.machine_input_dao import MachineInputDao
from utils.base_exception_handler import BaseExceptionHandler



class TestMachineInputDao(unittest.TestCase):

    def test_sum_picked_layers_last_minute(self):
        # arrange
        machine_input_dao = MachineInputDao()
        timestamp = int(datetime.timestamp(datetime.now()))

        # assert
        try:
            machine_input_dao.sum_picked_layers_last_minute(timestamp=timestamp)
        except BaseExceptionHandler:
            self.fail("MachineInputDao.sum_picked_layers_last_minute() raised BaseExceptionHandler unexpectedly!")
