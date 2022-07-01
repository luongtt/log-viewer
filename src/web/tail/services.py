import subprocess
from src.web.config.app import AppConfig


def tail(app, socket_io, namespace):
    f = subprocess.Popen(['tail', '-F', AppConfig.FILE_NAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        line = f.stdout.readline()
        with app.app_context():
            socket_io.emit("line", line.decode("utf-8"), namespace=namespace)
