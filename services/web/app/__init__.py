from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app) #database object
migrate = Migrate(app,db) #object responsible for tracking changes in DB

from app import routes, models