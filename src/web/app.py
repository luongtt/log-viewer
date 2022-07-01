import eventlet
import src.web.tail.services as TailService
from flask import Flask
from flask_socketio import SocketIO
from src.web.tail.views import tail
from src.web.config.app import AppConfig
from src.web.tail.socket import TailSocket

app = Flask(__name__, template_folder='templates', static_folder='static')
socket_io = SocketIO()
eventlet.monkey_patch()


def _register_blueprint():
    app.register_blueprint(tail)


def _on_namespace_socket():
    socket_io.on_namespace(TailSocket('/tail'))


def run_web():
    _register_blueprint()
    socket_io.init_app(app, cors_allowed_origins="*")
    _on_namespace_socket()
    eventlet.spawn(TailService.tail, app, socket_io, '/tail')
    socket_io.run(app, host=AppConfig.HOST, port=AppConfig.PORT, use_reloader=False, debug=True)
