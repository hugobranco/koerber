from dao.machine_input_metrics_dao import MachineInputMetricsDao
from libs.metrics.speed_metrics import SpeedMetrics
from libs.metrics.rate_metrics import RateMetrics
from libs.metrics.speed_rate_metrics import SpeedRateMetrics
from utils.base_exception_handler import BaseExceptionHandler


class BuildMetrics():

    @staticmethod
    def build_speed_metrics_by_dates(ini_timestamp: int, end_timestamp: int) -> dict:
        """
            build speed metrics by each machine. Get the metrics between ini_timestamp and end_timestamp and build a
            dictionary with the speed metrics by machine id

            :param ini_timestamp:
                 get metrics with timestamp >= to this param
            :param end_timestamp:
                get metrics with timestamp >= to this param

            :return:
                return a dictionary with all speed metrics between dates to each machine
        """
        # get metrics data
        machine_input_metrics_dao = MachineInputMetricsDao()
        machine_inputs_metrics = machine_input_metrics_dao.get_metrics_by_date(
            ini_timestamp=ini_timestamp, end_timestamp=end_timestamp
        )

        try:
            # save metrics by machine
            speed_metrics_dict = dict()
            for machine_inputs_metric in machine_inputs_metrics:
                if (machine_inputs_metric.machine_id not in speed_metrics_dict):
                    speed_metrics_dict[machine_inputs_metric.machine_id] = list()

                speed_metrics_dict[machine_inputs_metric.machine_id].append(
                    SpeedMetrics(
                        speed=machine_inputs_metric.speed_layers_stacking_minute,
                        timestamp=machine_inputs_metric.timestamp
                    )
                )
            return speed_metrics_dict
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    @staticmethod
    def build_rate_metrics_by_dates(ini_timestamp: int, end_timestamp: int) -> dict:
        """
            build rate metrics by each machine. Get the metrics between ini_timestamp and end_timestamp and build a
            dictionary with the rate metrics by machine id

            :param ini_timestamp:
                 get metrics with timestamp >= to this param
            :param end_timestamp:
                get metrics with timestamp >= to this param

            :return:
                return a dictionary with all rate metrics between dates to each machine
        """
        # get metrics data
        machine_input_metrics_dao = MachineInputMetricsDao()
        machine_inputs_metrics = machine_input_metrics_dao.get_metrics_by_date(
            ini_timestamp=ini_timestamp, end_timestamp=end_timestamp
        )

        try:
            # save metrics by machine
            rate_metrics_dict = dict()
            for machine_inputs_metric in machine_inputs_metrics:
                if (machine_inputs_metric.machine_id not in rate_metrics_dict):
                    rate_metrics_dict[machine_inputs_metric.machine_id] = list()

                rate_metrics_dict[machine_inputs_metric.machine_id].append(
                    RateMetrics(
                        rate=machine_inputs_metric.rate_layers_stacking_minute,
                        sum_layers_last_minute=machine_inputs_metric.sum_layers_last_minute,
                        timestamp=machine_inputs_metric.timestamp
                    )
                )
            return rate_metrics_dict
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    @staticmethod
    def build_all_metrics_by_dates(ini_timestamp: int, end_timestamp: int) -> dict:
        """
            build speed and rate metrics by each machine. Get the metrics between ini_timestamp and end_timestamp and
            build a dictionary with the speed and rate metrics by machine id

            :param ini_timestamp:
                 get metrics with timestamp >= to this param
            :param end_timestamp:
                get metrics with timestamp >= to this param

            :return:
                return a dictionary with all speed and rate metrics between dates to each machine
        """
        # get metrics data
        machine_input_metrics_dao = MachineInputMetricsDao()
        machine_inputs_metrics = machine_input_metrics_dao.get_metrics_by_date(
            ini_timestamp=ini_timestamp, end_timestamp=end_timestamp
        )

        try:
            # save metrics by machine
            all_metrics_dict = dict()
            for machine_inputs_metric in machine_inputs_metrics:
                if (machine_inputs_metric.machine_id not in all_metrics_dict):
                    all_metrics_dict[machine_inputs_metric.machine_id] = list()

                all_metrics_dict[machine_inputs_metric.machine_id].append(
                    SpeedRateMetrics(
                        speed=machine_inputs_metric.speed_layers_stacking_minute,
                        rate=machine_inputs_metric.rate_layers_stacking_minute,
                        sum_layers_last_minute=machine_inputs_metric.sum_layers_last_minute,
                        timestamp=machine_inputs_metric.timestamp
                    )
                )
            return all_metrics_dict
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))
