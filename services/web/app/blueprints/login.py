from flask import Blueprint

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/')
def login():
    return "This should be the login page"  


 