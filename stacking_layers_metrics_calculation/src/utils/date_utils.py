from datetime import datetime
from utils.base_exception_handler import BaseExceptionHandler



class DateUtils():

    @staticmethod
    def datetime_string_to_datetime_obj(datetime_string: str, datetime_format: str) -> datetime:
        """
            cast a string datetime to a datetime instance with the datetime_format received in param datetime_format

            :param datetime_string:
                datetime string to be casted to daetime instance
            :param datetime_format:
                the datetime dormat

            :return:
                return a datetime instance with the datetime format provided by datetime_format param
        """
        try:
            return datetime.strptime(datetime_string, datetime_format)
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))


    @staticmethod
    def timestamp_to_datetime(timestamp: int) -> datetime:
        """
            cast a timestamp to a datetime instance

            :param timestamp:
                timestamp to be casted

            :return:
                return a datetime instance
        """
        try:
            return datetime.fromtimestamp(timestamp)
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))



    @staticmethod
    def timestamp_to_datetime_str_with_format(timestamp: int, datetime_format: str):
        """
            cast a timestamp value in a datetime string with datetime_format

            :param timestamp:
                timestamp value to be casted
            :param datetime_format:
                formate oh the datetime value

            :return:
                return a datetime string value formatted in datetime_format
        """
        try:
            datetime_value = datetime.fromtimestamp(timestamp)
            return datetime_value.strftime(datetime_format)
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))
