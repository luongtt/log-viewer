import argparse
import configparser

from src.web.config import app as config_app
from src.web import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='web log viewer')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='host')
    parser.add_argument('--port', type=str, default=9090, help='listen port')
    parser.add_argument('--file', type=str, default='/var/log/syslog', help='file tail follow')
    parser.add_argument('--config', type=str, default='config/web.ini', help='configuration file (INI)')
    args = parser.parse_args()
    config_parse = configparser.ConfigParser()
    config_parse.read(args.config)
    config_app.set_config(args.host, args.port, args.file, config_parse['BASE_AUTH'])
    config_app.set_path_with_list(config_parse['PATH'])
    app.run_web()
