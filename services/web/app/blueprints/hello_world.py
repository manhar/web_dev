from flask import Blueprint

hello_world_bp = Blueprint('hello_world_bp', __name__)

@hello_world_bp.route('/')
def index():
    return "This is an example app"