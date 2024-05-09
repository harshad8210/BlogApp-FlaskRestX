from flask_marshmallow.fields import fields
from marshmallow import validate

from flaskblog import marshmallow
from flaskblog.user.model import User
from flaskblog.user.validation import username_validation, email_validation, password_validation


class UserRegisterRequestSchema(marshmallow.Schema):
    """
    user registration schema
    """
    username = fields.Str(required=True, validate=[validate.Length(min=6, max=12), username_validation], )
    email = fields.Email(required=True, validate=email_validation)
    password = fields.Str(required=True, validate=password_validation)


class UserLoginRequestSchema(marshmallow.Schema):
    """
    user login schema
    """
    email = fields.Email(required=True, validate=email_validation)
    password = fields.Str(required=True, validate=password_validation)


class UserRegisterResponseSchema(marshmallow.SQLAlchemyAutoSchema):
    """
    user registration response schema
    """
    class Meta:
        model = User
        exclude = ('password', 'id')


class UserChangePasswordSchema(marshmallow.Schema):
    """
    user change password schema
    """
    current_password = fields.Str(required=True)
    new_password = fields.Str(required=True, validate=password_validation)
    confirm_password = fields.Str(required=True)


class UserForgotPassSchema(marshmallow.Schema):
    """
    user forgot password mail send schema
    """
    email = fields.Email(required=True, validate=email_validation)


class UserResetPassSchema(marshmallow.Schema):
    """
    user reset password schema
    """
    password = fields.Str(required=True, validate=password_validation)
