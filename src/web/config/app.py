import json
from configparser import SectionProxy

PATH_WHITE_LIST = []


class AppConfig(object):
    HOST = '0.0.0.0'
    PORT = 9090
    FILE_NAME = '/var/log/syslog'
    USER = ''
    PASSWD = ''
    LINES = 100


def set_line_conf(lines: int):
    AppConfig.LINES = lines


def set_file_conf(path: str):
    AppConfig.FILE_NAME = path


def set_path_with_list(path: SectionProxy):
    global PATH_WHITE_LIST
    PATH_WHITE_LIST = json.loads(path["WHITE_LIST"])


def set_config(host: str, port: int, file_name: str, auth: SectionProxy):
    AppConfig.HOST = host
    AppConfig.PORT = port
    AppConfig.FILE_NAME = file_name
    AppConfig.USER = auth['USER']
    AppConfig.PASSWD = auth['PASSWD']
