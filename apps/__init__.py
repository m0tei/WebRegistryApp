
import os

from flask import Flask
from flask_login import LoginManager
from importlib import import_module

from .socketio import socketio

login_manager = LoginManager()

def register_extensions(app):
    login_manager.init_app(app)
    socketio.init_app(app)

def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app) 
    return app
