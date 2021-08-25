from fastapi import Response, status

from utils.web_server import WebServer
from utils.custom_logger import CustomLogger
from utils.cfg_reader import CfgReader



class MasterController():

    web_server = WebServer.fast_api_obj
    logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)


    @staticmethod
    @web_server.get("/", description="Home endpoint", name="Home endpoint")
    def home():
        return {'Info': 'Web server is ON and working'}



    @staticmethod
    def return_request_error(error_message: str, http_status_code: int, response: Response):
        """
            when is an error return to client http request the error

            :param error_message:
                string with error message
            :param http_status_code
                http status code to return
            :param response:
                http response

            :return:
                return a dictionary with the error
        """
        response.status_code = http_status_code
        return {
            'error': error_message
        }
