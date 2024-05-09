from flask_restx import Resource, Api
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from flaskblog.user.service import UserOperation

user_router = Blueprint('User', __name__)
user_api = Api(user_router, prefix='/user')
user_ns = user_api.namespace("User", description="User Operations")


class UserRegistration(Resource):

    def post(self):
        """
        creates a new user.
        :return: json registration schema response data
        """
        user_operations = UserOperation(request)
        return user_operations.create_new_user()


class UserLogin(Resource):

    def post(self):
        """
        login user.
        :return: json login schema response data
        """
        user_operations = UserOperation(request)
        return user_operations.login_user()


class ChangeUserPassword(Resource):
    @jwt_required()
    def put(self):
        """
        changes a logged-in user password.
        :return: messages
        """
        user_operations = UserOperation(request)
        return user_operations.change_user_pass()


class ForgotUserPassword(Resource):

    def post(self):
        """
        sends a forgot password request mail.
        :return: message
        """
        user_operations = UserOperation(request)
        return user_operations.forgot_user_password()


class ResetUserPassword(Resource):

    def post(self, token):
        """
        resets the user password.
        :return: message
        """
        user_operations = UserOperation(request)
        return user_operations.reset_user_password(token=token)


# user blueprint API routes
user_api.add_resource(UserRegistration, '/registration')
user_api.add_resource(UserLogin, '/login')
user_api.add_resource(ChangeUserPassword, '/change-password')
user_api.add_resource(ForgotUserPassword, '/forgot-password')
user_api.add_resource(ResetUserPassword, '/reset-password/<token>')
