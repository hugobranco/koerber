import logging



class CustomLogger():

    log_format = "%(asctime)s %(levelname)-8s [%(message)s]"


    def __init__(self, level: int, name: str):
        logging.basicConfig(level=level, format=self.log_format)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level=level)


    def debug(self, message: str):
        self.logger.debug(message)


    def info(self, message: str):
        self.logger.info(message)


    def error(self, message: str):
        self.logger.error(message)


    def warning(self, message: str):
        self.logger.warning(message)


    def critical(self, message: str):
        self.logger.critical(message)


    def set_level(self, level: int):
        self.logger.setLevel(level=level)
