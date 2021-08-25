from datetime import datetime
from models.master_model import MasterModel

from sqlalchemy import Column, Integer



class MachineInputMetrics(MasterModel):
    __tablename__ = 'machine_input_metrics'

    machine_id = Column(Integer)
    picked_layers = Column(Integer)
    speed_layers_stacking_minute = Column(Integer)
    sum_layers_last_minute = Column(Integer)
    rate_layers_stacking_minute = Column(Integer)
    timestamp = Column(Integer)


    def __init__(self, machine_id=None, picked_layers=None, speed_layers_stacking_minute=None,
                 sum_layers_last_minute=None, rate_layers_stacking_minute=None, timestamp=None):
        self.machine_id = machine_id
        self.picked_layers = picked_layers
        self.speed_layers_stacking_minute = speed_layers_stacking_minute
        self.sum_layers_last_minute = sum_layers_last_minute
        self.rate_layers_stacking_minute = rate_layers_stacking_minute
        self.timestamp = timestamp
        self.datetime = datetime.fromtimestamp(timestamp)
