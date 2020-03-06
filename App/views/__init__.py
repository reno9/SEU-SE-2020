from App.views.enterprise_view import blue_enter
from App.views.scholar_view import blue_scholar


def init_views(app):
    app.register_blueprint(blue_scholar)
    app.register_blueprint(blue_enter)