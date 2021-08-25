import unittest
from datetime import datetime
from random import randint

from dao.machine_input_dao import MachineInputDao
from utils.base_exception_handler import BaseExceptionHandler


class TestMachineInputDao(unittest.TestCase):

    machine_input_dao = MachineInputDao()

    def test_get_max_seq_number_value(self):
        try:
            self.machine_input_dao.get_max_seq_number_value()
        except BaseExceptionHandler:
            self.fail("MachineInputDao.get_max_seq_number_value() raised BaseExceptionHandler unexpectedly!")


    def test_is_duplicate_record(self):
        # arrange
        seqnum = 1
        machine_id = 1
        picked_layers = randint(1, 8)
        timestamp = int(datetime.timestamp(datetime.now()))


        try:
            self.machine_input_dao.is_duplicate_record(
                seqnum=seqnum, machine_id=machine_id, picked_layers=picked_layers, timestamp=timestamp
            )
        except BaseExceptionHandler:
            self.fail("MachineInputDao.get_max_seq_number_value() raised BaseExceptionHandler unexpectedly!")



