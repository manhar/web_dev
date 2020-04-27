from flask import Blueprint, render_template
from app.auth import auth_forms

auth_bp = Blueprint('auth_bp',  __name__)

@auth_bp.route('/')
def login():
    form = auth_forms.LoginForm()
    return render_template("login.html", title="Sign in", form=form)

@auth_bp.route('/forgot_password/')
def forgot_password():
    return "This should be page for forgot password"

@auth_bp.route('/signup/')
def signup():
    return "This should be page for signup"

 