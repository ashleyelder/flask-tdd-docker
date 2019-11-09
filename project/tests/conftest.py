import pytest

from project import app, db

# define a test_app and test_database (for initializing a test database) fixture


@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()