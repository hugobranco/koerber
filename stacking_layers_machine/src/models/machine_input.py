from datetime import datetime
from models.master_model import MasterModel
from utils.base_exception_handler import BaseExceptionHandler

from sqlalchemy import Column, Integer



class MachineInput(MasterModel):
    __tablename__ = 'machine_inputs'


    seqnum = Column(Integer)
    machine_id = Column(Integer)
    picked_layers = Column(Integer)
    timestamp = Column(Integer)


    def __init__(self, seqnum=None, machine_id=None, picked_layers=None, timestamp=None):
        try:
            self.seqnum = seqnum
            self.machine_id = machine_id
            self.picked_layers = picked_layers
            self.timestamp = timestamp
            if(timestamp is not None):
                self.datetime = datetime.fromtimestamp(timestamp)
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))
