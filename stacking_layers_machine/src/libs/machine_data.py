from datetime import datetime
from random import randint

from dao.machine_input_dao import MachineInputDao


class MachineData():

    machine_input_dao = MachineInputDao()

    # this sequence number is always incremented and it starts with the higher value existent in machine_inputs
    #   database table
    seqnum = 1
    machine_id = 1
    timestamp: int
    picked_layers: int
    get_max_from_database = True



    @classmethod
    def get_random_machine_data(cls) -> dict:
        """
            create a random machine data to send to machine metrics service. Send a dictionary with this structure:
            {
               seqnumber: 1, # incremented value
               machineId: 1,
               timestamp: 111111, # datetime now
               pickedLayers: 3 # random number from 1 to 8
            }

            :return:
                return dictionary with random machine data
        """
        # TODO:
        # check if can get first record from machine_inputs database. This is just a work around to check database
        #   connection. This has to be replaced by just a check if connection is on or off. This is the wrong way.
        #   Make this because only can send machine data if database connection is on

        if(cls.get_max_from_database):
            cls.seqnum = cls.machine_input_dao.get_max_seq_number_value()
            cls.get_max_from_database = False

        if(cls.machine_input_dao.get_one_record()):
            cls.__generate_machine_random_data()

            return {
                'seqnum': cls.seqnum,
                'machineId': cls.machine_id,
                'timestamp': cls.timestamp,
                'pickedLayers': cls.picked_layers
            }
        else:
            return {}



    @classmethod
    def __generate_machine_random_data(cls):
        """
            generate machine random data. Check if generated data already exists in machine_input database table and if
            the generated values already exists have to generate again
        """
        cls.seqnum += 1
        cls.timestamp = int(datetime.timestamp(datetime.now()))
        cls.picked_layers = randint(1, 8)

        while(cls.machine_input_dao.is_duplicate_record(seqnum=cls.seqnum, machine_id=cls.machine_id,
                                                        timestamp=cls.timestamp, picked_layers=cls.picked_layers)):
            cls.__generate_machine_random_data()
