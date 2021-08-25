import unittest
from datetime import datetime, timedelta

from libs.metrics.build_metrics import BuildMetrics
from utils.base_exception_handler import BaseExceptionHandler


class TestBuildMetrics(unittest.TestCase):

    # arrange
    ini_timestamp = int(datetime.timestamp(datetime.now() - timedelta(hours=2)))
    end_timestamp = int(datetime.timestamp(datetime.now() + timedelta(hours=2)))

    def test_build_speed_metrics_by_dates(self):
        # assert
        try:
            BuildMetrics.build_speed_metrics_by_dates(
                ini_timestamp=self.ini_timestamp, end_timestamp=self.end_timestamp
            )
        except BaseExceptionHandler:
            self.fail("BuildMetrics.build_speed_metrics_by_dates() raised BaseExceptionHandler unexpectedly!")



    def test_build_rate_metrics_by_dates(self):
        # assert
        try:
            BuildMetrics.build_rate_metrics_by_dates(
                ini_timestamp=self.ini_timestamp, end_timestamp=self.end_timestamp
            )
        except BaseExceptionHandler:
            self.fail("BuildMetrics.build_rate_metrics_by_dates() raised BaseExceptionHandler unexpectedly!")



    def test_build_all_metrics_by_dates(self):
        # assert
        try:
            BuildMetrics.build_all_metrics_by_dates(
                ini_timestamp=self.ini_timestamp, end_timestamp=self.end_timestamp
            )
        except BaseExceptionHandler:
            self.fail("BuildMetrics.build_all_metrics_by_dates() raised BaseExceptionHandler unexpectedly!")
