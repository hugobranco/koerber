import unittest
from datetime import datetime, timedelta

from dao.machine_input_metrics_dao import MachineInputMetricsDao
from utils.base_exception_handler import BaseExceptionHandler


class TestMachineInputMetricsDao(unittest.TestCase):

    def test_get_metrics_by_date(self):
        # arrange
        machine_input_metrics_dao = MachineInputMetricsDao()
        ini_timestamp = int(datetime.timestamp(datetime.now()))
        end_timestamp = int(datetime.timestamp(datetime.now() + timedelta(hours=1)))

        # assert
        try:
            machine_input_metrics_dao.get_metrics_by_date(ini_timestamp=ini_timestamp, end_timestamp=end_timestamp)
        except BaseExceptionHandler:
            self.fail("MachineInputMetricsDao.get_metrics_by_date() raised BaseExceptionHandler unexpectedly!")
