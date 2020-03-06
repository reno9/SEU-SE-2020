from flask import request


def load_middleware(app):
    @app.before_request
    def before():
        print("中间件", request.url)