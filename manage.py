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


if __name__ == '__main__':
    cli()