import subprocess
from src.web.config.app import AppConfig


def tail(app, socket_io, namespace):
    cur_line = AppConfig.LINES
    cur_file = AppConfig.FILE_NAME
    sub_ps = subprocess.Popen(['tail', '-F', cur_file, '-n', str(cur_line)],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with app.app_context():
        while True:
            if cur_line != AppConfig.LINES or cur_file != AppConfig.FILE_NAME:
                cur_line = AppConfig.LINES
                cur_file = AppConfig.FILE_NAME
                sub_ps.kill()
                sub_ps = subprocess.Popen(['tail', '-F', cur_file, '-n', str(cur_line)],
                                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            line_content = sub_ps.stdout.readline()
            socket_io.emit("line", line_content.decode("utf-8"), namespace=namespace)
