import unittest
from libs.machine_data import MachineData


class TestMachineData(unittest.TestCase):

    def test_get_random_machine_data(self):
        # Assert
        assert type(MachineData.get_random_machine_data()) is dict
