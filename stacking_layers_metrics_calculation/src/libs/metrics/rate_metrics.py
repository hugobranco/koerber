from dataclasses import dataclass
from utils.date_utils import DateUtils


@dataclass
class RateMetrics():
    rate: int
    sum_layers_last_minute: int
    timestamp: int
    rate_minute: str = ''
    datetime: str = ''


    def __post_init__(self):
        self.rate_minute = f"{self.rate}%/min"
        self.datetime = DateUtils.timestamp_to_datetime_str_with_format(
            timestamp=self.timestamp, datetime_format='%Y-%m-%dT%H:%M:%S'
        )
