from flask import Blueprint, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from ..config.app import AppConfig

tail = Blueprint('', __name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    users = {
        AppConfig.USER: generate_password_hash(AppConfig.PASSWD)
    }
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@tail.route('/')
@auth.login_required
def home():
    res = {"file": AppConfig.FILE_NAME}
    return render_template('home/index.html', **res)
