import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        logs_dir = os.path.join(os.getcwd(), 'logs')
        log_path = os.path.join(logs_dir, 'automation.log')
        fileHandler = logging.FileHandler(log_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)

        return logger
