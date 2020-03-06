from flask import Blueprint

blue_enter = Blueprint("enter", __name__, url_prefix='/enterprise')

@blue_enter.route('/')
def hello():


    return "enterprise_view"