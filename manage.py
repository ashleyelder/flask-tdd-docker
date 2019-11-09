from flask.cli import FlaskGroup

from project import app


# flaskgroup instance to etend normal CLI with commands related to flask app
cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()