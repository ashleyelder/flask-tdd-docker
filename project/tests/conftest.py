import pytest

from project import create_app, db  # updated


@pytest.fixture(scope='module')
def test_app():
    app = create_app()  # new
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()