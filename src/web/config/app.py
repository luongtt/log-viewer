from configparser import SectionProxy


class AppConfig(object):
    HOST = '0.0.0.0'
    PORT = 9090
    FILE_NAME = '/var/log/syslog'
    USER = ''
    PASSWD = ''


def set_config(host: str, port: int, file_name: str, auth: SectionProxy):
    AppConfig.HOST = host
    AppConfig.PORT = port
    AppConfig.FILE_NAME = file_name
    AppConfig.USER = auth['USER']
    AppConfig.PASSWD = auth['PASSWD']
