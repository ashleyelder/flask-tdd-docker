# project/api/users.py


from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import User

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UsersList(Resource):
    def post(self):
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')
        db.session.add(User(username=username, email=email))
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': f'{email} was added!'
        }
        return response_object, 201


api.add_resource(UsersList, '/users')