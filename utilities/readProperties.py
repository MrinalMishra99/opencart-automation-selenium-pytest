import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + "\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = (config.get('commonInfo', 'baseUrl'))
        return url
