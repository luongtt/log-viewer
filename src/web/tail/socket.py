from flask_socketio import Namespace
from src.web.config.app import set_line_conf, set_file_conf
from src.web.config import app


class TailSocket(Namespace):
    def on_connect(self):
        pass

    def on_set_line(self, line):
        set_line_conf(line)

    def on_set_file(self, file: str):
        if file not in app.PATH_WHITE_LIST:
            return
        set_file_conf(file)
