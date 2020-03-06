from flask import Flask
from App.middleware import load_middleware
from App.settings import envs
from App.ext import init_ext
from App.views import init_views


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app=app)
    init_views(app=app)
    load_middleware(app)
    return app