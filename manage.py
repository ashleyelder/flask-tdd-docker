# manage.py


import sys

from flask.cli import FlaskGroup

from project import create_app, db   # new
from project.api.models import User  # new


app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# populate the database with some initial data
@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='michael', email="hermanmu@gmail.com"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org"))
    db.session.commit()


if __name__ == '__main__':
    cli()