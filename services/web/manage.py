from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app  import app, db
from app.models import User, Post
#migrate = Migrate(db) #object responsible for tracking changes in DB



cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()


if __name__ == "__main__":
    cli()
